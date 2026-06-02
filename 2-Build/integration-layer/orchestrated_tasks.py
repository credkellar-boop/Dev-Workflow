# Import your logic
from distributed_lock import DistributedLock
from weighted_balancer import WeightedBalancer

# 1. Initialize the global DLM for all workers
global_lock = DistributedLock()

# 2. Initialize the Weighted Balancer with your container capacities
balancer = WeightedBalancer({'node_high_perf': 5, 'node_standard': 1})

def perform_secure_task(task_id):
    # ATTEMPT LOCK (Prevents race conditions)
    if global_lock.acquire(task_id, "worker_1"):
        try:
            target = balancer.get_next()
            print(f"✅ Secured task {task_id} and routed to {target}")
        finally:
            global_lock.release(task_id, "worker_1")
    else:
        print("⏳ Task currently locked by another worker. Skipping.")
