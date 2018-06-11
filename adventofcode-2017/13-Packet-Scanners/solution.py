
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
# In this situation, you are caught in layers 0 and 6,  
# because your packet entered the layer when its scanner was at the top when you entered it.  
# You are not caught in layer 1, since the scanner moved into the top of the layer once you were already there.  
# 
# The severity of getting caught on a layer is equal to its depth multiplied by its range.  
# (Ignore layers in which you do not get caught.) The severity of the whole trip is the sum of these values.  
# In the example above, the trip severity is 0*3 + 6*4 = 24.  
# 
# Given the details of the firewall you've recorded, if you leave immediately, what is the severity of your whole trip?  

# In[14]:


# figure out how to traverse a list forwards, then backwards based on the tick


# In[15]:


# Understanding generators (keyword=yield) https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do

def f123():
    yield 1
    yield 2
    yield 3

for item in f123():
    print item


# In[16]:


a=list(range(4))
b=list(reversed(a[1:-1]))
print a
print b


# In[ ]:


# Elegant answer that only works in Python3
# https://stackoverflow.com/questions/50701772/how-to-traverse-a-list-until-it-reaches-the-last-element-then-traverse-it-backw/50701884#50701884

def bounce(list1):
    yield from list1
    yield from list(reversed(list1[1:-1]))
    
for x in bounce(range(4)):
    print x


# In[18]:


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


# In[19]:


def move_scanner(length,tick):
    """
    Return index of Scanner based on how long this layer is (length)
    and what tick (picosecond) are we on
    """
    forwards=list(range(length))
    backwards=list(reversed(forwards))[1:-1]
    generator=cycle(forwards+backwards)
    
    return list(islice(generator,tick,tick+1))[0]


# In[ ]:


# Alternative way of finding index of the scanner, 
# sum(d*r for d,r,R in S if not d%R) # R= 2*range-2, d%R gives position of scanner


# In[20]:


print move_scanner(3,0) #Ans should be 0
print move_scanner(3,1) #Ans should be 1
print move_scanner(3,2) #Ans should be 2
print move_scanner(3,3) #Ans should be 1
print move_scanner(3,4) #Ans should be 0


# In[21]:


# The user/pointer will be at layer n at n ticks.
for n in range(5):
    print 'Pointer is at layer {}'.format(n)


# In[22]:


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
        


# In[23]:


test=[
    '0: 3',
    '1: 2',
    '4: 4',
    '6: 4',
]


# In[24]:


create_layers(test)


# In[25]:


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


# In[26]:


solve(test)


# In[27]:


with open('input.txt') as f:
    INPUTS=[i[:-1] for i in f.readlines()]
INPUTS[:5]


# In[28]:


# My wrong answer
solve(INPUTS)


# In[29]:


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


# In[30]:


# The error was caused by my poor way of parsing the input.txt
# Layer 88 had a depth of 14, but I captured it as a depth of 1
# Because i used i[:-1] which did not work for 2-digit depths


# In[31]:


# Correction
with open('input.txt') as f:
    INPUTS=[i.strip('\n') for i in f.readlines()]
INPUTS[:5]


# In[32]:


solve(INPUTS)


# --- Part Two ---
# 
# Now, you need to pass through the firewall without being caught - easier said than done.
# 
# You can't control the speed of the packet, but you can delay it any number of picoseconds.
# 
# For each picosecond you delay the packet before beginning your trip, all security scanners move one step.
# 
# You're not in the firewall during this time; you don't enter layer 0 until you stop delaying the packet.
# 
# 
# In the example above, if you delay 10 picoseconds (picoseconds 0 - 9), you won't get caught:
# 
# Because all smaller delays would get you caught, the fewest number of picoseconds you would need to delay to get through safely is 10.
# 
# What is the fewest number of picoseconds that you need to delay the packet to pass through the firewall without being caught?
# 

# In[33]:


import itertools


# In[34]:


def solve2(INPUTS):
    """
    Given a list of inputs, return the delay to not get caught by the scanner
    """
    d=create_layers(INPUTS)

    for delay in itertools.count():
        TICKS=range(max(d.keys())+1+delay)[delay:]
        caught=0
        
        for t in TICKS:
            try:
                layer=d[t-delay]
                if move_scanner(len(layer),t)==0:
                    #print 'Delay={} Caught at layer {} depth {}'.format(delay,t,len(layer))
                    caught+=1

            except KeyError:
                pass
        
        #print caught
        if caught==0:
            return delay
        
    
    return 9999 #no answer found
    


# In[35]:


# Demo of counter
for delay in itertools.count():
    print range(6+1+delay)[delay:]
    if delay==5:
        break


# In[36]:


solve2(test)


# In[ ]:


solve2(INPUTS)

# I believe the solution here is correct but it runs WAY too slow because I'm looping through every step. 
# The final ans is in the millions. So this is a terribly inefficient way to find the answer.


# In[56]:


# Creating the layers
def create_layers2(input_list):
    """
    Inputs: str(layer_id,layer_length), eg. '0: 3'
    Output: dict{key=layer_id, values=[0,1,2...layer_length],2*range-2 }
    """
    list_=[]
    for string in input_list:
        # Parse string eg. "0: 3"
        a,b=string.split(': ')
        layer_id=int(a)
        layer_length=int(b)

        list_.append((layer_id,layer_length,2*layer_length-2))
    
    return list_
        


# In[57]:


M=create_layers2(test)
M


# In[58]:


S=create_layers2(INPUTS)


# In[81]:


# Correct answer online for Part 2
(i for i in itertools.count() if all((i+d)%R for d,r,R in S)).next()


# In[ ]:


## Breaking it down
next                          #python3 syntax, python2 is .next()
(i for i in itertools.count() # generator that produces 0,1,2,3...
 if 
 all(                         # returns True only if all inner conditions are True
     (i+d)%R for d,r,R in S   # formula outputting index
 )
)


# In[ ]:


# every i in the list comprehension needs to be a non-None value before all(...) returns True
all(i for i in [1,2,3,4,5])


# In[85]:


all(i for i in [1,2,3,4,5,None])


# In[ ]:


## Better worded but same model answer solution

lines = [line.split(': ') for line in sys.stdin.readlines()]

heights = {int(pos): int(height) for pos, height in lines}

def scanner(height, time):
    offset = time % ((height - 1) * 2)

    return 2 * (height - 1) - offset if offset > height - 1 else offset

part1 = sum(pos * heights[pos] for pos in heights if scanner(heights[pos], pos) == 0)

part2 = next(wait for wait in itertools.count() if not any(scanner(heights[pos], wait + pos) == 0 for pos in heights))
permalinkembedsavegive gold

