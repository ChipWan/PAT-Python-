class Vertex:
    def __init__(self):
        self.visited=False
        self.weight=0

class Graph:
    def __init__(self,c):
        self.V={}
        self.E={}
        self.crisis=c
        self.sumWe=0
    def add_vertex(self,item_v):
        self.V[item_v]=Vertex()
        self.E[item_v]={}
    def add_edge(self,item_e1,item_e2,item_value):
        if not item_e1 in self.V:
            self.add_vertex(item_e1)
        if not item_e2 in self.V:
            self.add_vertex(item_e2)
        self.E[item_e1][item_e2]=1
        self.E[item_e2][item_e1]=1
        self.V[item_e1].weight+=item_value
        self.V[item_e2].weight+=item_value
    def dfs(self,start,item_list):
        item_list.append(start)
        self.sumWe+=self.V[start].weight
        self.V[start].visited=True
        for e in self.E[start]:
            if self.V[e].visited==False:
                self.dfs(e,item_list)
N,M=map(int,input().split())
g=Graph(M)
for i in range(N):
    tmp=input().split()
    a,b,c=tmp[0],tmp[1],int(tmp[2])
    g.add_edge(a,b,c)
#print(g.E)
count=0
result=[]
for e in g.V:
    if g.V[e].visited==False:
        tmp=[]
        g.sumWe=0
        g.dfs(e,tmp)
        if len(tmp)>2 and g.sumWe/2.0>g.crisis:
            result.append(max(tmp,key=lambda x: g.V[x].weight)+' '+str(len(tmp)))
            count+=1
print(count)
sorted(result)
for e in result:
    print(e)