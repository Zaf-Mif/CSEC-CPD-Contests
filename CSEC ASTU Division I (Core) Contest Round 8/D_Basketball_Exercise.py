def solve(n, h1, h2):
    # to have a maximum possible we need to find the tallest in the way they don't come consecutive
    # can't use sort as we need the original indices
    cnt = 0
    # it's like zigzag sometimes but not always foundh1, foundh2 = False, False
    th1, th2 = False, False
    for i in range(n-1):
        # mx = float("-inf")

        # mark which one os greater what if they r equal but this one only works if it's first time and we don't choose any
        if not th1 and not th2: 
            if h1[i] > h2[i]:
                # mx = h1[i]
                foundh1 = True
                foundh2 = False
            else:
                # mx = h2[i]
                foundh2 = True
                foundh1 = False
        elif th1:
            foundh2 = True
            foundh1 = False
            th1 = False
        elif th2:
            foundh1 = True
            foundh2 = False
            th2 = False

        # if they are equal
        if not foundh1 and not foundh2 and h1[i] == h2[i]:
            if h1[i+1] > h2[i+1]:
                cnt += h1[i]
                th1 = True
                th2 = False
            else:
                cnt += h2[i]
                th2 = True
                th1 = False 
            continue

        # identify whcih one to add
        if foundh1:
            if h1[i] + h2[i+1] > h1[i+1]:
                cnt += h1[i]
                th1 = True
                th2 = False

            else:
                # if it's less than don't add it and continue
                th1 = False
                th2 = False
                continue
        elif foundh2:
            if h2[i] + h1[+1] > h2[i+1]:
                cnt += h2[i]
                th2 = True
                th1 = False
            else:
                th1 = False
                th2 = False
                continue
    # add the last element
    if th1:
        cnt += h2[-1]
    elif th2:
        cnt += h1[-1]
    
    return cnt

n = int(input())
h1 = list(map(int,input().split()))
h2 = list(map(int,input().split()))
print(solve(n, h1, h2))