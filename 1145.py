from collections import deque

def main():
    # Читаем размеры лабиринта
    n, m = map(int, input().split())
    # Читаем m строк поля
    grid = [list(input().rstrip()) for _ in range(m)]

    # Направления движения (вверх, вниз, влево, вправо)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Ищем любую свободную ячейку для начала BFS
    start = None
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '.':
                start = (i, j)
                break
        if start:
            break

    # Функция BFS возвращает ((координаты самой удалённой ячейки, расстояние), карту расстояний)
    def bfs(s):
        dist = [[-1] * n for _ in range(m)]
        queue = deque([s])
        dist[s[0]][s[1]] = 0
        farthest = (s, 0)
        while queue:
            x, y = queue.popleft()
            d = dist[x][y]
            # Обновляем информацию о самой далёкой ячейке
            if d > farthest[1]:
                farthest = ((x, y), d)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '.' and dist[nx][ny] == -1:
                    dist[nx][ny] = d + 1
                    queue.append((nx, ny))
        return farthest, dist

    # Первый BFS: находим один из «концов» диаметра
    (f1, _), _ = bfs(start)
    # Второй BFS от найденного конца — находим сам диаметр
    (_, diameter), _ = bfs(f1)

    # Печатаем длину диаметра (минимальную длину нити)
    print(diameter)

if __name__ == '__main__':
    main()
