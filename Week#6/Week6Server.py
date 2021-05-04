from flask import Flask,request
import json
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from scipy.stats import zmap


app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/<USERNAME>/mysite/APPDATA.sqlite3'

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

        # You would not do the following in production:
        # You would have all the elements of the z-score calculation "cached" and only change it when needed
        return '{{ "Z-Score":{} }}'.format(zmap(JsonData["heatindex"],[RowObj.HeatIndex for RowObj in TempHumidityHeatIndex.query.all()]))
    elif request.method == "GET":
        return render_template("index.html",WeatherData = TempHumidityHeatIndex.query.all())

if __name__ == '__main__':
    database.create_all()
    app.run()
                                                                                                                  
