# 🛑 System Design: Rate Limiting

Notes on protecting application infrastructure from abuse, spam, and DoS attacks.

## Why Rate Limiting is Mandatory
* **Resource Preservation:** Prevents aggressive bots or broken infinite loops from draining server CPU and memory.
* **Cost Control:** Keeps operational costs down if you are paying for backend compute power or third-party APIs per request.

## The Token Bucket Algorithm
* **Capacity:** The maximum number of requests a user can burst at any single second.
* **Refill Rate:** How fast the user regains their allowance over time.
* **Advantage:** Highly memory-efficient and allows for minor traffic bursts while strictly enforcing a hard ceiling over time.

## Next-Level Build Idea
* *Goal:* Implement a concrete Token Bucket class inside `2-Build/` that uses system timestamps to calculate dynamic token refills without needing a heavy background thread.
