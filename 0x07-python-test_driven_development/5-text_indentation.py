#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in ".:?":
        text = (i + "\n\n").join([line.strip(" ") for line in text.split(i)])
    print(text, end="")
