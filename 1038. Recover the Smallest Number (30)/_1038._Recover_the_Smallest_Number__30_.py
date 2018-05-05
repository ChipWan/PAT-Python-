from functools import cmp_to_key
listOfin=list(input().split())
N=int(listOfin[0])
listOfin.pop(0)
result=''
def myLess(x,y):
    if x+y<y+x:
        return -1
    if x+y>y+x:
        return 1
    return 0
listOfin.sort(key=cmp_to_key(myLess))
for e in listOfin:
    result+=e
i=0
while int(result)!=0 and result[i]=='0':
    i+=1
result=result[i:]
if int(result)==0:
    print('0')
else:
    print(result)