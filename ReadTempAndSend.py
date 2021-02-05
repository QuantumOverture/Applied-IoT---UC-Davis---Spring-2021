# Citations:
# https://www.freva.com/2019/05/22/dht11-temperature-and-humidity-sensor-on-raspberry-pi/


import Adafruit_DHT
from time import sleep
sensor = Adafruit_DHT.DHT11
DHT11_pin = 4

while(True):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT11_pin)
    
    if humidity is not None and temperature is not None:
      print('Temperature={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
      print('Failed to get reading from the sensor. Try again!')
      exit(1)

    sleep(5)
