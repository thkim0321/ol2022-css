
# coding: utf-8

# # Write and read files
# ## Basics
# 
# ### modes:
# - **r** : read mode (default): use **read(), readline()**
# - **w** : write mode: existing files are overwritten. use **write('string')**
# - **a** : write append mode: appending string at the end of the file
# ### https://docs.python.org/3/library/functions.html#open

# In[21]:

f = open('helloworld.txt','w') # open in write (w) mode
f.write('hello world')         # write a string
f.close()                      # close file handle


# In[22]:

f = open('helloworld.txt','r') # open in read mode
message = f.read()             # read complete file
print(message)                 # print it
f.close()                      # close file handle


# In[23]:

f = open('helloworld.txt','a') # append mode
f.write('\nhello world again')
f.close()


# ### `with` : automatically closes the file

# In[24]:

with open('helloworld.txt') as f:
    message = f.read()
    print(message)


# ### `readline()` : use this when you have massive data

# In[29]:

with open('helloworld.txt') as f:
    line = f.readline()
    while line:
        print(line)
        line = f.readline()


# ### Example : Save a list to txt file

# In[5]:

# Let's save this list
user = ['AfD', 'CDU', 'CSU', 'fdp', 'spdde', 'Die Gruenen', 'dieLinke']


# example 1
with open('germany_party_account.txt','w') as f:
        for u in user:
            f.write('{}\n'.format(u)) # '\n': new line


# In[6]:

# example 2
with open('germany_party_account2.txt', 'w') as f:
    f.write("\n".join(user))


# ### Example: Save a multiple column values to csv file

# In[14]:

user_id = [844081278,20429858,21107582,39475170,26458162,14553288,44101578,35562287]


# In[19]:

with open('germany_party_account3.txt', 'w') as f:
    for u, i in zip(user, user_id):
        f.write('{},{}\n'.format(u, i))  # '\n': new line


# ## CSV library

# In[31]:

import csv
with open("germany_party_account4.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["username","user_id"])
    for u,i in zip(user,user_id):
        writer.writerow([u,i]) # <- It has to be a list !!! Be careful


# ### You can store list of dict() format easily

# In[37]:

# Lets store the info into the list of dictionary format

list_of_dict= []
for u, i in zip(user, user_id):
    list_of_dict.append({'username':u, 'user_id':i})
print(list_of_dict)


# In[38]:

with open('germany_party_account5.csv', 'w') as output_file:
    fc = csv.DictWriter(output_file, fieldnames=list_of_dict[0].keys())
    fc.writeheader()
    fc.writerows(list_of_dict)


# ## json format

# In[63]:

import json
tweet = {
    "created_at": 'Sat Feb 08 15:29:13 +0000 2020',
    "full_text": "I love python!",
    "user": {
        "id": "1234567890",
        "screen_name": "PythonLover"
    }
}


# In[65]:

tweet


# In[66]:

# Write tweet data into json format (Serialization)
with open("tweet_example.json", "w") as write_file:
    json.dump(tweet, write_file)


# In[68]:

# If you want to check how it looks like:
json.dumps(tweet) 


# In[69]:

# Read json format file (Deserialization)
with open("tweet_example.json", "r") as read_file:
    tweet2= json.load(read_file)


# In[70]:

tweet2


# ## Pickle: Python object serialization
# You can pickling any python object! Pickle is a binary serialization format, so use 'wb' or 'rb' mode.

# In[72]:

import pickle
with open('tweet_example.pickle', 'wb') as f: # set 'wb' instead of 'w'
    pickle.dump(data, f)


# In[73]:

with open('tweet_example.pickle', 'rb') as f:
    data = pickle.load(f)


# In[74]:

data


# In[ ]:



