import re


def fun(code):
    print('begin')
    lenStr = len(code)
    if lenStr < 8:
        return False
    else:
        wordRegex = re.compile(r'[a-zA-Z0-9]*')
        mo = wordRegex.search(code)
        if mo == None:
            print('mo is None')
        else:
            print('grop = '+mo.group())
            findNumRe= re.compile('\d+')
            if len(findNumRe.findall(code)) > 0 and len(findNumRe.findall(code)) < len(code):
                return True

    return False


res = fun('adf1adf')
print(res)
