cat = ['fat', 'black', 'loal']
size, color, disposition = cat

print(cat)
print(size)

cat.append('moose')
cat.insert(1, 'chicken')
print(cat)

cat.sort()
print(cat)

cat.insert(0, 'AAAAA')
print(cat)
cat.sort()
print(cat)
cat.append('ZZZZZZZ')
cat.sort()
print(cat)

print('$' * 30)
print('Helloworld!'[1])
print('Helloworld!'[0:5])
print('Helloworld!'[:5])
print('Helloworld!'[3:])

print('Remember, remember, the fiftth of November.'.split())
print('''Remember, remember, the fiftth of November
sdfsdfsaf
sadfsafdsadf
dddddddddd
ffffffffffff
eeeeeeeeee.'''.split())

t = '12345'

print(t)
print(t.ljust(6, '*'))
print(t.ljust(12, '*'))
print(t.rjust(6, '*'))
print(t.rjust(12, '*'))
print(t.center(12, '*'))

print('**' * 12)
import re

test = re.compile(r'\d{1,3}(.(\d{3}.)*\d{1,3})?')
print('1~~~~~~~~~~~~~~~~~~')
mo = test.search('1')
print(mo.group())
mo = test.search('1.234')
print(mo.group())
mo = test.search('1.234.43')
print(mo.group())
mo = test.search('1.324.234.5')
print(mo.group())
mo = test.search('1.123.123')
print(mo.group())
print('2~~~~~~~~~~~~~~~~~~')
mo = test.search('12')
print(mo.group())
mo = test.search('12.234')
print(mo.group())
mo = test.search('12.234.43')
print(mo.group())
mo = test.search('12.324.234.5')
print(mo.group())
mo = test.search('12.123.123')
print(mo.group())
print('3~~~~~~~~~~~~~~~~~~')
mo = test.search('123')
print(mo.group())
mo = test.search('123.234')
print(mo.group())
mo = test.search('123.234.43')
print(mo.group())
mo = test.search('123.324.234.5')
print(mo.group())
mo = test.search('123.123.123')
print(mo.group())
mo = test.search('123')
print(mo.group())
print('4~~~~~~~~~~~~~~~~~~')
mo = test.search('123.24')
print(mo.group())
mo = test.search('123.24.43')
print(mo.group())
mo = test.search('123.34.234.5')
print(mo.group())
mo = test.search('123.13.123')
print(mo.group())
mo = test.search('1223')
print(mo.group())
print('===' * 30)
print('===' * 30)

t = re.compile('([A-Z]\w+)+ Nakamoto')
mo = t.search('Nakamoto lalala')
if mo != None:
    print(mo)
mo = t.search('Satoshi Nakamoto')
if mo != None:
    print(mo)
mo = t.search('RoboCop Nakamoto ')
if mo != None:
    print(mo)
mo = t.search(' Nakamoto ')
if mo != None:
    print(mo)
mo = t.search('Mr. Nakamoto ')
if mo != None:
    print(mo)
mo = t.search('Mr Nakamoto')
if mo != None:
    print(mo)

print('===' * 30)
print('===' * 30)
t = re.compile('(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)', re.IGNORECASE)
mo = t.search('Alice eats apples.')
print(mo)
mo = t.search('Bob pets cats.')
print(mo)
mo = t.search('Carol throws baseballs.')
print(mo)
mo = t.search('Alice throws Apples.')
print(mo)
mo = t.search('BOB EATS CATS.')
print(mo)
mo = t.search('RoboCop eats apples.')
print(mo)
mo = t.search('ALICE THROWS FOOTBALLS.')
print(mo)
mo = t.search('Carol eats 7 cats.')
print(mo)


