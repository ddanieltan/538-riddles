#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

def main():
    with open('input/3.1.txt') as f:
        content=f.readlines()
        content=[x.strip('\n') for x in content]
        content=[x.strip() for x in content]
    print content


if __name__ == "__main__":
    main()

