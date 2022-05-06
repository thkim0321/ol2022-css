
# coding: utf-8

# In[1]:

import re
def get_float(s):
    m = re.search('\d+.\d+', s)
    if m:
        return float(m.group(0))
print('the number is: {}'.format(get_float('some text 2.5')))


# # Regural Expression (regexp)
# * it describes a set of strings
# * we say a string $s$ is matched by the regexp $r$ and the regexp $r$ matches string $s$
# * s = ~r

# ## Characters with special meanings:
# - **`.`**　: (a dot) matches any single character
# - **`r*`**:　arbitrary repetition of expression `r`(could be 0)
# - **`(r1|r2|...|ri)`**: matches one of the alternatives `r1...ri`
# - **`r?`**:　`(r|)`
# - **`r+`**:　`rr*`
# - **`[abc]`**:　`(a|b|c)` Note: special characters loose their special meaning
# - **`[^abc]`**:　negated character range: everything except `a, b` or `c`
# - **`ˆ,$`**:　line start, line end. `^[0-9.]*`: lines with only digits and dots

# ## Character classes:
# - **`\w, \W`**: word character, anything **BUT** word character
# - **`\d, \D`**:　decimal digit, anything **BUT** decimal digits
# - **`\s, \S`**:　white space character, anything **BUT** whitespace character

# ### More info: https://docs.python.org/3/library/re.html

# In[7]:

m = re.search(r'\d+\.\d+', '02.234')  #\. : escape special meaning
print(m)


# In[8]:

m = re.search(r'(\d|[1-9]\d+)\.\d+', '02.3') # avoid 0x.xxx ...
print(m)


# In[4]:

m = re.search(r'(\d|[1-9]\d+)(\.\d+)?','4') # now it matchs interger as well
print(m)


# In[10]:

m = re.search(r'[+-]?(\d|[1-9]\d+)(\.\d+)?','-4') # now it matches -X or +X
print(m)


# In[11]:

m = re.search(r'\w+[\w.]\w+@\w+\.\w+','some.guy@uni.mail')
print(m)


# ## `re`

# - `search`: search for a regular expression anywhere in the string. Returns `None` or `Match` pbject giving access to the captured group.  
# - `re.search(pattern, string, flags=0)`

# In[11]:

import re

m = re.search('(\d+) (\w+)', '100 kilomiter')
if m:
    print(m.group())  # match result
    print(m.start())  # start position
    print(m.end())    # end position
    print(m.span())   # (start , end) position


# In[12]:

pattern = re.compile(r'(\d+) (\w+)') # when you use pattern multiple time, this way is faster
m = pattern.search('100 kilometer')
print(m.group())


# - `re.sub` : substitude occurrences of a pattern
# - `re.sub(pattern, repl, string, count=0)`

# In[13]:

text = "abc123def456efg"
newtext = re.sub(r'[a-z]+', ' WORDS', text)
print(newtext)


# ### `flags`
# - `re.IGNORECASE` : case-insensitive matching
# - `re.DOTALL` : the dot also matches newlines

# In[14]:

m = re.search(r'cat','CAt',re.IGNORECASE)
print(m)


# In[15]:

text = 'I love c \nat'
print(text)
m = re.search(r'c..at',text, re.DOTALL)
print(m)


# In[ ]:



