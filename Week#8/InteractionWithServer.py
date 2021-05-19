import requests



# Change the url to your deployed AWS server
print(requests.post("http://127.0.0.1:5000/",data='{"heatindex":78.1,"error":-1,"correctlabel":-1}',headers={"Content-type":"application/json","Accept":"test/plain"}).text)


# Error check
print(requests.post("http://127.0.0.1:5000/",data='{"heatindex":78.1,"error":1,"correctlabel":1}',headers={"Content-type":"application/json","Accept":"test/plain"}).text)
print(requests.get("http://127.0.0.1:5000/").text)


# 9 more errors to force training
print(requests.post("http://127.0.0.1:5000/",data='{"heatindex":78.1,"error":1,"correctlabel":1}',headers={"Content-type":"application/json","Accept":"test/plain"}).text)
print(requests.post("http://127.0.0.1:5000/",data='{"heatindex":78.1,"error":1,"correctlabel":1}',headers={"Content-type":"application/json","Accept":"test/plain"}).text)
print(requests.post("http://127.0.0.1:5000/",data='{"heatindex":78.1,"error":1,"correctlabel":1}',headers={"Content-type":"application/json","Accept":"test/plain"}).text)
print(requests.post("http://127.0.0.1:5000/",data='{"heatindex":78.1,"error":1,"correctlabel":1}',headers={"Content-type":"application/json","Accept":"test/plain"}).text)
print(requests.post("http://127.0.0.1:5000/",data='{"heatindex":78.1,"error":1,"correctlabel":1}',headers={"Content-type":"application/json","Accept":"test/plain"}).text)
print(requests.post("http://127.0.0.1:5000/",data='{"heatindex":78.1,"error":1,"correctlabel":1}',headers={"Content-type":"application/json","Accept":"test/plain"}).text)
print(requests.post("http://127.0.0.1:5000/",data='{"heatindex":78.1,"error":1,"correctlabel":1}',headers={"Content-type":"application/json","Accept":"test/plain"}).text)
print(requests.post("http://127.0.0.1:5000/",data='{"heatindex":78.1,"error":1,"correctlabel":1}',headers={"Content-type":"application/json","Accept":"test/plain"}).text)
print(requests.post("http://127.0.0.1:5000/",data='{"heatindex":78.1,"error":1,"correctlabel":1}',headers={"Content-type":"application/json","Accept":"test/plain"}).text)
print(requests.post("http://127.0.0.1:5000/",data='{"heatindex":78.1,"error":1,"correctlabel":1}',headers={"Content-type":"application/json","Accept":"test/plain"}).text)