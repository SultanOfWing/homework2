# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math

from typing import List


def cyclicRoot():
    while True:
        try:
            a = int(input())
            if a < 0:
                break
            else:
                print(math.sqrt(a))
        except ValueError:
            print("Wrong input type: integer expected")


def find_max(n: int):
    try:
        print("Print number to comparison")
        current_min = int(input())
        for i in range(n - 1):
            print("Print another 4number to comparison")
            current_input = int(input())
            if current_input < current_min:
                current_min = current_input

        print(current_min)

    except ValueError:
        print("Wrong input type: integer expected")


def find_sum_or_multi(n_list: List[int], sign: str):
    if sign == "+":
        res = 0
        for i in n_list:
            assert isinstance(i, int)
            res += i
        print(res)
    if sign == "*":
        res = 1
        for i in n_list:
            assert isinstance(i, int) != 0
            res *= i
        print(res)


def find_fib(n: int):
    prev1 = 0
    prev2 = 1
    fib_list = [prev1, prev2]
    for i in range(n):
        current = prev1 + prev2
        fib_list.append(current)
        prev1 = prev2
        prev2 = current

    print(fib_list)


def find_fib_less_then(n: int):
    prev1 = 0
    prev2 = 1
    fib_list = [prev1, prev2]
    while True:
        current = prev1 + prev2
        if current < n:
            fib_list.append(current)
            prev1 = prev2
            prev2 = current
        else:
            break

    print(fib_list)


def celsius_to_fahrenheit(celsius_list: List[int]):
    for c in celsius_list:
        f = c * 1.8 + 32
        print(str(c) + " in celsius equals " + str(f) + " in fahrenheit")


def polygon_perimeter_by_coordinates(n: int):
    print("set 1st point x and y")
    prev_x_y = input().split(",")
    edge_coordinates_list = [prev_x_y]
    assert isinstance(int(prev_x_y[0]), int), print("Wrong format")
    assert isinstance(int(prev_x_y[1]), int), print("Wrong format")

    perimeter = 0
    for i in range(n - 1):
        print("set " + str(i + 2) + "st point x and y")
        x_y = input().split(",")
        edge_size = calculate_edge_size(prev_x_y, x_y)
        perimeter += edge_size
        prev_x_y = x_y
        edge_coordinates_list.append(prev_x_y)

    edge_size = calculate_edge_size(edge_coordinates_list[0], edge_coordinates_list[n - 1])
    perimeter += edge_size

    print(perimeter)


def calculate_edge_size(prev: list, current: list):
    a = ((int(current[0]) - int(prev[0])) ** 2)
    b = ((int(current[1]) - int(prev[1])) ** 2)
    return math.sqrt(a + b)


# cyclicRoot()
# find_max(4)
# find_sum_or_multi([3, 5, 7, 2], "+")
# find_fib(10)
# find_fib_less_then(21
# celsius_to_fahrenheit([4, 7, 8, 2, 9])
# polygon_perimeter_by_coordinates(5)


def average(list_n: list):
    avg = sum(list_n) / len(list_n)
    print("average: " + str(avg))
    for n in list_n:
        if n > avg:
            print("N bigger then average")
        elif n < avg:
            print("N less then average")
        else:
            print("N equals average")


def bigger_than_adjacent(list_n: list):
    l = []
    for n in range(len(list_n)):
        prev = list_n[n - 1]
        if n < len(list_n) - 1:
            _next = list_n[n + 1]
        else:
            _next = list_n[0]

        if list_n[n] > prev and list_n[n] > _next:
            l.append(list_n[n])

    print(l)


def reverse_list(list_n: list):
    list_n.reverse()
    print(list_n)


def take_sublist():
    l = [4, 7, 2, 4, 1, 7, 8, 3, 6, 2, 5, 3, 6, 7, 3, 2, 1, 5, 6, 7]
    while True:
        a = int(input())
        b = int(input())
        if a == b == 0:
            break
        elif a < b:
            print(l[a:b - 1])
        elif a > b:
            print(l[a:b + 1:-1])


def list_to_set(list_n: list):
    print(set(list_n))


def lists_intersection(list_n: list, list_m: list):
    print(list(set(list_n) & set(list_m)))


# add::name
# find::name
# list::
# delete::name
# stop::
def crm():
    l = []
    while True:
        inp = input().split("::")
        key = inp[0]
        value = inp[1]
        if key == "add":
            l.append(value)
        elif key == "find":
            if value in l:
                print("Exists")
            else:
                print("Not exists")
        elif key == "list":
            print(l)
        elif key == "delete":
            l.remove(value)
        elif key == "stop":
            break

# average([4, 5, 6, 7, 3, 4, 5])
# bigger_than_adjacent([4, 5, 6, 7, 3, 4, 5])
# reverse_list([1, 2, 3, 4, 5, 6])
# take_sublist()
# list_to_set([5, 5, 4, 3, 2, 4])
# lists_intersection([1, 2, 3, 4, 5], [1, 3, 5, 6])
# crm()
