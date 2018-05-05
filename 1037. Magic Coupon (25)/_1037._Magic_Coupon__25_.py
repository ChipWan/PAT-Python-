N=int(input())
NC=list(map(int,input().split()))
M=int(input())
NP=list(map(int,input().split()))
NC.sort()
NP.sort()
sum=0
i=0
while i<len(NC) and i<len(NP) and NC[i]<0 and NP[i]<0:
    sum+=NC[i]*NP[i]
    i+=1
i=len(NC)-1
j=len(NP)-1
while i>=0 and j>=0 and NC[i]>0 and NP[j]>0:
    sum+=NC[i]*NP[j]
    i-=1
    j-=1
print(sum)