def fib(n):
    if n == 1 or n == 2:
        return n
    else:
        return fib(n-2) + fib(n-1)

# O(2N) (2배씩 늘어남 계산 식이)


#memorization : 아주 간단한 테크닉
"""
cashing 한다고 생각

"""
f = list()
def fibDP(n):
    f[1] = f[2] = 1
    for i in range (1, n+1):
        f[n] = f[n-1] + f[n-2]
    return f[n]

# O(n) 내에 구동


