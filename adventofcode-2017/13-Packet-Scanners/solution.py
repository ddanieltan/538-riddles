
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

# In[1]:


# figure out how to traverse a list forwards, then backwards based on the tick


# In[2]:


# Understanding generators (keyword=yield) https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

def f123():
    yield 1
    yield 2
    yield 3

for item in f123():
    print item


# In[3]:


a=list(range(4))
b=list(reversed(a[1:-1]))
print a
print b


# In[32]:


# Elegant answer that only works in Python3
# https://stackoverflow.com/questions/50701772/how-to-traverse-a-list-until-it-reaches-the-last-element-then-traverse-it-backw/50701884#50701884

def bounce(list1):
    yield from list1
    yield from list(reversed(list1[1:-1]))
    
for x in bounce(range(4)):
    print x


# In[46]:


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


# In[55]:


def move_scanner(length,tick):
    """
    Return index of Scanner based on how long this layer is (length)
    and what tick (picosecond) are we on
    """
    forwards=list(range(length))
    backwards=list(reversed(forwards))[1:-1]
    generator=cycle(forwards+backwards)
    
    return list(islice(generator,tick,tick+1))[0]


# In[56]:


print move_scanner(3,0) #Ans should be 0
print move_scanner(3,1) #Ans should be 1
print move_scanner(3,2) #Ans should be 2
print move_scanner(3,3) #Ans should be 1
print move_scanner(3,4) #Ans should be 0


# In[1]:


def move_scanner(layer):
    """
    Move scanner within a layer on 1 tick
    Return new layer
    """
    
    output=list(layer)
    
    # find current index of scanner and direction
    index=0
    direction=''
    for i in output:
        if i!=None:
            index=output.index(i)
            direction=i
    
    #move 1 step forwards or backwards
    if direction=='f':
        if index+1==len(layer)-1: # swap f to b if we're at end of list
            output[index+1]='b'
        else:
            output[index+1]=direction
    elif direction=='b':
        if index-1==0:
            output[index-1]='f'
        else:
            output[index-1]=direction
        
    # remove initial entry
    output[index]=None

    
    return output


# In[2]:


move_scanner([None,None,'f',None])


# In[4]:


move_scanner([None,None,None,'b'])


# In[5]:


move_scanner([None,None,'b',None])


# In[6]:


move_scanner([None, 'b', None, None])


# In[7]:


test_inputs=[
    '0: 3',
    '1: 2',
    '4: 4',
    '6: 4',
]


# In[10]:


def parse_inputs(input_list,output={}):
    """
    Return a list of layers
    
    layer[0]=id
    layer[1]=[None, None, ..., None]
    """
    
    parsed=[i.split(': ') for i in input_list]
        
    for p in parsed:
        
        id_=int(p[0])
        initial_list=[None]*int(p[1])
        initial_list[0]='f'
        
        output[id_]=initial_list
        #output.append([id_,initial_list])
        
    return output
        


# In[11]:


parse_inputs(test_inputs)


# In[17]:


dictionary=parse_inputs(test_inputs)


# In[18]:


parse_inputs(test_inputs).keys()


# In[20]:


for i in range(6): #10 ticks
    for key,value in dictionary.iteritems():
        if i==key and value[0]=='f':
            print 'caught'
        else:
            dictionary[key]=move_scanner(value)

dictionary

