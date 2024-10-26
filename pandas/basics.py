#check version
import pandas as pd
print(pd.__version__)

#what is Series
print("A Pandas Series is like a column in a table.\nIt is a one-dimensional array holding data of any type.")
# series
cars=['Volve','Honda','Maruti']
sd=pd.Series(cars)
print(sd)
print(sd[1])

integers=[12,879,89,100,798]  
print(pd.Series(integers)) #print integer series data

floats=[12.89,879,89,100,798,656.24,111.123]
fd=pd.Series(floats) # print float series data
print(fd[5],fd[3]) #accessing individual values

#labels & Dtype change in Series data
#var=pd.Series([100,200,300,400,500],index=['a','b','c','d','e','f','g','h','i','j']) gives length doesnot match error
var=pd.Series([100,200,300,400,500],index=['a','b','c','d','e'],dtype='f')
print(var)
print(var['d'])

days={'Monday':1,'Tuesday':2,'Wednesday':3,'Thusday':4,'Friday':5,'Saturday':6,'Sunday':7}
daySeries=pd.Series(days)
print(daySeries)
print(daySeries['Saturday'])

#Create a Series using only data from 'Monday','Wednesday','Thusday':
print(pd.Series(daySeries,index=['Monday','Wednesday','Thusday']))

#what is dataframe
print("Data sets in Pandas are usually multi-dimensional tables, called DataFrames.\nSeries is like a column, a DataFrame is the whole table.")

#dataframe 
data={
    'car':['Volve','Honda','Maruti'],
    'speed':[120.53,78.97,100],
    'price':[1200000,500000,800000]
    }
df=pd.DataFrame(data)
print(df)

# locate row
print(df.loc[1]) # this return data in panda series
print(df.loc[[1,2]]) # return 1 and 2 row

# index and accessing
df=pd.DataFrame(data,index=['car1','car2','car3'])
print(df)

print(df.loc['car2'][1])
print(df.loc['car1'][1])
print(df.loc['car3'][0])
print(df.loc['car3']['car'])

#read csv file
reads=pd.read_csv('data.csv') #Load a comma separated file (CSV file) into a DataFrame
print(reads)

