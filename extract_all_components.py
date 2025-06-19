def dfs(v, graph, visited, component):
    visited[v] = True
    component.append(v)
    for u in graph[v]:
        if not visited[u]:
            dfs(u, graph, visited, component)


# Чтение графа из файла in.txt
with open('in.txt', 'r') as fin:
    tokens = list(map(int, fin.read().split()))

n = tokens[0]
graph = [[] for _ in range(n + 1)]
index = 1

# Для каждой вершины считываем список смежности (список заканчивается числом 0)
for i in range(1, n + 1):
    while tokens[index] != 0:
        graph[i].append(tokens[index])
        index += 1
    index += 1  # пропускаем ноль

# Поиск компонент связности с помощью DFS
visited = [False] * (n + 1)
components = []
for i in range(1, n + 1):
    if not visited[i]:
        component = []
        dfs(i, graph, visited, component)
        component.sort()  # сортировка вершин в компоненте по возрастанию
        components.append(component)

# Сортировка компонент по минимальной вершине
components.sort(key=lambda comp: comp[0])

# Запись результата в файл out.txt
with open('out.txt', 'w') as fout:
    fout.write(str(len(components)) + "\n")
    for comp in components:
        fout.write(" ".join(map(str, comp)) + "\n")
