## Reinforcement

"""
R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
"""


def is_multiple(n, m):
    if n == 0:
        raise ValueError("n values can't be a zero value")
    if not isinstance(n, (int, float)):
        raise ValueError("n value should be integer or float values")
    if not isinstance(m, (int, float)):
        raise ValueError("m value should be integer or float values")
    value_check = m % n
    if value_check != 0:
        return False
    else:
        return True


print(is_multiple(6, 2))
print(is_multiple(2, 6))
# print(is_multiple('a', 3))

"""
R-1.2 Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
"""


def is_even(k):
    if not isinstance(k, int):
        raise ValueError('k value should be an integer value')

    if (k & 1) != 1:
        return True
    else:
        return False


print(is_even(4))
# print(is_even(2.2))
# print(is_even('a'))

"""
R-1.3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
"""


def maxmin(data):
    sorted_values = sorted(data)
    return sorted_values[0], sorted_values[-1]


print(maxmin([1, 2, 3, 4, 5, 6]))

"""
R-1.4 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""


def sumsqrt(n):
    if n <= 0:
        raise ValueError('n should be a positive value')
    if not isinstance(n, int):
        raise ValueError('n value should be an integer')
    a = 0
    for i in range(1, n + 1):
        a += i ** 2
    return a


print(sumsqrt(90))

"""
R-1.5 Give a single command that computes the sum from Exercise R-1.4, rely-
ing on Python’s comprehension syntax and the built-in sum function.
"""


def sumsqrt_c(n):
    if n <= 0:
        raise ValueError('n should be a positive value')
    if not isinstance(n, int):
        raise ValueError('n value should be an integer')
    return


"""
R-1.6 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""


def sumsqrtodd(n):
    if n <= 0:
        raise ValueError('n should be a positive value')
    if not isinstance(n, int):
        raise ValueError('n value should be an integer')

    a = 0
    # while 0 < n + 1:
    #     if n & 1:
    #         a += n ** 2
    for i in range(1,n):
        if n & 1==0:
           a += n ** 2
    return a


print(sumsqrtodd(190))
