N=int(input())
listOfman={}
listOffem={}
for i in range(N):
    tmp=input().split()
    a,b,c,d=tmp[0],tmp[1],tmp[2],int(tmp[3])
    if b=='M':
        listOfman[a+' '+c]=d
    elif b=='F':
        listOffem[a+' '+c]=d
maxfem=max(listOffem,key=lambda x:listOffem[x]) if listOffem else None
minman=min(listOfman,key=lambda x:listOfman[x]) if listOfman else None
if maxfem:
   print(maxfem)
else:
    print("Absent")
if minman:
    print(minman)
else:
    print("Absent")
if maxfem and minman:
    print(listOffem[maxfem]-listOfman[minman])
else:
    print("NA")