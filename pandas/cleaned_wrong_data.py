#replacing value in dataset
import pandas as pd
df=pd.read_csv('data1.csv')

# for x in df.index:
#     if df.loc[x,"Duration"]>60:
#         df.loc[x,"Duration"]=60

# print(df.to_string())

#remove value in dataset
for x in df.index:
    if df.loc[x,"Duration"]>60:
        df.drop(x,inplace=True)
print(df.to_string())


#remove duplicate data
df=pd.read_csv('data1.csv')
df.drop_duplicates(inplace=True)
'''
Returns True for every row that is a duplicate, otherwise False:
print(df.duplicated())
'''
df=pd.read_csv('data.csv')
print(df.corr())
'''
The Result of the corr() method is a table with a lot of numbers that represents how well the relationship is between two columns.

The number varies from -1 to 1.

1 means that there is a 1 to 1 relationship (a perfect correlation), and for this data set, each time a value went up in the first column, the other one went up as well.

0.9 is also a good relationship, and if you increase one value, the other will probably increase as well.

-0.9 would be just as good relationship as 0.9, but if you increase one value, the other will probably go down.

0.2 means NOT a good relationship, meaning that if one value goes up does not mean that the other will.

What is a good correlation? It depends on the use, but I think it is safe to say you have to have at least 0.6 (or -0.6) to call it a good correlation.

'''