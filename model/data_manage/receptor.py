import pandas as pd
class Receptor:
    def __init__(self, csv):
        self.__df = pd.read_csv(csv)

    @property
    def df(self):
        return self.__df

