'''This function takes a single string of digits as
input and returns the same string with all leading
zeros removed. If the string is all zeros, the 
function returns '0'.
'''

# Time Complexity: O(n)
# Space Complexity: O(1)

def remove_leading_zeros(s):
    i = 0

    while i < len(s) and s[i] == '0':
        i += 1

    if i == len(s):
        return '0'
    return s[i:]