import os
import json

class DurableStorageEngine:
    def __init__(self, db_path="data.db", wal_path="wal.log"):
        self.db_path = db_path
        self.wal_path = wal_path
        self.memory_state = {}
        
        # On startup, initialize files and automatically check for crash recovery
        self._recover_if_needed()

    def _recover_if_needed(self):
        """Crash Recovery: Reads primary DB file first, then replays outstanding logs."""
        # 1. Load primary state database file if it exists
        if os.path.exists(self.db_path):
            with open(self.db_path, "r") as f:
                try:
                    self.memory_state = json.load(f)
                except json.JSONDecodeError:
                    self.memory_state = {}

        # 2. Replay WAL logs to reconstruct any un-checkpointed commits
        if os.path.exists(self.wal_path):
            print("🚨 [CRASH RECOVERY] Outstanding WAL log detected! Replaying logs to prevent data loss...")
            with open(self.wal_path, "r") as log_file:
                for line in log_file:
                    if line.strip():
                        tx = json.loads(line)
                        # Re-apply transaction mutations directly to memory state
                        self.memory_state[tx["key"]] = tx["val"]
            print("🏁 [RECOVERY COMPLETE] In-memory state synchronized perfectly.")

    def write_transaction(self, key, value):
        """Durability Rule: Write to WAL ledger first before modifying state."""
        tx_record = {"key": key, "val": value}
        
        # STEP 1: Append transaction to the WAL ledger file on disk
        with open(self.wal_path, "a") as log_file:
            log_file.write(json.dumps(tx_record) + "\n")
            
        # STEP 2: Commit modification to memory state
        self.memory_state[key] = value
        print(f"📥 [COMMIT] Key '{key}' -> '{value}' successfully secured in WAL ledger.")

    def checkpoint(self):
        """Flushes all un-checkpointed log modifications to primary storage disk."""
        print("\n🧹 [CHECKPOINT] Merging WAL log data into primary database file on disk...")
        
        # Save memory state to the primary structured DB storage file
        with open(self.db_path, "w") as f:
            json.dump(self.memory_state, f, indent=4)
            
        # Safely erase the WAL log since changes are now safely consolidated
        if os.path.exists(self.wal_path):
            os.remove(self.wal_path)
        print("💾 Primary database file consolidated. WAL cleared cleanly.")

    def read(self, key):
        return self.memory_state.get(key)

if __name__ == "__main__":
    print("--- Phase 1: Standard Writing & Checkpointing ---")
    db = DurableStorageEngine()
    db.write_transaction("user_100", "Alice_Data")
    db.write_transaction("user_101", "Bob_Data")
    db.checkpoint() # Safe consolidation

    print("\n--- Phase 2: Simulating Sudden Server Crash Mid-Write ---")
    db.write_transaction("user_102", "Unsaved_Crash_Data_Charlie")
    
    # Simulate a sudden kernel crash or power cut by dropping memory state abruptly 
    # without running .checkpoint() to write to data.db
    print("💥 [CRASH] System power cord yanked! Volatile memory state wiped instantly.")
    del db

    print("\n--- Phase 3: Rebooting and Restoring State ---")
    # Instantiating a new database engine instance simulates booting back up
    rebooted_db = DurableStorageEngine()
    
    print(f"\nVerifying recovered item: 'user_102' -> '{rebooted_db.read('user_102')}'")
