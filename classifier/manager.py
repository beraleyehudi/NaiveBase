from classification import Classifier
import requests
import pickle

class Manager:
    def __init__(self):
        self.classifier = Classifier(Manager.get_fit_data(), Manager.get_value_counts())
    
    @staticmethod
    def get_fit_data():
        data_response = requests.get("http://model-runing:8000/get fit data")
        data = pickle.loads(bytes.fromhex(data_response.json()))
  
        return data
        
    
    @staticmethod
    def get_value_counts():
        value_counts_response = requests.get("http://model-runing:8000/get value counts")
        value_count = pickle.loads(bytes.fromhex(value_counts_response.json()))
        return value_count

    
    def classifiication_result(self, string_of_features):
        
        return self.claasifier.classifies(string_of_features.split(","))