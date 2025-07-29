from fastapi import FastAPI
from manager import Manager

app = FastAPI()





@app.get("/")
def root():
    return f"this is root of classifier server"


@app.get("/enter features/{features}")
def names(features:str):
    return f"the result of your features, is: {Manager.classifiication_result(features)}"

