#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()
#TODO: Separate lines and add starts

print(text)
print('^'*20)
lines = text.split('\r\n')
for i in range(len(lines)):
    if len(lines[i]) >0:
   #     print(lines[i]+':'+str(len(lines[i])))
        lines[i] = '*'+lines[i]

text = '\r\n'.join(lines)
print('#'*20)

print(text)

str = '''jkfdjlsa
dsfjklajflksdaf
sadfjklsajfdls
fdsafsdafjkdsajflksa
'''

print(str)

