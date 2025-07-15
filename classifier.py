class Classifier:
    def __init__(self, sub_tables, classifiers):
        self.__sub_tables = sub_tables
        self.__classifiers = classifiers
        self.__classifier_proportional = classifiers.sum()



    def calculate_probability(self,args, proportion):

        result = 1
        for i in args:
            result *= i / proportion

        return result * proportion / self.__classifier_proportional


    def probability_of_classifier(self, list_of_features):

        classifiers_and_probability = {}
        for current_classifier in self.__classifiers.index:
            proportion = self.__classifiers[current_classifier]
            values_of_features = []
            for i in range(len(list_of_features)):
                try:
                    values_of_features.append(self.__sub_tables[i][current_classifier][list_of_features[i]])
                except:
                    # print("except")
                    values_of_features.append(1)
                    proportion += 1

            classifiers_and_probability[current_classifier] = self.calculate_probability(values_of_features,
                                                                        proportion)

        return classifiers_and_probability



    def classifies(self, list_of_features):

        d = self.probability_of_classifier(list_of_features)

        return max(d, key=d.get)