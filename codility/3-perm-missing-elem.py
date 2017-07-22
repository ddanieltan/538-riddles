#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import numpy as np

A=[2,3,1,5]

def solution(A):
    full_list = np.arange(max(A),0,-1)
    num = set(full_list)-set(A)
    print num.pop()

solution(A)
