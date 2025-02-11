# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Install Nginx
RUN apt-get update && apt-get install -y nginx

# Copy Nginx configuration
COPY api/nginx.conf /etc/nginx/conf.d/default.conf

# Expose the port
EXPOSE 80

# Start Nginx and FastAPI
CMD service nginx start && uvicorn main:app --host 0.0.0.0 --port 8000
