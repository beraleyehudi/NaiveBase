from classifier import Classifier
from fit import Fit
from UI.prints import Prints
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
            valid = True
            try:
                choose = options[choice - 1]
            except:
                print(f"please enter a number between 1 and {len(options)}")

        return choose


    @staticmethod
    def switch(option, options, functions, *args):
        return functions[options.index(option)](*args)

    @staticmethod
    def fill(df, target):
        columns = list(df.columns.drop(target))
        features = [0 for _ in range(len(columns))]
        # exit = False
        # while not exit:
        while columns:
            category = Functions.menu(Prints.CATEGORY, columns)
            feature = Functions.menu(Prints.FEATURE, df[category].unique())
            features[columns.index(category)] = feature
            columns.remove(category)

        print(Prints.RESULT_OF_CLASSIFIER)
        print(Classifier(Fit(df, target), df.value_counts(target)).classifies(features))

    @staticmethod
    def test(df, target):
        print(Prints.ACCURACY_PERCENTAGES)
        print(f'{Tester(df, target).teke_test()}%')

