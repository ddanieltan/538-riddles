#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Given a list of integers separated by a single space on standard input, 
print out the largest and smallest values that can be obtained by 
concatenating the integers together on their own line. 
"""
import sys

# https://stackoverflow.com/questions/8306654/finding-all-possible-permutations-of-a-given-string-in-python
def permutation(string):
    if len(string) <=1:
        return {str} #type=set
    perm_set = set()
    for index, char in enumerate(string):
        new_string = removeCharFromString(string, index)
        new_set = permutation(new_string)
        for element in new_set:
            perm_set.add(char+new_set[element]) #THIS IS where the code breaks
            # perm_set.add(char+"{}".format(element))
    return perm_set

def removeCharFromString(string, index):
    if index == len(string):
        return string[:index] + string[index:]
    else:
        return string[:index] + string[index+1:]

def main():
#     arguments = [num for num in sys.argv[1:]] #arguments are passed as strings
    # numbers = []
#     # for i in arguments:
    answer = permutation('123')
    print answer

    # create array of all possible numbers
    # print max
    

if __name__ == "__main__":
    print 'Entered {} arguments...'.format(len(sys.argv)-1)
    main()

