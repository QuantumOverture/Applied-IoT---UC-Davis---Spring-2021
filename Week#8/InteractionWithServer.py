import requests


JSONData = '{"heatindex":78.1,"error":-1,"correctlabel":-1}'

requests.post("",data=JSONData,headers={"Content-type":"application/json","Accept":"test/plain"})