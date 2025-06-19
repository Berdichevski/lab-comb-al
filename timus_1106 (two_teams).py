from collections import deque


def solve():
    N = int(input())
    adj = [[] for _ in range(N + 1)]  # 1-based indexing
    for i in range(1, N + 1):
        friends = list(map(int, input().split()))
        friends.pop()  # remove trailing 0
        for f in friends:
            adj[i].append(f)

    color = [None] * (N + 1)
    possible = True

    for start in range(1, N + 1):
        if color[start] is not None:
            continue
        q = deque()
        q.append(start)
        color[start] = 0

        while q and possible:
            v = q.popleft()
            for u in adj[v]:
                if color[u] is None:
                    color[u] = color[v] ^ 1
                    q.append(u)
                elif color[u] == color[v]:
                    pass  # We don't fail here, but need to check neighbors later

    # Now, check that every node has at least one neighbor of opposite color
    for v in range(1, N + 1):
        has_opposite = False
        for u in adj[v]:
            if color[u] != color[v]:
                has_opposite = True
                break
        if not has_opposite:
            possible = False
            break

    if not possible:
        print(0)
    else:
        team1 = [i for i in range(1, N + 1) if color[i] == 0]
        print(len(team1))
        if team1:
            print(' '.join(map(str, team1)))


solve()