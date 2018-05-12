
# coding: utf-8

# In[44]:


import pandas as pd
import numpy as np
airquality = pd.read_csv("C:/Users/Administrator/Desktop/Jupiter notebooks/DataSets/airquality.csv")
airquality.head(n=5)


# In[6]:


#1.	Fetch the observations for 9 day of June
airquality[airquality.Month==6][airquality.Day==9]


# In[9]:


#2.	Find Average temperature for the month of June
airquality[airquality.Month==6]['Temp'].mean()


# In[27]:


#3.	To which day of June has the least temperature
airquality[airquality.Month==6][['Day','Temp']].min()


# In[28]:


#4.	Find Maximum Ozone value for the month of May
airquality[airquality.Month==5]['Ozone'].max()


# In[32]:


#5.	Find the count of the missing values in the ozone column of the data set
airquality.Ozone.isnull().sum()


# In[35]:


#6.	Find out What is the mean of the Ozone column in this dataset
airquality['Ozone'].agg({'Ozone' : 'mean'})


# In[68]:


#7.	Find out which month has the highest temperature
airquality[airquality.Temp== airquality.Temp.max()]['Month']


# In[67]:


#8.	Find out the wind value when the Ozone becomes maximum
airquality[airquality.Ozone==airquality.Ozone.max()]['Wind']


# In[52]:


#9.	Find out the months for which the airquality observations have been carried out
list(airquality.Month.unique())


# In[55]:


#10.	Find the Ozone and temperature values for the 1st observation of every month.
airquality[airquality.Day==1][['Day','Ozone','Temp']]


# In[65]:


#11.	Which day of which month corresponds to the least Ozone Value.
airquality[airquality.Ozone==airquality.Ozone.min()][['Day', 'Month']]


# In[71]:


#12.	Convert the temperature for all the observations to Centigrade scale
airquality['temp_centi'] = ((airquality.Temp - 32) * (5/9))
airquality.head(n=5)

