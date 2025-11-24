from typing import List
import math

"""
Title: Binary Search Study Log
Author: Tatiana Brimm
Description:
  A chronological collection of my binary search practice problems and related algorithms.
  This file intentionally includes early, unrefined code to document growth and reasoning.
  Each section includes analysis, time/space complexity, and personal reflections.
"""

#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      1
#------------------------------------------------------------------------------------------------------------------------------------------------#
# Given a sorted array of integers nums and an integer target, return the index of target if it exists.
# otherwise, return -1.

#Input: array and target
#Output: index of target


def binary_search(nums: List[int], target: int) -> int:
    left = 0 
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1  # this is to close off the entire left side
        else:
            right = mid -1
    return -1


# Big O: O(log n)
# Space : O(1)
print(binary_search([1,3,4,5,6,7,8,9,10], 4))

#------------------------------------------------------------------------------------------------------------------------------------------------# 


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                       2
#------------------------------------------------------------------------------------------------------------------------------------------------#
#  Given a sorted array of integers nums, return the last occurrence of the target. If the target doesn't exist
#  return -1.


def last_occurence(nums: List[int], target: int):
    left = 0
    right = len(nums) -1
    result = -1
 
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            result = mid
            left = mid + 1
    
        elif nums[mid] < target:
            left = mid + 1
    
        else: 
            right = mid - 1

    return result

# BIG O : O(log n)
# Space: O(1)
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                       3
#------------------------------------------------------------------------------------------------------------------------------------------------#

# Find the target index
# input : SORTED list , target
# output : target index or -1

def target_index(nums: List[int], target: int) -> int:
    left,right = 0,len(nums) -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    return -1

# BIG O : O(log n)
# Space: O(1)
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                       4
#------------------------------------------------------------------------------------------------------------------------------------------------#


def insert_position(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

#so...it looks the same as target index im just returning left instead of -1 or target index. WHY left though? Remeber to study this Tati. 

#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                       5
#------------------------------------------------------------------------------------------------------------------------------------------------#
# Classic Binary Search (LeetCode)

#Given a sorted array of integers and a target value, return the index if the target is found; otherwise, return -1.

# Input: list, target 
# Output: target or -1

def find_target(nums: List[int], target: int) -> int: 
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            left = mid - 1
        else:
            right = mid + 1
            
    return -1


#Writing it one more time, had to glance more than twice, but essenttially I feel the muscle memory :)

def find_target2(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Big o: O(log n)
# Space: O(1)
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                       6
#------------------------------------------------------------------------------------------------------------------------------------------------#

# Search Insert Position - Return the index where the target should be inserted if it isn’t found.

# Input: list , target
# Output: index of target 


def index_target(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)-1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return mid



#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                       7 - 10/24/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#


# Leetcode   Q1. Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search for target in nums.
# Input: list, target
# Output: target index


def find_target_index(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) -1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            l = mid - 1
        else: 
            r  = mid + 1
    return -1




# Big O  = O(log n)
# Space = O(1)


#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                       8 - 10/24/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#
# Leetcode   Q2. Given a sorted array of distinct integers nums and a target value, return the index if the target is found.
#If not, return the index where it would be if it were inserted in order..

#Input: list, target
#Output: index


def search_insert_position(nums: List[int], target: int) -> int: 
    l, r = 0, len(nums) -1

    while l <= r:
        mid = ( l + r ) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l


#Big O  = O(log n) Space = O(1)
#Practice how to explan why L is being returned instead of -1

#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                       9 - 10/24/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#

# Leetcode   Q3. Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
# The returned integer should be non-negative as well. You must not use any built-in exponent function or operator (pow(x, 0.5) or x ** 0.5).

# Input: int
# output: sqr of x

def sqr_rt(x: int) -> int:
    if x < 2:
        return x
    left, right = 1, x // 2
    ans = 1
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            ans = mid 
            left = mid + 1
        else: 
            right = mid - 1
    return ans

#Copied this entire thing, going to need to have this broken down and explained. BUT...GOOD JOB FOR TRYING TATI, YOU'RE A ENGINEERING WIZZZZZZ
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                       10 - 10/25/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#
# Given a sorted array of integers nums and an integer target. Return the index of target if it exists, otherwise return -1.
# Input: sorted list, target
# Outout: index target

def target_index(nums: List[int], target: int) -> int:  #setting up the function, only accecpt a list/array of ints , target has to be an int as well
    left, right =  0, len(nums) -1  #This sets the window in which we will conduct the binary search. left starts at 0. right starts at the end of the array which is why len means to count the lengh of the array <- then -1 means the end of it.
    while left <= right: # this means the function will continue as long as left is less than right. You dont want left to = more than the right 
        mid = (left + right) // 2
        if nums[mid] == target: # I think this is checking the value and not the index , I get a bit confused with this part
            return mid # this returns the target index. I think
        elif nums[mid] < target:  #if nums[mid] is less than the target
            left = mid + 1  # this means we need to go to the right
        else:
            right = mid - 1 # if it's not smaller then the target then the only thing it can be is larger than the target so go left. 
    return -1 # if it cant be found at all, return -1. 

# BIG O : O(log n)
# Space: O(1)
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                       11 - 10/28/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#

# Question: Given a sorted list of integers and a target, return the index if the target is found. Otherwise, return -1.

# Input: list , target
# Output: index


def return_ind(nums: List[int], target: int) -> int: 
    l, r = 0, len(nums) -1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


print(return_ind([1,2,3,7,9], 7))
assert return_ind([1,2,3,7,9], 7) == 3

# BIG O : O(log n)
# Space: O(1)
# Time: 5 mins >
# Lesson Learned: remeber readability is important and this is an iterative implementation. Seems better than recursion honestly lol
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                       12 - 10/30/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#

# Binary Search (o(log n) - Given a sorted list of numbers, return the index of the target using binary search. If the element is not found, return -1.
# Input : sorted list , target
# Output : index

def binary_search1(nums: List[int], target: int) -> int:
    l,r = 0, len(nums)-1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

assert(binary_search1([1,2,3,4,5], 3)) == 2

# BIG O : O(log n)
# Space: O(1)
# Time: 3 mins >
# Lesson Learned: Practice makes perect. Good job tati , I'm awesome
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      13 - 10/30/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#

# Two Pointers  - Given a sorted list of integers and a target sum, return the pair of numbers that add up to that target

# Input: sorted list, target
# Output: pair of numbers that = target

def two_pointer1(nums: List[int], target: int) -> int: 
    l,r = 0, len(nums) -1
    j = 0
    while l <= r:
        mid = ( l + r) // 2
        if nums[mid]:
            pass

        # i just know i need to return J + mid = target


#correct version:

def two_pointer2(nums: List[int], target: int) -> int:
    l,r = 0, len(nums)-1   #set the window
    while l < r:  #as long as left is smaller than right then the loop will continue
        current_sum = nums[l] + nums[r]  # current_sum is basically adding up the two pointers that we need to find but combinign it i guess?
        if current_sum == target:  # if the current_sum == target then return the paris of numbers that add up to the current sum
            return (nums[l], nums[r])
        elif current_sum < target:
            l += 1
        else:
            r -= 1
    return None



# BIG O : O(log n)
# Space: O(1)
# Time: Stopped at 10 mins. 
# Lesson Learned: Be nice to yourself Tati. You're still new to this. So two pointers is basically an address that you're moving around. 
# use the same binary search logic at the core but were moving the pointers. 
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      14 - 11/03/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#
# Find the index of target
# Input: sorted list , target
# Output: index of target

def f_index(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

# BIG O : O(log n)
# Space: O(1)
# Time: 2 mins. 
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      15 - 11/03/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#
# Return True/False if target exist
# Input: sorted list, target
# Output: Boolean

def target_exist(nums: List[int], target: int) -> bool:
    l,r = 0, len(nums)-1

    while l <= r: 
        mid = (l + r) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return False

# BIG O : O(log n)
# Space: O(1)
# Time: 2 mins. 

#------------------------------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      16 - 11/03/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#
# Find insert position if target not present
# Input: sorted list, target
# Output: Boolean

def insert_pos(nums: List[int], target: int) -> bool:
    l,r = 0, len(nums)-1

    while l <= r: 
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l

# BIG O : O(log n)
# Space: O(1)
# Time: 2 mins. 
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      17 - 11/03/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#

# Find first occurence of target in a list with duplicates
# Input: sorted list, target
# Output: first occurence

def f_occurrence(nums: List[int], target: int) -> int:
    l,r = 0, len(nums)-1
    while l < r:
        mid = (l + r) // 2
        if mid == target:
            return mid
        
        #i forgot how to finish this off, but i know I want to check left to see if the first occurence showed up already


# BIG O : O(log n)
# Space: O(1)
# Time: Stopped at 8 mins. 


#Corrected version: 

def f_occurrence2(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    first = -1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            first = mid       # store current match
            r = mid - 1       # keep searching left side
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return first

#Every time you find the target, you don’t stop—you shrink the right boundary to look for an earlier duplicate.




#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      19 - 11/23/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#

# Find first occurence of target in a list with duplicates
# Input: sorted list, target
# Output: first occurence


def find_first_occurance(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)-1
    first = -1
    while l <= r: 
        mid = (l + r) // 2 # We create mid so we can start in the middle of the sorted list. O(log n)
        if nums[mid] == target:  #If mid equals target return
            first = mid  # store it 
            r = mid - 1 # shrink the right side. So we can check to see if the target showed up earlier
        elif nums[mid] < target:  # if mid is less than the target shrink the left side so we can focus on the number on the right. THe means the target hasn't shown up yet. 
            l = mid + 1   # SAHRINK THE LEFT side. 
        else:
            r = mid - 1  # if the mid is larger than the target then we will shrink the right side. 
    return first



#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      20 - 11/23/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#

# Write a function that takes a string s and returns the reverse of the string without using built-in reverse functions.

#Python shortcut
def reverse_a_string(s: str) -> str:
    return s[::-1]


def reverse_string_pointer(s: str) -> str: 
    l, r = 0, len(s)-1  # we set the pointers. Why? Because were going to have them swap with each other each time.
    s_list = list(s) # were going to turn it into a list because strings are not mutable. 

    while l < r: 
        s_list[l], s_list[r] = s_list[r], s_list[l] # we want to swap the pointers each time. 
        l += 1  # left will continue to move foward
        r -=1  # right will continue to move backward
    
    return "".join(s_list)  # this turns the list into a string


# Big O : O(log n)
# Space : O(n)


#------------------------------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      21 - 11/23/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#

# Write a function that takes a string s and returns True if it is a palindrome, ignoring:
# capitalization, spaces, punctuation
# any non-alphanumeric characters
# Otherwise return False.

def check_if_palindrome(s: str) -> bool:
    l,r = 0, len(s)-1

    while l <= r:

        while l <= r and not s[l].isalnum():
            l += 1
        while l <= r and not s[r].isalnum():
            r -= 1

        if s[l].lower() != s[r].lower():
            return False
        
        l += 1
        r -= 1
    
    return True



#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      22 - 11/23/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#

# Given a string s, return the index of the first character that does not repeat.
# If no such character exists, return -1.

# Input: s
# Output unquie character or -1

def find_unqiue_character(s: str):
    
    count = {}

    for char in s:
        count[char] = count.get(char,0) + 1
    for i, char in enumerate(s):
        if count[char] <= 1:
            return i
    return -1


def find_unique_char(s: str):
    count = {} #This is the dict, that we will store our chars in as we count. 

    for char in s:
        count[char] = count.get(char, 0) + 1 # This checks if char is already there and adds 1. If its not there yet , then it will be added with the number 1 as well. 
    for i, char in enumerate(s):  #now ere going to check which char has a count under 1. 
        if count[char] <= 1:
            return i # this returns the index
        
    return -1


        
            

   