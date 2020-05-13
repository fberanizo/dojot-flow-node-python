# Use an official Python runtime as a base image
FROM python:3.6-alpine

RUN apk add build-base linux-headers

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

RUN pip install -r requirements.txt

# Run runner.py when the container launches
ENTRYPOINT ["python", "-u", "main.py"]
CMD []