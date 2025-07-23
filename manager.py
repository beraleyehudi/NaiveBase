from data_manage.cleaner import Cleaner
from UI.prints import Prints
from UI.fuctions import Functions
from UI.data import Data
from data_manage.receprtor import Receptor


class Manager:
    @staticmethod
    def start(csv):
        print(Prints.WELCOME)
        # df = Receptor(input(Prints.enter_file())).df
        df = Manager.get_df(csv)
        classify = Functions.menu(Prints.SELECT_CLASSIFY, df.columns)

        choice = Functions.menu(Prints.WHAT_TO_DO, Data.WHAT_TO_DO_OPTIONS)
        Functions.switch(choice, Data.WHAT_TO_DO_OPTIONS, Data.WHAT_TO_DO_FUNCTIONS, df, classify)

    @staticmethod
    def get_df(csv):
        return Cleaner(Receptor(csv).df).df



