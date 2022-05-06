
# coding: utf-8

# # Comprehension
# ## list : `[expression for item in iterable if condition]`
# 

# In[1]:

# Please create a list [1,2,...,99]
# There are many ways to do. For example...
# Please create a list [1,3,5,7,....99] # list of odd numbers in range 1 to 100

num_list = []
for number in range(1,100):
    num_list.append(number)
print(num_list)


# In[3]:

# you can write this in one line
num_list = []
for number in range(1,100):
    num_list.append(number)
print(num_list)

num_list2 = [number for number in range(1,100)]
print(num_list2)


# In[4]:

print(list(range(1,100)))
print(list(range(1,100,2)))


# In[4]:

# Please create a list [1,3,5,7,....99] # list of odd numbers in range 1 to 100
odd_list = []
for number in range(1,100):
    if number % 2:  #  if number % 2 == 1
        odd_list.append(number)
print(odd_list)


# In[5]:

[number for number in range(1,100) if number % 2]
print(odd_list2)
odd_list = []
for number in range(1,100):
   if number % 2:  #  if number % 2 == 1
       odd_list.append(number)
print(odd_list)


# In[8]:

# what is going to happen?
print([number * 2 for number in range(1,100) if number % 2])


# ## dictionary comprehension: `{key_item: value_item for item in iterable}`
# 

# In[5]:

word = 'letters'
letter_counts={x: word.count(x) for x in 'letters'}
print(letter_counts)


# In[12]:

sentence = 'I like Python. I really do.'.split()
word_counts = {word: sentence.count(word) for word in sentence}
print(word_counts)


# In[ ]:



