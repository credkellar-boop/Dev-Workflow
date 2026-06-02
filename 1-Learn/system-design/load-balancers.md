# ⚖️ System Design: Load Balancers

Notes on scaling systems horizontally to handle high-concurrency traffic.

## Horizontal vs. Vertical Scaling
* **Vertical Scaling:** Upgrading a single server with more RAM and a stronger CPU. (Has a hard physical limit and introduces a single point of failure).
* **Horizontal Scaling:** Adding more cheap servers to a pool. Requires a **Load Balancer** to manage them.

## Core Responsibilities of a Load Balancer
1. **Traffic Distribution:** Uses algorithms like Round Robin or Least Connections to balance the workload.
2. **Health Checks:** Continuously pings backend servers. If a server dies, the load balancer stops routing traffic to it automatically.
3. **SSL Termination:** Decrypts incoming encrypted requests at the load balancer level so the backend servers don't waste CPU cycles handling cryptography.

## Next-Level Build Idea
* *Goal:* Update my `2-Build/` directory later with a reverse-proxy script that accepts incoming connections and forwards them to two different instances of my Python socket server.
