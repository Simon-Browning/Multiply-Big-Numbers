'''This function takes two strings of digits
representing positive integers as input and
returns the multiplied string. This algorithm
is equivalent to that used to multiply two large
numbers by hand.
'''

# Time Complexity: O(m * n)
# Space Complexity: O(m + n)

from Add import add
from Remove_Leading_Zeros import remove_leading_zeros

def standard(s1, s2):
    result = '0'
    j = len(s2) - 1

    # Iterate through second number backwards
    while j >= 0:
        sub_result = ['0'] * (len(s2) - j - 1)
        carry = 0
        i = len(s1) - 1

        # Iterate through first number backwards
        while i >= 0:
            d1 = int(s1[i])
            d2 = int(s2[j])

            total = (d1 * d2) + carry
            carry = total // 10
            sub_result.append(str(total % 10))

            i -= 1

        # Account for extra carry digit
        if carry > 0:
            sub_result.append(str(carry))

        result = add(result, ''.join(sub_result[::-1]))

        j -= 1

    return remove_leading_zeros(result)