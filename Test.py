import random
import time
from Karatsuba import Karatsuba
from Multiply import multiply
from Adaptive import adaptive

num1 = [random.randint(0, 9) for _ in range(25000)]
num2 = [random.randint(0, 9) for _ in range(25000)]

initial = time.time()

result1 = Karatsuba(num1, num2)
mid1 = time.time()

print(f'Karatsuba: {int((mid1 - initial) // 60)} min {int((mid1 - initial) % 60)} s')

result2 = multiply(num1, num2)
mid2 = time.time()

print(f'Standard: {int((mid2 - mid1) // 60)} min {int((mid2 - mid1) % 60)} s')

result3 = adaptive(num1, num2)
final = time.time()

print(f'Adaptive: {int((final - mid2) // 60)} min {int((final - mid2) % 60)} s')

print(result1 == result2)
print(result1 == result3)