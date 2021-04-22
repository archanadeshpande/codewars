# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 18:57:37 2021
Traversing binary tree preorder and postorder
@author: Admin
"""
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
        
def PreorderTraversal(Node):
        res = []
        if Node:
            res.append(Node.value)
            res = res + PreorderTraversal(Node.left)
            res = res + PreorderTraversal(Node.right)
        return res
    
def PostorderTraversal(Node):
        res = []
        if Node:
            res = PostorderTraversal(Node.left)
            res = res + PostorderTraversal(Node.right)
            res.append(Node.value)
        return res
