from Add import add
from Subtract import subtract
from Multiply import multiply

def adaptive(num1, num2):

    diff = len(num1) - len(num2)
    if diff > 0:
        num2 = [0] * diff + num2
    else:
        num1 = [0] * abs(diff) + num1

    if len(num1) < 100 and len(num2) < 100:
        return multiply(num1, num2)

    if len(num1) % 2 == 1:
        num1 = [0] + num1
        num2 = [0] + num2

    n = len(num1)
    half = int(n / 2)

    a = num1[:half]
    b = num1[half:]
    c = num2[:half]
    d = num2[half:]

    ac = adaptive(a, c)
    bd = adaptive(b, d)

    a_plus_b_c_plus_d = adaptive(add(a, b), add(c, d))
    ad_plus_bc = subtract(subtract(a_plus_b_c_plus_d, ac), bd)

    ac.extend([0] * n)
    ad_plus_bc.extend([0] * half)

    result = add(add(ac, ad_plus_bc), bd)

    return result