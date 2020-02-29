import unittest
import sort_algorithms as sa


def test_sort_1(sort_algorithm):
    print(f"Тестируем: {sort_algorithm.__doc__}")
    print("testcase #1:", end="")
    inp = [4, 5, 2, 1, 3]
    outs = [1, 2, 3, 4, 5]
    sort_algorithm(inp)
    print("Ok" if inp == outs else "Fail")


def test_sort_2(sort_algorithm):
    print(f"Тестируем: {sort_algorithm.__doc__}")
    print("testcase #2:", end="")
    inp = list(range(10, 20)) + list(range(0, 10))
    outs = list(range(0, 20))
    sort_algorithm(inp)
    print("Ok" if inp == outs else "Fail")


def test_sort_3(sort_algorithm):
    print(f"Тестируем: {sort_algorithm.__doc__}")
    print("Testcase #2:", end="")
    inp = [4, 4, 1, 3, 3]
    outs = [1, 3, 3, 4, 4]
    sort_algorithm(inp)
    print("Ok" if inp == outs else "Fail")


def test_sort_all(sort_algorithm):
    test_sort_1(sort_algorithm)
    test_sort_2(sort_algorithm)
    test_sort_3(sort_algorithm)


if __name__ == '__main__':
    test_sort_all(sa.bubble_sort)
    test_sort_all(sa.insert_sort)
    test_sort_all(sa.choise_sort)
    test_sort_all(sa.count_sort)
    test_sort_all(sa.merge_sort)
    test_sort_all(sa.quick_sort)
