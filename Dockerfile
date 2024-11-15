FROM python:3.12-slim

COPY requirements.txt .

ADD temperature_humidity_aht20.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "temperature_humidity_aht20.py"]
