FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the current directory to the /app directory inside the container
COPY . /app/

# Install dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Define the default command to run the Python application
CMD ["python3", "main.py"]
