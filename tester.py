from classifier import Classifier
from coach import Coach



class Tester:
    def __init__(self, df, target):
        # self.__df = df
        # self.__classifier = df.value_counts(target)
        # self.__practice = df.iloc[:len(df) * 70 // 100]
        # self.__test = df.iloc[len(df) * 70 // 100:]
        self.__random = df.sample(frac=0.7)
        self.__practice = self.__random
        self.__test = df.drop(self.__random.index)
        self.__coach = Coach(self.__practice, target).get_data_by_categories()
        self.__classifier_class = Classifier(self.__coach, df.value_counts(target))




    def teke_test(self):
        true = 0
        false = 0
        for i in self.__test.values:
            if self.__classifier_class.classifies(i[:-1]) == i[-1]:
                true += 1
            else:
                false += 1

        return true / (true + false) * 100




