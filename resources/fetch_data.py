# function for fetching data
# (create an SQLAlchemy db, once all the test pass) USE: try-except-finally

import pandas as pd
import sys

def data(investments_path):
    col_list = ['lycee', 'ville', 'annee_de_livraison', 'codeuai']
    try:
        data_inv = pd.read_csv(investments_path, delimiter=';', usecols=col_list)
        data_inv = data_inv[:50]
        return data_inv
    except FileNotFoundError as e:
        #print(e)
        return {'error': str(e)}
    except Exception as e:
        #print(e)
        return {'error': str(e)}

if __name__ == "__main__":
    
    # TO DO: --> make a package __init__.py
    # adding config path to the sys.path, NOT A PYTHONIC WAY TO DO IT!!
    sys.path.append( '/Users/aj/docs/scripts/git/python_rest_api')
    import config
    investments_path = config.PATH 
    d = data(investments_path) 