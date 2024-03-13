#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1, 10):
        if i >= j:
            continue
        elif i == 8 and j == 9:
            print('{:02}'.format(i * 10 + j))
        else:
            print('{:02}, '.format(i * 10 + j), end='')
