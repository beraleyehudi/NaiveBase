from classifier import Classifier
from fastapi import FastAPI
from get_data import GetData  

app = FastAPI()

data = GetData.data
value_counts = GetData.value_counts



@app.get("/")
def root():
    return f"this is root"

# @app.get("/test")
# def test():
#     return f'{Prints.ACCURACY_PERCENTAGES}{Tester(df, target).teke_test()}%'

@app.get("/enter features/{features}")
def names(features:str):
    return f"the result of your features, is: {Classifier(data, value_counts).classifies(features.split(','))}"

