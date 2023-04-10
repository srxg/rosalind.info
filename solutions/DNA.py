# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s
import numpy as np

# no error handling
def countNucleotides(s):
    counts = {'A': 0, 'C':0,'G':0,'T':0}
    for i in s:
        if i in counts.keys():
            counts[i]+=1
    return ' '.join(str(i) for i in counts.values())