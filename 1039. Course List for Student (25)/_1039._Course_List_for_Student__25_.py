N,K=map(int,input().split())
studentsOfcour={}
for i in range(K):
    a,b=map(int,input().split())
    tmplist=list(input().split())
    for e in tmplist:
        if e in studentsOfcour:
            studentsOfcour[e].append(a)
        else:
            studentsOfcour[e]=[a]
if N:
    students=list(input().split())
else:
    students=[]
for e in students:
    if e in studentsOfcour.keys():
       studentsOfcour[e].sort()
       tmps=str(studentsOfcour[e]).replace('[','')
       tmps=tmps.replace(']','')
       print(e,len(studentsOfcour[e]),tmps.replace(',',''))
    else:
        print(e+' '+'0')