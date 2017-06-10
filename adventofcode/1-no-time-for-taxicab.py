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

        #Figure out new orientation
        if turn=='R':
            co_ord.rotate(-1)
        else:
            co_ord.rotate()
        orientation = co_ord[0]

        #Walk steps, update position
        if orientation=='N':
            for _ in xrange(steps):
                y+=1
                log_and_check(x,y,log)
        if orientation=='E':
            for _ in xrange(steps):
                x+=1
                log_and_check(x,y,log)
        if orientation=='S':
            for _ in xrange(steps):
                y-=1
                log_and_check(x,y,log)
        if orientation=='W':
            for _ in xrange(steps):
                x-=1
                log_and_check(x,y,log)


def log_and_check(x,y,log):
    if [x,y] in log:
        print "(x,y)=({},{})".format(abs(x),abs(y))
        print 'x+y distance=',abs(x)+abs(y)
    else:
        log.append([x,y])



def main():
    #input
    inputs = 'L2, L3, L3, L4, R1, R2, L3, R3, R3, L1, L3, R2, R3, L3, R4, R3, R3, L1, L4, R4, L2, R5, R1, L5, R1, R3, L5, R2, L2, R2, R1, L1, L3, L3, R4, R5, R4, L1, L189, L2, R2, L5, R5, R45, L3, R4, R77, L1, R1, R194, R2, L5, L3, L2, L1, R5, L3, L3, L5, L5, L5, R2, L1, L2, L3, R2, R5, R4, L2, R3, R5, L2, L2, R3, L3, L2, L1, L3, R5, R4, R3, R2, L1, R2, L5, R4, L5, L4, R4, L2, R5, L3, L2, R4, L1, L2, R2, R3, L2, L5, R1, R1, R3, R4, R1, R2, R4, R5, L3, L5, L3, L3, R5, R4, R1, L3, R1, L3, R3, R3, R3, L1, R3, R4, L5, L3, L1, L5, L4, R4, R1, L4, R3, R3, R5, R4, R3, R3, L1, L2, R1, L4, L4, L3, L4, L3, L5, R2, R4, L2'

    # output
    # print walk(inputs)
    # test
    # print walk('L2, L3, L3, L4, R1, R2, L3, R3, R3, L1, L3, R2, R3, L3')
    print parse_instructions('R8, R4, R4, R8')
    # print walk(inputs)

if __name__ == "__main__":
    main()

