#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data = pd.read_csv('F:\Women_Clothing_Reviews_Text_Data\Ecommerce Purchases')
data


# In[3]:


data.head()


# In[4]:


data.tail()


# In[5]:


data.head(10) #it will give top 10 rows which answers our question


# In[6]:


#What are the last 10 rows in the data?
data.tail(10)


# In[8]:


#What is the data-type of each attribute in data?
data.dtypes  #as you can see it is not a method


# In[10]:


#What are the null values in the dataset?
data.isnull().sum()


# In[11]:


len(data.columns) #It tells total number of columns in dataset


# In[12]:


len(data)


# In[14]:


data.info()  #To get the information about the dataset


# In[16]:


data.columns  #It shows the column names in the dataset


# In[18]:


data['Purchase Price'].max() #To know the specific maximum purchase price


# In[19]:


data['Purchase Price'].min()  #It gives the minimum possible price


# In[21]:


#what is the average purchase price?
data['Purchase Price'].mean()


# In[23]:


#How many people have Fr as their language?
data.columns


# In[24]:


data['Language']


# In[27]:


len(data[data['Language'] == 'fr'])  #it tells total number of people having french as their language


# In[28]:


#Another way using count method 
data[data['Language']=='fr'].count()


# In[29]:


#FInd the job titles which contains engineer?
data.columns


# In[35]:


len(data[data['Job'].str.contains('engineer',case = False)]) #As engineer is in the strings so we are using str.contains


# In[41]:


#find the email of the person having the IP address as 132.207.260.22.
data[data['IP Address']=='132.207.160.22']['Email']


# In[43]:


#How many people have mastercard as their credit card provider and made a purchase above 50?
data.columns


# In[48]:


data[(data['CC Provider']=="Mastercard") & (data['Purchase Price'] > 50)].count()


# In[50]:


#What is the email of the person having credit card number as 4664825258997302?
data[data['Credit Card'] == 4664825258997302]['Email']


# In[51]:


#How many people purchase during the AM and during the PM?
data['AM or PM'].value_counts()


# In[52]:


#How many people have the credit card that exipres in 2020?
data.columns


# In[64]:


data['CC Exp Date']==2020


# In[70]:


len(data[data['CC Exp Date'].apply(lambda x:x[3:]=='20')]) #This Answers our question. Answer is 988 peoples whose cc not expirs in 2020.


# In[ ]:


#Find the Popular Email Providers in the dataset for the marketing campaigns?
list1 = []
for email in data['Email']:
     list1.append(email.split('@')[1])


# In[ ]:


data['temp']=list1


# In[72]:


data.head(1)


# In[71]:


data['Email']


# In[75]:


data['Email'].apply(lambda x:x.split('@')[1]).value_counts() #This answers the Question..Campaign shoud target Hotmail,yahoo,gmail.


# In[ ]:




