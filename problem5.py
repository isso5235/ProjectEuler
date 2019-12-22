# 2520 は 1 から 10 の数字の全ての整数で割り切れる数字であり,
# そのような数字の中では最小の値である.
# では, 1 から 20 までの整数全てで割り切れる数字の中で最小の正の数はいくらになるか.
#prime = [2,3,5,7,11,13,17,19]
prime = [2,3,5,7]
countedPrime = [0] * len(prime)
N = 10

def countPrime(n, p):
    count = 0
    r = n/p
    while r/n != 1:
        if r.is_integer():
            r = r/p
        else:
            return count
        count += 1
    return count

for i, p in enumerate(prime):
    for n in range(2, N + 1):
        if n > p:
            if (n/p).is_integer():
                count = countPrime(n, p)
                countedPrime[i] = count

print(countedPrime)