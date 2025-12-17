def check(n):
    # we have to return the number of pyramids that can be constructed with n cards
    # making 1 maximum pyramid with n cards then subtracting the used cards from n and repeating 
    count = 0
    # 3*h*(h+1)/2 - h tell us how many cards we need to make a pyramid of h height
    while n >= 2:
        h = 1
        while (3*h*(h+1)) // 2 - h <= n:
            h += 1 

        h -= 1
        n -= (3*h*(h+1)) // 2 - h  
        count += 1
    return count

t = int(input())
for _ in range(t):
    n = int(input())
    print(check(n))