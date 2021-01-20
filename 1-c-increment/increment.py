# -*- coding: utf-8 -*-
"""
Given a large non-negative integer x, find the number of decimal digits in x + 1.
Input
A non-negative integer x (0 ≤ x ≤ 101 000 000) with no leading zeroes.
Output
The number of decimal digits in x + 1.
"""

def count_digit(number, digit=-1):
    if digit == -1 or number is None:
        return -1
    count = 0
    for i in str(number):
        if i == str(digit):
            count += 1
    return count


def total_digits(x):
    nines = count_digit(x, digit=9)
    if nines == len(x):
        return len(x) + 1
    return len(x)


def solution(x):
    """
    Count the number of 9s present in x, if len(x) == number of nines, then (x+1) will have number of digits = len(x) +1
    else same as len(x)
    :param x: the input
    :return: total digits present in x + 1
    """
    if x is None:
        return x
    return total_digits(x)


def main():
    x = map(str, input().split())

    result = solution(list(x)[0])

    print(result)


if __name__ == '__main__':
    main()