#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Prime Factorization 
Have the user enter a number and find all Prime Factors (if there are any) and display them.
"""
import sys
import math

def isprime(number):
    if number==0: #0 is not prime
        return False
    elif number==1:
        return True
    elif number==2:
        return True
    elif number%2==0: #all even numbers are not prime
        return False
    else:
        for i in range(3,number-2,2): #check 3,5,7,9... 
            if number%i==0:
                return False
    return True


def main(number):
   prime_factors = [d for d in xrange(1,number+1) if isprime(d)]
   print prime_factors

if __name__ == "__main__":
    if len(sys.argv)!=2:
        print 'usage: python prime-factors.py <number>'
        sys.exit()
    number = int(sys.argv[1])
    main(number)

