
# coding: utf-8

# --- Day 13: Packet Scanners ---  
# You need to cross a vast firewall.  
# The firewall consists of several layers, each with a security scanner that moves back and forth across the layer.  
# To succeed, you must not be detected by a scanner.  
# 
# By studying the firewall briefly, you are able to record (in your puzzle input) the depth of each layer  
# and the range of the scanning area for the scanner within it, written as depth: range.  
# Each layer has a thickness of exactly 1.  
# A layer at depth 0 begins immediately inside the firewall; a layer at depth 1 would start immediately after that.  
# 
# For example, suppose you've recorded the following:  
# 
# 0: 3  
# 1: 2  
# 4: 4  
# 6: 4  
# This means that there is a layer immediately inside the firewall (with range 3),  
# a second layer immediately after that (with range 2), a third layer which begins at depth 4 (with range 4),  
# and a fourth layer which begins at depth 6 (also with range 4). Visually, it might look like this:  
# 
#  0   1   2   3   4   5   6  
# [ ] [ ] ... ... [ ] ... [ ]  
# [ ] [ ]         [ ]     [ ]  
# [ ]             [ ]     [ ]  
#                 [ ]     [ ]  
# Within each layer, a security scanner moves back and forth within its range.  
# Each security scanner starts at the top and moves down until it reaches the bottom,  
# then moves up until it reaches the top, and repeats.  
# A security scanner takes one picosecond to move one step. Drawing scanners as S,  
# the first few picoseconds look like this:  
# 
# 
# Picosecond 0:  
#  0   1   2   3   4   5   6  
# [S] [S] ... ... [S] ... [S]  
# [ ] [ ]         [ ]     [ ]  
# [ ]             [ ]     [ ]  
#                 [ ]     [ ]  
# 
# Picosecond 1:  
#  0   1   2   3   4   5   6  
# [ ] [ ] ... ... [ ] ... [ ]  
# [S] [S]         [S]     [S]  
# [ ]             [ ]     [ ]  
#                 [ ]     [ ]  
# 
# Picosecond 2:  
#  0   1   2   3   4   5   6  
# [ ] [S] ... ... [ ] ... [ ]  
# [ ] [ ]         [ ]     [ ]  
# [S]             [S]     [S]  
#                 [ ]     [ ]  
# 
# Picosecond 3:  
#  0   1   2   3   4   5   6  
# [ ] [ ] ... ... [ ] ... [ ]  
# [S] [S]         [ ]     [ ]  
# [ ]             [ ]     [ ]  
#                 [S]     [S]  
# Your plan is to hitch a ride on a packet about to move through the firewall.  
# The packet will travel along the top of each layer, and it moves at one layer per picosecond.  
# Each picosecond, the packet moves one layer forward (its first move takes it into layer 0),  
# and then the scanners move one step.  
# If there is a scanner at the top of the layer as your packet enters it, you are caught.  
# (If a scanner moves into the top of its layer while you are there, you are not caught:  
# it doesn't have time to notice you before you leave.) If you were to do this in the configuration above,  
# marking your current position with parentheses, your passage through the firewall would look like this:  
# 
# Initial state:  
#  0   1   2   3   4   5   6  
# [S] [S] ... ... [S] ... [S]  
# [ ] [ ]         [ ]     [ ]  
# [ ]             [ ]     [ ]  
#                 [ ]     [ ]  
# 
# Picosecond 0:  
#  0   1   2   3   4   5   6  
# (S) [S] ... ... [S] ... [S]  
# [ ] [ ]         [ ]     [ ]  
# [ ]             [ ]     [ ]  
#                 [ ]     [ ]  
# 
#  0   1   2   3   4   5   6  
# ( ) [ ] ... ... [ ] ... [ ]  
# [S] [S]         [S]     [S]  
# [ ]             [ ]     [ ]  
#                 [ ]     [ ]  
# 
# 
# Picosecond 1:  
#  0   1   2   3   4   5   6  
# [ ] ( ) ... ... [ ] ... [ ]  
# [S] [S]         [S]     [S]  
# [ ]             [ ]     [ ]  
#                 [ ]     [ ]  
# 
#  0   1   2   3   4   5   6  
# [ ] (S) ... ... [ ] ... [ ]  
# [ ] [ ]         [ ]     [ ]  
# [S]             [S]     [S]  
#                 [ ]     [ ]  
# 
# 
# Picosecond 2:  
#  0   1   2   3   4   5   6  
# [ ] [S] (.) ... [ ] ... [ ]  
# [ ] [ ]         [ ]     [ ]  
# [S]             [S]     [S]  
#                 [ ]     [ ]  
# 
#  0   1   2   3   4   5   6  
# [ ] [ ] (.) ... [ ] ... [ ]  
# [S] [S]         [ ]     [ ]  
# [ ]             [ ]     [ ]  
#                 [S]     [S]  
# 
# 
# Picosecond 3:  
#  0   1   2   3   4   5   6  
# [ ] [ ] ... (.) [ ] ... [ ]  
# [S] [S]         [ ]     [ ]  
# [ ]             [ ]     [ ]  
#                 [S]     [S]  
# 
#  0   1   2   3   4   5   6  
# [S] [S] ... (.) [ ] ... [ ]  
# [ ] [ ]         [ ]     [ ]  
# [ ]             [S]     [S]  
#                 [ ]     [ ]  
# 
# 
# Picosecond 4:  
#  0   1   2   3   4   5   6  
# [S] [S] ... ... ( ) ... [ ]  
# [ ] [ ]         [ ]     [ ]  
# [ ]             [S]     [S]  
#                 [ ]     [ ]  
# 
#  0   1   2   3   4   5   6  
# [ ] [ ] ... ... ( ) ... [ ]  
# [S] [S]         [S]     [S]  
# [ ]             [ ]     [ ]  
#                 [ ]     [ ]  
# 
# 
# Picosecond 5:  
#  0   1   2   3   4   5   6  
# [ ] [ ] ... ... [ ] (.) [ ]  
# [S] [S]         [S]     [S]  
# [ ]             [ ]     [ ]  
#                 [ ]     [ ]  
# 
#  0   1   2   3   4   5   6  
# [ ] [S] ... ... [S] (.) [S]  
# [ ] [ ]         [ ]     [ ]  
# [S]             [ ]     [ ]  
#                 [ ]     [ ]  
# 
# 
# Picosecond 6:  
#  0   1   2   3   4   5   6  
# [ ] [S] ... ... [S] ... (S)  
# [ ] [ ]         [ ]     [ ]  
# [S]             [ ]     [ ]  
#                 [ ]     [ ]  
# 
#  0   1   2   3   4   5   6  
# [ ] [ ] ... ... [ ] ... ( )  
# [S] [S]         [S]     [S]  
# [ ]             [ ]     [ ]  
#                 [ ]     [ ]  
# In this situation, you are caught in layers 0 and 6,  
# because your packet entered the layer when its scanner was at the top when you entered it.  
# You are not caught in layer 1, since the scanner moved into the top of the layer once you were already there.  
# 
# The severity of getting caught on a layer is equal to its depth multiplied by its range.  
# (Ignore layers in which you do not get caught.) The severity of the whole trip is the sum of these values.  
# In the example above, the trip severity is 0*3 + 6*4 = 24.  
# 
# Given the details of the firewall you've recorded, if you leave immediately, what is the severity of your whole trip?  

# In[47]:


# figure out how to traverse a list forwards, then backwards based on the tick


# In[48]:


# Understanding generators (keyword=yield) https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

def f123():
    yield 1
    yield 2
    yield 3

for item in f123():
    print item


# In[49]:


a=list(range(4))
b=list(reversed(a[1:-1]))
print a
print b


# In[50]:


# Elegant answer that only works in Python3
# https://stackoverflow.com/questions/50701772/how-to-traverse-a-list-until-it-reaches-the-last-element-then-traverse-it-backw/50701884#50701884

def bounce(list1):
    yield from list1
    yield from list(reversed(list1[1:-1]))
    
for x in bounce(range(4)):
    print x


# In[51]:


# Alternative solution using itertools.cycle
from itertools import cycle, islice

# create a generator
g = cycle([1,2,3])

# print out values
# Syntax for Python 2 = itertools.cycle.next()
# Syntax for Python 3 = next(itertools.cycle())
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()

print '\nFinding nth element in generator'
for i in range(10): # 5 ticks
    g.next()
    if i==6:
        print g.next()

g = cycle([1,2,3])
print '\n using islice'
# islice(generator, start_index, stop_index)
list(islice(g,4,5))[0]


# In[52]:


def move_scanner(length,tick):
    """
    Return index of Scanner based on how long this layer is (length)
    and what tick (picosecond) are we on
    """
    forwards=list(range(length))
    backwards=list(reversed(forwards))[1:-1]
    generator=cycle(forwards+backwards)
    
    return list(islice(generator,tick,tick+1))[0]


# In[53]:


print move_scanner(3,0) #Ans should be 0
print move_scanner(3,1) #Ans should be 1
print move_scanner(3,2) #Ans should be 2
print move_scanner(3,3) #Ans should be 1
print move_scanner(3,4) #Ans should be 0


# In[54]:


# The user/pointer will be at layer n at n ticks.
for n in range(5):
    print 'Pointer is at layer {}'.format(n)


# In[55]:


# Creating the layers
def create_layers(input_list):
    """
    Inputs: str(layer_id,layer_length), eg. '0: 3'
    Output: dict{key=layer_id, value=[0,1,2...layer_length]}
    """
    dict_={}
    for string in input_list:
        # Parse string eg. "0: 3"
        a,b=string.split(': ')
        layer_id=int(a)
        layer_length=int(b)

        dict_[layer_id]=range(layer_length)
    
    return dict_
        


# In[56]:


test=[
    '0: 3',
    '1: 2',
    '4: 4',
    '6: 4',
]


# In[57]:


create_layers(test)


# In[68]:


def solve(INPUTS):
    """
    Given a list of inputs, return severity
    Severity = layer1*id1 + layer2*id2 ...
    """

    d=create_layers(INPUTS)
    TICKS=range(max(d.keys())+1)
    severity=0

    for t in TICKS:
        try:
            layer=d[t]
            if move_scanner(len(layer),t)==0:
                print 'Caught at layer {} depth {}'.format(t,len(layer))
                severity+=(len(layer)*t)

        except KeyError:
            pass
    
    return severity


# In[69]:


solve(test)


# In[70]:


with open('input.txt') as f:
    INPUTS=[i[:-1] for i in f.readlines()]
INPUTS[:5]


# In[71]:


# My wrong answer
solve(INPUTS)


# In[67]:


# Correct Answer

total = 0

for line in INPUTS:
    layer, depth = list(map(int, line.split(": ")))
    try:
        if layer % ((depth - 1)*2) == 0:
            print 'Caught at layer {} depth {}'.format(layer,depth)
            total += layer*depth
    except ZeroDivisionError:
        pass

print(total)


# In[ ]:


# The error was caused by my poor way of parsing the input.txt
# Layer 88 had a depth of 14, but I captured it as a depth of 1
# Because i used i[:-1] which did not work for 2-digit depths


# In[75]:


# Correction
with open('input.txt') as f:
    INPUTS=[i.strip('\n') for i in f.readlines()]
INPUTS[:5]


# In[76]:


solve(INPUTS)

