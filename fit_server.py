from classifier import Classifier
from data_manage.cleaner import Cleaner
from fit import Fit
from data_manage.receprtor import Receptor
from fastapi import FastAPI
from tester import Tester
from UI.prints import Prints

app = FastAPI()

df = Cleaner(Receptor(r'health_generated.csv').df).df
target = df.columns[-1]




@app.get("/")
def root():
    return f"this is root"

@app.get("/get fit data")
def get_fit_data():
    return Fit(df, target).get_data_by_categories()

