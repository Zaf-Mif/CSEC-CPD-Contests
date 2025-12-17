n = int(input())
arr = "0"
for i in range(1, 1000):
    arr += str(i)
    if len(arr) > n:
        break
print(arr[n])
# 123456789101112131415  wsx 