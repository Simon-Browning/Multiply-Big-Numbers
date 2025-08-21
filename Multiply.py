def multiply(num1, num2):
    m = len(num1)
    n = len(num2)

    num1 = num1[::-1]
    num2 = num2[::-1]

    result = [0] * (m + n)

    for i in range(m):
        for j in range(n):
            d1 = num1[i]
            d2 = num2[j]

            result[i + j] += d1 * d2
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return result[::-1]