#!/usr/bin/env/python2.7
import random

class Driver:
    def __init__(self, prob_pulled_over):
        self.prob_pulled_over = prob_pulled_over
        self.no_of_tix = 0

def main():
    a = Driver(0.1)
    b = Driver(0.15)
    c = Driver(0.2)
    d = Driver(0.25)

    drivers = [a,b,c,d]
    trips = 0
    while len(drivers) > 0:
        #choose random driver
        chosen_int = random.randint(0,len(drivers))
        print chosen_int
        #roll if chosen driver gets a ticket
        roll = random.random()
        if roll <= drivers[chosen_int].prob_pulled_over:
            #give ticket
            drivers[chosen_int].no_of_tix += 1
        
        #remove driver if he has 3 tickets
        for driver in drivers:
            if driver.no_of_tix == 3:
                drivers.remove(driver)

        trips += 1

    print trips
        

if __name__ == "__main__":
    main()
