"""This is the LevelUp Python LevelUp called "Play The Waiting Game"""
import math
import time
import random


def waiting_game():

    number = random.randint(0,10)
    print("Your target time is " + str(number) + " seconds." )
    input("--- Press Enter to Begin ---")
    #get input
    #initialize timing function
    t1 = time.perf_counter()
    input("...Press Enter again after " + str(number) + " seconds...")
    #get input
    t2 = time.perf_counter()
    elapsed = t2-t1
    print(f"Elapsed Time: {t2-t1:0.4f} seconds.")
    if elapsed > number:
        print(f"({abs(elapsed - number):0.4f} seconds too slow)")
    elif elapsed < number:
        print(f"({abs(elapsed - number):0.4f} seconds) too fast)")
    elif elapsed == number:
        print("Whoa... you have amazing reflexes.")
    else:
        print("This is an error message. Something went wrong!")   
    return

waiting_game()