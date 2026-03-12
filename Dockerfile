FROM python:3.11-slim

# Installation of system dependencies for GeoPandas, Fiona, Shapely
RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    libgeos-dev \
    libproj-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Setting of the working directory
WORKDIR /app

# Copy Python dependencies first (for caching)
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . /app/

# Make sure main.py exists here and has `app = FastAPI()`
# Expose port (optional)
EXPOSE 8080


# Start Uvicorn dynamically using PORT
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}"]
