from classifier import Classifier
from data_manage.cleaner import Cleaner
from fit import Fit
from data_manage.receprtor import Receptor
from fastapi import FastAPI
from tester import Tester
from UI.prints import Prints
import requests
import pandas as pd

app = FastAPI()
df = Cleaner(Receptor(r'health_generated.csv').df).df
target = df.columns[-1]

def reconstruct_data(json_data):
    reconstructed = {}
    for key, records in json_data.items():
        reconstructed[int(key)] = pd.DataFrame(records)
    return reconstructed

response = requests.get("http://127.0.0.1/:80/get fit data")
data = reconstruct_data(response.json())



@app.get("/")
def root():
    return f"this is root"

# @app.get("/test")
# def test():
#     return f'{Prints.ACCURACY_PERCENTAGES}{Tester(df, target).teke_test()}%'

@app.get("/enter features/{features}")
def names(features:str):
    return f"the result of your features, is: {Classifier(data, df.value_counts(target)).classifies(features.split(','))}"

