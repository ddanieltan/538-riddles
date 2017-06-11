#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from collections import deque #double ended queue

def parse_instructions(input_string):
    x=0 #start at origin
    y=0
    co_ord = deque('NESW')
    orientation = co_ord[0] # Start facing North
    log=[]

    # parse string
    inputs1 = [word.strip() for word in input_string.split(',')] #split on comma, remove whitespace
    
    for i in inputs1:
        turn, steps = i[0],int(i[1:])
        if turn=='R':
            co_ord.rotate(-1)
        else:
            co_ord.rotate()
        orientation = co_ord[0]

        #Walk steps, update position
        if orientation=='N':
            for _ in xrange(steps):
                y+=1
                if log_and_check(x,y,log):
                    return x,y
        if orientation=='E':
            for _ in xrange(steps):
                x+=1
                if log_and_check(x,y,log):
                    return x,y
        if orientation=='S':
            for _ in xrange(steps):
                y-=1
                if log_and_check(x,y,log):
                    return x,y
        if orientation=='W':
            for _ in xrange(steps):
                x-=1
                if log_and_check(x,y,log):
                    return x,y

    return 0,0 


def log_and_check(x,y,log):
    if [x,y] in log:
        return True
    else:
        log.append([x,y])
        return False



def main():
    #input
    inputs = 'L2, L3, L3, L4, R1, R2, L3, R3, R3, L1, L3, R2, R3, L3, R4, R3, R3, L1, L4, R4, L2, R5, R1, L5, R1, R3, L5, R2, L2, R2, R1, L1, L3, L3, R4, R5, R4, L1, L189, L2, R2, L5, R5, R45, L3, R4, R77, L1, R1, R194, R2, L5, L3, L2, L1, R5, L3, L3, L5, L5, L5, R2, L1, L2, L3, R2, R5, R4, L2, R3, R5, L2, L2, R3, L3, L2, L1, L3, R5, R4, R3, R2, L1, R2, L5, R4, L5, L4, R4, L2, R5, L3, L2, R4, L1, L2, R2, R3, L2, L5, R1, R1, R3, R4, R1, R2, R4, R5, L3, L5, L3, L3, R5, R4, R1, L3, R1, L3, R3, R3, R3, L1, R3, R4, L5, L3, L1, L5, L4, R4, R1, L4, R3, R3, R5, R4, R3, R3, L1, L2, R1, L4, L4, L3, L4, L3, L5, R2, R4, L2'

    # output

    # test
    # parse_instructions('L2, L3, L3, L4, R1, R2, L3, R3, R3, L1, L3, R2, R3, L3')
    # x,y=parse_instructions('R8, R4, R4, R8')
    x,y=parse_instructions(inputs)
    print '(x,y)=({},{})'.format(x,y)
    print 'x + y =',abs(x)+abs(y)

    # parse_instructions(inputs)

if __name__ == "__main__":
    main()

