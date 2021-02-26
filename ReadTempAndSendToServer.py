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
        JSONData  = '{{ temperature:{}, humidity:{},heatindex:{} }}'.format(temperature, humidity,heatindex)
        print(JSONData)
        requests.post("http://ff4af2eff58c.ngrok.io",data=JSONData,headers={"Content-type":"application/json","Accept":"test/plain"})
    else:
      print('Failed to get reading from the sensor. Try again!')
      exit(1)

    sleep(3)
