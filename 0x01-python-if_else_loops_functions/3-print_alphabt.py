#!/usr/bin/python3

for i in range(97, 123):
    if i == 'e' or i == 'q':
	    continue
    else:
	    print(f'{chr(i)}'.format(chr(i)), end='')
