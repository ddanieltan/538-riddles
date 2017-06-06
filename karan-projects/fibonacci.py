#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Fibonacci Sequence 
Enter a number and have the program generate the 
Fibonacci sequence to that number or to the Nth number.
"""
import sys

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def main(limit):
    for i in range(limit):
        print fib(i)

if __name__ == "__main__":
    if len(sys.argv)!=2:
        print 'usage: python fibonacci.py <limit>'
        sys.exit()
    limit = int(sys.argv[1])
    main(limit)

