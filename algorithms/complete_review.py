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
        
#------------------------------------------------------------------------------------------------------------------------------------------------#

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

def move_zeros(nums: List[int]) -> None:  # This is making sure that we get a list back
    slow = 0  # set the pointer for our reckon mission

    for fast in range(len(nums)):  # fast is going to scount through each elementin the array to find its target
        if nums[fast] != 0: # if the variable that target is on isn't 0 then fast is going to move on. 
            nums[fast], nums[slow] = nums[slow], nums[fast]  # Fast continue to iterate through and slow continues to take fast position
            slow += 1  # Slow moves up 1 to keep up with fsat on this reckon mission
    


#------------------------------------------------------------------------------------------------------------------------------------------------#

# Q 7. Given an array nums, return True if any value appears at least twice,
# otherwise return False

# Input: Array
# Output: Boolean


def contain_duplicates(nums: List[int]) -> bool:
    count = set()  # this will be where we hold out variables

    for val in nums: # loop throuhg the entire array
        count.add(nums[val])
        if val in set:
            return True
    return False

# Corrected Version: 

def contain_duplicates(nums: List[int]) -> bool:
    count = set()  # this will be where we hold out variables

    for val in nums: # loop throuhg the entire array
        if val in count:
            return True
        count.add(val)
    return False
#------------------------------------------------------------------------------------------------------------------------------------------------#
# 8. Two Sum (Sorted Two Pointer)
# Given a sorted array nums and an integer target,
# return the indices of two elements that sum to target.
# Return [-1, -1] if none exist.
#

def two_sum_pointers(nums: List[int], target: int) -> List[int]:
    l, r = 0, len(nums)-1
    
    while l < r:
        concurrent_sum = nums[l] + nums[r]
        if concurrent_sum == target:
            return concurrent_sum
        elif concurrent_sum < target:
            l += 1
        else:
            r -= 1
    return [-1, -1]


# Correct Version: 

def two_sum_pointers(nums: List[int], target: int) -> List[int]:
    l, r = 0, len(nums) - 1

    while l < r:
        current = nums[l] + nums[r]
        if current == target:
            return [l, r]   # Remeber we want to return the list. The two indices
        elif current < target:
            l += 1
        else:
            r -= 1

    return [-1, -1]
#------------------------------------------------------------------------------------------------------------------------------------------------#

# 9. Given an array nums and integer k,
# return the maximum sum of any subarray of size k.


# Input : Array and K 
# Output : Max sum of subarray of k 


def max_subarray(nums: List[int], k: int) -> int:
    if k > len(nums):
        return 0
    
    
    for i in range(k):
        pass


#Corrected


def max_subbarray1(nums: List[int], k: int) -> int:
    if k > len(nums):
        return 0
    
    #Create the window! 
    current_sum = 0
    for i in range(k):
        current_sum += nums[i]
    best_sum = current_sum # set these variables
    l = 0  # set these variables

    for r in range(k, len(nums)):
        current_sum += nums[r]
        current_sum -= nums[l]
        l += 1

        best_sum = max(best_sum, current_sum)

    return best_sum



def max_subarray(nums: List[int], k: int) -> int:
    if k > len(nums):
        return 0
    
    current_nums = 0
    for i in range(k):
        current_nums += nums[i]
    
    best_sum = current_nums
    l = 0

    for r in range(k, len(nums)):
        current_nums += nums[r]
        current_nums -= nums[l]
        l += 1

        best_sum = max(best_sum, current_nums)
    
    return best_sum




#10 Longest Substring without repeating characters


#Input : string 
#Ouput : Int
def longest_substring(s: str) -> int: 
    l = 0   # Set the left pointer
    window = {}  # set the hash dict that we will store values
    best = 0  # This will add up as we find the sub arrays

    for r in range(s):
        char = s[r]
        window[char] = window.get(char,0) + 1

    while window[char] > 1: # if the value of k is greater than 1 that means there was a duplicate
        window[s[l]] -= 1 # were kicking out the left side and continueing to move foward
        l += 1  # were continuing to move u=foward

    best = max() # i don't understand this part so i left it as is. I saw what the answer is but I didn't add it because I dont understand it

    return best



# Corrected - (Wrong attempt)


def longest_substring_corrected(s: str) -> int:
    l = 0
    window = {}
    best = 0

    for r in range(len(s)):
        char = s[r]
        window[char] = window.get(char, 0) + 1

        while window[char] > 1:
            window[s[l]] -= 1
            l += 1

        best = max(best, r -l + 1)
    return best


# Corrected version 1


def longest_subarry(s: str) -> int:
    l = 0
    window = {}
    best = 0

    for r in range(len(s)):
        char = s[r]
        window[char] = window.get(char, 0) + 1

        while window[char] > 1:
            window[s[l]] -= 1
            l += 1

        best = max(best, r - l + 1)
    
    return best

# 11/18/2025 Study Block. 3 hours.


#Two Sums (HashMap)

def twoSum(nums: List[int], target: int) -> int:
    seen = {}

    for i, val in enumerate(nums):
        complement = target - val
        if complement in seen:
            return [seen[complement], i]
        seen[val] = i
    return [-1,-1]




# Contains Duplicates (Hashset)

def containsDuplicates(nums: List[int]) -> bool:
    count = set()

    for val in nums:
        if val in count:
            return True
        count.add(val)
    return False

# Remeber to check the set before adding any values to it. 



#Valid Parenthesis
# Stacks last in last out

def validParenthesis(s: str) -> bool:
    stack = []
    pairs = {
        ")":"(",
        "}":"{",
        "]":"["
    }

    # Now we want to add the keys to the stack
    for ch in s: 
        if ch in pairs.values():
            stack.append(ch)
        #Now lets check if its closing and we want to pair it to the stack
        elif ch in pairs.keys():
            if not stack:
                return False   # because closing cant come before begiining
        
            top = stack.pop() # this means the item at the end of the list gets popped. So the item at the top?


            if top != pairs[ch]:
                return False
        else:
            continue
        
    return len(stack) == 0


# Longest Common Prefix

def longestCommonPrefix(strs: List[str]) -> str:  # Were definnig a function called longestCommonPrefix. takes a list of strings, and returns the prefix (str)
    if not strs:   # if the list is empty then return empty string
        return ""

    strs.sort()   # Sort it so then the most common prefixes end up on the on the ssame side. So like it will sort the words from a to z. 
    first = strs[0]  # the smallest string alphabettically   EXAMPLE: flight
    last = strs[-1]  # the last largest string alphabetically   EXAMPLE : flower

    i = 0  # i will move across both strings
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1

    return first[:i] # Returns the slices out of the prefix




# 3SUM - Step by Step Explanation


#Easier if already solved 2 sum II


def threeSum(nums: List[int]) -> List[int]:
    res = []  # <- This is the results of the amount that will equal whatber  the conditon is
    nums.sort()  # <- Sort the array, it makes it easier to catch duplicates


    # Use each value as a possible first value

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:   # <- makes sure we don't resuse the same value in the same position, means this isn;t the firs tvalue in the input array, and a value checks that it's not the same value as the previous array. 
            continue

    # Now that we checked that edge case, lets start normal two sums
        l,r = i + 1, len(nums)-1

        while l < r: 
            three = a + nums[l] + nums[r]
            if three > 0:
                r -= 1
            elif three < 0:
                l += 1
            else:
                res.append([a + nums[r], nums[l]])  # We found the result that == 0
                l += 1  # keep searching for new combinations
                r -= 1

                # skip duplicates on the left side
                while nums[l] == nums[l-1] and l < r:  
                    l += 1
                    
    return res

        

    








