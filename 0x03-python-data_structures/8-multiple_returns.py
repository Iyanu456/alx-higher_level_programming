#!/usr/bin/python3
def multiple_returns(sentence):
    count = 0
    word = sentence[0]
    if len(sentence) == 0:
        word = None
    for i in sentence:
        count += 1
    return (count, word)
