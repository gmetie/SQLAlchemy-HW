import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station 


session = Session(engine)


app = Flask(__name__)


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/tobs<br/>"
    )

@app.route("/api/v1.0/precipitation")
def prcp():
    
    one_year_ago = dt.datetime(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= one_year_ago).\
    order_by(Measurement.date).all()

    dic = {date: prcp for date, prcp in results}
    
   
    return jsonify(dic)


@app.route("/api/v1.0/precipitation")
def prcp():
    
    one_year_ago = dt.datetime(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.date >= one_year_ago).\
    order_by(Measurement.date).all()

    dic2 = {date: tobs for date, tobs in results}
    
   
    return jsonify(dic2)


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    
    
    stations_results = session.query(Station.station, Station.name).all()
​
    
    all_stations = list(np.ravel(stations_results))
        
    return jsonify(all_stations)








if __name__ == '__main__':
    app.run(debug=True)
