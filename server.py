from fit import Fit
from fastapi import FastAPI
from manager import Manager

app = FastAPI()




@app.get("/")
def root():
    return f"this is root of v1 server"

@app.get("/get value counts")
def get_value_counts():
    return Manager.get_value_counts()

@app.get("/get fit data")
def get_fit_data():
    df = Manager.get_data()
    target = df.columns[-1]
    return Fit(df, target).get_data_modle()



