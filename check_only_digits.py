# Write a program to check if a string contains only digits.

while True:
    a = input("Enter any thing : ")
    b = (a.isdigit())

    if b == True:
        print("Its contain only digits : ")

    else:
        print("Its not contain digits Or Its contains a combination")

    repeat = input("Do you want to check again ? (y/n): ")
    if repeat == "n" or repeat == "no":
        break
