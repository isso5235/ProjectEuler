#左右どちらから読んでも同じ値になる数を回文数という.
# 2桁の数の積で表される回文数のうち, 最大のものは 9009 = 91 × 99 である.
#では, 3桁の数の積で表される回文数の最大値を求めよ.
def Palindrome(n):
    n = str(n)
    if n[0] == n[-1]:
        if n[1] == n[-2]:
            if n[2] == n[-3]:
                print(n)

for i in range(100, 1000):
    for j in range(100, 1000):
        Palindrome(i*j)
