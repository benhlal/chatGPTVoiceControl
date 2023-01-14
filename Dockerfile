# Use an official Python runtime as a base image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the code and requirements.txt file to the image
COPY complete.py .
COPY requirements.txt .

# Install required libraries
RUN pip install -r requirements.txt

# Run the command to start the application
CMD ["python", "/app/complete.py"]
