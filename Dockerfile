FROM python:3.12-slim

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libffi-dev \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ADD requirements.txt .

ADD temperature_humidity_aht20.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "temperature_humidity_aht20.py"]