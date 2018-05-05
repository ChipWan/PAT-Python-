N=int(input())
result=[]
test={'1':'@',
      '0':'%',
      'l':'L',
      'O':'o'
      }
for i in range(N):
    a,b=input().split()
    flag=False
    for e in test.keys():
        if e in b:
            b=b.replace(e,test[e])
            flag=True
    if flag:
        result.append(a+' '+b)
if len(result):
    print(len(result))
    for e in result:
        print(e)
else:
    if N==1:
        print("There is 1 account and no account is modified")
    else:
        print("There are %d accounts and no account is modified"%(N))