import time
import threading

class ResilientTarget:
    def __init__(self, name):
        self.name = name
        self.is_alive = True  # Simulated physical container state
        self.consecutive_failures = 0
        # Circuit states: "CLOSED", "OPEN", "HALF-OPEN"
        self.circuit_state = "CLOSED"
        self.last_state_change = time.time()

    def check_health(self):
        """Simulates an active background network ping or HTTP health probe."""
        # Circuit Breaker Logic based on health checks
        if not self.is_alive:
            self.consecutive_failures += 1
            if self.consecutive_failures >= 3 and self.circuit_state == "CLOSED":
                self.circuit_state = "OPEN"
                self.last_state_change = time.time()
                print(f"🚨 [CIRCUIT TRIPPED] {self.name} has failed 3 checks! Circuit is now OPEN.")
        else:
            self.consecutive_failures = 0
            if self.circuit_state == "OPEN":
                # Cooldown period of 3 seconds to transition to HALF-OPEN
                if time.time() - self.last_state_change > 3:
                    self.circuit_state = "HALF-OPEN"
                    print(f"🟡 [CIRCUIT COOLDOWN] {self.name} enters HALF-OPEN. Testing recovery traffic...")
            elif self.circuit_state == "HALF-OPEN":
                self.circuit_state = "CLOSED"
                print(f"🟢 [CIRCUIT RESET] {self.name} passed health check! Circuit is now CLOSED.")
        
        return self.is_alive

class ResilientLoadBalancer:
    def __init__(self, targets):
        self.targets = targets
        self.lock = threading.Lock()

    def route_request(self):
        """Routes traffic only to targets whose circuits are closed or trialing."""
        with self.lock:
            for target in self.targets:
                if target.circuit_state == "OPEN":
                    # Short-circuit request immediately to avoid waiting on a dead socket
                    print(f"⚡ [SHORT-CIRCUIT] Request blocked from hitting dead target: {target.name}")
                    continue
                
                print(f"🎯 [ROUTING] Routing traffic to: {target.name} (State: {target.circuit_state})")
                return True
            
            print("❌ [OUTAGE] All backends dead. Returning HTTP 503 Service Unavailable.")
            return False

def background_health_checker(targets):
    """Background loop tracking node availability every second."""
    while True:
        print("\n--- Running Background Health Probe Cycle ---")
        for target in targets:
            status = "ALIVE" if target.check_health() else "DEAD"
            print(f"📊 Node Telemetry: {target.name} is {status} | Circuit: {target.circuit_state}")
        time.sleep(1)

if __name__ == "__main__":
    # Initialize our nodes
    node_a = ResilientTarget("backend-container-A")
    lb = ResilientLoadBalancer([node_a])

    # Spin up active health monitoring daemon
    monitor_thread = threading.Thread(target=background_health_checker, args=([node_a],), daemon=True)
    monitor_thread.start()

    # Simulate runtime traffic requests over time
    time.sleep(0.5)
    lb.route_request()

    print("\n💥 [OUTAGE SIMULATION] Injecting container crash on backend-container-A...")
    node_a.is_alive = False

    # Wait for health checker to catch failures and trip circuit
    time.sleep(4)
    lb.route_request()  # Should short-circuit instantly

    print("\n🛠️ [RECOVERY SIMULATION] Rebooting container backend-container-A...")
    node_a.is_alive = True

    # Allow time for circuit to transition through HALF-OPEN back to CLOSED
    time.sleep(5)
    lb.route_request()
