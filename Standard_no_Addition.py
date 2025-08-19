'''This function is just like the standard 
multiplication function except that it does
not call on the external adding function
'''

# Time Complexity: O(n^2)
# Space Complexity: O(1)

def grade_school(s1, s2):
    s1 = s1[::-1]
    s2 = s2[::-1]

    result = [0] * (len(s1) + len(s2))

    for i in range(len(s1)):
        for j in range(len(s2)):
            d1 = int(s1[i])
            d2 = int(s2[j])

            result[i + j] += d1 * d2

            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return ''.join(map(str, result[::-1]))