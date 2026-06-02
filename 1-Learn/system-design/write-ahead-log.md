# 🗄️ Storage Engine Internals: Write-Ahead Logging (WAL)

Notes on achieving ACID data durability and preventing storage corruption using sequential transactional ledgers.

## The WAL Invariant
* **The Rule:** No data modifications can be written to the primary database page storage file until the corresponding transaction logs describing those modifications have been flushed to non-volatile disk memory.

## Operational Lifecycle
1. **Append:** Incoming transactional writes are recorded sequentially onto the end of the log file (`wal.log`).
2. **Acknowledge:** The client receives a success status once the log record is flushed to disk.
3. **Checkpointing:** Background workers periodically merge accumulated WAL records back into the main primary state storage engine file, clearing out old log history.
