# -*- coding: utf-8 -*-
"""
You are given a binary tree:

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, then root children (from left to right) are second and third, and so on.

Return empty list if root is None.

Example 1 - following tree:

                 2
            8        9
          1  3     4   5
Should return following list:

[2,8,9,1,3,4,5]
Example 2 - following tree:

                 1
            8        4
              3        5
                         7
Should return following list:

[1,8,4,3,5,7]
"""
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
        
def tree_by_levels(node):
    # final list val will be returned, tree node created as queue to handle tree nodes
    val, tree = [], [node]
    while tree:
        # pop the first element to get the value, first will be root 
        v = tree.pop(0)
        # if it is not empty
        if v is not None:
            # add it's value to the return list
            val.append(v.value)
            # add the left and right roots to the end of the queue
            tree += [v.left,v.right]
    # return the final list, otherwise return [] is empty
    return val if not node is None else []

