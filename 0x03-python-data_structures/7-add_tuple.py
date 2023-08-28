#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_ans = ()
    zero = (0,)
    for i in range(2):
        if len(tuple_a) < 2:
            tuple_a += zero
        if len(tuple_b) < 2:
            tuple_b += zero
        tuple_ans += (tuple_a[i] + tuple_b[i],)
    return tuple_ans
