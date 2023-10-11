"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here

    def helper(i):
        if i not in frequencies:
            frequencies[i] = 1
        else:
            frequencies[i] += 1

    for i in items:
        if isinstance(i, str):
            helper(i)
        else:
            i = str(i)
            helper(i)

    return frequencies
