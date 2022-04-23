import pandas as pd 

df = pd.read_csv('data.csv')

df2 = df[(df['Distance'] <= 100) & (df['Gravity'] >= 150) & (df['Gravity'] <= 350)]
print(len(df2))

df2.to_csv('newdata.csv', index=False)