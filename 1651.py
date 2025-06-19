import sys

def main():
    # Долго не мог понять, что не так со вводом
    # Читаем количество вершин
    try:
        first = input().split()
    except EOFError:
        return
    if not first:
        return
    n = int(first[0])

    # Считываем все следующие числа, пока не накопим n вершин цепи p
    p = []
    while len(p) < n:
        try:
            parts = input().split()
        except EOFError:
            break
        if not parts:
            continue
        p.extend(map(int, parts))
    # Обрезаем лишние, если вдруг прочитали больше n
    p = p[:n]

    # Если первая и последняя вершины совпадают, то сразу выводим это как подходящую цепь
    if p[0] == p[-1]:
        print(p[0])
        return

    # Для каждой вершины запомним её последнее вхождение, кроме последнего ребра
    last_pos = {}
    for i in range(n - 1):
        last_pos[p[i]] = i

    # Строим минимальную подцепь q, используем жадный алгоритм.
    # Из позиции i прыгаем к последнему вхождению p[i], а затем переходим по ребру
    res = [p[0]]
    i = 0
    while i < n - 1:
        j = last_pos[p[i]]   # последнее вхождение текущей вершины с исходящим ребром
        i = j + 1             # переходим по ребру к следующей вершине
        res.append(p[i])

    # Выводим
    print(" ".join(map(str, res)))

if __name__ == "__main__":
    main()
