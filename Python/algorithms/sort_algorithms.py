

def bubble_sort(inp):
    """Сортировка пузырьком"""
    inp_len = len(inp)
    for bypass in range(1, inp_len):
        for k in range(0, inp_len-bypass):
            if inp[k] > inp[k + 1]:
                inp[k], inp[k + 1] = inp[k + 1], inp[k]


def choise_sort(inp):
    """Сортировка вставками"""
    n = len(inp)
    for pos in range(0, n-1):
        for k in range(pos+1, n):
            if inp[k] < inp[pos]:
                inp[k], inp[pos] = inp[pos], inp[k]


def insert_sort(inp):
    """Сортировка выбором"""
    inp_len: int = len(inp)

    for top in range(1, inp_len):
        k = top
        while k > 0 and inp[k - 1] > inp[k]:
            inp[k], inp[k - 1] = inp[k - 1], inp[k]
            k -= 1


def count_sort(inp):
    """Сортировка подсчётом/частотный анализ"""
    inp_len: int = len(inp)
    numbers_count = 20
    numbers = [0] * numbers_count

    for i in range(inp_len):
        x = inp[i]
        numbers[x] += 1

    s = 0
    for v in range(0, numbers_count):
        k = numbers[v]
        for r in range(0, k):
            inp[s] = v
            s = s + 1


def merge_lists(list_a: list, list_b: list) -> list:

    """Слияние отсортированных списков
    """
    list_c = [None]*(len(list_a)+len(list_b))
    i = k = n = 0
    while i < len(list_a) and k < len(list_b):
        if list_a[i] < list_b[k]:
            list_c[n] = list_a[i]
            i += 1
            n += 1
        else:
            list_c[n] = list_b[k]
            k += 1
            n += 1
    while i < len(list_a):
        list_c[n] = list_a[i]
        i += 1
        n += 1
    while k < len(list_b):
        list_c[n] = list_b[k]
        k += 1
        n += 1
    return list_c


def merge_sort(inp):
    """Сортировка слиянием"""
    if len(inp) <= 1:
        return inp
    middle = len(inp) // 2
    left = [inp[i] for i in range(0, middle)]
    right = [inp[i] for i in range(middle, len(inp))]
    merge_sort(left)
    merge_sort(right)
    inp[:] = merge_lists(left, right)[:]


def quick_sort(inp):
    """Быстрая сортировка Хоара"""
    if len(inp) <= 1:
        return inp
    barrier = inp[0]
    left = []
    right = []
    middle = []

    for element in inp:
        if element < barrier:
            left.append(element)
        elif element == barrier:
            middle.append(element)
        else:
            right.append(element)
    quick_sort(left)
    quick_sort(right)
    inp[:] = (left + middle + right)[:]
