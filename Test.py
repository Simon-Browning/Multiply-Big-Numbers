import random
from Karatsuba import Karatsuba
from Multiply import multiply

num1 = [random.randint(0, 9) for _ in range(1000)]
num2 = [random.randint(0, 9) for _ in range(1000)]

result1 = Karatsuba(num1, num2)
result2 = multiply(num1, num2)

print(result1 == result2)