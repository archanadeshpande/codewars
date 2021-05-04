# -*- coding: utf-8 -*-
"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""

def solution(string,markers):
    text=string.split('\n') #creating a list of lines
    for marker in markers: #for every marker       
        #split the string on marker and keep only the first part removing whitespaces
        text = [line.split(marker)[0].strip() for line in text] 
    return '\n'.join(text) # join the text with newline characters 