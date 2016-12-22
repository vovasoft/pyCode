import pprint
message = 'It was a bright could day in April, and the clocks were striking thirteen.'
count={}
for charactor in message:
    count.setdefault(charactor,0)
    count[charactor]=count[charactor]+1
res={}
print(pprint.pformat(res))
print(res)