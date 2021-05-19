from flask import Flask,request
import json
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
import numpy as np
from tensorflow.keras.models import save_model
from tensorflow.keras.models import load_model

application = Flask(__name__)

application.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///APPDATAErrors.sqlite3'

database = SQLAlchemy(application)
class HeatIndexErrors(database.Model):
    SendID = database.Column(database.Integer, primary_key = True)
    HeatIndex = database.Column(database.Integer)
    CorrectLabel = database.Column(database.Integer) #  0 off | 1 on

    def __init__(self, HeatIndexSent, LabelSent):
        self.HeatIndex = HeatIndexSent
        self.CorrectLabel= LabelSent


@application.route('/',methods=["POST","GET"])
def StoreOrDisplayData(): # JsonData -> Error,heatindex,correctlabel
    if request.method == "POST":
        JsonData = json.loads(request.data)
        
        if JsonData["error"] == 1:
        
            database.session.add(HeatIndexErrors(JsonData["heatindex"],JsonData["correctlabel"]))
            database.session.commit()
            if  len(HeatIndexErrors.query.all()) >= 10:
                NNetNew = load_model("NNetFiles")
                DatabaseResponse = HeatIndexErrors.query.all()
                X = [[Value.HeatIndex] for Value in DatabaseResponse]
                Y = [Value.CorrectLabel for Value in DatabaseResponse]
                # Parse Input -> get labels and values then compile
                NNetNew.fit(X,Y,epochs=2,batch_size=2)
                save_model(NNetNew,"NNetFiles")
                # Clear Database
                database.session.query(HeatIndexErrors).delete()
                database.session.commit()
                return "Retrained model"
            else:
                return "Recieved Error.Current Errors: {}. Retraining starts at 10.".format(len(HeatIndexErrors.query.all()))
            
        else:
            NNet = load_model("NNetFiles")
            if NNet.predict_classes([[JsonData["heatindex"]]]) == 1:
              return '{ "Fan": 1 }'
            else:
              return '{ "Fan": 0 }'
              
    elif request.method == "GET":
        return render_template("index.html",WeatherData = HeatIndexErrors.query.all())

if __name__ == '__main__':
    database.create_all()
    application.run()