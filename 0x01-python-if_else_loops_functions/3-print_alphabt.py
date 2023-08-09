#!/usr/bin/python3

for i in range(97, 123):
    if i == 'e' or i == 'q':
	    continue
    else:
	    print(chr(i), end='')
