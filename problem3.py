#13195 の素因数は 5, 7, 13, 29 である.
#600851475143 の素因数のうち最大のものを求めよ.
import math

N = 13195
prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113]
max = 2

for i in prime:
    if N % i == 0:
        max = i

print(max)