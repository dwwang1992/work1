#!/usr/bin/python35
# -*- coding: utf-8 -*-
# author: WangDaWei


def func(x):
    if x == 1:
        return 1
    else:
        return x * func(x - 1)


def main(wid):
    print('hello,everybody!')
    print(func(wid))


if __name__ == '__main__':
    main(10)
    print(1*2*3*4*5*6*7*8*9*10)
