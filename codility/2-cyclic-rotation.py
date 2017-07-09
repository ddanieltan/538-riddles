#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from collections import deque

def solution(A, K):
    d = deque(A)
    d.rotate(K)
    d=list(d)
    return d

