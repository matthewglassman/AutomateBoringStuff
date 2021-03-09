#!/usr/bin/python3
# bulletPointAdder.py - Adds Wikipedia bullet points to start
# of each line of text on the clipboard

import pyperclip

text = pyperclip.paste()

# Separate lines and add stars.

lines = text.split('\n')
for index in range(len(lines)):  # loop through all indexes in the "lines" list
    lines[index] = '* ' + lines[index]  # add a star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)
print(text)
