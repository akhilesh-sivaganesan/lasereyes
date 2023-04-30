# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /

# Copy the current directory contents into the container at /app
COPY . /

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Expose port 5000 for Flask app to listen on
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=my_script.py

# Run the command to start the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
