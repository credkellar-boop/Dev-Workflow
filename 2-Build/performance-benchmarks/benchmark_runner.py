import time
import random

# Emulating the behavior of our mini-hash-table (O(1)) vs a linear array lookup (O(n))
class MockLinearArrayStore:
    def __init__(self):
        self.store = []
    def insert(self, key, val):
        self.store.append((key, val))
    def find(self, target_key):
        for key, val in self.store:
            if key == target_key:
                return val
        return None

class MockFastHashStore:
    def __init__(self, capacity=20000):
        self.capacity = capacity
        self.slots = [None] * self.capacity
    def _hash(self, key):
        return sum(ord(c) for c in key) % self.capacity
    def insert(self, key, val):
        idx = self._hash(key)
        self.slots[idx] = val
    def find(self, key):
        idx = self._hash(key)
        return self.slots[idx]

def run_stress_test(data_scale):
    print(f"\n🚀 Generating Dataset Scale: {data_scale} records...")
    linear_store = MockLinearArrayStore()
    hash_store = MockFastHashStore(capacity=data_scale * 2)

    # Generate distinct random keys
    test_keys = [f"key_token_{i}_{random.randint(1000,9999)}" for i in range(data_scale)]
    
    # Hydrate both storage targets
    for key in test_keys:
        linear_store.insert(key, "payload_data")
        hash_store.insert(key, "payload_data")

    # Select a random subset of keys to query for the latency benchmark
    query_sample = random.sample(test_keys, min(1000, data_scale))

    print(f"⏱️ Simulating {len(query_sample)} concurrent random lookups...")

    # --- Test 1: Linear Scan (O(n)) ---
    start_time = time.perf_counter()
    for q_key in query_sample:
        linear_store.find(q_key)
    linear_duration = time.perf_counter() - start_time

    # --- Test 2: Hash Direct Address (O(1)) ---
    start_time = time.perf_counter()
    for q_key in query_sample:
        hash_store.find(q_key)
    hash_duration = time.perf_counter() - start_time

    # Display performance metrics
    print(f"📊 [LINEAR STORE O(n)] Latency: {linear_duration:.5f} seconds")
    print(f"⚡ [HASH STORE   O(1)] Latency: {hash_duration:.5f} seconds")
    
    speedup = linear_duration / max(hash_duration, 1e-9)
    print(f"🏆 Custom Hash Engine performed {speedup:.1f}x FASTER than linear scan.")

if __name__ == "__main__":
    print("=== System Performance Stress Suite ===")
    # Run test at small scale
    run_stress_test(1000)
    # Run test at 10x scale to prove O(n) grows while O(1) stays flat
    run_stress_test(10000)
