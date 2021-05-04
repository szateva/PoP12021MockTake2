# 13021326

""" Consider the function most_frequent(L) that takes an non-empty list L of numbers
and returns such number from L that occurs most frequently. (Frequency of occurrence
of an element in a list L is the number of times it occurs in L.) If there are several
numbers that occur most frequently, it returns the smallest of them. You may assume
that L has only numbers and is non-empty.
Write a pytest program with six test cases to check the correctness of most_frequent.
(Note that you do NOT need to implement the function most_frequent itself.) Diver-
sity of your tests is important in marking. """

import pytest
from implementation_file import *

# simple case
def test_most_frequent1():
    L = [1, 2, 3, 4, 5, 5]
    assert most_frequent(L) == 5

# two most frequent
def test_most_frequent2():
    L = [1, 1, 2, 3, 4, 5, 5]
    assert most_frequent(L) == 1

# negative numbers
def test_most_frequent3():
    L = [-1, -1, 3, 4, 7]
    assert most_frequent(L) == -1

# floats
def test_most_frequent4():
    L = [1, 7, 2.5, 9, 2.5]
    assert most_frequent(L) == 2.5

# only one occurrence each
def test_most_frequent5():
    L = [7, -3, 4.5, 8, -1]
    assert most_frequent(L) == -3

# all numbers are the same
def test_most_frequent6():
    L = [2, 2, 2, 2, 2]
    assert most_frequent(L) == 2