import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    nums = list(map(int, data))
    m = len(nums) // 2  # число рёбер
    edges = [(nums[2*i], nums[2*i+1]) for i in range(m)]

    # Вычисление степеней вершин
    deg = {}
    for u, v in edges:
        deg[u] = deg.get(u, 0) + 1
        deg[v] = deg.get(v, 0) + 1
    verts = list(deg.keys())
    n = len(verts)
    vidx = {v: i for i, v in enumerate(verts)}

    # Построение матрицы инцидентности для системы уравнений

    # Матрица A размера n x m над GF(2) и вектор правой части b
    # A[i][j] = 1, если вершина i инцидентна ребру j, иначе 0
    A = [[0] * m for _ in range(n)]
    b = [0] * n
    # Заполняем матрицу A
    for j, (u, v) in enumerate(edges):
        A[vidx[u]][j] = 1
        A[vidx[v]][j] = 1
    # Заполняем b: b[i] = deg(vert_i) mod 2
    for v, i in vidx.items():
        b[i] = deg[v] % 2

    # Метод Гаусса над GF(2)
    rank = 0
    for col in range(m):
        # Ищем строку-пивот с единицей в столбце col
        pivot = None
        for r in range(rank, n):
            if A[r][col] == 1:
                pivot = r
                break
        if pivot is None:
            continue
        # Меняем строки pivot и rank
        A[rank], A[pivot] = A[pivot], A[rank]
        b[rank], b[pivot] = b[pivot], b[rank]
        # Обнуляем единицу в этом столбце во всех других строках
        for r in range(n):
            if r != rank and A[r][col] == 1:
                # над GF(2): вычитание = сложение = XOR
                for c in range(col, m):
                    A[r][c] ^= A[rank][c]
                b[r] ^= b[rank]
        rank += 1
        if rank == n:
            break

    # Проверка совместности
    # Если есть строка вида [0,...,0] | 1, то нет решения
    for r in range(rank, n):
        if all(x == 0 for x in A[r]) and b[r] == 1:
            print(0)
            return
    # Иначе решение существует
    print(1)

if __name__ == "__main__":
    main()