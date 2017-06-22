#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
https://codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
Find value that occurs in odd number of elements.

Solution:
https://www.martinkysel.com/codility-oddoccurrencesinarray-solution/
https://en.wikipedia.org/wiki/Bitwise_operation

"""
def solution(A):
    odd_num = 0
    for num in A:
        odd_num ^= num # XOR bitwise operation
    return odd_num

def main():
    test = [9,3,9,3,9,7,9]
    print 'test'
    print solution(test)
