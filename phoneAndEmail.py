#! python3
# ! phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard

import pyperclip, re

phoneRegex = re.compile('''(
    (\d{3,4}|\(\d{3,4}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.) \s*(\d(2,5)))?
)''', re.VERBOSE)

# TODO: Create email regex
emailRegex = re.compile('''(
    [a-zA-Z0-9._+%-]+
    @
    [a-zA-Z0-9._]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)
# TODO: Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for group in phoneRegex.findall(text):
    phoneNum = '-'.join(group[1], group[3], group[5])
    if group[8] != '':
        phoneNum += ' x' + group[8]
        matches.append(phoneNum)
for group in emailRegex.findall(text):
    matches.append(group[0])

# TODO: Copy result to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copy lalala')
    print('\n'.join(matches))
else:
    print('None')