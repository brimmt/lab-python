from typing import List
import math

"""
Title: Hash Map Study Log
Author: Tatiana Brimm
Description:
  A chronological collection of my hash map and hash set practice problems and related algorithms.
  This file intentionally includes early, unrefined code to document growth and reasoning.
  Each section includes analysis, time/space complexity, and personal reflections.
"""



#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      1
#------------------------------------------------------------------------------------------------------------------------------------------------#

#HashMap - Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#still new to this lol we got this TATI! 
#time: 8:11 PM - 8:18
#Input: array and target
#Output: return the indices of the TWO numbers that add up to the target
# BIG O - This is going to be O(1) <- Because its super fast and only hitting a few elements once? not sure lol I only know O(n) AND O(log n) rn

def two_sums(nums: List[int], target: int) -> int: #I know I don't have to add the LIST[int] and int -> int, but I want to practice ensureing correct paramenters from now.
    seen = {}   # I added complement = 0  at first but remembered i want to store values i've seen already 
    for i,val in nums:
        complement = val - target
        if complement in seen:
            return [seen[i], complement[i]]
    
    #Correct: 

def twoo_sums(nums: List[int], target: int) -> List[int]:
    seen = {}  # key = number, value = index
    for i, val in enumerate(nums):
        complement = target - val
        if complement in seen:
            return [seen[complement], i]
        seen[val] = i
    return [-1, -1]  # fallback, shouldn't happen if solution guaranteed

# Big O : O(n)
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      2
#------------------------------------------------------------------------------------------------------------------------------------------------#
#Contain Duplicate 
#input : array
#output: true or false

def containn_duplicate(nums):
    seen = set()  # attaches a set to the variable seen
    for num in nums: #lets loop through the array
        if num in seen: #if num is found in seen 
            return True # return true
        else: 
            seen.add(num) # if not add it to num
    return False # if not return false

#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      3
#------------------------------------------------------------------------------------------------------------------------------------------------#

#Valid Anagram
#Input: two strings



def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    count = {}
    for c in s:
        count = count.get(c,0) + 1
    for c in t:
        if c not in count:
            return False
        count[c] -= 1
        if count[c] < 0:
            return False
    return True
     

#Remeber to study more, this is new so REMEBER: Check length, count 1, then subtract for the other set. 
# Big O : O(n)

#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      4
#------------------------------------------------------------------------------------------------------------------------------------------------#

#Hashmap Practice: Contains Duplicates
#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Input: list
# Output: boolean

def duplicates_contained(nums):
    seen = set()  #Create a set to store elements
    for i in nums: #Loop through the elements
        if i not in seen: # If I is not in the set that we created
            seen.add(i) #Add it
        else:
            return True # If I is in seen then return True because that means we have duplicates
    return False # if we loop through the entire thing and the same i was neve seen twice then return False there are no duplicates
#---------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      5
#------------------------------------------------------------------------------------------------------------------------------------------------#



#Hashmap Practice: Two Sum 
#Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.
# Input: list, target
# Output: indices of two nums = target

def two_summs(nums: List[int],target: int) -> int:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement],i]
        seen[num] = i
    return ["No solution"]

#Big O: O(n)
#Space: O(n)
#Lesson Learned: I need more practice, remeber Tati that return is pulling from the dictinary we created as a placeholder in the beginning
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      6 - 10/21/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#

#Given an integer array nums, return True if any value appears at least twice, otherwise return False.
#input: list
#output : boolean

def linear_duplicates(nums: List[int]) -> bool:
    count = {}

    for i, val in enumerate(nums):
        if val not in count:
            count[i] = val
        return False
        
#Problem for why I didn't solve this. One the return was inside the loop so it stopped after the first iteration
#two I was storing indexes when it wasn't needed. I only needed val. I couldn't used a set.

#Corrected answer


def linear_duplicates2(nums: List[int]) -> bool:
    count = {}

    for val in nums:
        if val in count:
            return True
        count[val] = True # marks as seen

    return False


#With a set

def linear_duplicates3(nums: List[int]) -> bool:
    seen = set()

    for val in nums:    #loop through the list and pull the val
        if val in seen: # if val is already in seen, return True it has duplicates
            return True
        seen.add(val)   #Else add val to set and return False

    return False

#Rewrite it until it sticks.

def linear_duplicates4(nums: List[int]) -> bool:
    seen = set()

    for val in nums:
        if val in seen:
            return True
        seen.add(val)

    return False



def linear_duplicates5(nums: List[int]) -> bool:
    seen = set()

    for val in nums:
        if val in seen: 
            return True
        seen.add(val)
    return False


def linear_duplicate6(nums: List[int]) -> bool:
    seen = set()


    for val in nums: 
        if val in seen:
            return True
        seen.add(val)
    return False

#Big O: O(n)
#Space: O(n)
#Lesson Learned: Could use set or dictionary

#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      6 - 10/21/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#

#Input: list , target
#Output 0,1

def two_sums_linear(nums: List[int], target: int) -> int:
    seen = {}

    for i,val in enumerate(nums):
        complement = target - val
        if complement in seen:
            return [seen[complement],i]
        seen[val] = i   #This is basically saying if its not in seen then add it. 
    return [-1,-1]


#Big O: O(n)
#Space: O(n)
#Lesson Learned: seen[val] = i adds i if its not already in it. Could use seen.get earlier maybe?
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      7 - 10/21/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#
#Input: list
#Output: boolean

def contains_duplicates_linear(nums: List[int]) -> bool:
    seen = set()

    for val in nums: 
        if val in seen:
            return True
        seen.add(val)  # Careful tati <- You acciedntly added brackets []. Updated it to the correct parathenses since its a method
    return False


def contains_duplicates_linear1(nums: List[int]) -> bool:
    seen = {}

    for val in nums:
        if val in seen:
            return True
        seen[val] = True  #True becomes the key value for the value
    return False

#Big O: O(n)
#Space: O(n)
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      8 - 10/21/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#
# Valid Anagram
# Input: str
# Output: boolean

def valid_anagram_linear(s,r):
   if len(s) != len(r):
       return False
   count = {}

   for c in s:
       count = count.get(c,0) + 1  # Forgot count[c]
   for c in r:
       if c not in count:
           return False
       count[c] -= 1
       if count[c] < 0:
            return False
    
   return True


#Had to copy from my previous valid anagram. I have the right idea but essentially I was missing some variable placements.

def valid_anagram_linear2(s,r):
    if len(s) != len(r):
        return False
    count = {}
    
    for c in s:
        count = count.get(c,0) + 1
    for c in r: 
        if c not in count:
            return False
        count[c] -= 1
        if count[c] < 0:
            return False
    return True

# Drill

def valid_anagram_linear3(s,r):
    if len(s) != len(r):
        return False
    count = {}
    for c in s:
        count[c] = count.get(c,0) + 1
    for c in r:
        if c not in count:
            return False
        count[c] -= 1
        if count[c] < 0:
            return False
    return True
#Big O: O(n)
#Space: O(n)
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      9 - 10/21/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#
#First Unique Character in a String

# Input: string
# Output 0 or -1 if no unqiues

def unique_char_linear(str):
    count = {}

    for char in str:
        count = count.get(char,0) + 1  #forgot count[char] stop doing that lol
        if count[char] == 1:
            return 0
    return -1


#Corrected version

def unique_char_linear2(s: str) -> int:
    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1

#Practice drills
def unique_char_linear3(s: str) -> int:
    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1

#Big O: O(n)
#Space: O(n)
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      9 - 10/28/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#

#TWO SUM
#Return indices of the two numbers thtat add up to the target
#Input: List, Target
#Output: 2 nums = target


def twoo_summ(nums: List[List], target: int) -> int:
    seen = {}

    for i, val in enumerate(nums):
        complement = target - val
        if complement in seen:
            return (seen[complement],i)   #< it needs () to return indices. This si the corrent way
        seen[val] = i
    return -1


#had to peek at old equation. I got stuck on the return part. I was going to use seen.get since it adds after checking if its not there, then it would skip the seen[val] = i part?
print(two_summs([1,2,3,4,5,6],5))

#Big O: O(n)
#Space: O(n)
#------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      9 - 10/30/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#
#HashMap - Given a string, count how many times each letter appears. Return the result as a dictionary. 
# Input: string
# Output: Dictionary

def count_s(s: str) -> dict:
    count = {}

    for val in s:
        count[val] = count.get(val, 0) + 1
    return count

#Big O: O(1)
#Space: O(1)
#Time: 2>

print(count_s("bug"))
assert count_s("bug") == {"b" : 1, "u" : 1, "g" : 1}
#------------------------------------------------------------------------------------------------------------------------------------------------#