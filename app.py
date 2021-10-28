import config
import flask
from flask import request, jsonify, make_response, json, render_template
from flask_restful import Resource, Api, reqparse, abort
import pandas as pd
from resources import fetch_data as fd # for fetching data 
#from werkzeug.exceptions import flaskHTTPException

# TO DO: --> Use SQL as a database once its validated on the batch data

app = flask.Flask(__name__)
api = Api(app)
app.config["DEBUG"] = True

# ref data: https://www.data.gouv.fr/fr/datasets/operations-de-construction-et-de-renovation-dans-les-lycees-francilens/#
investments_path = config.PATH

# TO DO: --> add other var once the testing has been validated on the initial batch of data

'''investment_args.add_argument("agent", type=str, help="Name of the company", required=True)
investment_args.add_argument("titreoperation", type=str)
investment_args.add_argument("ppi", type=str, help="Delivery year")
investment_args.add_argument("high school", type=str, help="Name of the operation is required")
investment_args.add_argument("market_notification", type=str, help="Name of the company")
investment_args.add_argument("longitude", type=float, help="Name of the operation is required", required=True)
investment_args.add_argument("progress_state", type=str, help="Name of the company")
investment_args.add_argument("amount_of_ap_votes_en_meu", type=float, help="Delivery year")
investment_args.add_argument("cao_attribution", type=str, help="Name of the operation is required")
investment_args.add_argument("latitude", type=float, help="Name of the company", required=True)
investment_args.add_argument("maitrise_d_oeuvre", type=str, help="Delivery year")
investment_args.add_argument("mode_de_devolution", type=str, help="Delivery year")
investment_args.add_argument("annee_d_individualisation", type=str, help="Name of the operation is required")
investment_args.add_argument("envelope_prev_en_meu", type=float, help="Name of the company", required=True)'''

# class for getting all investments and creating new 
class Investments(Resource):

    def get(self):
        
        data = fd.data(investments_path)
        
        if not isinstance(data, pd.DataFrame):
            #return {'from': 'app.py'}, 500
            abort(500, description = 'Internal server error, data fetching issues!')

        data = data.to_dict()
        
        return data, 200
        #return render_template('index.html',result=data)

    def post(self):

        investment_post_args = reqparse.RequestParser()
        investment_post_args.add_argument("id", type=str, required=True)
        investment_post_args.add_argument("lycee", type=str, required=True)
        investment_post_args.add_argument("ville", type=str, required=True)
        investment_post_args.add_argument("year", type=int, required=True)

        args = investment_post_args.parse_args()

        data = fd.data(investments_path)
        
        if not isinstance(data, pd.DataFrame):
            abort(500, description = 'Internal server error, data fetching issues!')

        if args['id'] in list(data['codeuai']):
            #data = data.to_dict()
            return {'error': 'data already exists'}, 409 #conflict
        else: 
            data_ret = {
                'codeuai': args['id'],
                'lycee': args['lycee'],
                'ville': args['ville'],
                'annee_de_livraison': args['year']
            }
            # TO DO: --> append it to db as well
            # data = data.append(data_ret, ignore_index=True)
            return data_ret, 200
    
    @app.errorhandler(404)
    def error_404(error):
        message = "OOPS!! The requested URL was not found on the server.  Error 404"
        return make_response(jsonify({'error': message}), 404)
  
# for getting investments based on cities
class Investments_ville(Resource):
    def get(self, ville):

        data = fd.data(investments_path)

        if not isinstance(data, pd.DataFrame):
            abort(500, description = 'Internal server error, data fetching issues!')

        # TO DO: --> work on regex to query miscellaneous (lowercase/uppercase/prefix/suffix) string filtering  
        data = data[data['ville'].str.contains(ville)]
        if data.empty:
            return {'error': 'no city found'}, 400 # bad request
        data = data.to_dict() 
        return data, 200

# for getting an investment and updating the existing ones based on Id
class Investments_id(Resource):
    
    def get(self, id):
        
        data = fd.data(investments_path)
        if not isinstance(data, pd.DataFrame):
            abort(500, description = 'Internal server error, data fetching issues!')
        
        data = data[data['codeuai'] == id]  
        if data.empty:
            return {'error': 'no id found'}, 400 # bad request     
        data = data.to_dict() 
        return data, 200

    def patch(self, id):

        investment_patch_args = reqparse.RequestParser()
        investment_patch_args.add_argument("lycee", type=str)
        investment_patch_args.add_argument("ville", type=str)
        investment_patch_args.add_argument("year", type=int)
        args = investment_patch_args.parse_args()

        data = fd.data(investments_path)
        
        if not isinstance(data, pd.DataFrame):
            abort(500, description = 'Internal server error, data fetching issues!')

        new_data = data[data['codeuai'] == id]
        if new_data.empty:
            return {'error': 'no id found'}, 400
        
        if args['lycee']:
            data.loc[data['codeuai'] == id, 'lycee'] = args['lycee']
        if args['ville']:
            data.loc[data['codeuai'] == id, 'ville'] = args['ville']
        if args['year']:
            data.loc[data['codeuai'] == id, 'annee_de_livraison'] = args['year']

        data = data.to_dict()
        # TO DO: --> save the data once the updates are made
        # data.to_csv('Investments.csv', index=False)  # save back to CSV
        return data, 200


api.add_resource(Investments, '/investments')

api.add_resource(Investments_ville, '/investments/city/<string:ville>')

api.add_resource(Investments_id, '/investments/id/<string:id>')


if __name__ == "__main__":
    app.run()
