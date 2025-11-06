
from typing import List
import math

"""
Title: Two Pointers Study Log
Author: Tatiana Brimm
Description:
  A chronological collection of my two pointers practice problems and related algorithms.
  This file intentionally includes early, unrefined code to document growth and reasoning.
  Each section includes analysis, time/space complexity, and personal reflections.
"""

#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      1 - 10/28/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#

#Two Pointers: Move all zeros to the end while maintaining the order of the other numbers.
  
            
# Never used two pointers before I think , but lol lets have fun haha. 

def move_zeros(nums: List[int]) -> int:
    count = []

    for val in nums:
        if val == 0:
            nums.remove(val)
            count.append(val)
        nums.extend(count)
    return nums
        

#Corrected code

def move_zeros1(nums: list[int]) -> list[int]:
    j = 0 # this is the first pointer, write pointer

    for i in range(len(nums)):
        if nums[i] != 0:  #if the value at this index doesn't match zero
            nums[j] = nums[i] #this line copies the non zero number into the next open spot
            j += 1

    while j < len(nums):  #this fills the remaining part of the list with zeros
        nums[j] = 0
        j += 1  #moves to the next open spot
    
    return nums

#Write again for muscle memory

def move_zeros2(nums: List[int]) -> List[int]:
    j = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1
    while j < len(nums):
        nums[j] = 0
        j += 1
    return nums


def move_zeros3(nums: List[int]) -> List[int]:

    j = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1

        while j < len(nums):
            nums[j] = 0
            j += 1
        return nums
    
#Big O: O(n) <- It's still looping through the entire list.
#Space : O(n) <- because were only using 2 variables 


#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      2 - 10/30/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#

#Two Pointers  - Given a sorted list of integers and a target sum, return the pair of numbers that add up to that target

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
        if current_sum == target:  # if the current_sum == target then return the paris of numbers that add up to teh current sum
            return (nums[l], nums[r])
        elif current_sum < target:
            l += 1
        else:
            r -= 1
    return None


#Big O: O(n) <- It's still looping through the entire list.
#Space : O(n) <- because were only using 2 variables 
#Lessons Learned: I need to get use to this. Its a bt mind boggling but super fun. 


#10/31/2025 <- Space is actully O(1), constant time because those two variables are stored, so there not new colletions of variables being used. 
#------------------------------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      3 - 11/06/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#

# Two Pointers - Move zeros to the end
# Input: list
# Output: List with zeros at the end

#Trying the different speeds pattern
# Fast scans and slow tracks where the next non-zero should go

def move_zeros(nums: List[int]) -> List[int]:
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow] #its sending back the index, i usually put the variable "val" but i see that it changes to fast to track better
            slow += 1 # This is basically having the slow to keep moving to the next index in the list
    return nums

