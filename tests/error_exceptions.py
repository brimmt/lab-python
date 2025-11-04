
"""
Title: Error Handling Study Log
Author: Tatiana Brimm
Description:
  A chronological collection of my error and exception practice problems.
  This file intentionally includes early, unrefined code to document growth and reasoning.
  Each section includes analysis, time/space complexity, and personal reflections.
"""

#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      1  - 11/3/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#


# try: this is the block of cod to be attempted
# execpt: block of code will exectue in case there isan error in try block
# finally: A final block of code to be exectured, regardless of an error


#Example 1



def add(n1,n2):
    print(n1+n2)

number1 = 10

#number2 = input("please provide a number: ")

#add(number1,number2)


#Will recieve a TypeError <- Can't add an int and str together.  This will stop the entire codebase until this is fixed. 

#Fix

try:
    result = 10 + 10
except:
    print("Hey it looks like you aren't adding correctly")
else:
    print("Add went well!")

result


#Example 2

try:
    f = open('testfile', 'r')
    f.write("Write a test line")
except TypeError:
    print("There was an type error")
except OSError:
    print("Hey you have an OS error")    #This error is a permission error
finally:
    print("I always run")




# Example 3

def ask_for_int():
    
    while True:
        try:
            result = int(input("Please provide number:"))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes thank you")
            break
        finally:
         print("End of try/execpt/finally")

ask_for_int()




#------------------------------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      4  - 11/4/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#
# Errors and Exception Homework

# 1.  Handle the exception thrown by the code below by using try and except blocks.
 
try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print("Can't multiple int and str")
finally:
    print("Just checking")


# 2. Handle the exception thrown by the code below by using try and except blocks. Then use a finally blcok to print "All Done"
try:
    x = 5
    y = 0

    z = x/y
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print("All done") 




# 3. Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    
    while True:
        try:
            result = input("Please enter a number: ")
        except:
            print("Whoops! Please enter a number")
            continue
        else:
            break

    print(result**2)

#------------------------------------------------------------------------------------------------------------------------------------------------#

# Pylint - Unit Testing

def myfunc():
    '''
    A Simple Function
    '''
    first = 1
    second = 2
    print(first)
    print(second)

myfunc()

# Your code has been rated at 4.46/10 (previous run: 2.96/10, +1.50)
# Lol this is fun! I like this alot!  Tati remember to come back and organize this to try to get 10/10. 

#------------------------------------------------------------------------------------------------------------------------------------------------#