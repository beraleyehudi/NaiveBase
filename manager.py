from classifier import Classifier
from cleaner import Cleaner
from coach import Coach
from UI.prints import Prints
from UI.fuctions import Functions
from UI.data import Data
from receprtor import Receptor
from tester import Tester


class Manager:
    @staticmethod
    def start(csv):
        print(Prints.WELCOME)
        # df = Receptor(input(Prints.enter_file())).df
        df = Cleaner(Receptor(csv).df).df
        classify = Functions.menu(Prints.SELECT_CLASSIFY, df.columns)

        choice = Functions.menu(Prints.WHAT_TO_DO, Data.WHAT_TO_DO_OPTIONS)
        Functions.switch(choice, Data.WHAT_TO_DO_OPTIONS, Data.WHAT_TO_DO_FUNCTIONS, df, classify)

