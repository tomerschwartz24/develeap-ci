# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exposing port 80 outside of the container 
EXPOSE 80

# Define environment variable
ENV NAME counter-service

# Run counter-service.py when the container launches
CMD ["python", "counter-service.py"]
