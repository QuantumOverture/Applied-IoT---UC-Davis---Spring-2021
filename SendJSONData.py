# Citations
# https://www.freva.com/2019/05/22/dht11-temperature-and-humidity-sensor-on-raspberry-pi/
# https://www.wpc.ncep.noaa.gov/html/heatindex_equation.shtml
# https://stackoverflow.com/questions/5466451/how-can-i-print-literal-curly-brace-characters-in-a-string-and-also-use-format
# https://stackoverflow.com/questions/9733638/how-to-post-json-data-with-python-requests

import Adafruit_DHT
from time import sleep
import requests
sensor = Adafruit_DHT.DHT11
DHT11_pin = 4

while(True):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT11_pin)
    if humidity is not None and temperature is not None:
        T = (temperature * (9/5)) + 32
        RH = humidity
        heatindex = -42.379 + (2.04901523*T) + (10.14333127*RH) - (0.22475541*T*RH) - (0.00683783*T*T) - (0.05481717*RH*RH) + (0.00122874*T*T*RH) + (0.00085282*T*RH*RH) - (0.00000199*T*T*RH*RH)
        JSONData  = '{{ "temperature":{}, "humidity":{}, "heatindex":{} }}'.format(temperature, humidity,heatindex)
        requests.post("<Enter web hook URL here>",data=JSONData,headers={"Content-type":"application/json","Accept":"text/plain"})
        print(JSONData)
    else:
      print('Failed to get reading from the sensor. Try again!')
      exit(1)

    sleep(3)
