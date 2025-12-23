from math import gcd
def solve(n):
    # the question asks to return a, b which they are summed and give a+b = n and
    # also both a and b are > 0
    #  the lcm of (a,b) = minimum values of all a,b iterate over n is not possible as it is 10^9
    # whAT TO ITERATate n // 2 for 10^ 9 is 5*10^8 which is still large but we have to find a way to optimize it girl
    # what if i iterate until sqrt(n) but that will not give all possible a,b
    # we may have multiple a,b that sum to n so we need to find the minimum lcm
    # lcm is minimum when gcd is maximum as lcm = a*b // gcd(a,b)
    # the maximum gcd of a and b is when both are equal or as close as possible so what if we do the n // 2
    if n % 2 == 0:
        return [n // 2, n // 2]
    # if n is odd we can return n//2 and n//2 + 1 but for 9 it's returning 3, 6 for 5 also 4, 1 so 
    # lcm(a,b) = (a*b) // gcd(a,b)
    # the trick is when n is odd and we have to find 2 numbers that sum n and their gcd high and lcm min

    '''
    mn = float('inf')
    ansa, ansb = -1, -1
    for a in range(1, (n // 2) + 1):
        b = n - a
        lcm = (a * b) // gcd(a, b)
        if lcm < mn:
            mn = lcm
            ansa, ansb = a, b
    return [ansa, ansb]
    '''
    # what if we iterate untill sqrt(n) can we cover all possible values of a and b which has max gcd -> min lcm

    # if n is even, we can return n//2 and n//2
    if n % 2 == 0:
        return [n // 2, n // 2]

    # if n is odd, we want to find a and b such that a + b = n and gcd(a,b) is maximum
    # the maximum gcd occurs when a and b are as close as possible
    # so we try to find the largest divisor of n that is less than or equal to sqrt(n)
t = int(input())
for _ in range(t):
    n = int(input())
    print(*solve(n))