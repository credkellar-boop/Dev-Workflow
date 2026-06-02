# 📉 System Design: Circuit Breakers & Health Monitoring

Notes on designing fault-tolerant networks that gracefully handle downstream outages.

## Core Mitigation Strategies
* **Active Health Checking:** The proxy periodically pings a dedicated `/health` endpoint on backend instances to verify runtime readiness *before* routing user traffic to them.
* **The Circuit Breaker Pattern:** Prevents an application from repeatedly trying to execute an operation that's highly likely to fail, saving socket resources and protecting user experience.

## Circuit State Transitions
1. `CLOSED`: Everything is operational. Requests are allowed through.
2. `OPEN`: Downstream target is down. Requests are short-circuited instantly without hitting the wire.
3. `HALF-OPEN`: Cooldown elapsed. Trialing a subset of real traffic to check if the target recovered.
