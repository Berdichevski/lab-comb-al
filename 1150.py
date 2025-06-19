#Петя Васечкин решил пронумеровать страницы в своей тетради числами от 1 до N.
# Определите количество нулей, единиц, …, девяток, которые ему потребуются.

def count_page_digits(N):

    counts = [0] * 10
    pos = 1  # текущий разряд, будем умножать на 10

    while pos <= N:
        higher = N // (pos * 10)
        current = (N // pos) % 10
        lower = N % pos

        # для цифр 1–9
        for d in range(1, 10):
            counts[d] += higher * pos
            if current > d:
                counts[d] += pos
            elif current == d:
                counts[d] += lower + 1

        # для нулей - без ведущих
        if higher > 0:
            counts[0] += (higher - 1) * pos
            if current > 0:
                counts[0] += pos
            elif current == 0:
                counts[0] += lower + 1

        pos *= 10

    return counts


if __name__ == "__main__":
    N = int(input())
    result = count_page_digits(N)
    for cnt in result:
        print(cnt)
