# -*- coding: utf-8 -*-

import sys


def get_max(inp):
    if inp is None:
        return inp
    return max(inp)


def count_max(inp, _max):
    if inp is None or _max is None:
        return inp
    count = 0
    for i in inp:
        if i == _max:
            count += 1
    return count


def get_index(inp, _max, which_no):
    i = 0
    for x in range(len(inp)):
        if inp[x] == _max:
            i += 1
            if i == which_no:
                return x


def solution(inp):
    if inp is None:
        return inp
    count = count_max(inp, get_max(inp))
    idx = inp.index(get_max(inp))
    if count > 1:
        idx = get_index(inp, get_max(inp), 3)
    del inp[idx]
    return inp


def main():
    n = int(input())
    a = list(map(int, input().split()))

    result = solution(inp=a)

    # your code

    print(" ".join(map(str,result)))


if __name__ == '__main__':
    main()