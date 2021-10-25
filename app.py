import flask
from flask import request, jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd

app = flask.Flask(__name__)
api = Api(app)
app.config["DEBUG"] = True

# ref data: https://www.data.gouv.fr/fr/datasets/operations-de-construction-et-de-renovation-dans-les-lycees-francilens/#
investments_path = './data/investments.csv'


investment_put_args = reqparse.RequestParser()
investment_put_args.add_argument("lycee", required=True)
investment_put_args.add_argument("annee_de_livraison", required=True)
investment_put_args.add_argument("ville", required=True)
investment_put_args.add_argument("titreoperation", type=str, help="Name of the operation is required", required=True)
investment_put_args.add_argument("codeuai", type=str, required=True)

'''investment_put_args.add_argument("agent", type=str, help="Name of the company", required=True)
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

class Investments(Resource):
    def get(self):
        # add try - error
        col_list = ['titreoperation', 'lycee', 'ville', 'annee_de_livraison', 'codeuai']
        data = pd.read_csv(investments_path, delimiter=';', usecols=col_list)        
        data = data[:5].to_dict() # getting only 5 top data
        return {'data': data}, 200 
    
    def post(self):
        #return {'data': 'test'}

        args = investment_put_args.parse_args()  # parse arguments to dictionary

        # read our CSV
        data = pd.read_csv('users.csv')

        return {'data': 'test'}
            
        '''if args['company'] in list(data['entreprise']):
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

if __name__ == "__main__":
    app.run()
