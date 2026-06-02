import time
import threading

class TokenBucketRateLimiter:
    def __init__(self, capacity, refill_rate_per_sec):
        self.capacity = float(capacity)
        self.refill_rate = float(refill_rate_per_sec)
        self.tokens = float(capacity)
        self.last_refill_time = time.time()
        self.lock = threading.Lock()

    def _refill(self):
        """Internal helper to calculate elapsed time and add tokens dynamically."""
        now = time.time()
        elapsed = now - self.last_refill_time
        
        # Calculate tokens gained since last execution
        tokens_to_add = elapsed * self.refill_rate
        
        # Add tokens without exceeding max bucket capacity
        self.tokens = min(self.capacity, self.tokens + tokens_to_add)
        self.last_refill_time = now

    def allow_request(self):
        """Evaluates token availability. Returns True if allowed, False if limited."""
        with self.lock:
            self._refill()  # Bring the bucket configuration up to date
            
            if self.tokens >= 1.0:
                self.tokens -= 1.0
                print(f"🟢 Request Allowed. Tokens remaining: {self.tokens:.2f}")
                return True
            else:
                print(f"🔴 HTTP 429 Too Many Requests! Rate Limit Exceeded. Tokens remaining: {self.tokens:.2f}")
                return False

# Verification workflow execution simulation
if __name__ == "__main__":
    # Create a bucket: Max 3 tokens, refills at a rate of 1 token per second
    limiter = TokenBucketRateLimiter(capacity=3, refill_rate_per_sec=1)

    print("--- Simulating Rapid Request Burst (Exceeding Capacity) ---")
    for i in range(5):
        print(f"Request #{i+1}: ", end="")
        limiter.allow_request()
        time.sleep(0.1) # Fast bursts

    print("\n--- Sleeping for 2 seconds to allow token refill ---")
    time.sleep(2.0)

    print("\n--- Simulating New Requests After Refill Recovery ---")
    for i in range(2):
        print(f"Post-recovery Request #{i+1}: ", end="")
        limiter.allow_request()
