#!/usr/bin/env/python2.7
"""
Four co-workers carpool to work each day. 
A driver is selected randomly for the drive to work and again randomly for the drive home. 
Each of the drivers has a lead foot, and each has a chance of being ticketed for speeding. 
Driver A has a 10 percent chance of getting a ticket each time he drives, 
Driver B a 15 percent chance, Driver C a 20 percent chance, and 
Driver D a 25 percent chance. The state will immediately revoke 
the license of a driver after his or her third ticket, 
and a driver will stop driving in the carpool once his license is revoked. 
Since there is only one police officer on the carpool route, 
a maximum of one ticket will be issued per morning and a max of one per evening.

Assuming that all four drivers start with no tickets, 
how many days can we expect the carpool to last until 
all the drivers have lost their licenses?
"""
import random

class Driver:
    def __init__(self, prob_pulled_over):
        self.prob_pulled_over = prob_pulled_over
        self.no_of_tix = 0

def testNumberOfTrips():
    a = Driver(0.1)
    b = Driver(0.15)
    c = Driver(0.2)
    d = Driver(0.25)

    drivers = [a,b,c,d]
    trips = 0
    while len(drivers) > 0:
        #choose random driver
        chosen_int = random.randint(0,len(drivers)-1) #0,1,2,3
        
        #roll if chosen driver gets a ticket
        roll = random.random()
        if roll <= drivers[chosen_int].prob_pulled_over:
            #give ticket
            drivers[chosen_int].no_of_tix += 1
        
        #remove driver if he has 3 tickets
        for driver in drivers:
            if driver.no_of_tix == 3:
                drivers.remove(driver)
        
        #log 1 trip (Morning Trip, Evening Trip)
        trips += 1

    return trips

def main():
    sumOfTrips = 0
    for _ in range(0,1000):
        sumOfTrips += testNumberOfTrips()

    # average no. of trips = sumOfTrips/1000
    # average no. of days = avg. no. of trips/2
    print sumOfTrips/2000.0
        
if __name__ == "__main__":
    main()
