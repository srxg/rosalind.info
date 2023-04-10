'''
Given: A DNA string t

having length at most 1000 nt.

Return: The transcribed RNA string of t.
'''

def transcribe(t):
    assert len(t) <= 1000 and 0 <= len(t)
    u = ''.join(['U' if i == 'T' else i for i in t.upper()])
    return u