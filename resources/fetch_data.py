# function for fetching data
# (create an SQLAlchemy db, once all the test pass) USE: try-except-finally

import pandas as pd

def data(investments_path):
    col_list = ['lycee', 'ville', 'annee_de_livraison', 'codeuai']
    try:
        data_inv = pd.read_csv(investments_path, delimiter=';', usecols=col_list)
        data_inv = data_inv[:5]
        return data_inv
    except FileNotFoundError as e:
        print(e)
        return None
    except Exception as e:
        print(e)
        return None

if __name__ == "__main__":
    investments_path = './data/investments.csv'
    d = data(investments_path) 