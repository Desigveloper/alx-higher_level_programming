#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        first = None
        return first

    length = len(sentence)
    first = sentence[0]

    return length, first