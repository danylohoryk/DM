import Lab1, Lab2, Lab3, Lab4

while True:
    print("Which lab you want to run:\n1. Lab 1\n2. Lab 2\n3. Lab 3\n4. Lab 4\n5. Exit")
    num = int(input("Enter the laboratory number: "))
    numbers = [1, 2, 3, 4, 5]
    if num not in numbers:
        print("You enter wrong laboratory number!")
        num = int(input("Enter the laboratory number: "))
    if num in numbers:
        if num == 1:
            print("\nLab 1 starting ...\n")
            Lab1.lab1("l1_1.txt")
            print("\nend\n")
        if num == 2:
            print("\nLab 2 starting ...\n")
            Lab2.lab2("l2-1.txt")
            print("\nend\n")
        if num == 3:
            print("\nLab 3 starting ...\n")
            Lab3.lab3("l3-1.txt")
            print("\nend\n")
        if num == 4:
            print("\nLab 4 starting ...\n")
            Lab4.lab4("l4-1.txt")
            print("\nend\n")
        if num == 5:
            break
