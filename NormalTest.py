spam={'color':'red','age':42}
for v in spam.items():
    print(v)

print(type(spam.keys()))
li=list(spam.keys())
print(li)
print(type(li))

print('color' in spam)
print('vova' in spam)
print('age'
)

print(spam.get('color',22))
print(spam.get('vova',11))

print('*'*20)
spam.setdefault('vova',123123123)
print(spam.get('vova'))
