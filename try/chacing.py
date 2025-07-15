import pandas as pd
import try_2
def checks(df2):
    true = 0
    false = 0
    for i in df2.values:
        if try_2.max_classifier(try_2.classifier(i[:-1])) == i[-1]:
            true += 1
        else:
            false += 1

    return true/(true+false)*100

df = pd.read_csv(r'../table/health_generated.csv')
print(f"{checks(df.iloc[len(df) * 70 // 100:])} %")

