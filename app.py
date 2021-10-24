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
  },
  {
    "titreoperation" : " Local restructuring released by the CDES " ,
    "company" : " DBS / Societep / CPA " ,
    "delivery_year" : " 2003 " ,
    "city" : " Paris 11th " ,
    "agent" : " SEMAEST " ,
    "number_of_lots" : 3 ,
    "ppi" : " 2001/2006 " ,
    "high school" : " Paul-Poiret " ,
    "market_notification" : " 2000-05-09 " ,
    "codeuai" : " 0750558Z " ,
    "longitude" : 2.375017810000031 ,
    "progress_state" : " Operation delivered " ,
    "amount_of_p_votes_en_meu" : 2.6 ,
    "cao_attribution" : " 2001-11-26 " ,
    "latitude" : 48.85455877800007 ,
    "maitrise_d_oeuvre" : " Boiron " ,
    "mode_de_devolution" : " Separate batches " ,
    "annee_d_individualisation" : " 1999 " ,
    "envelope_prev_en_meu" : 1.98
  },
  {
    "titreoperation" : " Restructuring of the catering service " ,
    "company" : " DBS / IDFC " ,
    "delivery_year" : " 2005 " ,
    "city" : " Paris 16th " ,
    "agent" : " SEMAEST " ,
    "number_of_lots" : 2 ,
    "ppi" : " 2001/2006 " ,
    "high school" : " Octave-Feuillet " ,
    " market_notification " : " 2001-10-05 " ,
    "codeuai" : " 0750796H " ,
    "longitude" : 2.272447646000046 ,
    "progress_state" : " Operation delivered " ,
    "amount_of_ap_votes_en_meu" : 1.87 ,
    "cao_attribution" : " 2002-10-06 " ,
    "latitude" : 48.86126927400005 ,
    "maitrise_d_oeuvre" : " Lescot / Sincoba " ,
    "mode_de_devolution" : " Separate batches " ,
    "annee_d_individualisation" : " 2000 " ,
    "envelope_prev_en_meu" : 1.37
  }
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Archive</h1>
<p>A prototype API for investments.</p>'''


@app.route('/api/v1/resources/investments/all/', methods=['GET'])
def api_all():
    return jsonify(investments)


@app.route('/api/v1/resources/investments', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'codeuai' in request.args:
        codeuai = str(request.args['codeuai'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in investments:
        if investments['codeuai'] == codeuai:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()