#!/usr/bin/env python3

def happy_new_year():
    for i in range(10, 0, -1):  # Countdown from 10 to 1
        print(i)
    print("Happy New Year!")  # Print the final message

def square_integers(int_list):
    squared_list = []  # Initialize an empty list to store squared integers
    for i in int_list:
        if isinstance(i, int):
            squared_list.append(i ** 2)  # Append the squared value to the list
    return squared_list  # Return the list of squared integers

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    pass
