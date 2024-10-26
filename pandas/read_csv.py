import pandas as pd

print(pd.options.display.max_rows) #display max no.of rows in system


pd.options.display.max_rows = 9999 #increase max rows to display full data
#read csv file
df=pd.read_csv('data.csv') #Load a comma separated file (CSV file) into a DataFrame
print(df)

print(df.to_string())

print("--------------read top 10 values from data.csv---------------")
print(df.head(10))

print("--------------read botton 10 values from data.csv---------------")
print(df.tail(10)) #head() and tail() print default 5 values 

print("--------------read top 10 values from data.csv---------------")
print(df.info())