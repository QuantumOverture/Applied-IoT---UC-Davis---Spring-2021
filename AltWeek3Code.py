# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_dht
import requests

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D18)


while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        T = temperature_c * (9 / 5) + 32
        RH = dhtDevice.humidity
        heatindex = heatindex = -42.379 + (2.04901523*T) + (10.14333127*RH) - (0.22475541*T*RH) - (0.00683783*T*T) - (0.05481717*RH*RH) + (0.00122874*T*T*RH) + (0.00085282*T*RH*RH) - (0.00000199*T*T*RH*RH)
        JSONData = "{{ temperature:{},humidity:{},heatindex:{} }}".format(T,RH,heatindex)
        requests.post("<WEBHOOK URL HERE>",data=JSONData,headers={'Content-type':"application/json","Accept":"text/plain"})
        print(JSONData)
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.5)
