#!/usr/bin/python3

for i in range(0, 9):
    for j in range(0, 10):
        if j == i:
            continue
        if not i * j ==  72:
            if not i == j:
                print(f"{i:d}{j:d}".format(i, j), end=', ')
        else:
            print(f"{i:d}{j:d}".format(i, j), end='')
print("")
