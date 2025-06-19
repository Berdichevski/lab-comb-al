#Какое может быть минимальное число жителей города, где кондукторы составляют строго более P%,
# но строго менее Q% населения? Ограничения: 0.01 ≤ P, Q ≤ 99.99.
# Числа P и Q могут быть заданы с точностью до сотых долей.


from decimal import Decimal
def main():

    #могут быть в одной или 2ух строках
    parts = input().strip().split()
    if len(parts) >= 2:
        P_str, Q_str = parts[0], parts[1]
    else:
        P_str = parts[0]
        Q_str = input().strip()

    #переводим проценты в дробные части десятичной дроби
    P_i = int(Decimal(P_str) * 100)
    Q_i = int(Decimal(Q_str) * 100)

    #перебираем возможное число жителей N
    for N in range(1, 100001):
        #формула выводится из того, что у нас k/N * 100 > P
        k_min = (P_i * N) // 10000 + 1
        #а эта из того что k/N * 100 < Q
        k_max = ((Q_i * N) - 1) // 10000

        if k_min <= k_max:
            print(N)
            return

if __name__ == "__main__":
    main()
