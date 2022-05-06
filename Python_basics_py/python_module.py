#!/usr/bin/env python
# coding: utf-8

# # import module ( the way we can use Python libraries)

# In[2]:


import statistics          # import statistics 
statistics.mean([1,2,3])   # we call mean function in statistics -> MODULE.FUNCTION 


# In[4]:


import statistics as s     #  we name statistics -> s
s.mean([1,2,3])


# In[8]:


from statistics import mean # we only import mean function from statistics
mean([1,2,3])               # we don't need to call statistics anymore. BUT this is not recommendable to avoide name crush.

