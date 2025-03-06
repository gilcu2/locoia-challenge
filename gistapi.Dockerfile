# Use the official Python base image
FROM python:3.12-slim

# Set the working directory inside the container
#WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY gistapi /gistapi

# Expose the port on which the application will run
EXPOSE 8000

# Run the application using gunicorn server
ENV PYTHONPATH=.
CMD gunicorn --bind 0.0.0.0:8000 gistapi.app:app
