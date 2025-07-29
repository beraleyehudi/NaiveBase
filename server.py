from fastapi import FastAPI
from manager import Manager

app = FastAPI()
@app.get("/")
def root():
    return f"this is root of naive base (v1) server"

@app.get("/enter features/{string_of_features}")
def enter_features(string_of_features: str):
    """
    Endpoint to classify the input features.
    :param string_of_features: Comma-separated string of features.
    :return: Classification result.
    """
    return f"the result of these features, is: {Manager.classifiication_result(string_of_features)}"