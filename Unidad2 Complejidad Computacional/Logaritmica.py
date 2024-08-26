def ciclo_logaritmico():
    n = 64  # O(1)
    i = 0  # O(1)
    k = 0  # O(1)
    while (n > 1):  # O(log_{2}(n) + 1)
        n = n / 2  # O(log_{2}(n))
        k = k + 1  # O(log_{2}(n))

    print(f"n:{n}, k:{k}")  # O(1)


ciclo_logaritmico()
