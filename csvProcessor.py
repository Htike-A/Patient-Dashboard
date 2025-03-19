import pandas as pd
import os

import joblib
import pandas as pd

def display_csv():
    #file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Feeding Dashboard data.csv")
    df = pd.read_csv('csv/Feeding Dashboard data.csv')
    df = df.fillna(0)
    return df.to_dict(orient='records')

def process_csv(file_name):
    
    #file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Feeding Dashboard data.csv")
    new_data = pd.read_csv(file_name)

    Ids = new_data['encounterId']

    new_data=new_data.drop(['referral', 'encounterId'], axis = 1)

    new_data = new_data.fillna(0)


    pipeline = joblib.load('trained_pipeline.pkl')

    new_data['referral'] = pipeline.predict(new_data)
    new_data.insert(0, 'encounterId', Ids)
    new_data_dict = new_data.to_dict(orient='records')

    return new_data_dict
