# 1. Write program to sorted string in alphabetically in python

while True:
         a = input("Enter any thing: ")
         b = sorted(a)
         print(b)
         repeat = input("Would you like to repeat? (y/n): ")
         if repeat == "n" or repeat == "N":
             break