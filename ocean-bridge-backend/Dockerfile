# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY agl-python-helpers /app/agl-python-helpers
RUN pip3 install --user --upgrade pip
RUN chmod -R 777 /app/agl-python-helpers
RUN chmod -R +x /app/agl-python-helpers
RUN pip3 install /app/agl-python-helpers --no-cache-dir --user

# Copy the rest of the application code to the container
COPY . .


# Expose the port that the application will run on
EXPOSE 80

# Start the application using the "uvicorn" ASGI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--ssl-version", "tls1.2", "--ssl-keyfile", "/etc/ssl/private/key.key", "--ssl-certfile", "/etc/ssl/certs/cert.crt"]

#change file name