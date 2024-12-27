# Use official Python image as a base image
FROM python:3.11-slim

# Set environment variables to prevent Python from buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt /app/requirements.txt

# Install dependencies and OpenSSH server
RUN apt-get update && apt-get install -y \
    openssh-server && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Set up SSH
RUN mkdir /var/run/sshd && \
    echo 'root:password' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/UsePAM yes/UsePAM no/' /etc/ssh/sshd_config

# Expose ports for the application and SSH
EXPOSE 8000 22

# Copy the rest of the application code
COPY . /app

# Command to run both SSH server and the application
CMD ["/bin/sh", "-c", "/usr/sbin/sshd -D & gunicorn --bind 0.0.0.0:8000 app:app"]
