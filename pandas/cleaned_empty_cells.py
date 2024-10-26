import pandas as pd
df=pd.read_csv('data.csv')

# print(df.head(30))
#print(df.to_string()) # uncomment to see full file content

#remove empty cell by removing that particular rows using dropna()
new_df=df.dropna()
#print(new_df.head(30))

#print(new_df.to_string()) # uncomment to see full file content

'''Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
If you want to change the original DataFrame, use the inplace = True argument:
the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.
'''
# df.dropna(inplace=True)
#print(df.to_string())

#The fillna() method allows us to replace empty cells with a value:

df=pd.read_csv('data.csv')
# df.fillna(150,inplace=True)

# print(df.to_string())

print("--------------------------fill 150 only for calories column only------------------")
# df['Calories'].fillna(1000,inplace=True)
# print(df.to_string())

print("--------------------------fill 150 only for calories column only------------------")
x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)
print(x)
print(df.to_string())
