# Base image with Python
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Copy requirements first
COPY req.txt .

# Install packages
RUN pip install --no-cache-dir -r req.txt

# Copy project files
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]