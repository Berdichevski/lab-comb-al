from collections import deque, defaultdict

n = int(input())
teams = [input().split() for _ in range(n)]

graph = defaultdict(set)

for team in teams:
    for i in range(3):
        for j in range(i + 1, 3):
            graph[team[i]].add(team[j])
            graph[team[j]].add(team[i])

print(graph)

dist = {}

if "Isenbaev" in graph:
    dist["Isenbaev"] = 0
    queue = deque(["Isenbaev"])

    while queue:
        current = queue.popleft()
        current_dist = dist[current]

        for neighbor in graph[current]:
            if neighbor not in dist:
                dist[neighbor] = current_dist + 1
                queue.append(neighbor)
            else:
                dist[neighbor] = min(current_dist + 1, dist[neighbor])

all_participants = sorted(graph.keys())

for participant in all_participants:
    print(participant, dist.get(participant, "undefined"))
