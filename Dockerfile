# Use the official Python base image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

COPY . /app

# Create a virtual environment
RUN pip install virtualenv

# Activate env
RUN /bin/bash -c "virtualenv env --python=python3.8"

# Install all the dependencies
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 7755

# Run run.sh when the container launches
CMD ["bash", "run.sh"]