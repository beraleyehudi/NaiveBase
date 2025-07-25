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

@app.get("/test")
def test():
    return f'{Prints.ACCURACY_PERCENTAGES}{Tester(df, target).teke_test()}%'

@app.get("/enter features/{features}")
def names(features:str):
    return f"the result of your features, is: {Classifier(Fit(df, target), df.value_counts(target)).classifies(features.split(','))}"

