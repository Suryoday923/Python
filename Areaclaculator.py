print ("******* Area Claculator *******")
while True:
    print ("""Press 1 to calculate area of Square
    press 2 to calculate area of Rectangle
    press 3 to calculate area of circle
    press 4 to calculate area of triangle""")

    choice = int(input("Enter your number 1-4: "))

    if choice == 1:
        while True:
            side = float(input("Enter the side length: "))
            area = side**2
            print ("The area of square is: ", area)
            repeat = input("Do you want to try again with square? ")
            if repeat == "n" or repeat == "N":
                break

    elif choice == 2:
        while True:
            length = float(input("Enter the length of rectangle: "))
            width = float(input("Enter the width of rectangle: "))
            area = length * width
            print ("The area of rectangle is: ", area)
            repeat = input("Do you want to try again with rectangle? ")
            if repeat == "n" or repeat == "N":
                break

    elif choice == 3:
        while True:
            radius = float(input("Enter the radius of circle: "))
            area = 3.14 * radius**2
            print ("The area of circle is: ", area)
            repeat = input("Do you want to try again with circle? ")
            if repeat == "n" or repeat == "N":
                break

    elif choice == 4:
        while True:
            height = float(input("Enter the height of triangle: "))
            base = float(input("Enter the base of triangle: "))
            area = ((1/2) * base * height)
            print ("The area of triangle is: ", area)
            repeat = input("Do you want to try again with triangle? ")
            if repeat == "n" or repeat == "N":
                break

    repeat1 = input("Do you want to repeat the menu again? ")
    if repeat1 == "n" or repeat1 == "N":
        break



