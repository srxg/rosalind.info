'''
Given: A DNA string s

of length at most 1000 bp.

Return: The reverse complement sc
of s.
'''

def reverse_complement(s):
    comps = {'A' : 'T', 'C' : 'G', 'T' : 'A', 'G' : 'C'}
    sc = ''.join(comps[char] for char in s.upper()[::-1])
    return sc