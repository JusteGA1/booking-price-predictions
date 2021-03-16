# Price prediction app

App is intended for predicting price of hotels in Vilnius, Lithuania. All requests and responses are saved to database. 
Model was trained on Booking.com data (March-May, 2021) and can predict price by given parameters: stars (from 3 to 5), longitude,  latitude, distance to the centre, review score and review amount. Trained model is saved to _model.pkl_ file. 

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Code Examples](#code-examples)
* [Status](#status)
* [License](#license)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
App was written for learning purposes.  

- Flask app (_app.py_ file) has two routes:
    * POST (../predict) route to reach model and send its outputs as a response;  
For prediction mandatory fields are longitude, latitude, distance, review score and review amount. Stars are optional.   
Prediction data is processed with input_processor.py file in utils folder.
    * GET (../last_requests) route to return most recent requests and responses in JSON format. Returns 10 as default but can be any number if specified.  
    
- Database:
There is a class database for creating a database structure and adding/extracting items. 

## Technologies
* Python - version 3.8
* Flask - version 1.1.2
* psycopg2-binary - version 2.8.6
* numpy - version 1.19.5
   
_for more please read requirements.txt_

## Setup
- Create a PostgreSQL database on Heroku
- Add database credentials to .env file (you can use .env.example as a reference) 
- Run `pip install -r requirements.txt` to install project requirements
- Run `python database/database.py` to create a database structure and add initial categories 
- Run Flask to run an app

## Code Examples
```python
features_for_prediction = {"inputs":
                           [
                               {"longitude": 25.285243, 
                               "latitude": 54.685095,
                               "distance": 300,
                               "review_score": 8.3,
                               "review_amount": 3006,
                               "stars3": 0.0,
                               "stars4": 1.0,
                               "stars5": 0.0}
                           ]
                          }

response = requests.post(predict_url, json.dumps(features_for_prediction))
print (f"response: {json.loads(response.content)}")
```

## Status
Project is: _finished_

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Inspiration
Learning @Turing College

## Contact
Created by [Juste Gaviene](mailto:juste.gaviene@gmail.com?subject=[GitHub]%20Source%20Han%20Sans)
