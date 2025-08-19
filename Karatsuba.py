'''This function takes two strings of digits representing 
large integers and returns the multiplied result as a 
string. It uses the Karatsuba algorithm, which is
significantly faster than the standard algorithm
for large numbers.
'''

from Pad_with_Zeros import pad_with_zeros
from Remove_Leading_Zeros import remove_leading_zeros
from Add import add
from Subtract import subtract

# Time Complexity: O(n^lg3) = O(n^1.585)
# Space Complexity: O(nlgn)

def Karatsuba(s1, s2):

    # Base case
    if len(s1) == 1 and len(s2) == 1:
        return str(int(s1) * int(s2))

    # Make both numbers have the same length
    s1, s2 = pad_with_zeros(s1, s2)

    # Partition numbers into halves for divide and conquer
    n = len(s1)
    half = n // 2

    a = s1[:n - half]
    b = s1[n - half:]
    c = s2[:n - half]
    d = s2[n - half:]

    # Calculate needed numbers recursively
    ac = Karatsuba(a, c)
    bd = Karatsuba(b, d)

    a_plus_b_c_plus_d = Karatsuba(add(a, b), add(c, d))
    ac_plus_bd = add(ac, bd)
    ad_plus_bc = subtract(a_plus_b_c_plus_d, ac_plus_bd)

    # Combine the results
    ac = ac + '0' * (half * 2)
    ad_plus_bc = ad_plus_bc + '0' * half

    result = add(ac, add(ad_plus_bc, bd))

    # Remove any leading zeros
    result = remove_leading_zeros(result)

    return result