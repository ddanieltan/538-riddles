#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
https://www.reddit.com/r/dailyprogrammer/comments/6fe9cv/20170605_challenge_318_easy_countdown_game_show/
Given a set of numbers X1-X5, calculate using mathematical operations to solve for Y. 
You can use addition, subtraction, multiplication, or division.
Unlike "real math", the standard order of operations (PEMDAS) is not applied here. 
Instead, the order is determined left to right.
"""
import sys

def main(inputs):
    operands = '+-/*'

    # break inputs into arguments and final answer
    arguments = inputs[:-1]
    final_ans = int(inputs[-1])

    # create every single possible combination

    # evaluate if they come up to the answer


if __name__ == "__main__":
    inputs = []
    for i,value in enumerate(sys.argv):
        if i==0: #skip 1st argument
            continue
        inputs.append(int(value))

    main(inputs)

