from UI.prints import Prints
from classifier import Classifier
from cleaner import Cleaner
from coach import Coach
from UI.prints import Prints
from receprtor import Receptor
from tester import Tester

class Functions:
    @staticmethod
    def menu(title: str, options: list):
        valid = False
        choose = None
        print(title, "\n")
        for i in range(len(options)):
            print(f"{i + 1}: {options[i]}")
        while not valid:
            choice = int(input("enter your choice:\n"))
            try:
                choose = options[choice - 1]
            except:
                print(f"please enter a number between 1 and {len(options)}")

        return choose


    @staticmethod
    def switch(option, options, functions, *args):
        return functions[options.index(option)](*args)

    @staticmethod
    def fill(df, classify):
        columns = list(df.columns.drop(classify))
        features = [0 for i in range(len(columns))]
        # exit = False
        # while not exit:
        while columns:
            category = Functions.menu(Prints.CATEGORY, columns)
            feature = Functions.menu(Prints.FEATURE, df[category].unique())
            features[columns.index(category)] = feature
            columns.remove(category)

        print(Prints.RESULT_OF_CLASSIFIER)
        print(Classifier(Coach(df, classify), df.value_counts(classify)).classifies(features))

    @staticmethod
    def test(df, classify):
        print(Prints.ACCURACY_PERCENTAGES)
        print(f'{Tester(df, classify).teke_test()}%')

