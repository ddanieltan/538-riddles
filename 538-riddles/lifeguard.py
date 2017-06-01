#!/usr/bin/env/python2.7
# -*- coding: utf-8 -*-
"""
You’re a lifeguard standing on the beach,
right at the edge of the water, and gazing out over the ocean.
You see someone drowning 100 meters to the right of you and 100 meters away from shore. 
You can run 100 meters in 15 seconds and swim 100 meters in 75 seconds. 
(The beach drops off steeply, meaning that you can’t run in the water.) 
What’s the fastest you can get to the victim?
"""
import math

speed_on_sand = 100/15.0
speed_in_water = 100/75.0

# find x
fastest_time=9999
for i in range(1,101,1): #start at 1, stop at 101, increment by 1
    total_time= i*speed_on_sand + math.sqrt(math.pow(100-i,2) + math.pow(100,2))*speed_in_water
    if total_time < fastest_time:
        fastest_time = total_time

print fastest_time
