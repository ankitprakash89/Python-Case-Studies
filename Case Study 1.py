
# coding: utf-8

# In[71]:


import pandas as pd
import numpy as np 
oj = pd.read_csv("C:/Users/Administrator/Desktop/Jupiter notebooks/oj.csv", header = 0)
oj.head()


# In[9]:


#1.	Find the dimensions of the oj data set
np.shape(oj)


# In[29]:


#2.	Find the structure of the data set
oj.info()


# In[14]:


#3.	Find out the column names in the data set
oj.columns


# In[16]:


#4.	Describe the data set
oj.describe()


# In[26]:


#1.	Fetch the first row 3rd column from the data set
print (oj.ix[0, 'week'])


# In[40]:


#2.	Fetch the first, second and Third columns of the oj data frame
print (oj.iloc[0:,0:3])


# In[41]:


#3.	Fetch the first, second, eighth and the 456th rows of the 1st, third and the sixth columns of the data frame
print(oj.iloc[[0,1,7,455],[0,2,5]])


# In[44]:


#4.	Fetch the top 5 rows of the brand column
print (oj.ix[0:4, 'brand'])


# In[50]:


#5.	Fetch top 5 rows of the brand, week and feat details
print (oj.ix[0:5, ['brand','week','feat']])


# In[68]:


#6.	Fetch the details of all distinct stores
print(oj.groupby('store').['store'].agg(['count']))


# In[57]:


#7.	Fetch all the observations for Tropicana brand
print(oj[oj['brand'] == 'tropicana'])


# In[79]:


#8.	Fetch all the observations for Tropicana brand using query function
oj.query("(brand=='tropicana')")


# In[76]:


#9.	Fetch bottom 5 observations for those who have bought Tropicana or dominics
trop_oj = oj[(oj['brand'] == 'tropicana')| (oj['brand'] == 'dominicks')]
print(trop_oj.tail(n=5))


# In[72]:


#10.	Fetch the income, brand, price observations with Tropicana brand without feature advertisement
trop_oj = oj[oj['brand'] == 'tropicana']
print (oj.ix[0:,['income', 'brand', 'price']])


# In[140]:


#11.	Add a new column in the dataset: logInc which is the logarithm of the income
oj['logInc'] = np.log(oj.INCOME)
oj.head(n=5)


# In[133]:


#12.	Sort the Data in the increasing order of the week
oj.sort_values('week')


# In[136]:


#13.	Sort the data in the decreasing order of Income
oj.sort_values('INCOME', ascending=False)


# In[93]:


#14.	Find the mean of the juice price for each brand
oj.groupby('brand')['price'].agg(np.mean)


# In[97]:


#15.	Find the average income for each brand and at each store
oj.groupby(['brand','store'])['INCOME'].agg(np.mean)


# In[145]:


#16.	Find:
#a.	Mean and std deviation of the income
mean_income= round(np.mean(oj.INCOME),2)
sd_income = round(np.std(oj.INCOME),2)
print(mean_income,sd_income)

#b.	For income greater than or equal to 10.5, find the mean income
s = oj[oj.INCOME>10.5]
mean_in = np.mean(s.INCOME)
print(mean_in)

#c.	For each brand having price >=2.5 find the mean, median, sd of the log of income
import math
df = oj[oj.price>=2.5
df.sort_values('INCOME', ascending=True)
df.groupby('brand').agg({'INCOME':np.mean, 'INCOME':np.median, 'logInc':np.std})


# In[141]:


#17.	Find the Cross tabulation of brands and feature advertisement
pd.crosstab(oj.brand, oj.feat)

