

#Defining all the functions of calculator 

def sum(a,b):
    return f"The sum of {a} and {b} is found to be {a+b}"

def subtract(a,b):
    return f"The subtraction of {a} and {b} is found to be {a-b}"

def multiplication(a,b):
    return f"The multiplication of {a} and {b} is found to be {a*b}"

def division(a,b):
    return f"The division of {a} and {b} is found to be {a/b}"


#Starting the functions of calculator

greet = "Welcome to the Simple Calculator"
print(greet.center(50,"*"))    #make the center greet and at both sides will print the asteric

#using while True so that loop will be continously executed until and unless we use the break statement or quit the program
while True:
    print("""\n
Select the option which you want to perform
1 : Sum
2 : Suctract
3 : Multiply
4 : Division
5 : Exit
""")
    while True:    #Will continue to be executed until the user select the appropiate function
        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice.isdigit():
            choice = int(choice)
            if choice in [1,2,3,4,5]:  #checking if the choice is present in the list or not which is basically the list of all the choices available
                break   #will break the inner loop when user have been entered the right choices other wise the loop will be contnuously executed
            else:
                print("Select an appropiate option.")
        else:
            print("Kindly enter digit")
    try:
        a = int(input("Enter the 1st number: ")) #taking input the vlaue 
        b = int(input("Enter the second number: "))
        if choice == 1:  #checking the user has entered which value
            print(sum(a,b))
        elif choice == 2:
            print(subtract(a,b))
        elif choice == 3:
            print(multiplication(a,b))
        elif choice == 4:
            print(division(a,b))
        else:
            print("Ok The program is being quitting. ")
            quit()
    except ZeroDivisionError:  #handling the error if zero division arises this part will be executed
        print("Zero division error kindly dont chose the second number")
    except ValueError:
        print("Invalid input")