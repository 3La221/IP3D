# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /ip3d

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose port 8000 for the application
EXPOSE 8000

# Set the environment variable for Django settings module
ENV DJANGO_SETTINGS_MODULE=base.settings

# Command to run the Django application
CMD ["gunicorn", "base.wsgi:application", "--bind", "0.0.0.0:8000"]
