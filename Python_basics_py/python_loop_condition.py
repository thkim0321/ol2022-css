
# coding: utf-8

# # Indentation block
# Python uses indentation to compose statements into blocks
# - a block starts with a block statement followed by a colon
# - all statements inside the block have a higher indentation depth
# - statements on the same nesting level must have equal indentation
# - the block ends by decreasing the indentation levels to a previous one

# # loop
# ## for

# In[3]:

# for targets in expressions:
#     statements


# In[1]:

for i in range(5):  # range(5) = 0,1,2,3,4. Check list(range(5)).
    print(i)


# In[4]:

print(range(5))
print(list(range(5)))


# In[6]:

### range(start, end, step) : returns sequence of number
list(range(0, 10, 2))


# In[1]:

animals = ['cat', 'dog', 'bird']
for animal in animals:  # this is possible because list is 'iterable'
    print(animal)


# In[8]:

for i in range(0, len(animals)):
    print(animals[i])


# ## while

# In[9]:

# while loop: execute till a condition evaluates to False
# while condition:
#     statements


# In[10]:

current = 0
while current < len(animals):
    print(animals[current])
    current += 1


# ## other iterable type: string, tuple, dict, set

# In[1]:

d = {'germany': 'Angela Merkel', 
     'us': 'Donald Trump', 'france': 'Emmanuel Macron',
     'uk': 'Theresa May'}
for key in d:  # it returns key in dictionary
    print(key)


# In[3]:

for val in d.values():  # if you want to print values
    print(val)


# In[4]:

for key in d:
    print(key,d[key])


# In[5]:

for key in d:
    print('key:'+ key +', Value:'+ d[key])


# In[7]:

# Handy Tip! Let's use string.format() to create 
# a string with other information.
for key in d:
    print('Key:{}, Value:{}'.format(key,d[key]))


# In[2]:

# aligning: https://docs.python.org/3/library/string.html
# < left align, > right align, ^ centered. 
# number : width

for key in d:
    print('Key:{:>7}, Value:{:>10}'.format(key,d[key]))


# In[2]:

# string.format{} example
age = 3; name = 'Max'
print('My dog\'s name is {1} and he is {0} years old. {1} likes chasing birds.'.format(age,name))


# ### zip(): combine more than two list

# In[18]:

col_names = ['Country', 'Name', 'Born', 'Party']
germany = ['Germany', 'Angela Merkel', 1954, 'CDU']


# In[16]:

for i in zip(col_names, germany):
    print(i)


# In[19]:

list(zip(col_names,germany))


# In[20]:

# tip: you can create dict using zip()
dict(zip(col_names, germany))


# ### break and continue

# In[6]:

# break: stop execution and continue after the loop
# continue: stops execution of the loop body and start 
# with the next item
for i in range(5):
    if i % 2 == 1:  # 1 (true) or 0 (false)
        continue
    print(i)


# In[22]:

count = 0
while True:
    print(count)
    count += 1
    if count == 5:
        break


# In[7]:

while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())


# # if, elif, else
# 
# `if expression:  # execute if expression evaluates to True -> boolean 
#     statements
# elif expression:
#     statements
# else:
#     statements`

# In[8]:

weather = input("How is the weather today?")

if weather == 'good':
    print("Let's go out")
elif weather == 'bad':
    print("Let's study Python Programming")
else:
    print("Ah..you choose")


# In[ ]:



