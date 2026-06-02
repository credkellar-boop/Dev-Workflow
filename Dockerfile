# Use a lightweight Python base
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the specific script for this service
# Replace 'your_script.py' with the specific file (e.g., api_gateway.py)
COPY . /app

# Expose the necessary port (Example: 8000)
EXPOSE 8000

# Command to run the service
CMD ["python", "your_script.py"]
