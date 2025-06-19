import sys
from collections import defaultdict, deque

def solve():
    N = int(sys.stdin.readline())
    adj = []
    door_info = []  # Для каждой комнаты список (комната, индекс двери)
    degrees = [0] * N
    # Построим список смежности и проверим степени
    for room in range(N):
        parts = list(map(int, sys.stdin.readline().split()))
        m = parts[0]
        neighbors = parts[1:]
        adj.append(neighbors)
        degrees[room] += m
        for neighbor in neighbors:
            degrees[neighbor - 1] += 1  # Нумерация с 1 в входных данных

    # Проверим, что все степени четные или ровно две нечетные
    odd_degrees = sum(1 for d in degrees if d % 2 != 0)
    if odd_degrees != 0 and odd_degrees != 2:
        print("Impossible")
        return

    # Теперь нужно построить эйлеров путь или цикл и раскрасить двери
    # Для этого создадим структуры для хранения рёбер и их цветов
    # Каждую дверь между a и b представим как два направленных ребра (a->b) и (b->a)
    # Нумерация комнат с 0 для удобства
    edge_colors = {}  # (a, b) -> цвет с точки зрения a (G или Y)
    # Для каждой комнаты создадим список смежных комнат и индексов дверей
    # Но проще работать с мультиграфом, учитывая, что двери могут вести в одну и ту же комнату
    # Поэтому для каждой комнаты будем хранить список смежных комнат в порядке входных данных
    # и отмечать, какие рёбра уже использованы

    # Построим граф как список смежности с рёбрами (to, door_index)
    graph = [[] for _ in range(N)]
    door_indices = {}  # (u, v, idx_in_u) -> global_idx или что-то ещё
    # Нам нужно для каждой комнаты u и её двери в порядке входных данных знать, куда она ведёт (v)
    # и её индекс в комнате u
    # Создадим список всех дверей и их направлений
    doors = []
    for u in range(N):
        neighbors = adj[u]
        for idx_in_u, v in enumerate(neighbors):
            v -= 1  # приводим к 0-based
            doors.append((u, v, idx_in_u))

    # Теперь нужно пройти по эйлерову пути и раскрасить рёбра
    # Используем алгоритм иерхольцера
    # Найдём стартовую вершину (если есть нечётные, начинаем с одной из них)
    start = 0
    for u in range(N):
        if degrees[u] % 2 != 0:
            start = u
            break

    stack = [start]
    path = []
    current_edge = [0] * N  # Указатель на следующее неиспользованное ребро для каждой вершины
    temp_edges = [[] for _ in range(N)]
    # Построим временный граф с рёбрами
    for u in range(N):
        neighbors = adj[u]
        for v in neighbors:
            v -= 1
            temp_edges[u].append(v)

    # Теперь алгоритм иерхольцера
    while stack:
        u = stack[-1]
        if current_edge[u] < len(temp_edges[u]):
            v = temp_edges[u][current_edge[u]]
            stack.append(v)
            current_edge[u] += 1
        else:
            path.append(stack.pop())

    # Теперь path содержит вершины в порядке обхода, но нам нужны рёбра
    # Раскрасим рёбра в порядке обхода: чередуем G и Y
    color = 'G'
    edge_colors = {}
    for i in range(len(path) - 1):
        u = path[i]
        v = path[i + 1]
        # Находим соответствующую дверь в комнате u
        # Нам нужно найти индекс двери в комнате u, ведущей в v
        neighbors = adj[u]
        target_v = v + 1  # так как во входных данных номера 1-based
        # Ищем первое вхождение target_v в neighbors после уже обработанных дверей
        # Для этого в комнате u ищем дверь, ведущую в v, которую ещё не красили
        found = False
        for idx_in_u in range(len(neighbors)):
            if neighbors[idx_in_u] == target_v:
                key = (u, v, idx_in_u)
                if key not in edge_colors:
                    edge_colors[key] = color
                    # Также добавляем обратное ребро (v, u) с противоположным цветом
                    # Находим индекс этой двери в комнате v
                    neighbors_v = adj[v]
                    for idx_in_v in range(len(neighbors_v)):
                        if neighbors_v[idx_in_v] == u + 1:  # так как u 0-based во внутреннем представлении
                            key_v = (v, u, idx_in_v)
                            edge_colors[key_v] = 'Y' if color == 'G' else 'G'
                            break
                    color = 'Y' if color == 'G' else 'G'
                    found = True
                    break
        if not found:
            pass  # Это не должно случиться в эйлеровом пути

    # Теперь для каждой комнаты собираем цвета дверей в порядке входных данных
    output = []
    for u in range(N):
        neighbors = adj[u]
        colors = []
        for idx_in_u in range(len(neighbors)):
            v = neighbors[idx_in_u] - 1
            key = (u, v, idx_in_u)
            colors.append(edge_colors.get(key, 'G'))  # По умолчанию, если не нашли (не должно быть)
        output.append(''.join(colors))

    # Проверим, что в каждой комнате разница между G и Y не более 1
    possible = True
    for u in range(N):
        count_g = output[u].count('G')
        count_y = output[u].count('Y')
        if abs(count_g - count_y) > 1:
            possible = False
            break
    if possible:
        print('\n'.join(output))
    else:
        print("Impossible")

solve()