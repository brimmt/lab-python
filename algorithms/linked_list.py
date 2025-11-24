""" Title: Linked List Study Log
Author: Tatiana Brimm
Description:
  A chronological collection of my linked lists practice problems and related algorithms.
  This file intentionally includes early, unrefined code to document growth and reasoning.
  Each section includes analysis, time/space complexity, and personal reflections.
"""



# Singly Linked Lists

class SinglyNode:
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    

Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

Head.next = A
A.next = B
B.next = C  # C.next would be pointed to null 


#Traverse the list - O(n)

curr = Head   # We usually only start with access from the Head. 

while curr:
    print(curr)
    curr = curr.next     # This function will transverse through the list until it hits null.


#Diplay linked List - 0(n)
# 
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print('->'.join(elements))


display(Head)



#Search for node value - O(n)

def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    return False

search(Head, 2)




#Doubly Linked Lists

class DoublyNode:
    
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


    def __str__(self):
        return str(self.val)
    

head = tail = DoublyNode(1)   # gives access to head and tail


#Display - o(n)

def display(head):
    curr = head
    elements = []
    while curr: 
        elements.append(str(curr.val))
        curr = curr.next
    print("<->".join(elements))


#------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                      3 - 11/23/2025
#------------------------------------------------------------------------------------------------------------------------------------------------#

# Given the head of a linked list, determine if the list contains a cycle.
# Return:
# True if there’s a cycle
# False otherwise


# WRONG
def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        if slow != fast:   # Breaks the logic
            fast = fast.next.next
            slow = slow.next
            return False
        else:
            slow == fast
        return True
    

#Correct 


def hasCycle_correct(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
        
    return False