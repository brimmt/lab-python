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





# Errors and Exception Homework

#------------------------------------------------------------------------------------------------------------------------------------------------#