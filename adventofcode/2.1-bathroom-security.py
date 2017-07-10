#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import pandas as pd

def get_result(instruction,start_x,start_y):
    grid=[['1','2','3'],['4','5','6'],['7','8','9']]
    #xy
    #00 01 02
    #10 11 12
    #20 21 22

    x,y=start_x,start_y
    
    for i in instruction:
        if i=='U' and y>0:
            y-=1
        if i=='D' and y<2:
            y+=1
        if i=='L' and x>0:
            x-=1
        if i=='R' and x<2:
            x+=1

    return grid[y][x]

def parse_instruction(string):
    #split on new line, strip whitespace
    return [word.split() for word in string.splitlines()]

def main():
    input_string="""ULL
    RRDDD
    LURDL
    UUUUD"""
    instructions=parse_instruction(input_string)
    output=[]
    for i in range(len(instructions)):
        print instructions[i]

    print get_result('ULL',1,1)

if __name__ == "__main__":
    main()

