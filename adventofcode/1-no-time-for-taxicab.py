#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import urllib2

class Move:
    def __init__(self):
        self.orientation='north'
        self.x=0 #starting coordinates
        self.y=0

def main():
    #constants
    inputs = 'L2, L3, L3, L4, R1, R2, L3, R3, R3, L1, L3, R2, R3, L3, R4, R3, R3, L1, L4, R4, L2, R5, R1, L5, R1, R3, L5, R2, L2, R2, R1, L1, L3, L3, R4, R5, R4, L1, L189, L2, R2, L5, R5, R45, L3, R4, R77, L1, R1, R194, R2, L5, L3, L2, L1, R5, L3, L3, L5, L5, L5, R2, L1, L2, L3, R2, R5, R4, L2, R3, R5, L2, L2, R3, L3, L2, L1, L3, R5, R4, R3, R2, L1, R2, L5, R4, L5, L4, R4, L2, R5, L3, L2, R4, L1, L2, R2, R3, L2, L5, R1, R1, R3, R4, R1, R2, R4, R5, L3, L5, L3, L3, R5, R4, R1, L3, R1, L3, R3, R3, R3, L1, R3, R4, L5, L3, L1, L5, L4, R4, R1, L4, R3, R3, R5, R4, R3, R3, L1, L2, R1, L4, L4, L3, L4, L3, L5, R2, R4, L2'
    right_orientations = {
            'north' : 'east',
            'east' : 'south',
            'south' : 'west',
            'west' : 'north'
            }

    left_orientations = {
            'north' : 'west',
            'west' : 'south',
            'south' : 'east',
            'east' : 'north'
            }

    #parse inputs
    inputs = [word.strip() for word in inputs.split(',')] #split on comma, remove whitespace
    for instruction in inputs:
        if instruction[0] == 'L':
        if instruction[0] == 'R':

    # print coordinates of HQ

if __name__ == "__main__":
    main()

