from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'

database = SQLAlchemy(app)
class Colleges(database.Model):
   SchoolID = database.Column(database.Integer, primary_key = True)
   SchoolName = database.Column(database.String(100))
   City = database.Column(database.String(50))
   
   def __init__(self, Name, City):
        self.SchoolName = Name
        self.City = City

@app.route("/")
def HomePage():
    print(Colleges.query.all())
    if len(Colleges.query.all()) <= 0:
        UCD = Colleges("University of California, Davis","Davis")
        SacState = Colleges("California State University, Sacramento","Sacramento")
        database.session.add(UCD)
        database.session.add(SacState)
        database.session.commit()
    return render_template("index.html",UniData = Colleges.query.all())
    
if __name__ == "__main__":
    database.create_all()
    app.run()