import requests
import manager

# print(requests.get("http://localhost:8000/get value counts").json())
# print(requests.get("http://localhost:8000/get fit data").json())
print(manager.Manager.get_data())
print(manager.Manager.get_value_counts())