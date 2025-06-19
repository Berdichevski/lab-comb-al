from collections import deque


def is_bipartite(adj_matrix, n):
    # Инициализируем список цветов: -1 означает, что вершина ещё не раскрашена
    # Два возможных цвета: 0 и 1
    colors = [-1] * n

    # Используем очередь для обхода графа в ширину
    queue = deque()

    # Так как граф связный, начинаем обход с вершины 0 (которая соответствует вершине 1 по условию)
    colors[0] = 0
    queue.append(0)

    # Обход графа
    while queue:
        u = queue.popleft()
        # Проходим по всем вершинам, чтобы проверить наличие ребра от вершины u к вершине v
        for v in range(n):
            if adj_matrix[u][v] == 1:  # Если существует ребро между u и v
                if colors[v] == -1:
                    # Если вершина v ещё не раскрашена, раскрашиваем её в противоположный цвет к u
                    colors[v] = 1 - colors[u]
                    queue.append(v)
                elif colors[v] == colors[u]:
                    # Если смежные вершины имеют одинаковый цвет, граф не является двудольным
                    return None
    return colors


def main():
    # Чтение входных данных из файла in.txt
    with open("in.txt", "r") as fin:
        lines = fin.readlines()

    # Первая строка содержит количество вершин
    n = int(lines[0].strip())

    # Чтение матрицы смежности
    adj_matrix = []
    for line in lines[1:]:
        row = list(map(int, line.split()))
        adj_matrix.append(row)

    # Проверка на двудольность графа
    colors = is_bipartite(adj_matrix, n)

    # Запись результатов в файл out.txt
    with open("out.txt", "w") as fout:
        if colors is None:
            # Если граф не двудольный, выводим "N"
            fout.write("N")
        else:
            # Если граф двудольный, формируем две доли.
            # Заметим, что вершины нумеруются с 1, поэтому прибавляем 1 к индексам.
            set0 = [i + 1 for i in range(n) if colors[i] == 0]
            set1 = [i + 1 for i in range(n) if colors[i] == 1]

            # Сортируем множества вершин по возрастанию номеров
            set0.sort()
            set1.sort()

            # Первая доля должна содержать вершину с минимальным номером (вершина 1)
            fout.write("Y\n")
            fout.write(" ".join(map(str, set0)) + "\n")
            fout.write(" ".join(map(str, set1)))


if __name__ == "__main__":
    main()
