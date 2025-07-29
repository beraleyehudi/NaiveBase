from fastapi import FastAPI
from manager import Manager
import pickle


app = FastAPI()




@app.get("/")
def root():
    return f"this is root of model server"

@app.get("/get value counts")
def get_value_counts():
    """
    Endpoint to get value counts of the target column.
    :return: Value counts in hex format."""
    return pickle.dumps(Manager.get_value_counts()).hex()
    

@app.get("/get fit data")
def get_fit_data():
    """
    Endpoint to get fit data.
    :return: Fit data in hex format."""
    return pickle.dumps(Manager.get_fit_data()).hex()

    
       
    




