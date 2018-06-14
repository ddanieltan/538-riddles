
# coding: utf-8

# I found a good link about the power of vectorizing functions + practice questions here:
# 
# 
# https://softwareengineering.stackexchange.com/questions/254475/how-do-i-move-away-from-the-for-loop-school-of-thought?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
# 
# There's also a good article about this topic here:
# 
# http://kitchingroup.cheme.cmu.edu/blog/2013/02/26/Sums-products-and-linear-algebra-notation-avoiding-loops-where-possible/

# In[24]:


import numpy as np


# In[25]:


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
    


# In[26]:


# Solution 1
def sumproducts_vectorized(x,y):
    """
    Return the sum of x[i] * y[j] for all pairs of indices i, j.
    """
    return np.sum(x)*np.sum(y)


# In[27]:


# Test 1
old=sumproducts(np.arange(100),np.arange(100))
new=sumproducts_vectorized(np.arange(100),np.arange(100))

try: 
    assert(old==new)
    print 'test passed'
    get_ipython().magic(u'timeit -n 100 old')
    get_ipython().magic(u'timeit -n 100 new')
    
except AssertionError:
    print 'test failed'
    print 'New solution gave a different ans ({}) vs. original ({})'.format(new,old)



# In[28]:


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


# In[38]:


# Solution 2
def countlower_vectorized(x,y):
    """
    Return the number of pairs i, j such that x[i] < y[j].
    """
    
    return np.sum(np.searchsorted(np.sort(x),y))


# In[ ]:


get_ipython().magic(u'pinfo2 np.searchsorted')

"""
    Find the indices into a sorted array `a` such that, if the
    corresponding elements in `v` were inserted before the indices, the
    order of `a` would be preserved.
    
    Examples
    --------
    >>> np.searchsorted([1,2,3,4,5], 3)
    2
    >>> np.searchsorted([1,2,3,4,5], 3, side='right')
    3
    >>> np.searchsorted([1,2,3,4,5], [-10, 10, 2, 3])
    array([0, 5, 1, 2])
"""


# In[37]:


np.searchsorted([1,2,4],[3,5])
# The output [2,3] is equivalent to saying for each term in [3,5]
# For 3, there are 2 items in 1st list that are smaller
# For 5, there are 3 items in 1st list that are smaller
# summing up the results, we get all pairs of x[i]<y[j]


# In[36]:


countlower([1,2,4],[3,5])


# In[39]:


# Test 2
old=countlower(np.arange(100),np.arange(100))
new=countlower_vectorized(np.arange(100),np.arange(100))

try:
    assert(old==new)
    print 'test passed'
    get_ipython().magic(u'timeit -n 100 old')
    get_ipython().magic(u'timeit -n 100 new')
except AssertionError:
    print 'test failed'
    print 'New solution gave a different ans ({}) vs. original ({})'.format(new,old)


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

