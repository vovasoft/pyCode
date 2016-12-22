def eggs(some):
    some.append('hello')
spam = [1,2,3]
eggs(spam)
print(spam)


import copy
spam=['A','B','C','D']
cheese = copy.copy(spam)
cheese[1]=42

print(spam)
print(cheese)


l1 = [1,[0,0,0],3]
l2 = [4,5,6]
l3 = [l1,l2]
print(l3)

# l4 = l3
l4 = copy.deepcopy(l3)
l4[0][1][1]=42
print(l3)
print(l4)
print('**'*20)

