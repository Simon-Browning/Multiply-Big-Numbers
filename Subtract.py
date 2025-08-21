def subtract(num1, num2):
    m = len(num1)
    n = len(num2)

    num1 = num1[::-1]
    num2 = num2[::-1]

    result = []
    carry = 0

    for i in range(m):
        d1 = num1[i]
        if i < n:
            d2 = num2[i]
        else:
            d2 = 0

        total = d1 - d2 - carry
        if total < 0:
            result.append(total + 10)
            carry = 1
        else:
            result.append(total)
            carry = 0

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return result[::-1]