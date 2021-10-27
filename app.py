import flask
from flask import request, jsonify, make_response
from flask_restful import Resource, Api, reqparse
import pandas as pd
from resources import fetch_data as fd # for fetching data 

# TO DO: Use SQL as a database once its validated on the batch data (TIPS: MongoDB)

app = flask.Flask(__name__)
api = Api(app)
app.config["DEBUG"] = True

# ref data: https://www.data.gouv.fr/fr/datasets/operations-de-construction-et-de-renovation-dans-les-lycees-francilens/#
investments_path = './data/investments.csv'

'''investment_put_args = reqparse.RequestParser()
investment_put_args.add_argument("lycee", type=str, required=True)
investment_put_args.add_argument("annee_de_livraison", type=int)
investment_put_args.add_argument("ville", type=str, required=True)
investment_put_args.add_argument("codeuai", type=str, required=True)'''

# TO DO: add these once the testing has been validated on the initial batch of data

'''investment_put_args.add_argument("agent", type=str, help="Name of the company", required=True)
investment_put_args.add_argument("titreoperation", type=str)
investment_put_args.add_argument("ppi", type=str, help="Delivery year")
investment_put_args.add_argument("high school", type=str, help="Name of the operation is required")
investment_put_args.add_argument("market_notification", type=str, help="Name of the company")
investment_put_args.add_argument("longitude", type=float, help="Name of the operation is required", required=True)
investment_put_args.add_argument("progress_state", type=str, help="Name of the company")
investment_put_args.add_argument("amount_of_ap_votes_en_meu", type=float, help="Delivery year")
investment_put_args.add_argument("cao_attribution", type=str, help="Name of the operation is required")
investment_put_args.add_argument("latitude", type=float, help="Name of the company", required=True)
investment_put_args.add_argument("maitrise_d_oeuvre", type=str, help="Delivery year")
investment_put_args.add_argument("mode_de_devolution", type=str, help="Delivery year")
investment_put_args.add_argument("annee_d_individualisation", type=str, help="Name of the operation is required")
investment_put_args.add_argument("envelope_prev_en_meu", type=float, help="Name of the company", required=True)'''

# for getting all investments
class Investments(Resource):
    def get(self):
        # TO DO: add try - error
        data = fd.data(investments_path)
        data = data.to_dict() # getting only 5 top data
        return data, 200 

    def post(self):

        investment_put_args = reqparse.RequestParser()
        investment_put_args.add_argument("id", type=str, required=True)
        investment_put_args.add_argument("lycee", type=str, required=True)
        investment_put_args.add_argument("ville", type=str, required=True)
        investment_put_args.add_argument("year", type=int, required=True)

        args = investment_put_args.parse_args()

        data = fd.data(investments_path)
        if args['id'] in list(data['codeuai']):
            #data = data.to_dict()
            return {'data': 'id already exists'}, 409 # conflict
        else: 
            data_ret = {
                'codeuai': args['id'],
                'lycee': args['lycee'],
                'ville': args['ville'],
                'annee_de_livraison': args['year']
            }
            return data_ret, 200
    
    @app.errorhandler(404)
    def error_404(error):
        message = "OOPS!! The requested URL was not found on the server.  Error 404!"
        return make_response(jsonify({'error': message}), 404)

# for getting investments based on cities
class Investments_ville(Resource):
    def get(self, ville):
        # TO DO: add try - error
        data = fd.data(investments_path)
        data = data[data['ville'].str.contains(ville)]       
        data = data.to_dict() 
        return data, 200

# for getting an investment based on Id
class Investments_id(Resource):
    # TO DO: add try error
    def get(self, id):
        data = fd.data(investments_path)
        data = data[data['codeuai'] == id]       
        data = data.to_dict() 
        return data, 200

    '''args = investment_put_args.parse_args()  # parse arguments to dictionary

        # read our CSV
        data = pd.read_csv('users.csv')

        return {'data': 'test'}
            
        if args['company'] in list(data['entreprise']):
            return {
                'message': f"'{args['userId']}' already exists."
            }, 401
        
        else:
            # create new dataframe containing new values
            new_data = pd.DataFrame({
                'entreprise': args['company'],
                'annee_de_livraison': args['delivery_year'],
                'ville': args['city']
            })

            # add the newly provided values
            data = data.append(new_data, ignore_index=True)
            data.to_csv('users.csv', index=False)  # save back to CSV
            return {'data': data.to_dict()}, 200  # return data with 200 OK'''

api.add_resource(Investments, '/investments')

api.add_resource(Investments_ville, '/investments/city/<string:ville>')

api.add_resource(Investments_id, '/investments/id/<string:id>')


if __name__ == "__main__":
    app.run()
