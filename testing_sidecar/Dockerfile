# Use the official Python image as a base
FROM python:3.9-slim

# Install Docker CLI
RUN apt-get update && \
    apt-get install -y docker.io && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY script.py .
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Command to run the script
CMD ["python", "script.py"]