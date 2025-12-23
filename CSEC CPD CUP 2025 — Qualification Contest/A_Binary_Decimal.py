def solve(n):
    # to find the number that sum to n but they contain either 1 or 0
    # 121 -> 110 + 11 = 121 it's 2 numbers so we return 2
    # 5 -> the minimum number is 1 + 1 + 1 + 1 + 1 = 5
    # 100000000000 -> already in binary so we return 1
    #  the number that contain either 1 or 0 is 1, 10, 11, 100, 110, 111, 1000, 1100, 1110, 1111 ...
    # so we can make like for 5 the next less binary number is 1 then 5 -1 = 4 then again 1 then 3 then again 1 then 2 then again 1 then 1 so 5 1's so we return 5
    # if it's already binary we return 1

    if all(c in '01' for c in str(n)):
        return 1
    # for 121 -> 110 + 11
    # the nearest less binary number for 121 is 111 -> 121-111 = 10 then 10 is binary then we return 2 which is 111+10
    # find the nearest less binary number
    cnt = 0
    while n > 0:
        num = ''
        for digit in str(n):
            if digit != '0':
                num += '1'
            else:
                num += '0'
        nearest = int(num)
        n -= nearest
        cnt += 1
    return cnt
    
        
t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
    