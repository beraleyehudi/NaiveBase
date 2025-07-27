from fit import Fit
from fastapi import FastAPI
from manager import Manager
import pickle

app = FastAPI()




@app.get("/")
def root():
    return f"this is root of v1 server"

@app.get("/get value counts")
def get_value_counts():
    with open("value_counts.pkl", "wb") as file:
        value_counts = pickle.dump(Manager.get_value_counts, file)
    return value_counts

@app.get("/get fit data")
def get_fit_data():
    df = Manager.get_data()
    target = df.columns[-1]
    with open("fit_data.pkl", "wb") as file:
        fit_data = pickle.dump(Fit(df, target).get_data_by_categories(), file)
    return fit_data



