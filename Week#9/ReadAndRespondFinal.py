import RPi.GPIO as GPIO
import time
import threading
import board
import adafruit_dht
import requests
import json

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D18)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4,GPIO.OUT)


Lock = threading.Lock()
heatindex = 0
FanState = False

def SendError(channel):
        global Lock
        global heatindex
        global FanState
        Lock.acquire()
        JSONData = '{{ "heatindex":{},"error":1,"correctlabel":{} }}'.format(heatindex,int(not FanState))
        Lock.release()
        SigResponse = requests.post("http://iottestserver-env.eba-4vmugdcx.us-east-2.elasticbeanstalk.com/",data=JSONData,headers={"Content-type":"application/json","Accept":"test/plain"})
        print(SigResponse.text)

GPIO.add_event_detect(26,GPIO.FALLING ,callback=SendError,bouncetime=500)



while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        T = temperature_c * (9 / 5) + 32
        RH = dhtDevice.humidity
        Lock.acquire()
        heatindex = heatindex = -42.379 + (2.04901523*T) + (10.14333127*RH) - (0.22475541*T*RH) - (0.00683783*T*T) - (0.05481717*RH*RH) + (0.00122874*T*T*RH) + (0.00085282*T*RH*RH) - (0.00000199*T*T*RH*RH)
        Lock.release()
        JSONData = '{{ "heatindex":{},"error":-1,"correctlabel":-1 }}'.format(heatindex)
        SigResponse = requests.post("http://iottestserver-env.eba-4vmugdcx.us-east-2.elasticbeanstalk.com/",data=JSONData,headers={'Content-type':"application/json","Accept":"text/plain"})
        print(JSONData)
        JSONResponse = json.loads(SigResponse.text)
        Lock.acquire()
        if JSONResponse["Fan"] == 1:
            FanState = True
            GPIO.output(4,GPIO.HIGH)
        else:
            FanState = False
            GPIO.output(4,GPIO.LOW)
        Lock.release()            
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        GPIO.cleanup()
        raise error

    time.sleep(2.5)
