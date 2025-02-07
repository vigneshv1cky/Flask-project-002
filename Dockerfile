# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
# COPY requirements.txt .

# Install the dependencies
RUN pip install flask

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the app
CMD ["flask", "run", "--host", "0.0.0.0"]