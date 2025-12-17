n = int(input())
a = list(map(int, input().split()))

# forming teams of three by 2 1 and 3 1
ones = a.count(1)
twos = a.count(2)
#  amount of 1 and amount of 2 makes team of 3 
# print(ones, twos)
if ones > twos:
    teams = twos
    ones -= twos
    teams += (ones // 3)
    print(teams)
else:
    teams = ones
    print(teams)