from classification import Classifier
import requests
import pickle

class Manager:
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

    @staticmethod
    def classifiication_result(string_of_features):
        fit_data = Manager.get_fit_data()
        value_counts = Manager.get_value_counts()
        return Classifier(fit_data, value_counts).classifies(string_of_features.split(","))