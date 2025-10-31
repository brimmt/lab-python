from typing import List
import math

"""
Title: Linear Search Study Log
Author: Tatiana Brimm
Description:
  A chronological collection of my linear search practice problems and related algorithms.
  This file intentionally includes early, unrefined code to document growth and reasoning.
  Each section includes analysis, time/space complexity, and personal reflections.
"""

#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      1
#------------------------------------------------------------------------------------------------------------------------------------------------#
def linear_search_first(nums: List[int], target: int) -> int:
    for i, val in enumerate(nums):
        if val == target:
            return i
    return -1


print(linear_search_first([1,2,3,4,5,6,7,8], 4))
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      2
#------------------------------------------------------------------------------------------------------------------------------------------------#
# Linear Search - Given an array nums and a target, return the index of the first occurrence of target.
#  If it doesn't exist, return -1.




def linear_search(nums: List[int], target: int) -> int:
    
    for i, val in enumerate(nums):
        if val == target:
            return i
    return -1   


# Big O - O(n) <- each element gets looped through
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      3
#------------------------------------------------------------------------------------------------------------------------------------------------#

def first_occurence(nums: List[int], target: int) -> int:
    

    for i,val in enumerate(nums):
        if nums[i] == target:
            return i
    return -1


# # Big O - O(n)
#Tati enumerate isn't witchcraft ,it gives the value and index. Lol WE GO THIS ! 
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      4
#------------------------------------------------------------------------------------------------------------------------------------------------#
#First index occurnece
#Input : nums and target
#Output : index

def f_occurance(nums, target):
    
    for i, val in enumerate(nums):
        if val == target:
            return i
    return -1

print(f_occurance([1,2,3,4,5], 4))

#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      5 - 10/19/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#


# Find the index of a target element in an array

# Input : target and array
# Output: index of target

def find_index(nums: List[int], target: int) -> int:
    for i, val in enumerate(nums):     #This gives us back the index and value
        if val == target:
            return i
        
print(find_index([1,2,3,4,5], 5))

# Big O : O(n)
#Good job Tati , you did it without any help :) YOUR SO SMART -Tati 
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      6 
#------------------------------------------------------------------------------------------------------------------------------------------------#

#Return the maximum/minimum value in a list

# Input: list
# Output: max & min val

def maxmin(nums: List[int]) -> int:
    sorted_list = nums.sort()
    max_val = nums[-1] 
    min_val = nums[0]
    return min_val, max_val 

print(maxmin([1,5,6,2,4,3]))

#Parts Fixed : 
# nums.sort(), (start at the begining of the list) -> return nums[0], nums[-1]


#Option 2

def maxmin2(nums: List[int]) -> int:
    max_val = 0
    min_val = 0

    for i,val in enumerate(nums):
        if val > nums[i + 1]:
            min_val = val
        else:
            max_val = val


#Good try heres the fix tati:  
def maxminfix(nums: List[int]) -> int:

    max_val = nums[0] 
    min_val = nums[0]

    for val in nums: 
        if val > max_val:
            max_val = val 
        elif val < min_val: min_val = val
    return min_val, max_val 

#Rewrite without looking over and over until its muscle memory

def maxmin3(nums: List[int]) -> int:
    max_val = nums[0]
    min_val = nums[0]

    for val in nums: 
        if val > max_val:
            max_val = val
        elif val < min_val:
            min_val = val
    return min_val, max_val


def maxmin4(nums: List[int]) -> int:
    max_val = nums[0]
    min_val = nums[0]

    for val in nums: 
        if val > max_val:
            max_val = val 
        elif val < min_val:
            min_val = val
    return max_val, min_val

#Big O : O(n)
#Space : O(1) <- only used 2 variables
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      7 
#------------------------------------------------------------------------------------------------------------------------------------------------#
#Count how many times a value appears in a list

#Input: list and target
#Output : amount of times target appears

def count_occurance(nums: List[int], target: int) -> int:
    count = 0

    for val in nums:
        if val == target:
            count += 1
    return count

print(count_occurance([1,2,3,2,2,5], 2))

# Good job tati you did that in under 5 mins. No help. 
# Big O : O(n)

#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      8 - 10/21/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#
#Check if an array is sorted
#Input: list
#output: true or false

def array_sorted(nums: List[int]):
    
    for val in nums:
        if val > nums[val + 1]:
            return False
        else:
           return True 
                 
#Corrected version + drills. Continue to rewrite it until I can without looking for help. 
def array_sorted_corrected(nums: List[int]) -> bool:
    for i, val in enumerate(nums):
        if i+ 1 < len(nums) and val > nums[i + 1]:
            return False
    return True

def array_sorted_corrected2(nums: List[int]) -> bool:
    for i, val, in enumerate(nums):
        if i + 1 < len(nums) and val > nums[i + 1]:
            return False
    return True

def array_sorted_corrected3(nums: List[int]) -> bool:
    for i , val in enumerate(nums):
        if i + 1 < len(nums) and val > nums[i + 1]:
            return False
    return True

# Big O: O(n)
# Space: O(n) 
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      9
#------------------------------------------------------------------------------------------------------------------------------------------------#

# Maximum Number
# Input: List
# Ouput: Max num

def max_num_linear(nums: List[int]) -> int:
    max_num = nums[0]

    for num in nums:
        if num > max_num:
            max_num = num
    return num

#solved in 2 mins >:) im so cool lol let me test it 

print(max_num_linear([1,2,3,4,8,7,10]))
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      10 - 10/28/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#

#Given a list of integers and a target value, return the index of the first occurence of the target or -1 if its not found. 
#input: list, target
#output: first occurence

def fi_occurr(nums: List[int], target: int) -> int:
    
    for i, val in enumerate(nums):
        if val == target:
            return i
    return -1


print(fi_occurr([1,2,3,4], 3))

#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      11 - 10/28/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#

#Return how many times a given value appears in a list.
# Input: List , Target
# Output: int

def count_occur(nums: List[int], target: int) -> int:
    count = 0

    for val in nums:
        if val == target:
            count += 1
    return count

print(count_occur([1,1,1,1,2,4,5], 1))
assert count_occur([1,2,3,5,5], 5) == 2

# Big O: O(n)  Best: O(1)
# Space: O(n) 
# Time: 1 min > 
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      12 - 10/28/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#

#Find Maximum Number
# Input: List
# Output: int
def largest_num(nums: List[int]) -> int:
    max = nums[0]

    for num in nums:
        if num > max:
            max = num
    return max

print(largest_num([1,2,3,4,5,6,9,2]))
assert(largest_num)
# Big O: O(n)  Best: O(1)
# Space: O(n) 
# Time: 1 min > 
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      13 - 10/28/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#

# Reverse String
# Input: string
# Output: reversed string

def reverse_string(s):
    return s[::-1]

print(reverse_string('soda'))
assert(reverse_string)

# Big O: O(n)  Best: O(1)
# Space: O(n) 
# Time: 1 min > 
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      14 - 10/28/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#
#Planindrome check

def palindrome_prac(s: str) -> bool:
    
    if s != s[::-1]:
        return False
    else:
        return True
    

print(palindrome_prac('moon'))
assert(palindrome_prac('moon')) == False

# Big O: O(n)  Best: O(1)
# Space: O(n) 
# Time: 1 min > 
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      15 - 10/30/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#


#Linear Search (O(n)) - Given a list of integers and a target, return True if the target exists in the list, else False.

def linear_search1(nums: List[int], target: int) -> int:
    for val in nums:
        if val == target:
            return True
    return False

assert(linear_search1([1,2,3,4,5], 2)) == True


# Big O: O(n)  Best: O(1)
# Space: O(n) 
# Time: 1 min > 
#------------------------------------------------------------------------------------------------------------------------------------------------#