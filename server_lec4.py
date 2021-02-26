from flask import Flask,request
app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def hello_world():
    if request.method == "POST":
        print(request.data)
        return "GOT IT!"
    elif request.method == "GET":
        return "SEE TERMINAL"

if __name__ == '__main__':
   app.run()
