
# coding: utf-8

# In[42]:


import pandas as pd
import numpy as np 
store = pd.read_csv("C:/Users/Administrator/Desktop/Jupiter notebooks/Store.csv", header = 0, encoding="latin")
store.head(n=5)


# In[16]:


#1.How many unique cities are the orders being delivered to
cities = store.City.unique()
print(len(cities))


# In[14]:


#•	What is the total quantity sold in the East Region?
store_east = store[store.Region =='East']
total_quantity = np.sum(store_east.Quantity)
print(total_quantity)


# In[17]:


#•	Find the sum of the quantity sold in the East Region
store_east = store[store.Region =='East']
total_quantity = np.sum(store_east.Quantity)
print(total_quantity)


# In[19]:


#•	In the south region sort the sales in decreasing order
store[store.Region =='South'].sort_values('Sales', ascending=False)


# In[22]:


#•	Find the mean of quantity for every region
store.groupby('Region')['Quantity'].agg(np.mean)


# In[21]:


#•	Find the mean of sales for every category
store.groupby('Category')['Sales'].agg(np.mean)


# In[24]:


#•	Find the max, min, sum of sales and profit for every category
store.groupby('Category')[['Sales','Profit']].agg({'max', 'min','sum'})


# In[25]:


#•	Find sum of sales and max profit for every segment
store.groupby('Segment').agg({'Sales':np.sum,'Profit':np.max})


# In[26]:


#•	For every segment find the mean of the discount
store.groupby('Segment')['Discount'].agg(np.mean)

#•	For every segment find the most profitable customers
def get_cid(profit):
    profit = profit.max()
    return store[store.Profit == profit]['Customer Name']
group_seg = store.groupby('Segment').agg({'Profit':[get_cid,'max']})
print(group_seg)
# In[62]:


a = [store.groupby('Segment').max()['Profit']]
b= [store.Profit]
store[['Customer Name','Segment']][np.in1d(b,a)]


# In[31]:


#•	What are the top 5 categories that give maximum profit?
cities = store.Country.unique()
print(cities)


# In[38]:


#•	What is the Total Sales, Quantity, Discount, Profit across Total US.
store.groupby('Region').sum()[['Sales','Quantity','Discount','Profit']]


# In[60]:


#•	How many times has it taken more than 5 days from placing an order to shipping
store['Order Date'] =pd.to_datetime(store['Order Date'])
store['Ship Date'] = pd.to_datetime(store['Ship Date'])
TimeTaken = store['Ship Date']- store['Order Date']
sum(TimeTaken >'5 days')


# In[71]:


#•	Find the total number of orders in every category which has been shipped with a duration > 5 days
store['Order Date'] =pd.to_datetime(store['Order Date'])
store['Ship Date'] = pd.to_datetime(store['Ship Date'])
store['TimeTaken'] = store['Ship Date']- store['Order Date']
s1 = store[store.TimeTaken > '5 days']
s1.groupby('Category').count()['TimeTaken']


# In[75]:


#•	What’s the percentage of items which has been shipped within 5 days
store['Order Date'] =pd.to_datetime(store['Order Date'])
store['Ship Date'] = pd.to_datetime(store['Ship Date'])
store['TimeTaken'] = store['Ship Date']- store['Order Date']
a = store[store.TimeTaken < '5 days'].count()['TimeTaken']
b = store.count()['TimeTaken']
per = a/b*100
print(per)


# In[80]:


#•	What’s the percentage of items which has been shipped after 5 days
store['Order Date'] =pd.to_datetime(store['Order Date'])
store['Ship Date'] = pd.to_datetime(store['Ship Date'])
store['TimeTaken'] = store['Ship Date']- store['Order Date']
a = store[store.TimeTaken > '5 days'].count()['TimeTaken']
b = store.count()['TimeTaken']
per = a/b*100
print(per)

