import pandas as pd
df = pd.read_csv(r'C:\Users\User\Desktop\csv\buys_computer2.csv')
print(df)
print(df.iloc[:len(df) *70 // 100])
print(df.iloc[len(df) * 70 // 100:])
print(df.iloc[1].values)
# df = df.drop(df.columns[0], axis=1)
print(df.columns)

# for i in range(len(df) * 70 // 100):
#     print(df.drop(df.columns[0], axis=1).iloc[i].values)