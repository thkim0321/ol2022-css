
# coding: utf-8

# In[2]:

print('Hello, everyone!')


# In[288]:

# <- comments
# Python interpreter ignore lines start with #


# # Basics
# ### Assigning variables

# In[3]:

age = 34
height = 158


# In[4]:

age, height = 20, 170 #multiple assignments in one line


# ### Printing

# In[5]:

print(age)


# In[7]:

print(age, height)


# In[8]:

print('age = ', age) #concatenate arguments


# ### dynamic typing

# In[10]:

print(type(age))


# In[11]:

age = 'twenty'
type(age) # type of age is now changed


# ### Python is 'Strong typing'

# In[17]:

introduce = 'I am ' + age # OK
print(introduce)


# In[1]:

introduce = 'I am ' + 20 # error


# In[22]:

introduce = 'I am ' + str(20) # OK
print(introduce)


# In[23]:

type(str(20))


# # Scalar data types
# ### boolean
# 

# In[25]:

yes = True
no = False
print(yes); print(int(yes)) 
print(no); print(int(no))


# ### int, float
# 

# In[32]:

a = 10; print(type(a))
b = 10.0; print(type(b))


# ### math

# In[38]:

a = 42
b =  4

a/b # devision: always a float is returned.


# In[39]:

a//b # floor division


# In[40]:

a % b # remainder


# In[42]:

a**b # exponentiation(a to the b-th power)


# ### Assigning priority

# In[50]:

c = 10
c = c + 10 # update value c
print(c)


# In[51]:

c += 10
print(c)


# ### Accuracy of int and float
# - int: can be any length

# In[54]:

a = 1234567893456789456789345678
print(a + 1)


# - Floating point number: accurate up to 15 decimal places

# In[55]:

a = 2
a += 10**(-1)
a += 10**(-1)
a += 10**(-1)
print(a) 


# ### change type

# In[14]:

print(True); print(type(True)); print(int(True))


# In[9]:

True + 1


# In[59]:

int(34.8) # below decimal point are omitted


# In[60]:

int('11') # number written in str -> int


# In[61]:

int('twenty') # Error


# ### comparison operators (it returns True or False)

# In[65]:

x = 10
5 < x


# In[66]:

5 < x < 20


# In[67]:

5 < x and x < 20


# In[68]:

x >100 or x < 15


# ### Mutable vs. Immutable
# - Immutable

# In[69]:

a = 3
b = a
print(b)


# In[70]:

a = 4
print(b)


# - Mutable

# In[71]:

a = [1]
b = a
print(b)


# In[72]:

a[0] = 100
print(b)


# ## Differences between '==', 'is'
# - == : equality
# - is : identity (i.e., same object or not)

# In[74]:

a = 10
b = 10
c = 10.0
a == b


# In[75]:

a == c


# In[76]:

a is b


# In[77]:

a is c


# In[84]:

a = ['a']
b = ['a']
a == b # they have same value


# In[85]:

a is b # they are not the same object


# # Sequence types
# 
# ## String
# ### Generate string

# In[87]:

"Oldenburg" # double quoto
'Oldenburg' # single quoto


# In[88]:

"'Hey!', she said." # String contains quoto


# In[91]:

long_sentence = """ This is a long long long....
                    sentence """
print(long_sentence)


# In[93]:

## change other type to string
str(10.2)


# In[94]:

str(True)


# ## How to handle string
# 
# ### Escape \

# In[102]:

print("First sentence\nNext sentence") #next line
print("First sentence\tNext sentence") # tab
print("\"First sentence\"\tNext sentence") # quotation
print("First sentence\\Next sentence") # backspace


# ### add strings using +
# 

# In[106]:

"Taehee"+" Kim"


# In[107]:

vorName = "Taehee"
vorName + " Kim"


# ## Slicing
# ### seq[start: end: step] -> work for any sequence such as list, tuple, string

# In[126]:

numbers = "0123456789"
len(numbers) # check the length of string


# In[127]:

numbers[0]


# In[131]:

numbers[1:]


# In[132]:

numbers[:2] # it prints end-1, in this case 2-1=1


# In[133]:

numbers[-1:] # negative indices are count from the back (-1 = len(seq) -1)


# In[134]:

numbers[::1]


# In[135]:

numbers[::-1]


# In[136]:

numbers[0] = "n" # Error: immutable -> replace(), slicing etc


# In[138]:

"n"+numbers[1:]


# ### split() and join()
# 
# - split(): split a string based on argument( such as ',') and store into a list
# - join(): opposite function to split

# In[143]:

animals = "dog, cat, bird"
animals_split = animals.split(',') # split when there is ','
print(animals_split)


# In[144]:

animals.split() # split when there is a space


# In[145]:

"Guten Tag".split()


# In[148]:

','.join(animals_split) # ',' <- string you want to put between


# ## List : Mutable, order is preserved, contains arbitrary types
# ### Create list: [] or list()

# In[154]:

weekdays = ['Mon','Tue','Wed','Thu']
print(weekdays)


# In[155]:

list_any_type = ['cat',1,10.5,True]
print(list_any_type)


# In[156]:

list_any_type[3]


# In[158]:

type(list_any_type[3])


# In[159]:

empty_list = list()
empty_list


# ### change other type to list: list()

# In[162]:

list("abcdefg")


# ### Slicing (same as string example)

# In[170]:

weekdays[0]


# In[171]:

weekdays[0:2]


# ### Nested list, i.e., list in list
# Note: you can handle matrix using libraries, Numpy and Pandas which will be introduced later

# In[172]:

list_a = [1,2,3]
list_b = ['cat','dog','bird']
list_all = [list_a, list_b]
list_all


# In[190]:

col_names = ['Country','Name','Born','Party']
germany = ['Germany','Angela Merkal', 1954, 'CDU']
us = ['United States', 'Donald Trump', 1946, 'Republican']
france = ['France','Emmanuel Macron', 1677, 'REM']

head_of_gov = [col_names, germany, us, france]
head_of_gov # matrix


# In[191]:

head_of_gov[1][1]


# ### List is mutable! So we can change,add, and delete elements

# In[192]:

# change
germany[1] = 'Angela Merkel' # change. -> head_of_gov[1][1] = 'Angela Merkel'
head_of_gov


# In[193]:

# append()
germany.append('Chancellor')
head_of_gov


# In[194]:

# extend() vs. append
more_info = [2005, 'Female']
germany.append(more_info) #if you use append, 'more_info' would be treated as one element
head_of_gov


# In[195]:

# del vs. remove
del germany[-1] # delete it!
print(germany)


# In[197]:

germany.remove('Chancellor')
print(germany)


# In[198]:

germany.extend(more_info)


# In[199]:

print(germany)


# ### index(), in, count
# - index():check position of an element in a list
# - in : check if an element exists in a list
# - count: count an element

# In[201]:

germany.index('CDU')


# In[202]:

germany[3]


# In[203]:

'CDU' in germany


# In[205]:

germany.count('CDU')


# In[206]:

len(germany)


# ### how to copy list
# - list type is 'mutable'
# - copy a list as a new list: 1) copy(), 2) list(), 3) [:]

# In[207]:

a = [1,2,3]
b = a.copy()
c = list(a)
d = a[:]


# In[208]:

a[0] = 'Hello!'
print(a)
print(b)
print(c)
print(d)


# ### sort() and sorted()

# In[227]:

a = [1,4,2,3,6]
a.sort() # sort an object 'a' itself
a


# In[228]:

a.sort(reverse=True)
a


# In[213]:

sorted_a = sorted(a) # store sorted result in another object


# In[214]:

sorted_a


# In[226]:

a # a's order remain the same


# ## Tuple: Immutable. You cannot change, add, delete an element
# ### () or tuple()

# In[ ]:

# Change tuple to list
t1 = ("a","b","c") # create tuple
t2 = 1,2,3 # you can omit ()
print(t1)
print(t2)


# ### It is immutable

# In[232]:

t1[0] = "d" # we cannot change item of tuple


# In[234]:

t1_list = list(t1)
t1_list[0] = "d"
print(t1_list)


# ### Unpack (Tuple and list)

# In[236]:

d,e,f = t1
print(d)
print(e)
print(f)


# In[240]:

g,h,i = t1_list
print(g)
print(h)
print(i)


# ### Exchange values at once

# In[241]:

d,e,f = g,h,i
print(d)


# ## Dictionary : Store {key: value}. Mutable, the order is not preserved.
# - create: {} dict()
# - key should be immutable type, i.e., tuple, int, string (no list, dict, set)
# - key duplication is not allowed

# In[242]:

d = {'germany': 'Angela merkal'}
print(d)


# In[243]:

# [key] : add and change element
d['us'] = 'Donald Trump'
print(d)


# In[244]:

# change element
d['germany'] = 'Angela Merkel'
print(d)


# In[250]:

# update()
other_dict = {'france': 'Emmanuel Macron', 'japan': 'Shinjiro Abe'}
d.update(other_dict)
print(d)


# In[251]:

# delete
'japan' in d    # check key 'japan' is in dictionary (note: not 'value')
del d['japan']  # delete key 'japan'
print(d)


# In[255]:

print(d.keys())    # get all keys (iterable)


# In[256]:

print(d.values())  # get all values (iterable)


# In[257]:

print(d.items())   # get all items in tuple (key: value) (iterable)


# In[266]:

d2 = d # create identical dictionary
d3 = d.copy() # copy and create other dictionary


# In[263]:

d['uk'] = 'Theresa May'
print(d2)
print(d3)


# In[271]:

# create dict using dict()
# you can create dict from any type of data which has two sequential elements
a = [(1,2),(2,3)]
dict(a)


# ## Set: Mutable
# ### create: set() or { values }

# In[272]:

# Let's suppose there is a Twitter user A. 
#We have a list of users who retweeted A's post 
# in the past.
retweet_a = ['b','c','e','h','r','b','b','c','h']


# In[274]:

# How many unique users in a list? 
#We can just use set().
retweet_a_set = set(retweet_a)
len(retweet_a_set)


# In[282]:

# Let's suppose we also have retweet user list of user B.
retweet_b = ['a','c','a','h','z']


# In[283]:

# How many users were retweeted both A an B? -> Check 'intersection'
retweet_b_set = set(retweet_b)
print(retweet_a_set & retweet_b_set)
print(len(retweet_a_set & retweet_b_set))


# In[285]:

# Count all the unique users? -> check 'union'
print(retweet_a_set | retweet_b_set)
print(len(retweet_a_set | retweet_b_set))


# In[287]:

# Inclusion
retweet_a_set >= retweet_b_set 


# In[ ]:



