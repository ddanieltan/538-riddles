#!/sr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
BinaryGap
Find longest sequence of zeros in binary representation of an integer.

https://codility.com/programmers/lessons/1-iterations/binary_gap/
"""
import sys

# Convert base10 number to binary
def to_binary(num):
    rm = []
    quotient = num
    while quotient!=1:
        remainder = quotient%2
        rm.append(remainder)
        quotient = quotient/2
    rm.append(1) # add 1 to the end of list
    rm.reverse() # reverse list
    output=''.join(str(x) for x in rm)
    return output #FYI, it's returning a string

def longest_length_of_zeroes(string_binary):
    count = 0
    max_count = 0
    index_of_1s = [i for i,char in enumerate(string_binary) if char == '1']
    string_binary = string_binary[min(index_of_1s):max(index_of_1s)+1]
    for i in string_binary:
        if i == '0':
            count+=1
            if count > max_count:
                max_count = count
        if i == '1':
            count=0
    return max_count

def main(num):
    string_binary=to_binary(num)
    print 'Base 10 : {}, Binary: {}'.format(num,string_binary)
    print 'Longest sequence of zeros = {}'.format(longest_length_of_zeroes(string_binary))
    return longest_length_of_zeroes(string_binary)
    
if __name__ == "__main__":
    main(int(sys.argv[1]))

