
# coding: utf-8

# # method (functions)

# # function definition
# 
# `def name(parameters):
#      statements
#      return expression`
# 
# # function call
# if there is `return`:
# 
# `var = name(arguments)`
# 
# if there is no `return`:
# 
# `name(arguments)`

# In[2]:

def split(float_value):  # an argument is float_value
    """Split a float value into interger and decimal part

    :param float_value: a float number
    :return: integer and decimal number
    """
    ap = float_value - int(float_value)
    return int(float_value), ap


# In[3]:

split(3.5)


# In[17]:

a, b = split(float_value=3.5)
print(a,b)


# In[18]:

def foo(a, b=3.14):  # we can set defalt value for each parameter
    return a * b


# In[20]:

foo(3) # 3 * 3.14


# In[21]:

foo(2, 3) # 2 * 3


# In[22]:

### What is going to happen?


# In[23]:

def num_size(num):
    if num > 100:
        return True
    else:
        return False


# In[24]:

number = 10
if num_size(number): # calling function
    print(str(number) + " is bigger than 100")
else:
    print(str(number) + " is smaller than 100")


# ### docstring: explain your function

# In[25]:

help(split)


# In[26]:

print(split.__doc__)


# # map and lambda
# ## **`map()`** function apply a function on all the elements of specified iterable items and return map object. 

# In[30]:

def double(x):
    return x * 2
lst = [1, 2, 3, 4, 5, 6, 7]


# In[31]:

list(map(double,lst)) # We can convert a map object to a list


# In[43]:

for e in map(double, lst): # map object is iterable. So we can extract items using for loop.
    print(e)


# ## **`lambda`** function is a small anonymous function. It can only have one expression (i.e., one line of code).

# In[49]:

def double(x):
    return x * 2
double_lambda = lambda x: x * 2
double_lambda(2)


# In[50]:

list(map(lambda x: x * 2, lst))


# In[5]:

# typical usage of lambda function
score = [("Adam", 64), ("Bob", 82), 
         ("Charlie", 21), ("David", 91)]

score.sort(key=lambda x: x[1])

def foo(x):
    return x[1]
score.sort(key=foo) # https://docs.python.org/3/howto/sorting.html

print(score)


# In[53]:

a = [
      [1,7,'z'],
      [3,2,'x'],
      [1,8,'r'],
      [2,2,'s'],
      [1,9,'b'],
      [2,2,'a']
    ]


# In[54]:

a


# In[55]:

a.sort(key=lambda x:x[2])
print(a)


# In[56]:

a.sort(key=lambda x:x[0])
print(a)


# In[ ]:



