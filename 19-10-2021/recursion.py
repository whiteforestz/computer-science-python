for i in range(0, 10):
    print(i, end=' ')


def print_nth_item(n: int, max_n: int):
    if n == max_n:
        return None

    print(n, end=' ')
    print_nth_item(n + 1, max_n)


print_nth_item(0, 10)
