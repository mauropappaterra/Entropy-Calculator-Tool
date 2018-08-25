# Entropy Calculator Tool
# model.py
# Created by Mauro J. Pappaterra on 25 of August 2018.
import math

def getEntropy (size, choose):
    "Takes the size of a set and the number of elements to be selected from the set, calculates entropy"
    entropy = math.log(size, 2) * choose
    return round(entropy, 2) # rounded to two digits

def estimateLength(size, n):
    """Takes the size of a set (s) and an entropy value (n)
    returns the number of elements that need to be selected from the set
    to achieve the same entropy value"""
    entropy = n / math.log(size, 2)
    return str(round(entropy, 2))
