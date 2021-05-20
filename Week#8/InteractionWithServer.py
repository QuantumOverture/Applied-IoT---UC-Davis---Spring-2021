import requests


# Change the url to your deployed AWS server
print(requests.post("<Your website>",data='{"heatindex":78.1,"error":-1,"correctlabel":-1}',headers={"Content-type":"application/json","Accept":"test/plain"}).text)

# Error check
for i in range(1,12):
    print(requests.post("<Your website>",data='{"heatindex":78.1,"error":1,"correctlabel":1}',headers={"Content-type":"application/json","Accept":"test/plain"}).text)
