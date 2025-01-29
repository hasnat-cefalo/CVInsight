# Base image
FROM python:3.10-slim AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libblas-dev \
    liblapack-dev \
    cython3 \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY .env .env
# Install the spaCy model (replace `en_core_web_sm` with the model you need)
#RUN python -m spacy download en_core_web_sm

# Backend image
FROM base AS backend

# Copy backend code
COPY app/ ./app/

# Run as non-root user
RUN useradd -m cefalo
USER cefalo

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# UI image
FROM base AS ui

# Copy UI code
COPY ui/ ./ui/

# Run as non-root user
RUN useradd -m cefalo
USER cefalo

EXPOSE 8501

CMD ["streamlit", "run", "ui/app.py", "--server.port=8501", "--server.address=0.0.0.0"]