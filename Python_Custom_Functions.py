""""
Question 1:

Title: Even Odd number

Parameters:
--number(int) and check whether the number is odd or even

Returns:
--It will return the result in the form of str and int whether the number is odd or even.

Test Case 1:
Number = 20
Expected Result : 20 is even.
Actual Result : 20 is even .

Test Case 2:
Number = 19
Expected Result : 19 is odd.
Actual Result : 20 is odd.
"""
def even_odd_number(number):
    if number%2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

print("Question#1 \nTitle: Even Odd number")
print("\n")
print(even_odd_number(20))
print("\n")
print(even_odd_number(19))

""""
Question 2:

Title: Finding  Min and Max number sequence in a list 

Parameters:
--list which will contain the list 

Returns:
--Integer.


Test Case 1:
list = [1,2,3,4,5,6]
Expected Result : max=6 ,min =1
Actual Result :max=6 ,min =1

Test Case 2:
list = [20,30,40,67]
Expected Result : max = 67 , min =20
Actual Result : max = 67 , min =20
"""
def min_max(lst):
    max = lst[0]
    for i in range(len(lst)):
        if lst[i]>max:
            max = lst[i]
        else:
            pass    

    min = lst[0]
    for i in range(len(lst)):
        if lst[i]<min:
            min = lst[i]
        else:
            pass    
    
    return f"The max and min number in the list {lst} is found to be {max} and {min} respectively"

print("\nQuestion#2 \nTitle: Finding  Min and Max number sequence in a list")

print(min_max([1,2,3,4,5,6]))
print(min_max([20,30,40,67]))

""""
Question 3:

Title: Table of any number.
Parameters:
--The number for which we want to find the table.
--The number n by which we want to find our table 
Returns:
--Print the table in the form of columns and rows


Test Case 1:
number = 9
end = 10

Test Case 2:
number = 20
end = 10
"""

def table(number,n):
    for i in range(n):
        print(f"{number} x {i+1} = {number*i}")


print("\nQuetion#3 \nTitle: Table of any number.")
print("\n")
table(9,10)
print("\n\n\n")
table(20,10)

""""
Question 4:

Title: Factorial  any number.
Parameters:
--number(int) 
Returns:
--Print the factorial of the number


Test Case 1:
number = 5
Expected answer :
Actual Answer :

Test Case 2:
number = 0
Expected Answer :
Actual Answer :
"""

def factorial(number):
    if number == 0 or number == 1:
        return f"The factorial of {number} is 1"
    else:
        fact = 1
        for i in range(1,number+1):    # since the loop will be executed till n-1 
            fact*=i
        return f"The factorial of {number} is {fact}"
    
print("\nQuestion#4 \nTitle: Factorial  any number")
print("\n")
print(factorial(0))
print("\n")
print(factorial(5))

"""
Question 5:

Title: Finding min and max numbers in a list

Parameters:
--list

Returns:
--It will return the sum of all the elements in the list.

Test Case 1:
list = [1,2,3,4,5,6]
Expected Result : 21
Actual Result :21

Test Case 2:
list = [20,30,40,67]
Expected Result :157 
Actual Result : 157

"""
#Function to find the sum of all the elements in a list 

def sum_of_list(lst):
    sum = 0
    for i in range(len(lst)):
        sum+=lst[i]

    return f"The sum of the {lst} is found to be {sum}"
print("\n\nQuestion#5 \nTitle: Finding min and max numbers in a list")
lst_1 = [1,2,3,4,5,6]
lst_2 = [20,30,40,67]
print("\n")
print(sum_of_list(lst_1))
print("\n")
print(sum_of_list(lst_2))

"""
Question 6:

Title: Generating acsending and decending numbers sequence using loop

Parameters:
--numbers 

Returns:
--ascended list or descended list

Test Case 1 of ascend:
numbers = [25,34,67,23,14]
Expected Result : [14,23,25,34,67]
Actual Result : [14,23,25,34,67]
 
Test Case 1 of descend:
numbers = [25,34,67,23,14]
Expected Result : [67,34,25,23,14]
Actual Result : [67,34,25,23,14]
 

"""

def ascending(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            temp = lst[j]
            if lst[j]>lst[j+1]:
                lst[j] = lst[j+1]
                lst[j+1] =temp
            else:
                pass 
    return f"The list in ascending order is {lst}"

def descending(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            temp = lst[j]
            if lst[j]<lst[j+1]:
                lst[j] = lst[j+1]
                lst[j+1] =temp
            else:
                pass 
    return f"The list in descending order is {lst}"

print("\n")
print("\nQuestion#6 \nTitle: Generating acsending and decending numbers sequence using loop ")
print("\n")
print(ascending([25,34,67,23,14]))

print(descending([25,34,67,23,14]))

"""Question 7:

Title: Generating acsending and decending numbers sequence using loop

Parameters:
--radius

Returns:
--area of the circle

Test Case of radius:
radius = 3m
Expected value :
Actual value   : 
"""

def area_of_circle(radius):
    return f"The area is found to be {3.1452*(radius)**2} square meter"

print("\nQuestion#7 \nTitle: Radius of any circle")
print("\n")
print(area_of_circle(2))

"""Question 8:

Title: Convert Celsius to Fahrenheit and vice versa

Parameters:
--temperature in celsius or in farenheit 

Returns:
--celsius to farenheit or vice versa

Test Case of celsius to farenheit:
radius = 50 c
Expected value : 122F
Actual value   : 122F

Test Case of farenheit to celsius:
radius = 50 F
Expected value : 10C
Actual value   :10C
"""
def celsius_to_farenheit(celsius):
    faren = ((9/5)*celsius)+32
    return f"The temperature of {celsius}C is equivalent to {faren}F"

def farenheit_to_celsius(faren):
    celsius= ((faren - 32)*(5/9))
    return f"The temperature of {faren}F is equivalent to {celsius}C"

print("\nQuestion#8 \nTitle: Convert Celsius to Fahrenheit and vice versa\n")
print(f"\n{celsius_to_farenheit(50)}")
print(f"\n{farenheit_to_celsius(50)}")

"""Question 9:

Title: Sum of the n positive integer

Parameters:
--n

Returns:
--sum(integer)

Test 1:
n = 5
Expected value :15
Actual value   :15

Test 2:
n = 50 
Expected value :1275
Actual value   :1275
"""
def sum_to_n(n):
    sum = 0
    for i in range(n+1):
        sum+=i
    return f"The sum to {n} is found to be {sum}"

print("\nQuestion#9 \nTitle: Sum of the n positive integer")
print(f"\n{sum_to_n(5)}")
print(f"\n{sum_to_n(50)}")

"""Question 10:

Title: Linear Search

Parameters:
--list ,the number which is required 

Returns:
--index of that element 

Test 1:
lst = [1,4,5,7,8]
required number = 9
Expected value :number is not found
Actual value   :number is not found

Test 2:
lst = [13,5,68,90]
required number = 90
Expected value :the number is found to be at 3 index 
Actual value   :the number is found to be at 3 index
"""

def linear_search(lst,n):   #the lst is the list in which we have to find the required number
                            # n is the number which we have to find
    for i in range(len(lst)):
        if lst[i] == n:
            return f"The number {n} is found to be at index {i} in the list {lst}"
    else:
        return f"{n} is not found in the list {lst}"
print("\nQuestion#10 \nTitle: Linear search")
print(f"\n{linear_search([1,4,5,7,8],9)}")
print(f"\n{linear_search([13,5,68,90],90)}")