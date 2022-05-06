
# coding: utf-8

# # Handling exceptions
# ### Python Build-in Exceptions: https://docs.python.org/3/library/exceptions.html#BaseException 

# In[1]:

# Python raises exceptions when it encounter errors. For example..

Print('Hello!') # -> NameError


# ## `try, except, else, finally`

# In[34]:

short_list = ['a', 'b', 'c']

for position in [0,'str',1,2,3]:
    print(short_list[position])


# In[36]:

short_list = ['a', 'b', 'c']
for position in [0,'str',1,2,3]:
    try:
        print(short_list[position]) # do something
    except:                         # but if there is an exception
        pass                        # do nothing


# In[2]:

short_list = ['a', 'b', 'c']

for position in [0,'str',1,2,3]:
    try:
        print(short_list[position])
    except TypeError as type:       # If there is a TypeError,
        print('type error:',type)         # print ('type error')
    except IndexError as index:     # If there is a IndexError,
        print('index error:',index)        # print ('index error')
    except Exception as others :    # If there is a other exception,
        print(others)               # print it's value.
    else:                           # else: if there was no exception, execute it.
        print('success')
    finally:                        # finally: execute it regardless of exceptions.
        print('Finished')


# In[ ]:



