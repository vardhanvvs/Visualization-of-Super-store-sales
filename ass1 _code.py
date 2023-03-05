# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 20:32:53 2023

@author: Vardhan
"""

#importing matplotlib.pyplot and pandas libraries

import pandas as pd
import matplotlib.pyplot as plt 


def orders_per_month():
    '''
    

    Returns
    -------
    ord_per_month : <class 'dict'> (dictionary)
        This function consists instructions that will convert the orders per
        day count to orders per month and then stores it into a dictionary.

    '''
    #creating a dictionary 'ord_per_month' to store number of orders per month
    ord_per_month={}
    
    #loop to extract number of orders per month  from number of orders per day
    #and appending it to dictionary'ord_per_month'
    for i in range(2014,2018):
        for j in range(1,13):
            if j<10:
                ord_per_month[str(i)+'-0'+str(j)]=0
                for k,l in orders_per_day.iterrows():
                    if l['Order Date'][0:7]==(str(i)+'-0'+str(j)):
                        ord_per_month[str(i)+'-0'+str(j)] =\
                            ord_per_month[str(i)+'-0'+str(j)] + l['count']
            if j>10:
                ord_per_month[str(i)+'-'+str(j)]=0
                for k,l in orders_per_day.iterrows():
                    if l['Order Date'][0:7]==(str(i)+'-'+str(j)):
                        ord_per_month[str(i)+'-'+str(j)] =\
                            ord_per_month[str(i)+'-'+str(j)] + l['count']
    return ord_per_month                   
    

#defining a function for performing value.counts operation on a column
#and passing two arguments dataframe,column name
def delivery_class_of_sales(df,col_name):
    '''
    

    Parameters
    ----------
    df : pandas.DataFrame
        df is an superstore dataset of csv file.
    col_name : STR
        takes input as a column and then performs value counts operation 
        on that specific column.

    Returns
    -------
    new_df : pandas.DataFrame
        returns a new data frame after performing value counts operation.

    '''
    new_df=df[col_name].value_counts()
    return new_df


#defining a function for performing value.counts operation on a column
#and passing two arguments dataframe,column name
def sector_wise_sales(df,col_name):
    '''
    

    Parameters
    ----------
    df : pandas.DataFrame
        df is an superstore dataset of csv file.
    col_name : STR
        takes input as a column and then performs value counts operation 
        on that specific column.

    Returns
    -------
    new_df : pandas.DataFrame
        returns a new data frame after performing value counts operation and 
        reset index method.

    '''
    new_df=df[[col_name]].value_counts()
    new_df=new_df.reset_index()
    new_df=new_df.rename({0:'count'},axis=1)
    return new_df

#reading superstore_train.csv file
superstore_data=pd.read_csv("superstore_train.csv")

#counting number of orders per day using  value_counts method 
#and assigning it to order_date_count

order_date_count=superstore_data[['Order Date']].value_counts()

#create a datarame using order_date_count
orders_per_day=pd.DataFrame(order_date_count)

#renaming the column '0' to 'count' using rename function
orders_per_day=orders_per_day.rename({0:'count'},axis=1)

# sorts the data frame based on index
orders_per_day=orders_per_day.sort_index()

#reseting the index of dataframe df2 from 'order date' to integer numbers 
orders_per_day=orders_per_day.reset_index()


#creating a dataframe 'ord_per_month_df' using the dictionary 'ord_per_month'
ord_per_month_df=pd.DataFrame(data=orders_per_month(),index=[0])

#transposing the 'ord_per_month_df'(row to columns) 
ord_per_month_df_t=ord_per_month_df.transpose()

#resetting the index of 'ord_per_month_df_t' to integer numbers
ord_per_month_df_t=ord_per_month_df_t.reset_index()

#renaming the the columns using the rename function 
ord_per_month_df_t=\
 ord_per_month_df_t.rename({'index':'Year_month',0:'count'},axis=1)

#creating two new columns using split function 
ord_per_month_df_t['Year']=ord_per_month_df_t['Year_month'].str[0:4]
ord_per_month_df_t['Month']=ord_per_month_df_t['Year_month'].str[5:7]

print(ord_per_month_df_t)

#plotting the graph over 'count' column
plt.figure()
plt.plot(ord_per_month_df_t[ord_per_month_df_t['Year']=='2014']['Month'],
 ord_per_month_df_t[ord_per_month_df_t['Year']=='2014'].iloc[:,1],label='2014',
 marker='o')
plt.plot(ord_per_month_df_t[ord_per_month_df_t['Year']=='2015']['Month'],
 ord_per_month_df_t[ord_per_month_df_t['Year']=='2015'].iloc[:,1],label='2015',
 marker='o')
plt.plot(ord_per_month_df_t[ord_per_month_df_t['Year']=='2016']['Month'],
 ord_per_month_df_t[ord_per_month_df_t['Year']=='2016'].iloc[:,1],label='2016',
 marker='o')
plt.plot(ord_per_month_df_t[ord_per_month_df_t['Year']=='2017']['Month'],
 ord_per_month_df_t[ord_per_month_df_t['Year']=='2017'].iloc[:,1],label='2017',
 marker='o')
plt.grid()
plt.xlabel('Months')
plt.ylabel('Number of orders')
plt.title('Monthly Sales of Goods')
plt.legend(title='Year')
plt.show()                    

#plot 2

# calling the function and storing it in df_2
df_2=delivery_class_of_sales(superstore_data,'Ship Mode')

#creating a list of colors 
col=["red","blue","green","yellow"]

#creating a list 'e' and assigning it to explode for exploding attribute in 
#pie function 
e=[0.05,0,0,0]

#plotting  a bar graph using matplotlib.pyplot library as plt
plt.figure(figsize=(8,8))
plt.pie(df_2,labels=df_2.index,colors=col,explode=e,autopct='%.2f%%',
        shadow=True)
plt.title('Delivery Class')
plt.legend()
plt.show()

#plot 3

# calling the function and storing it in df_2
df_2=sector_wise_sales(superstore_data,'Segment')

#creating a list of colors 
cl=["red","blue","green"]

#plotting  a pie chart using matplotlib.pyplot library as plt
plt.figure()

#assigning the bar graph to a variable container
container=plt.bar(df_2['Segment'],df_2['count'],color=cl)

#takes container as an input and labels the exact count on  the edge of the bar
plt.bar_label(container,label_type='edge')

#labelling x-axis
plt.xlabel('Sectors')

#labelling y-axis
plt.ylabel('Number of Goods Sold')
plt.title('Goods Sold in different Sectors')
plt.show()

         







            
        
                
