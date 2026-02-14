def find_Min_Difference(L, P):
    L.sort()
    min_diff = float('inf')

    for i in range(len(L) - P + 1):
        diff = L[i + P - 1] - L[i]
        min_diff = min(min_diff, diff)

    return min_diff
L = list(map(int, input().split()))
P = int(input())
print(find_Min_Difference(L, P))