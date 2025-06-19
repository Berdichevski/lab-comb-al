from collections import deque
import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    grid = [list(input().strip()) for _ in range(N)]

    # Отметим входы как доступные клетки
    reachable = [[False] * N for _ in range(N)]
    q = deque()
    for sx, sy in [(0, 0), (N - 1, N - 1)]:
        if grid[sx][sy] == '.':
            reachable[sx][sy] = True
            q.append((sx, sy))

    # Запустим BFS чтобы найти все клетки, в которые мы сможем попасть от двух входов
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if not reachable[nx][ny] and grid[nx][ny] == '.':
                    reachable[nx][ny] = True
                    q.append((nx, ny))

    # Считаем видимые стенки
    faces = 0
    for x in range(N):
        for y in range(N):
            if not reachable[x][y]:
                continue
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Соседняя клетка внутри поля
                if 0 <= nx < N and 0 <= ny < N:
                    if grid[nx][ny] == '#':
                        faces += 1
                else:
                    # Сосед за границей поля - это стена по периметру, кроме входов в (0,0) и (N-1,N-1)
                    if x == 0 and y == 0 and (dx, dy) in [(-1, 0), (0, -1)]:
                        continue
                    if x == N - 1 and y == N - 1 and (dx, dy) in [(1, 0), (0, 1)]:
                        continue
                    faces += 1

    # Чтобы посчитать площадь, умножим количество видимых стен на площадь одной
    area = faces * 9
    print(area)


if __name__ == "__main__":
    main()
