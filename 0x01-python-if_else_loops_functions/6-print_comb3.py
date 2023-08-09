#!/usr/bin/python3

for i in range(0, 9):
    for j in range(0, 10):
        if j == i or i > j and (i * 10 + j) % 10 == j:
            continue
        else:
            if not j * i == 72:
                print(f"{i:d}{j:d}".format(i, j), end=', ')
            else:
                print(f"{i:d}{j:d}".format(i, j), end='')
print("")
