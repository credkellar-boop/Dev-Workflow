import time
import queue
import threading
import random

class MessageBroker:
    def __init__(self):
        # Core FIFO queue structure to store message tasks safely across threads
        self.task_queue = queue.Queue()
        self.running = True

    def publish(self, task_type, payload):
        """Allows producers to drop structured message payloads into the FIFO queue."""
        message = {"task_type": task_type, "payload": payload, "timestamp": time.time()}
        self.task_queue.put(message)
        print(f"📥 [PRODUCER] Published task '{task_type}' into the broker queue.")

    def start_worker(self, worker_id):
        """Worker loop that continuously pulls and processes tasks from the broker."""
        print(f"⚙️ [WORKER {worker_id}] Booted and listening for tasks...")
        
        while self.running or not self.task_queue.empty():
            try:
                # Wait for a task to arrive with a brief timeout to check running status
                task = self.task_queue.get(timeout=1)
                
                print(f"🚀 [WORKER {worker_id}] Picked up '{task['task_type']}' (Data: {task['payload']})")
                
                # Simulate varying backend execution compute loads
                processing_time = random.uniform(0.5, 1.5)
                time.sleep(processing_time)
                
                print(f"✅ [WORKER {worker_id}] Finished '{task['task_type']}' in {processing_time:.2f}s")
                self.task_queue.task_done()
                
            except queue.Empty:
                # No tasks in queue at the moment, loop back or terminate if shutdown triggered
                continue

    def shutdown(self):
        self.running = False
        print("\n🛑 [BROKER] Shutdown signal sent. Processing remaining items...")

# Simulation of a high-concurrency architecture environment
if __name__ == "__main__":
    broker = MessageBroker()

    # Spin up 3 isolated backend worker consumer threads running concurrently
    workers = []
    for i in range(1, 4):
        t = threading.Thread(target=broker.start_worker, args=(i,))
        t.start()
        workers.append(t)

    print("\n--- Simulating High-Traffic Ingestion Burst ---")
    time.sleep(0.5)
    
    # Producer drops a heavy sequence of heavy jobs into the pipeline
    broker.publish("GENERATE_REPORT", {"report_id": 9001, "format": "PDF"})
    broker.publish("AUDIT_LOG", {"user_id": 412, "action": "CURRENCY_EXCHANGE"})
    broker.publish("SYNC_WALLET", {"wallet_address": "0xMONAD_ALPHA"})
    broker.publish("GENERATE_REPORT", {"report_id": 9002, "format": "CSV"})
    broker.publish("PROCESS_CHECK", {"check_id": 7711, "amount": 2500})

    # Wait for all published items to be picked up by the worker threads
    broker.task_queue.join()
    
    # Gracefully wind down the cluster infrastructure
    broker.shutdown()
    for t in workers:
        t.join()
        
    print("🏁 All task messages processed safely. Cluster clean exit.")
