def incremento_variables():
    n = 100  # O(1)
    i = 0  # O(1)
    j = 0  # O(1)
    k = 0  # O(1)

    while i <= n:  # O(n) + O(1) = O(n + 1)
        while j <= n:  # O(n(n + 1))
            j = j + 1  # O(nxn)
        i = i + 1  # O(n)
        k = k + 1  # O(n)

    print(f"i:{i},j:{j},k:{k}")


incremento_variables()
