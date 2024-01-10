# Use an official Python runtime as a parent image
FROM python:3.9-slim as sentiment

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy only what we need
COPY docker_requirements.txt .

# Install required packages
RUN pip install --no-cache-dir -r docker_requirements.txt

# Remove the requirements file after installing packages
RUN rm docker_requirements.txt

# Copy the rest of the current directory contents into the container at /usr/src/app
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Define environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run your_script.py when the container launches
CMD ["flask", "run"]
