#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Collatz Conjecture - Start with a number n > 1. 
Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2. 
If n is odd, multiply it by 3 and add 1.
"""
import sys

def main(n):
    steps=0
    while n != 1:
        if n%2==0:
            n = n/2
            steps+=1
        else:
            n = (n*3) + 1
            steps+=1
    print steps


if __name__ == "__main__":
    #validate
    if len(sys.argv)>2:
        print 'Usage: python collatz.py n'
        sys.exit()
    if int(sys.argv[1])<=1:
        print 'n must be > 1'
        sys.exit()
    main(int(sys.argv[1]))

