# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# 1. Copy only the requirements file first from its correct location
#    This allows Docker to cache the dependency installation layer
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. Copy the rest of the application code from the 'app' directory
COPY app/ .

# 3. Copy the templates directory from the root
COPY templates/ ./templates/

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
