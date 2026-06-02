# Step 1: Use an official, lightweight Python runtime blueprint
FROM python:3.11-slim

# Step 2: Set the internal working directory inside the container system
WORKDIR /app

# Step 3: Copy our asynchronous server script into the container workspace
COPY async_server.py .

# Step 4: Expose the network port our server listens on inside the container
EXPOSE 8085

# Step 5: Define the execution command to launch our system on container boot
CMD ["python", "async_server.py"]
