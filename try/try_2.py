import pandas as pd


def max_classifier(d):
    return max(d, key=d.get)

df = pd.read_csv(r'../table/health_generated.csv')
df = df.iloc[:len(df) * 70 // 100]

columns = df.columns
def create_dict_of_sub_tables_by_columns(df, columns, classifier):
    dictionary1 = {}

    for i in range(len(columns)):
        dictionary1[i] = df.groupby(classifier)[columns[i]].value_counts()

    return dictionary1

dictionary_of_sub_tables = create_dict_of_sub_tables_by_columns(df, columns[:-1], columns[-1])
classifier_and_its_value = df.value_counts(columns[-1])
classifier_proportional = len(df)

def calculate(args, proportion):
    # print(args, proportion)

    result = 1
    for i in args:
        result *= i/proportion

    return result * proportion / classifier_proportional


def classifier(list_of_features):
    classifiers_and_probability = {}
    for current_classifier in classifier_and_its_value.index:
        # print(current_classifier)
        proportion = classifier_and_its_value[current_classifier]
        values = []
        for i in range(len(list_of_features)):

            try:
                values.append(dictionary_of_sub_tables[i][current_classifier][list_of_features[i]])
            except:
                # print("except")
                values.append(1)
                proportion += 1

        classifiers_and_probability[current_classifier] = calculate(values, proportion)

    return classifiers_and_probability

# finaly = classifier(('>40','high', 'no', 'fair'))
# print(finaly, max_classifier(finaly))




