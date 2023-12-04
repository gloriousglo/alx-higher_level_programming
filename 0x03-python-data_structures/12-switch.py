#!/usr/bin/python3
a = 89
b = 10
def switch_values(a, b):
    a, b = switch_values(a, b)

print("After switching: a={:d} - b={:d}".format(a, b))
