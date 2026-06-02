# ⚡ System Design: Caching Strategies

Notes on optimizing data retrieval latencies using high-speed in-memory storage.

## Why Caching Matters
* **Disk vs. RAM:** Traditional databases (PostgreSQL, MySQL) read/write to disk, which is slow. Caches (Redis) keep data in RAM, offering sub-millisecond retrieval speeds.
* **Reduces DB Load:** Protects your primary database from being hammered by repetitive, identical queries.

## Cache Hits vs. Cache Misses
* **Cache Hit:** Requested data is found in the cache. Fast execution path.
* **Cache Miss:** Requested data is missing. The application must perform a slow fallback query to the main DB.

## Common Strategies
* **Cache-Aside:** Simple, reliable, and data is only cached when explicitly requested.
* **LRU Eviction Policy:** Automatically removes the oldest, least-visited entries when RAM limits are reached.

## Next-Level Build Idea
* *Goal:* Build a lightweight, thread-safe Key-Value store in `2-Build/` that uses an in-memory dictionary with manual time-to-live (TTL) expiration tracking.
