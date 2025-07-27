import pandas as pd
import requests
import pickle

class Manager:
    # print("Manager class initialized")
    # @staticmethod
    # def reconstruct_data(json_data):
    #     reconstructed = {}
    #     for key, records in json_data.items():
    #      reconstructed[int(key)] = pd.DataFrame(records).set_index("risk")
    #     return reconstructed
    
    @staticmethod
    def get_data():
        data_response = requests.get("http://v1-runing:8000/get fit data")
        data = pickle.loads(bytes.fromhex(data_response.json()))
  
        return data
        
    
    @staticmethod
    def get_value_counts():
        value_counts_response = requests.get("http://v1-runing:8000/get value counts")
        value_count = pickle.loads(bytes.fromhex(value_counts_response.json()))
        return value_count