def main():
    import heapq

    with open("in.txt", "r") as fin:
        tokens = fin.read().split()

    it = iter(tokens)
    n = int(next(it)) #кол-во вершин в первой строке ввода

    #потом n строк вида (узел,вес,узел,...) пока не 0
    graph = {i: [] for i in range(1, n + 1)}
    for i in range(1, n + 1):
        while True:
            next_token = next(it)
            if next_token == "0":
                break
            v = int(next_token)
            w = int(next(it))
            graph[i].append((v, w))

    #потом две строки откуда куда
    source = int(next(it))
    destination = int(next(it))

    #сначала всем вершинам минмакс задаем бесконечным, кроме начальной вершины (массив предыдущих пуст)
    INF = float('inf')
    cost = {i: INF for i in range(1, n + 1)}
    cost[source] = 0
    parent = {i: None for i in range(1, n + 1)}

    heap = [(0, source)]
    while heap:
        #команда попает минимальный по первому эл. пары элемент кучи
        cur_cost, u = heapq.heappop(heap)
        #если значение больше, то нам не интересно
        if cur_cost > cost[u]:
            continue
        #если дошли до конца, то можно делать брейк
        if u == destination:
            break
        #иначе проходим по всем из след[] и если новый вес ниже вычисленного ранее, перезаписываем стоимость и предка
        for v, w in graph[u]:
            new_cost = max(cur_cost, w)
            if new_cost < cost[v]:
                cost[v] = new_cost
                parent[v] = u
                #дописываем в кучу новую вершину
                heapq.heappush(heap, (new_cost, v))

    if cost[destination] == INF:
        with open("out.txt", "w") as fout:
            fout.write("N")
        return

    path = []
    node = destination
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()

    with open("out.txt", "w") as fout:
        fout.write("Y\n")
        fout.write(" ".join(map(str, path)) + "\n")
        fout.write(str(cost[destination]))


if __name__ == '__main__':
    main()
