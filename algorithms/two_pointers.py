
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


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      4 - 11/10/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#

# Reverse Array (Converging)  Pointers start on opposite ends and move toward each other
# Input: Array
# Output: Reversed Array


def reverse_array(nums: List[int]) -> List[int]:
    left,right = 0, len(nums) -1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]  #All were doing here is swapping the indexes
        left += 1  #We want left to go forward 
        right -= 1  #We want right to go backwards
    return nums

# Big O : 0(n)
# Space : O(1)
# good job tati you got it on the first try :) You're SO AWESOMEEE SAUCEEEE


#Reverse Array 11/22/2025
#Input: Array
#Output: Reversed Array



"""11/22/2025 Purpose was to rewrite without looking. Hadn't done this algorithm in a week. Refreshing memory and adding reverse string to the mix. """

def reverse_array1(nums: List[int]) -> int:
    l,r = 0, len(nums)-1  #We want set the pointers. One in the begining and one in the back. We do this because were going to swap their positions with each other
    
    while l < r:  # This while conditon means the function will continue until l is greater than r which means theres no more numbers to iterate over
        nums[l],nums[r] = nums[r],nums[l]  # Now all were doing is swapping the index
        l += 1  #move left to the right
        r -= 1 # move right to the left
    return nums  # once done return the new element

#Big 0: O(n) # It's O n because n is derminted by how lon gthe list is.
# Space O(1)  #Theres onlt 2 elements were working with



## Wrong. 
def reverse_string(str: str) -> str:  #This ensures we get back a string
    l,r = str[0], str[-1]  # this sents the pointers to start the begining and end of the string/  # YOU WANT THE INDEX NOT THE VALUE. 

    while l < r:   # I don't know but this just felt right. I know I wanted a while loop
        str[l], str[r] = str[r], str[l]   #pointer will swap places as it itertate.   # CANT SWAP STRINGS IN PYTHON. They are immutable
        l += 1   #tells left pointer move right
        r -= 1  #tells right pointer to move left
    return str  #return the reversed string


#Correct 

def reverse_string(s: str) -> str:
    s = list(s) # convert string to list so we can mutate
    l,r = 0, len(s)-1

    while l < r:
        s[l],s[r] = s[r], s[r]
        l += 1
        r -= 1
    return "".join(s)
#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      5 - 11/11/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#

# Fixed Window (Sliding Window) - Find max sum of any subarray of size 3
# Given an array of integers nums and a number k,
# find the maximum sum of any contiguous subarray of size k.

# Input: list, k ( the fixed window size )
# Output: subarray size of 3

def max_sum_subarray(nums, k):
    max_sum = 0   # initialize a variable to store the largest sum found while sliding the window
    window_sum = sum(nums[:k])  # takes k first elements and sum them up
    max_sum = window_sum  # stores the sum as max_sum

    for right in range(k, len(nums)):   # move the right pointers across the array starting from index k, for each element added to the right one elemet falls off from the left
        window_sum += nums[right] - nums[right - k]  # add new number entering on the right and subtract the number leaving the left
        max_sum = max(max_sum, window_sum) # each time we slide we check if our new window's sum is greater than our previous max_sum

    return max_sum


def max_sum_subarray2(nums, k):
    max_sum = 0
    window_sum = sum(nums[:k])
    max_sum = window_sum


    for right in range(k, len(nums)):
        window_sum += nums[right] - nums[right - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      6 - 11/19/2025  - Converging two-pointer
#------------------------------------------------------------------------------------------------------------------------------------------------#

""" Given a sorted array of integers nums and an integer target,
#return True if there exist two distinct numbers such that nums[left] + nums[right] == target.
Otherwise return False. """

#Input : Sorted array, and target
#Output: two distinct nums that equal target == true


def two_sums(nums: List[int], target: int) -> bool:
    l, r = 0, len(nums) -1

    while l < r:
        concurrent_sum = nums[l] + nums[r]
        if target == concurrent_sum:
            return True
        elif concurrent_sum < target:
            l += 1
        else:
            r -= 1
    return False

# Big O , is O(n) becaues we still have to touch each element. Best case is O(1) if target == concurrent_sum.
# Space COmplexity <- is O(1) because we are only listing 3 variables that essentially are constant, it wont grow in size. 

assert two_sums([1,2,3,4,5,6,7], 5) == True


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      7 - 11/19/2025  - Merging two-sorted lists
#------------------------------------------------------------------------------------------------------------------------------------------------#


"""
Given two sorted arrays:

nums1 = [1,3,5]
nums2 = [2,4,6]


Return this:

[1,2,3,4,5,6]

"""

def merge_arrays(nums1, nums2):
    p1 = p2 = 0 # <- #This sets the pointer for both lists
    result = [] # <- #This is where we will append the new list

    while p1 < len(nums1) and p2 < len(nums2):  #This is setting the window for both arrays
        if nums1[p1] < nums2[p2]:   # if nums1[p1] is less than p2 then we want to add that to the new list and then move p1
            result.append(nums1[p1])
            p1 += 1
        else:
            result.append(nums2[p2]) # If not we add p2 to the new list instead and move it. 
            p2 += 1

    result.extend(nums1[p1:]) # this basically adds the remaindig to the list. Kind of like how in javascript you use "..." to flatten out the array.
    result.extend(nums2[p2:])

    return result



#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      8 - 11/22/2025  - Palindrome
#------------------------------------------------------------------------------------------------------------------------------------------------#


# Input: "racecar" → True
# Input: "hello" → False

# Two pointers move inward checking characters.

def palindrome(str: str) -> bool:
    r = str[-1]

    for l in str:
        if l != r:
            return False
    return True


# Correct

def palindrome1(str: str) -> bool: 
    l, r = 0, len(str)-1 # I want the indexes. 

    while l < r:
        if str[l] != str[r]:
            return False
        l += 1
        r -= 1
    return True

def palindrome2(str: str) -> bool:
    l,r = 0, len(str)-1

    while l < r: 
        if str[l] != str[r]:
            return False
        l += 1
        r -= 1
    return True


# Actual Leetcode question #125
def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # Skip non-alphanumeric on left
            while l < r and not s[l].isalnum():
                l += 1

            # Skip non-alphanumeric on right
            while l < r and not s[r].isalnum():
                r -= 1

            # Now compare lowercase versions
            if s[l].lower() != s[r].lower():
                return False

            # Move pointers inward ONLY AFTER a valid comparison
            l += 1
            r -= 1

        return True


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      8 - 11/22/2025  - Remove Duplicates From Sorted Array 
#------------------------------------------------------------------------------------------------------------------------------------------------#

def remove_duplicates(nums: List[int]) -> List[int]:
    slow = 0 

    for fast in range(1,len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

        return slow + 1   



    



