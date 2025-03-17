import pandas as pd
import os

def process_csv(file_name):
    
    #file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Feeding Dashboard data.csv")
    df = pd.read_csv(file_name)
    df.dropna(inplace=True)

    a = df[df['referral'] == 1]

    df_list_dict = df.to_dict(orient='records')

    return df_list_dict
