#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from IPython.display import display


# In[13]:


movie = pd.read_csv('data/movie.csv')
movie2 = movie[['movie_title', 'title_year', 'imdb_score']]
movie3 = movie2.sort_values(['title_year','imdb_score'], ascending=False)
movie_top_year = movie3.drop_duplicates(subset='title_year')
movie_top_year.head()


# In[ ]:




