first_number = int(input("Enter dirst number: "))

second_number = int(input("Enter second number: "))

    if first_number > 0 and second_number > 0:
        print ("Q1")

    elif first_number < 0 and second_number > 0:
        print ("Q2")

    elif first_number < 0 and second_number < 0:
        print ("Q3")

    elif first_number > 0 and second_number < 0:
        print ("Q4")
    
    elif first_number == second_number:
        print("origin")

    elif y == 0 and x != 0:
        print("x-axis")

    elif x == 0 and y != 0:
        print("y-axis")
