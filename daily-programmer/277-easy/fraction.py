#!/usr/bin/env python2.7
"""
://www.reddit.com/r/dailyprogrammer/comments/4uhqdb/20160725_challenge_277_easy_simplifying_fractions/
"""
import sys

def main(num,den):
    #find greatest common divisor using Euclid's Algorithm
    #gcd(a,b)
    #  gcd(a,0)=a 
    #  gcd(a,b)=gcd(b,a %b)
    a = num
    b = den
    while b: #ie. while b != 0
        a,b = a, a%b
    print num/a, den/a

if __name__ == "__main__":
    # fraction.py num den
    if len(sys.argv) !=3:
        print 'Usage: python fraction.py numerator denominator'
        sys.exit()
    else:
        num = int(sys.argv[1])
        den = int(sys.argv[2])
        main(num,den)

