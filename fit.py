class Fit:
    def __init__(self, df, target):
        self.__df = df
        self.__target = target
        self.__columns = df.columns.drop(self.__target)




    # def get_data_by_categories(self):
    #     dictionary = {}
    #     for i in range(len(self.__columns)):
    #         dictionary[i] = self.__df.groupby(self.__target)[self.__columns[i]].value_counts()
    #
    #     return dictionary

    def get_data_by_categories(self):
        dictionary = {}
        for i in range(len(self.__columns)):
            series = self.__df.groupby(self.__target)[self.__columns[i]].value_counts()
            df = series.reset_index(name="count")  # נהפוך לסוג DataFrame שטוח
            dictionary[i] = df.to_dict(orient="records")  # JSON-ידידותי
        return dictionary

