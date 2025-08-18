'''This function takes two strings of digits as input.
It outputs the same two strings except that the shorter 
string will have extra zeros appended to the beginning 
to make the two strings the same length'''

# Time Complexity: O(min(m, n))
# Space Complexity: O(1)

def pad_with_zeros(s1, s2):    
    needed_zeros = len(s1) - len(s2)

    if needed_zeros < 0:
        return ''.join(['0'] * (-needed_zeros)) + s1, s2
    
    return s1, ''.join(['0'] * needed_zeros) + s2