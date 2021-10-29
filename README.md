# This repo consists the code for developing the rest APIs using Flask in Python

## Project

Paris Region wants to have a web application to track the investments it makes for its high schools buildings. They provided you the [`investments.csv`](data/investments.csv) files containing the existing investments. For more info on the dataset please follow along the [ref](https://www.data.gouv.fr/fr/datasets/operations-de-construction-et-de-renovation-dans-les-lycees-francilens/)


## Folder Contents:
```
rest_api  
  |  
  |---data   
  |     |  
  |     |---investments.csv: The data source which is explored using this API  
  |  
  |---resources    
  |     |
  |     |---fetch_data.py: The python file which fetches the data (also limits the columns and number of rows)
  |
  |---.gitignore: Describes the files and folders which shouldnt be pushed in the repo
  |
  |---Procfile: to serve the live deployment on Heroku
  |
  |---README.md: You are looking at me
  |
  |---app.py: Flask API endpoint script
  |
  |---config.py: contains all the global variables for the module
  |
  |---front.html: This html page renders the '/investments' endpoint 
  |
  |---requirements.txt: List of all necessary packages for the building an env
  |
  |---test.py: performs testing on the endpoints and APIs created.
```  


## General information

To avoid data cluttering certain things have been done: 
- The number of records is kept minimum here (15)
- the number of columns are 4 namely 'ville', 'codeuai', 'lycee', 'annee_de_livraison'  
NOTE: Both these parameters can be modified by going to `resources/fetch_data.py`

Instead of setting up database, I've directly used the .csv file to get the data from and used [pandas](https://pandas.pydata.org/docs/) for data manipulation.


## Building the env and testing   
The taks is performed using Python 3.9.7

### Build
- Clone the repo locally
- Create a virtual env `python3 -m venv rest_api`  
- Activate the env: `source rest_api/bin/activate`  
- Get all the packages: `pip install -r requirements.txt`

### Testing
The app is built in a modular fashion as oppose to monolithic approach, so we'll perform the back-end (APIs) testing and front-end seperately.

#### Back-end APIs
- Open a terminal in the folder and run app.py `python app.py`.  
- Test different endpoints `/investments`: to list all the investments, `/city/<string:city>`: to get all the investments for the city, `/id/<string:id>`: to get a specific investment based on id.  
- Or, the better way of testing all the endpoints is to run `test.py`, which sends different requests (get, post, patch) to all the created endpoints.
- The app is also live deployed on Heroku (PaaS) platform, you can test endpoint on following link as well: https://rest-api-investments.herokuapp.com/investments

#### Front-end
As the monolithic approach was not followed, I am not performing the server side rendering. I've created a separate html file which calls the API and displays the investments in the table, we can also perform the filtering on the displayed data.  

Open the `front.html` file in your browser and you should see the app 
