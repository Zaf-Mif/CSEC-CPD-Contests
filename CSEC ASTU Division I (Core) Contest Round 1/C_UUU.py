from collections import Counter


def solve(n,k,a,b):
    # we need not choose from the k , dupicates, time
    # extracting the not choosen
    not_choosen = k - len(set(a))

    #  filtering the duplicates
    cnt = Counter(a)
    duplicate = {}
    for key, value in cnt.items():
        if value > 1:
            duplicate[key] = value

    arr = [[] for _ in range(max(a) + 1)]
    for i in range(n):
        if cnt[a[i]] > 1:
            arr[a[i]].append(b[i])

    mndup = []
    for key in duplicate:
        arr[key].sort()
        mndup.extend(arr[key][:-1])

    mndup.sort()
    time = sum(mndup[:not_choosen]) if not_choosen > 0 else 0
    return time

n, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(solve(n,k,a,b))


