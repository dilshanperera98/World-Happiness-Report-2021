#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


sns.set_style('darkgrid')
plt.rcParams['font.size']=15
plt.rcParams['figure.figsize']=(10,7)
plt.rcParams['figure.facecolor']='#FFE584'


# In[5]:


data = pd.read_csv('//Users//dilshanperera//Documents//My_Projects//world-happiness-report-2021.csv')


# In[6]:


data.head()


# In[7]:


data_columns = ['Country name','Regional indicator','Ladder score','Logged GDP per capita','Social support','Healthy life expectancy','Freedom to make life choices','Generosity','Perceptions of corruption']


# In[8]:


data = data[data_columns].copy()


# In[12]:


happy_df = data.rename({'Country name':'country_name' , 'Regional indicator':'regional_indicator' , 'Ladder score':'ladder_score', 'Logged GDP per capita':'logged_GDP_per_capita' , 'Social support':'social_support' , 'Healthy life expectancy':'healthy_life_expectancy' , 'Freedom to make life choices':'freedom_to_make_life_choices' , 'Generosity':'generosity' , 'Perceptions of corruption':'perceptions_of_corruption'}, axis =1)


# In[13]:


happy_df.head()


# In[14]:


happy_df.isnull().sum()


# In[16]:


# Plor between ladder and GDP

plt.rcParams['figure.figsize'] = (15,7)
plt.title('Plot between Ladder score and GDP')
sns.scatterplot(x = happy_df.ladder_score, y = happy_df.logged_GDP_per_capita, hue = happy_df.regional_indicator, s = 200);

plt.legend(loc = 'upper left', fontsize = '10')
plt.xlabel('Ladder Score')
plt.ylabel('GDP per capital')


# In[17]:


gdp_region = happy_df.groupby('regional_indicator')['logged_GDP_per_capita'].sum()
gdp_region


# In[19]:


gdp_region.plot.pie(autopct = '%1.1f%%')
plt.title('GDP by Region')
plt.ylabel('')


# In[20]:


# Total Countries

total_country = happy_df.groupby('regional_indicator')[['country_name']].count()
print(total_country)


# In[22]:


# Correlation Map

cor = happy_df.corr(method = "pearson")
f, ax = plt.subplots(figsize = (10,5))
sns.heatmap(cor, mask = np.zeros_like(cor, dtype=np.bool),
           cmap = "Blues",square=True,ax=ax)


# In[23]:


# Corruption in regions

corruption = happy_df.groupby('regional_indicator')[['perceptions_of_corruption']].mean()
corruption


# In[24]:


plt.rcParams['figure.figsize'] = (12,8)
plt.title('Perception of Corruption in various Regions')
plt.xlabel('Regions',fontsize = 15)
plt.ylabel('Corruption Index',fontsize = 15)
plt.xticks(rotation= 30 , ha = 'right')
plt.bar(corruption.index,corruption.perceptions_of_corruption)


# In[25]:


top_10 = happy_df. head (10)
bottom_10 = happy_df.tail (10)


# In[30]:


fig, axes= plt.subplots(1,2, figsize= (16, 6))
plt.tight_layout(pad= 2)
xlabels= top_10.country_name
axes[0].set_title('Top 10 happiest countries Life Expectancy')
axes [0].set_xticklabels(xlabels, rotation=45, ha='right')
sns.barplot(x= top_10.country_name, y= top_10.healthy_life_expectancy, ax= axes[0]) 
axes[0].set_xlabel('Country Name') 
axes[0].set_ylabel ('Life expectancy') 

xlabels= bottom_10.country_name
axes[1].set_title('Bottom 10 least happy countries Life Expectancy')
axes[1].set_xticklabels(xlabels, rotation=45, ha='right')
sns.barplot(x= bottom_10.country_name, y= bottom_10.healthy_life_expectancy, ax= axes[1])
axes [1]. set_xlabel ('Country Name') 
axes [1].set_ylabel ('Life expectancy')
                                                                                                                
                                                                                                                
                                                                                                                
                                                                                                                


# In[32]:


plt.rcParams['figure.figsize']=(15,7)
sns.scatterplot(x= happy_df.freedom_to_make_life_choices, y= happy_df.ladder_score, hue= happy_df.regional_indicator, s=200)
plt.legend(loc='upper left',fontsize='12')
plt.xlabels= ('Freedom to make life choices')
plt.ylabels= ('Ladder Score')



# In[38]:


country = happy_df.sort_values(by='perceptions_of_corruption').tail(10)
plt.rcParams['figure.figsize'] = (12, 6)
plt.title( 'Countries with Most Perception of Corruption') 
plt.xlabel('Country', fontsize = 13)
plt.ylabel ('Corruption Index', fontsize = 13)
plt.xticks(rotation = 30, ha='right')
plt.bar(country.country_name, country.perceptions_of_corruption)


# In[39]:


# corruption vs happiness

plt.rcParams['figure.figsize']=(15,7)
sns.scatterplot(x= happy_df.ladder_score, y= happy_df.perceptions_of_corruption, hue= happy_df.regional_indicator, s=200)
plt.legend(loc='lower left',fontsize = '14')
plt.xlabel=('Ladder Score')
plt.ylabel=('Corrption')


# In[ ]:




