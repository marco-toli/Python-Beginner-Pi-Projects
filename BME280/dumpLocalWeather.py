import bme280
import smbus2
from time import sleep

port = 1
address = 0x76 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

bme280_data = bme280.sample(bus,address)
humidity  = bme280_data.humidity
pressure  = bme280_data.pressure
ambient_temperature = bme280_data.temperature
print(humidity, pressure, ambient_temperature)
sleep(1)

f = open("/home/pi/Documents/Python-Beginner-Pi-Projects/BME280/meteoLocal.txt", "w")
f.write(
       str(int(ambient_temperature)) + "\n" +
       str(int(pressure)) + "\n" +
       str(int(humidity)) + "\n" )
f.close()

