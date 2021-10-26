# function for fetching data
# (create a SQLAlchemy db, once all the test passes) 

import pandas as pd

investments_path = './data/investments.csv'

def data(investments_path):
    col_list = ['titreoperation', 'lycee', 'ville', 'annee_de_livraison', 'codeuai']
    data = pd.read_csv(investments_path, delimiter=';', usecols=col_list)
    data = data[:5]
    return data

if __name__ == "__main__":
    investments_path = './data/investments.csv'
    d = data(investments_path) 