#!/usr/bin/python3
def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0

    while i < len(text) and text[i] == " ":
        i += 1

    while i < len(text):
        if text[i] in ".?:":
            print(text[i], end="")
            print("\n")
            try:
                if text[i + 1] == " ":
                    while text[i + 1] == " ":
                        i += 1
            except IndexError:
                break
        else:
            print(text[i], end="")
        i += 1
    return
