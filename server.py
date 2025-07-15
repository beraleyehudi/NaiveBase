from typing import Union
from classifier import Classifier
from cleaner import Cleaner
from coach import Coach
from receprtor import Receptor
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return f"this is root"

@app.get("/names/{features}")
def names(features:str):
    df = Cleaner(Receptor(r'table\health_generated.csv').df).df
    return f"the result of your features, is: {Classifier(Coach(df, df.columns[-1]), df.value_counts(df.columns[-1])).classifies(features.split(','))}"

