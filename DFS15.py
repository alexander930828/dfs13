from matplotlib.colors import same_color
from numpy import double


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [False] * n
s = []

def DFS(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str, s)))
        return

    l = 0
    for i in range(idx, n):
        if not visited[i] and arr[i] != l:
            visited[i] = True
            s.append(arr[i])
            l = arr[i]
            DFS(depth+1, idx+1, n, m)
            visited[i] = False
            s.pop()

DFS(0, 0, n, m)