# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Argument for versioning
ARG VERSION=latest

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Create a directory for static files
RUN mkdir /app/staticfiles

# Run migrations and collect static files
RUN python manage.py migrate
RUN python manage.py collectstatic --no-input

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Expose port 8000

# Run locally. left port is local, right port is docker
#docker run -p 8000:8000 wisdom-pets-1.0
