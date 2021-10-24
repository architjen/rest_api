import flask
from flask import request, jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd

app = flask.Flask(__name__)
api = Api(app)
app.config["DEBUG"] = True

investments_path = './data/investments.csv'

# some test data for our catalog in the form of a list of dictionaries.
investments = [
    {
    "titreoperation" : " Renovation of facades, compliance of workshops and creation of students ' homes " ,
    "company" : " Coulon SA " ,
    "delivery_year" : " 2006 " ,
    "city" : " Paris 12th " ,
    "agent" : " SEMAEST " ,
    "ppi" : " 2001/2006 " ,
    "high school" : " Furniture-trades " ,
    "market_notification" : " 2002-10-28 " ,
    "codeuai" : " 0750784V " ,
    "longitude" : 2.391504327000064 ,
    "progress_state" : " Operation delivered " ,
    "amount_of_ap_votes_en_meu" : 1 ,
    "cao_attribution" : " 2005-10-02 " ,
    "latitude" : 48.84675373500005 ,
    "maitrise_d_oeuvre" : " Laumonnier Menninger / SLI " ,
    "mode_de_devolution" : " General Ent " ,
    "annee_d_individualisation" : " 1998 " ,
    "envelope_prev_en_meu" : 0.43
  }]

class Investments(Resource):
    def get(self):
        data = pd.read_csv(investments_path, delimiter=';')
        data = data[:5].to_dict()
        return {'data': data}, 200
        

api.add_resource(Investments, '/investments')

if __name__ == "__main__":
    app.run()
