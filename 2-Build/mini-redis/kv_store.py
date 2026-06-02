import time
import threading

class MiniRedis:
    def __init__(self):
        # Clear-text core storage dictionaries
        self.store = {}
        self.expirations = {}
        self.lock = threading.Lock()

    def set(self, key, value, ttl_seconds=None):
        """Stores a key-value pair with an optional expiration timestamp."""
        with self.lock:
            self.store[key] = value
            if ttl_seconds:
                self.expirations[key] = time.time() + ttl_seconds
            else:
                self.expirations.pop(key, None) # Remove old TTL if overwritten
            print(f"📥 SET: '{key}' -> '{value}' (TTL: {ttl_seconds}s)")

    def get(self, key):
        """Retrieves a value if it exists and hasn't expired yet."""
        with self.lock:
            # Check if key expired
            if key in self.expirations and time.time() > self.expirations[key]:
                print(f"⏰ TTL Expired! Evicting stale key: '{key}'")
                self.store.pop(key, None)
                self.expirations.pop(key, None)
                return None
            
            value = self.store.get(key)
            print(f"📤 GET: '{key}' -> '{value}'")
            return value

# Quick verification workflow execution
if __name__ == "__main__":
    cache = MiniRedis()
    
    print("--- Testing Basic Operations ---")
    cache.set("session_101", "user_authenticated_data")
    cache.get("session_101")
    
    print("\n--- Testing TTL Expiration Eviction ---")
    # Set a key that expires in exactly 2 seconds
    cache.set("temp_token", "secret_abc_123", ttl_seconds=2)
    
    print("Immediate check:")
    cache.get("temp_token") # Should return the token
    
    print("\nSleeping for 3 seconds...")
    time.sleep(3)
    
    print("\nPost-expiration check:")
    cache.get("temp_token") # Should trigger eviction and return None
