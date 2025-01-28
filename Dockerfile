# Base image
FROM python:3.9-slim AS base

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Backend image
FROM base AS backend

WORKDIR /app

# Copy backend code
COPY app/ ./app/

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# UI image
FROM base AS ui

WORKDIR /app

# Copy UI code
COPY ui/ ./ui/

EXPOSE 8501

CMD ["streamlit", "run", "ui/app.py", "--server.port=8501", "--server.address=0.0.0.0"]