#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.
"""
import sys

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

def test1():
    check = isprime(7)
    assert check==True

def test2():
    check = isprime(28)
    assert check==False

def main():
    print 'test'

if __name__ == "__main__":
    test1()
    test2()
    main()

