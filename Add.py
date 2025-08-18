'''This function takes two strings of digits as input
representing two positive integers. 
It outputs the sum of the two integers that the input
strings represent as a string.
'''

# Time Complexity: O(max(m, n))
# Space Complexity: O(1)

def add(s1, s2):
    
    # Function assumes that s1 is a longer string that s2
    if len(s1) < len(s2):
        return add(s2, s1)

    result = []
    carry = 0
    i = len(s1) - 1
    j = len(s2) - 1

    # Iterate through the two strings backwards
    while i >= 0:
        d1 = int(s1[i])
        if j >= 0:
            d2 = int(s2[j])
        else:
            d2 = 0

        total = d1 + d2 + carry
        carry = total // 10
        result.append(str(total % 10))

        i -= 1
        j -= 1

    # Account for extra carry digit
    if carry == 1:
        result.append('1')

    return ''.join(result[::-1])