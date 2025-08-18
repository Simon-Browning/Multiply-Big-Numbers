'''This function takes two strings as input that
represent two positive integers and subtracts them.
It outputs the result as a string.
Note: This function only works if the first number
is larger than the second. That is, this function
is unable to produce negative results.
Note: This can leave leading zeros, but that is not
an issue for how this function will be used
'''

# Time Complexity: O(max(m, n))
# Space Complexity: O(1)

def subtract(s1, s2):
    result = []
    carry = 0
    i = len(s1) - 1
    j = len(s2) - 1

    # Iterate through both strings backwards
    while i >= 0:
        d1 = int(s1[i])
        if j >= 0:
            d2 = int(s2[j])
        else:
            d2 = 0

        if d1 - carry < d2:
            result.append(str(d1 - d2 - carry + 10))
            carry = 1
        else:
            result.append(str(d1 - d2 - carry))
            carry = 0

        i -= 1
        j -= 1

    return ''.join(result[::-1])