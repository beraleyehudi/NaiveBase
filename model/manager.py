from data_manage.cleaner import Cleaner
from data_manage.receptor import Receptor
from fit import Fit

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
        return df.value_counts(target)
    
    @staticmethod
    def get_fit_data():
        df = Manager.get_data()
        target = df.columns[-1]
        return Fit(df, target).get_data_by_categories()