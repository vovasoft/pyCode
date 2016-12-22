def printTable (strl):
    row = len(strl[0])
    for i in range(row):
        str=[]
        for j in range(len(strl)):
            str.append(strl[j][i])
        print(' '.join(str).rjust(20))



strlist = [['apples','oranges','cherries','banana'],
           ['Alice','Bob','Carol','David'],
           ['dogs','cats','moose','goose']]
print(strlist)

printTable(strlist)