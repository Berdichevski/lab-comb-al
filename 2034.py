import sys

def main():

    data = sys.stdin.read().split()
    it = iter(data)
    M = int(next(it))
    N = int(next(it))
    K = int(next(it))

    # Строим список смежности: adj[u] - список v, доступных из u
    adj = [[] for _ in range(M)]
    for _ in range(K):
        u = int(next(it)) - 1  # переводим, чтобы нумерация была с 0
        v = int(next(it)) - 1
        adj[u].append(v)

    pairU = [-1] * M
    pairV = [-1] * N

    # Используем недавно пройденный алгоритм Куна
    def kun(u, visited):

        # visited — массив посещённых u, чтобы избежать зацикливания.
        if visited[u]:
            return False
        visited[u] = True
        for v in adj[u]:
            # Если v свободна или можно переподобрать её текущего партнёра
            if pairV[v] == -1 or kun(pairV[v], visited):
                pairU[u] = v
                pairV[v] = u
                return True
        return False

    # Для каждой вершины левой доли пытаемся увеличить паросочетание
    matching = 0
    for u in range(M):
        visited = [False] * M
        if kun(u, visited):
            matching += 1

    # По теореме размер минимального реберного покрытия = размер максимального паросочетания
    result = M + N - matching

    # Вывод результата
    print(result)

if __name__ == '__main__':
    main()
