import time

class MiniAPIGateway:
    def __init__(self):
        # Declarative routing map matching URL prefixes to mock internal cluster nodes
        self.routing_table = {
            "/api/v1/cache": "internal-cluster-redis-service:8081",
            "/api/v1/tasks": "internal-cluster-worker-queue:8089",
            "/api/v1/server": "internal-cluster-async-http:8085"
        }

    def process_request(self, path, headers):
        print(f"\n🌐 [GATEWAY INGRESS] Intercepted request target path: '{path}'")

        # 1. Edge Security Step: Mock JWT Signature Check
        auth_token = headers.get("Authorization")
        if not auth_token or "secret_jwt_sig" not in auth_token:
            print("🚨 [SECURITY REJECTION] Missing or invalid authorization signature at the edge!")
            return "HTTP/1.1 401 Unauthorized\r\n\r\n"

        # 2. Path-Based Dynamic Routing Step
        target_service = None
        for prefix, destination in self.routing_table.items():
            if path.startswith(prefix):
                target_service = destination
                break

        if not target_service:
            print(f"❌ [ROUTING ERROR] No internal route matching prefix pattern for path: '{path}'")
            return "HTTP/1.1 404 Not Found\r\n\r\n"

        # 3. Forward Payload to Target Backend Service
        print(f"🔀 [REVERSE PROXY] Forwarding request downstream -> http://{target_service}{path}")
        
        # Simulating instantaneous internal high-speed network transit loop
        time.sleep(0.1) 
        
        mock_backend_html = f"<html><body>⚡ Proxied Response from {target_service}</body></html>"
        return f"HTTP/1.1 200 OK\r\nContent-Length: {len(mock_backend_html)}\r\n\r\n{mock_backend_html}"

if __name__ == "__main__":
    gateway = MiniAPIGateway()

    print("=== Simulation 1: Unauthenticated Intrusion Attempt ===")
    bad_headers = {"User-Agent": "Mozilla/5.0"}
    gateway.process_request("/api/v1/cache/user_100", bad_headers)

    print("\n=== Simulation 2: Authenticated Cache Read Request ===")
    good_headers = {"Authorization": "Bearer encoded_claims.payload_set.secret_jwt_sig"}
    gateway.process_request("/api/v1/cache/user_100", good_headers)

    print("\n=== Simulation 3: Authenticated Async Server Routing ===")
    gateway.process_request("/api/v1/server/dashboard", good_headers)

    print("\n=== Simulation 4: Invalid Path Fallback Handle ===")
    gateway.process_request("/api/v1/unknown-service/endpoint", good_headers)
