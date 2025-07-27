from fit import Fit
from fastapi import FastAPI
from manager import Manager
import pickle
import pandas as pd

app = FastAPI()




@app.get("/")
def root():
    return f"this is root of v1 server"

@app.get("/get value counts")
def get_value_counts():
    return pickle.dumps(Manager.get_value_counts()).hex()
    

@app.get("/get fit data")
def get_fit_data():
    df = Manager.get_data()
    target = df.columns[-1]
    
    return pickle.dumps(Fit(df, target).get_data_by_categories()).hex()
    
       
    




