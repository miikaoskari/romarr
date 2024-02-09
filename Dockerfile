# Use an official Python runtime as a parent image
FROM python:3.12.1-alpine

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Node.js and npm
RUN apk add --update nodejs npm

# Copy frontend directory and install dependencies
COPY frontend/ ./frontend/
WORKDIR /app/frontend
RUN npm install

# Build the frontend
RUN npm run build

# Switch back to the main directory
WORKDIR /app

# Make port 80 available to the world outside this container
EXPOSE 8000

# Run main.py when the container launches
CMD ["python", "src/main.py"]