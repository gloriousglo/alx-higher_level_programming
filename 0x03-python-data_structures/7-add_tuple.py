#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = (1, 89)
tuple_b = (88, 11)

new_tuple = add_tuple(tuple_a, tuple_b)
print("Adding tuples: {} + {} = {}".format(tuple_a, tuple_b, new_tuple))

tuple_c = add_tuple(tuple_a, (1,))
print("Adding tuples: {} + {} = {}".format(tuple_a, (1,), tuple_c))

tuple_d = add_tuple(tuple_a, ())
print("Adding tuples: {} + {} = {}".format(tuple_a, (), tuple_d))``
