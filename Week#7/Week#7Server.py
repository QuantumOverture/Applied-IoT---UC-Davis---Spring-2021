from flask import Flask,request
import json
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
import tensorflow as tf
import numpy as np


app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/<USER>/mysite/APPDATA.sqlite3'

database = SQLAlchemy(app)
class TempHumidityHeatIndex(database.Model):
    SendID = database.Column(database.Integer, primary_key = True)
    Temp = database.Column(database.Integer)
    HeatIndex = database.Column(database.Integer)
    Humidity = database.Column(database.Integer)

    def __init__(self, TempSent, HeatIndexSent, HumiditySent):
        self.Temp = TempSent
        self.HeatIndex = HeatIndexSent
        self.Humidity = HumiditySent


@app.route('/',methods=["POST","GET"])
def StoreOrDisplayData():
    if request.method == "POST":
        JsonData = json.loads(request.data)
        print(JsonData)
        database.session.add(TempHumidityHeatIndex(JsonData["temperature"],JsonData["heatindex"],JsonData["humidity"]))
        database.session.commit()

        interpreter = tf.lite.Interpreter(model_path="/home/<USER>/mysite/model.tflite.temphumid")
        interpreter.allocate_tensors()
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        # Test the model on random input data.
        # This is the first row of data
        input_data = np.array([[float(JsonData["heatindex"])]], dtype=np.float32)
        interpreter.set_tensor(input_details[0]['index'], input_data)

        # Run model
        interpreter.invoke()


        # Collect data
        output_data = interpreter.get_tensor(output_details[0]['index'])
        print("Class: ",end="")
        if output_data[0] >= 0.5:
          return '{ "Fan": 1 }'
        else:
          return '{ "Fan": 0 }'

    elif request.method == "GET":
        return render_template("index.html",WeatherData = TempHumidityHeatIndex.query.all())

if __name__ == '__main__':
    database.create_all()
    app.run()