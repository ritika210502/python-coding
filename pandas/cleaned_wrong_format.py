'''Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.

'''
import pandas as pd
df=pd.read_csv('data1.csv')

#correct format
# df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

print(df.to_string())
#remove rows
df.dropna(subset=['Date'],inplace=True)
print(df.to_string())
