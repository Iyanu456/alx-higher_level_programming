#!/usr/bin/python3
def multiple_returns(sentence):
    count = 0
    word = sentence[0]
    if sentence == None:
        word = None
    for i in sentence:
        count += 1
    return (count, word)
