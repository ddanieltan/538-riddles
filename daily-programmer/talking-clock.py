#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
https://www.reddit.com/r/dailyprogrammer/comments/6jr76h/20170627_challenge_321_easy_talking_clock/
Sample Input data
00:00
01:30
12:05
14:01
20:29
21:00

Sample Output data
It's twelve am
It's one thirty am
It's twelve oh five pm
It's two oh one pm
It's eight twenty nine pm
It's nine pm
"""
import sys

def main(user_input):
    #Dictionary
    num2words={1:'One',2:'Two',3:'Three', 4:'Four', 5:'Five',
            6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',
            11:'Eleven',12:'Twelve',
            20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty'
            }

    #Parse user input into HH and mm
    HH, mm = user_input.split(':')
    HH = int(HH)
    mm = int(mm)

    if HH>12:
        ampm='pm'
        HH -=12
    else:
        ampm='am'
    hour = num2words.get(HH)
    
    # handling 00-09 min
    if mm==0:
        minute=''
    elif mm<10:
        minute = 'oh '+num2words.get(mm)
    else:
        minute=num2words.get(mm)
    if minute is None:
        minute = num2words.get(mm-mm%10)+'-'+num2words.get(mm%10)

    #Print output
    output = "It's {} {} {}".format(hour,minute,ampm)
    if HH==0 and mm==0:
        print 'It\'s midnight'
    else:
        print output

if __name__ == "__main__":
    main('00:00')
    main('01:30')
    main('12:05')
    main('14:01')
    main('20:29')
    main('19:37')
    main('21:00')

