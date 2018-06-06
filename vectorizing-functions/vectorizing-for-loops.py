
# coding: utf-8

# I found a good link about the power of vectorizing functions + practice questions here:
# 
# 
# https://softwareengineering.stackexchange.com/questions/254475/how-do-i-move-away-from-the-for-loop-school-of-thought?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
# 
# There's also a good article about this topic here:
# 
# http://kitchingroup.cheme.cmu.edu/blog/2013/02/26/Sums-products-and-linear-algebra-notation-avoiding-loops-where-possible/

# In[11]:


import numpy as np


# In[29]:


# Problem 1
def sumproducts(x, y):
    """Return the sum of x[i] * y[j] for all pairs of indices i, j.

    >>> sumproducts(np.arange(3000), np.arange(3000))
    20236502250000

    """
    total_x=0
    for i in x:
        total_x+=i
    
    total_y=0
    for i in y:
        total_y+=i
    
    return total_x*total_y
    


# In[30]:


# Solution 1
def sumproducts_vectorized(x,y):
    """
    Return the sum of x[i] * y[j] for all pairs of indices i, j.
    """
    return np.sum(x)*np.sum(y)


# In[31]:


# Test 1
print sumproducts(np.arange(100),np.arange(100))
print sumproducts_vectorized(np.arange(100),np.arange(100))

get_ipython().magic(u'timeit -n 100 sumproducts(np.arange(100),np.arange(100))')
get_ipython().magic(u'timeit -n 100 sumproducts_vectorized(np.arange(100),np.arange(100))')


# In[3]:


# Problem 2
def countlower(x, y):
    """Return the number of pairs i, j such that x[i] < y[j].

    >>> countlower(np.arange(0, 200, 2), np.arange(40, 140))
    4500

    """
    result = 0
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] < y[j]:
                result += 1
    return result


# In[32]:


# Solution 2
def countlower_vectorized(x,y):
    """
    Return the number of pairs i, j such that x[i] < y[j].
    """
    
    return len(np.array(x)<np.array(y))


# In[34]:


# Test 2
print countlower(np.arange(100),np.arange(100))
print countlower_vectorized(np.arange(100),np.arange(100))

#%timeit -n 100 sumproducts(np.arange(100),np.arange(100))
#%timeit -n 100 sumproducts_vectorized(np.arange(100),np.arange(100))


# In[ ]:


# Problem 3
def cleanup(x, missing=-1, value=0):
    """Return an array that's the same as x, except that where x ==
    missing, it has value instead.

    >>> cleanup(np.arange(-3, 3), value=10)
    ... # doctest: +NORMALIZE_WHITESPACE
    array([-3, -2, 10, 0, 1, 2])

    """
    result = []
    for i in range(len(x)):
        if x[i] == missing:
            result.append(value)
        else:
            result.append(x[i])
    return np.array(result)


# In[ ]:


# Solution 3

