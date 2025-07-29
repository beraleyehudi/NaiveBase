from model.data_manage.cleaner import Cleaner
from model.data_manage.receptor import Receptor
from model.fit import Fit
from classifier.classifier import Classifier

class Manager:
    
    @staticmethod
    def table_from_csv(csv):
   
        return Cleaner(Receptor(csv).df).df
    
    @staticmethod
    def get_data():
        return Manager.table_from_csv(r'model/health_generated.csv')
    
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
    
    @staticmethod
    def classifiication_result(string_of_features):
        fit_data = Manager.get_fit_data()
        value_counts = Manager.get_value_counts()
        return Classifier(fit_data, value_counts).classifies(string_of_features.split(","))