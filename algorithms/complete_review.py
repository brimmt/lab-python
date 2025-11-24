from typing import List

# Reverse String (Two-Pointer Version — NO slicing)
# Prompt: Write a function that reverses a string using two pointers.
# Input: string
# Output: Reverse String


def reverse_string(s: str) -> str:   # Ensures a string is returned
    l,r = 0, len(s)-1  # Sets the pointers on either end
    s = list(s) # creates a list because strings are immutable

    while l < r:  #Continues loop untilconditions are met
        s[l], s[r] = s[r], s[l] # Swaps variable in each pointer index
        l += 1  # moves left foward
        r -= 1 # moves r backwards
    return "".join(s)  # turns the list back into a string

# BIG O = O(n) <- because we will iterate through each element once
# WRONG! Space(1) = Were only using 3 variables, the two pointers and the string we turned into a list
# Correct Space O(n) <- because i created a new list size of n

#------------------------------------------------------------------------------------------------------------------------------------------------#
# WRONG ! # 2. Valid Palindrome 

# Input: string
# Output: Boolean

def check_if_palindrome(s: str) -> bool:  # This ensures we recevive a boolean and input a string
    l,r = 0, len(s)-1  # Sets the pointers from either end

    while l <= r:  # continues the loop until conditons are met
        while l <= r and not s[l].isalnum(): # Skips over any non alnum on lower end
            l += 1   # move l foward
        while l <= r and not s[r].isalnum(): # skips over any non alnum on higher end
            r -= 1 # move r backward
        if s[l].lower() != s[r].lower(): # covers upper case edge case, and compares pointers
            return False  # returns false if this condition is met and they aren't equal
    return True

#BIG O = O(n) <- because iteration amount will depend on howlong the string is
# Space(1) <- were only using 2 variables


# Correction

def check_if_palindrome1(s: str) -> bool:
    l,r = 0, len(s) -1

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





# 3. First Unique Character

#Prompt:
# Return the index of the first non-repeating character in a string.
# Return -1 if none exists.

# Input: str
# Output : unqiue char or -1 if none exist


def find_unique_char(s: str):    # input a string only
    count = {}  # create a dict to store values so we can reference later 

    for char in s: # for loop to loop through string
        count[char] = count.get(char, 0) + 1  # now we add to the dict
    for i,char in enumerate(s): # now second for loop will check for  each key that only has a value of 1
        if count[char] <= 1:
            return i # return the index
    return -1 # if none exist return -1


# BIG O , is O(n) because it depends on the length of s
# Space : O(n) <- becuse this also depends on the length of s and we don't how big the dict could get. 

# Corrected Version

def find_unique_char1(s: str) -> int:
    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for i, char in enumerate(s):
        if count[char] == 1:
            return i

    return -1

#------------------------------------------------------------------------------------------------------------------------------------------------#
# 4. Character Frequency Map 

# Input: string
# Output: dict

def char_frequency(s: str) -> dict:
    count = {}
    

    for char in s:
        count[char] = count.get(char, 0) + 1
    return count


print(char_frequency("Teesting"))

# BIG O = O(n) <- depends on how many elemets to loop through
# Space O(n) <- Because of the dictionary, of size n
        


# WRONG !
# 5. Anagram check
# Return True if s1 and s2 are anagrams 
# (same letters, same counts, possibly different order), otherwise False.

def check_if_anagrams(s1: str, s2: str) -> bool:
    s = s1.lower()
    s = s2.lower()

    s1_dict = {}
    s2_dict = {}

    for char in s1:
        s1_dict[char] = s1_dict.get(char, 0) + 1
    for char in s2:
        s2_dict[char] = s2_dict.get(char, 0) + 1
    if s1[char] != s2[char]:
        return False
    
    return True

# BIG O = O(n)
# Space O(n)?  Wouldn't me using 2 dictonaries and 2 variables make this O(n)

        

# Corrected Version

def check_if_anagrams1(s1: str, s2: str) -> bool:
    s1 = s1.lower()
    s2 = s2.lower()

    if len(s1) != len(s2):
        return False
    
    count = {}

    #First loop will add to the dict

    for char in s1:
        count[char] = count.get(char, 0) + 1
    # Now we will loop through the second string and substract if we see the amount
    for char in s2:
        count[char] = count.get(char, 0) - 1

    for val in count.values():
        if val != 0:
            return False
    return True

#------------------------------------------------------------------------------------------------------------------------------------------------#

#Given an array nums, move all zeroes to the end in-place,
# while keeping the order of non-zero elements.

#Input: Array
# Output : Array - all zeros in the back

def move_zeros(nums: List[int]) -> List:  # This is making sure that we get a list back
    slow = 0  # set the pointer for our reckon mission

    for fast in range(len(nums)):  # fast is going to scount through each elementin the array to find its target
        if nums[fast] != 0: # if the variable that target is on isn't 0 then fast is going to move on. 
            nums[fast], nums[slow] = nums[slow], nums[fast]  # Fast continue to iterate through and slow continues to take fast position
            slow += 1  # Slow moves up 1 to keep up with fsat on this reckon mission
    return nums # Return the list with all the enemnies '0' in the back!


#------------------------------------------------------------------------------------------------------------------------------------------------#

# Q 7. Given an array nums, return True if any value appears at least twice,
# otherwise return False









