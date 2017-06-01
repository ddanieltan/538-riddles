#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
From a shuffled deck of 100 cards that are numbered 1 to 100, 
you are dealt 10 cards face down. 
You turn the cards over one by one. 
After each card, you must decide whether to end the game. 
If you end the game on the highest card in the hand you were dealt, you win;
otherwise, you lose.

What is the strategy that optimizes your chances of winning? 
How does the strategy change as the sizes of the deck and the hand are changed?
"""
# solution: http://www.laurentlessard.com/bookproofs/pick-a-card/
import random

def main():
    dealt_hand=random.sample(xrange(1,101),10)
    print dealt_hand
    highest_card = max(dealt_hand)

    selected_card = 0
    for i in dealt_hand:
        # reveal 1 card
        # update largest card
        if dealt_hand[i] > selected_card:
            selected_card = dealt_hand[i]
        # decide to play or quit
    
    #
if __name__ == "__main__":
    main()

