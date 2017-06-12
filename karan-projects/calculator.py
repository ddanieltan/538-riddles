#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Calculator - A simple calculator to do basic operators. Make it a scientific calculator for added complexity.
"""
import sys

def main(inputs):
    # parse inputs
    # print answer
    print 'test'


if __name__ == "__main__":
    #validation
    # for now my calculator only accepts <int> <operand> <int>
    for i in range(len(sys.argv)):
        if i==0:
            continue
        # if i is odd, input needs to be int
        if i%2!=0:
            if not int(sys.argv[i].isdigit()):
                print 'enter integers'
                sys.exit()
        # if i is even, input needs to be an operand
        if i%2==0:
            if sys.argv[i] not in ['+','-','*','/']:
                print 'Usage: python calculator.py <integer> <operand> <integer>'
                sys.exit()
        
    main(sys.argv[1:])

