class Vertex:
    def __init__(self):
        self.visited=False
        self.total=0
        self.prior=float('inf')
def myprior(g,s,x):
    if g.V[x].visited==False:
       if g.V[x].prior==float('inf'):
           g.V[x].prior=g.V[s].prior+1          

class Graph:
    def __init__(self):
        self.V={}
        self.E={}
    def add_vertex(self,item_v):
        self.V[item_v]=Vertex()
        self.E[item_v]={}
    def add_edge(self,item_e1,item_e2,value_v):
        if not item_e1 in self.V:
            self.add_vertex(item_e1)
        if not item_e2 in self.V:
            self.add_vertex(item_e2)
        flag=True
        for e in self.E[item_e1]:
            if e==item_e2:
                self.E[item_e1][item_e2]+=value_v
                flag=False
                break
        if flag:
            self.E[item_e1][item_e2]=value_v
        flag=True
        for e in self.E[item_e2]:
            if e==item_e1:
                self.E[item_e2][item_e1]+=value_v
                flag=False
                break
        if flag:
            self.E[item_e2][item_e1]=value_v
    def pfs(self,start,func):
        result=[start]
        self.V[start].visited=True
        self.V[start].prior=0
        while 1:
            for e in self.E[start]:
                func(self,start,e)
            start=min(self.V,key=lambda x: self.V[x].prior if self.V[x].visited==False else float('inf'))
            if self.V[start].visited==True:
                break
            self.V[start].visited=True
            result.append(start)
        return result

N,M=map(int,input().split())
g=Graph()
for i in range(N):
    x=input().split()
    a,b=x[0],x[1]
    c=int(x[2])
    g.add_edge(a,b,c)
    g.V[a].total+=c
    g.V[b].total+=c
#print(g.E)
gang_total=0
ganglist=[]
for e in g.V:
    if g.V[e].visited==False:
        tmp=g.pfs(e,myprior)
        if len(tmp)>2:
            total=0
            for x in tmp:
                total+=g.V[x].total
            if total/2.0>M:
                ganglist.append(max(tmp,key=lambda x:g.V[x].total)+' '+str(len(tmp)))
                gang_total+=1
print(gang_total)
sorted(ganglist)
for e in ganglist:
    print(e)