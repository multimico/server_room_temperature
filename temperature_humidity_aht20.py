#!/usr/bin/env python
#
# Library for Grove - I2C Industrial Grade Temperature & Humidity Sensor (AHT20)
# (https://wiki.seeedstudio.com/Grove-AHT20-I2C-Industrial-Grade-Temperature&Humidity-Sensor/)



import time
from grove.i2c import Bus
import smbus2
from influxdb_client import InfluxDBClient, Point, WriteOptions

class GroveTemperatureHumidityAHT20(object):
    def __init__(self, address=0x38, bus=1):
        self.address = address

        # I2C bus
        self.bus = smbus2.SMBus(1)

    def read(self):
        self.bus.write_i2c_block_data(self.address, 0x00, [0xac, 0x33, 0x00])

        # measurement duration < 16 ms
        time.sleep(0.016)

        data = self.bus.read_i2c_block_data(self.address, 0x00, 6)

        humidity = data[1]
        humidity <<= 8
        humidity += data[2]
        humidity <<= 4
        humidity += (data[3] >> 4)
        humidity /= 1048576.0
        humidity *= 100

        temperature = data[3] & 0x0f
        temperature <<= 8
        temperature += data[4]
        temperature <<= 8
        temperature += data[5]
        temperature = temperature / 1048576.0*200.0-50.0  # Convert to Celsius

        return temperature, humidity


def main():
    bucket = "server_room_temperatur"
    org = "gs" 
    token = "4vyu6-wrsop1GtYk4aAH1IeX8lJD0ky4OSgQZ7urU04XXtvEBoMC4ePTZ4AIkQq4kxPD75SUzuoKEI8HYhAA1g=="  
    url = "http://160.85.84.78:8086/"

    # Initialize the InfluxDB client
    client = InfluxDBClient(url=url, token=token, org=org)
    write_api = client.write_api(write_options=WriteOptions(batch_size=1))
    sensor = GroveTemperatureHumidityAHT20()
    while True:
        temperature, humidity  = sensor.read()

        print('Temperature in Celsius is {:.2f} C'.format(temperature))
        print('Relative Humidity is {:.2f} %'.format(humidity))
	# Create a data point for InfluxDB
        point = (
            Point("environmental_data")
            .field("temperature", temperature)
            .field("humidity", humidity)
        )
        # Write the data point to InfluxDB
        write_api.write(bucket=bucket, record=point)

        time.sleep(1)


if __name__ == "__main__":
    main()
