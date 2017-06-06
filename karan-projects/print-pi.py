#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Find PI to the Nth Digit 
Enter a number and have the program generate PI up to that many decimal places. 
Keep a limit to how far the program will go.
"""
import sys

def main(limit):
    PI = 22.0/7
    print round(PI,limit)

if __name__ == "__main__":
    if len(sys.argv)!=2:
        print 'usage: python print-pi.py <limit>'
        sys.exit()
    limit = int(sys.argv[1])    
    main(limit)

