class Coach:
    def __init__(self, df, target):
        self.__df = df
        self.__target = target
        self.__columns = df.columns.drop(self.__target)




    def get_data_by_categories(self):
        dictionary = {}
        for i in range(len(self.__columns)):
            dictionary[i] = self.__df.groupby(self.__target)[self.__columns[i]].value_counts()

        return dictionary

