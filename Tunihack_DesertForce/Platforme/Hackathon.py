#!/usr/bin/env python
# coding: utf-8

# In[11]:


# import Python libraries we will need later

import pandas as pd   #for DataFrames  -- resembles relational DB and SQL
import numpy as np    #for mathematical operations -- resembles Matlab
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn import metrics
from flask import jsonify
from flask import Flask
from flask_cors import CORS, cross_origin


# In[68]:


#1 How many rows and columns are there in the data frame returned by read_csv function ? (45000, 15)
filepath = "./depenses-decembre-2017.csv"
df = pd.read_csv(filepath)
df.shape

filepath = "./recettes-2017.csv"
df2 = pd.read_csv(filepath)
# In[69]:



# In[71]:


# In[61]:


df.columns


# In[72]:


df.dtypes


# In[53]:


df.describe()


# In[74]:


app = Flask(__name__)
CORS(app)
@app.route('/summary')
def summary():
    return df.to_json(orient='values')

@app.route('/summary2')
def summary2():
    return df2.to_json(orient='values')



@app.route('/sum1')
def sum1():
	return str(df.Annuel_expenses.sum())

@app.route('/sum2')
def sum2():
	return str(df2.revenue.sum())

@app.route('/Makess')
def mak():
	return str(df2.values[11][1])

@app.route('/Parking')
def park():
	return str(df2.values[12][1])

@app.route('/Telephone')
def tel():
	return str(df.values[12][1])

@app.route('/Maa')
def maa():
	return str(df.values[10][1])


@app.route('/Rang')
def rg():
	return str(165)

@app.route('/Courant')
def cr():
	return str(df.values[11][1])

# In[ ]:


#filepath = "./simulationdata.csv"
#df0 = pd.read_csv(filepath)


# In[245]:


#df0


# In[246]:


#Y=df0.cost.values


# In[247]:


#Y


# In[248]:


#type(Y)


# In[249]:


#X=df0.values


# In[250]:


#type(X)


# In[251]:


#X.shape


# In[ ]:





# In[252]:


#Xtrain, Xtest, ytrain, ytest = train_test_split(X, Y, test_size=0.25)


# In[253]:


#Xtrain.shape


# In[254]:


#Xtest.shape


# In[255]:


#print(Xtrain)


# In[256]:


#print(ytrain)


# In[257]:


#from sklearn.linear_model import LinearRegression


# In[258]:


#model1 = LinearRegression()


# In[259]:


#model1.fit(Xtrain, ytrain)


# In[260]:


#model1.coef_


# In[261]:


#max(abs(model1.coef_))


# In[262]:


#ypred = model1.predict(Xtest)


# In[263]:


#type(ypred)


# In[ ]:



#@app.route('/cost', methods=['POST']) 
#def summary():
    #x=floatrequest.nb
    #y=request.nv
    #y=request.nv
    #y=request.nv
    #y=request.nv
    #y=request.nv
    #res=model1.predict(x)
    #return str(res)
from flask import render_template


@app.route('/home')
def sd():
    page_name='dashboard'
    return render_template('%s.html' % page_name)
