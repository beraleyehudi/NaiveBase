from data_manage.cleaner import Cleaner
from data_manage.receprtor import Receptor

class Manager:
    
    @staticmethod
    def table_from_csv(csv):
   
        return Cleaner(Receptor(csv).df).df
    
    @staticmethod
    def get_data():
        return Manager.table_from_csv(r'health_generated.csv')
    
    @staticmethod
    def get_value_counts(): 
        df = Manager.get_data()
        target = df.columns[-1]
        return df.value_counts(target).reset_index(name="count").to_dict(orient="records")