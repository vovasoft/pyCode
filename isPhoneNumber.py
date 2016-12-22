def isphoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


message = 'Call me at 415-555-1011 tomorrow, 415-555-9999 is my office'

for i in range(len(message)):
    chunk = message[i:i + 12]
    if isphoneNumber(chunk):
        print('phone number found: ' + chunk)
print('done')

print("************************************")
import re

phoneNumRegex = re.compile('\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Call me at 415-555-1011 tomorrow, 415-555-9999 is my office')
print('Phone number found: ' + mo.group())
print("************************************")
import re

phoneNumRegex = re.compile('(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('Call me at (415) 555-1011 tomorrow')
print('Phone number found: ' + mo.group())
print('Phone number found: ' + mo.group(0))
print('Phone number found: ' + mo.group(1))
print('Phone number found: ' + mo.group(2))

print("************************************")
heroRegex = re.compile('Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())
mo3 = heroRegex.findall('Batman and Tina Fey')
print(mo3[1])

print('*****' * 10)
batRegex = re.compile('Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batman , Batbat, lost a wheel')
print(mo.group())
print(mo.group(0))
print(mo.group(1))
print('*****' * 10)
batRegex = re.compile('Bat(wo)?man')  # 0次或1次
mo1 = batRegex.search('The Adventr Batman')
mo2 = batRegex.search('heheheh  Batwoman')

print(mo1.group())
print(mo2.group())
print('*****' * 10)
batRegex = re.compile('Bat(wo)*man')  # 0次或多次
mo1 = batRegex.search('The Adventr Batman')
mo2 = batRegex.search('heheheh  Batwowowowoman')

print(mo1.group())
print(mo2.group())
print('*****' * 10)
batRegex = re.compile('Bat(wo)+man')  # 一次或多次
mo1 = batRegex.search('The Adventr Batwoman')
mo2 = batRegex.search('heheheh  Batwowowowoman')
mo3 = batRegex.search('The Adventr Batman')
print(mo1.group())
print(mo2.group())
print(mo3)
print('*****' * 10)
haRegex = re.compile('(ha){3}')
mo = haRegex.search('hah-hahaha-hahaha')
print(mo.group())
#贪心和非贪心
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
greedyHaRegex=re.compile('(ha){1,5}?')
mo1=greedyHaRegex.search('hahahaha')
print(mo1.group())

