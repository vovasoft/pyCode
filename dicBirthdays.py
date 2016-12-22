birthdays={'Alice':'Apr 1','Bob':'Dec 12','Carol':'mar 4'}

while True:
    print('Enter xxx')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name]+' is the birthday of ' +name)
    else :
        print('I don\'t have birthdays information for '+namew)
        print('What is their birthday')
        bday=input()
        birthdays[name]=bday
        print('birthday database updated.')
