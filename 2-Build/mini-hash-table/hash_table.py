class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        # Initialize internal storage array with empty buckets for Separate Chaining
        self.buckets = [[] for _ in range(self.capacity)]

    def _custom_hash(self, key):
        """Generates a predictable bucket index using a basic polynomial string hash."""
        hash_value = 0
        prime_multiplier = 31
        
        for char in str(key):
            hash_value = (hash_value * prime_multiplier) + ord(char)
            
        # Bind the raw integer result cleanly inside our allocated array bounds
        return hash_value % self.capacity

    def put(self, key, value):
        """Inserts or updates a key-value pair, handling potential collisions via chaining."""
        bucket_index = self._custom_hash(key)
        reference_bucket = self.buckets[bucket_index]

        # Scan the linked list chain to see if the key already exists
        for index, element in enumerate(reference_bucket):
            kv_key, kv_val = element
            if kv_key == key:
                print(f"🔄 Key match detected! Updating '{key}' -> '{value}' at bucket index {bucket_index}")
                reference_bucket[index] = (key, value)
                return

        # If it's a completely unique key, append it to resolve collisions via chaining
        if len(reference_bucket) > 0:
            print(f"⚠️ Collision alert! Appending '{key}' alongside existing data at bucket index {bucket_index}")
        else:
            print(f"📥 Storing unique key '{key}' at bucket index {bucket_index}")
            
        reference_bucket.append((key, value))

    def get(self, key):
        """Retrieves a value in constant time, skipping collisions by traversing the target chain."""
        bucket_index = self._custom_hash(key)
        reference_bucket = self.buckets[bucket_index]

        for kv_key, kv_val in reference_bucket:
            if kv_key == key:
                print(f"📤 Found value for '{key}' at bucket index {bucket_index} -> '{kv_val}'")
                return kv_val
                
        print(f"❌ Key '{key}' not found in bucket index {bucket_index}")
        return None

# Validation script execution
if __name__ == "__main__":
    table = HashTable(capacity=5) # Kept small explicitly to force hash collisions

    print("--- Basic Key Insertions ---")
    table.put("user_1", "Alice")
    table.put("user_2", "Bob")
    
    print("\n--- Simulating and Forcing Collisions ---")
    # Small capacity guarantees these keys will eventually hit matching bucket indices
    table.put("test_key_A", "Value_Alpha")
    table.put("test_key_B", "Value_Beta")
    
    print("\n--- Validating Retrieval Accuracy Across Collisions ---")
    table.get("test_key_A")
    table.get("test_key_B")
    table.get("invalid_user")
