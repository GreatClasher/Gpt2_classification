# Use the official Python base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
# COPY requirements.txt .

# Install the Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y git
RUN pip install uvicorn
RUN pip install fastAPI
RUN pip install -q git+https://github.com/huggingface/transformers.git
RUN pip install -q git+https://github.com/gmihaila/ml_things.git
RUN pip install torch

# Copy the rest of the application code into the container
COPY . .

# Expose the port on which the FastAPI server will run (change if needed)
EXPOSE 8000

# Start the FastAPI server when the container is run
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
