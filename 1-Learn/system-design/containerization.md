# 🐳 Infrastructure Architecture: Containerization & Docker

Notes on eliminating environment inconsistency and scaling software deploying using isolated application sandboxes.

## Containers vs. Virtual Machines
* **Virtual Machines:** Heavy abstraction layer. Isolates at the hardware level, bundling a full guest OS. High RAM overhead.
* **Containers:** Lightweight abstraction layer. Isolates at the OS process level, sharing the underlying host kernel. Near-zero performance overhead.

## Core Under-the-Hood Linux Primitives
Docker isn't magic; it is built on top of native Linux kernel features:
1. **Namespaces:** Isolates what a process can *see* (prevents a containerized app from seeing files, networks, or processes running on the host or other containers).
2. **Control Groups (cgroups):** Restricts what a process can *use* (allocates and throttles specific maximum allowances for CPU, RAM, and disk I/O).

## Next-Level Build Idea
* *Goal:* Write custom Dockerfiles for our `mini-http-server` and `mini-redis` cache inside `2-Build/`, then orchestrate them into a unified private network using a multi-container Docker Compose pipeline.
