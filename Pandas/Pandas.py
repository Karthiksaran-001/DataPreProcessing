import pandas as pd

df = pd.read_csv('Mysqldata.csv')
print(df.head())
print(str("-"*25)+"Tail"+str("-"*25))
print(df.tail())

print(type(df))