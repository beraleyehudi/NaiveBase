class Cleaner:
    def __init__(self, df):
        self.__df = self.clean(df.dropna())

    def clean(self, df):
        try:
            df = df.drop('id', axis=1)
        except:
            pass
        finally:
            return df

    @property
    def df(self):
        return self.__df