# Use basic image of Python
FROM python:3.11

# Setting working directory in container
WORKDIR /app

# Copy dependencies in container
COPY requirements.txt .

# Setting dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project in container
COPY . .

# Default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]