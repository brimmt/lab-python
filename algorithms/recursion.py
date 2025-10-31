from typing import List
import math

"""
Title: Recursion Study Log
Author: Tatiana Brimm
Description:
  A chronological collection of my recursion practice problems and related algorithms.
  This file intentionally includes early, unrefined code to document growth and reasoning.
  Each section includes analysis, time/space complexity, and personal reflections.
"""


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      1 - 10/29/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#


# Write a recursive function recursive_sum(n) that returns the sum of all numbers from 1 to n. 

def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return (n -1) + (n - 2)
    

#corrected version

def recursive_sum1(n):
    if n == 1:
        return 1
    else: 
        return n + recursive_sum1(n-1)
    

#what its doing:   recursive_sum1(5) -> 5 + recursive_sum1(4)  then recursive_sum(4) -> recursive_sum(3

#Need more practice. I see that I tried to use fibonacci the first time, and then chat gpt showed me the best way waas the calts method. I understand it a bit better but i need practice. 
#---------------------------------------------------------------------------------------------------------------------------------#