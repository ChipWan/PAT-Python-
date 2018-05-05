class Graph:
    def __init__(self,vn=0):
        self.vnum=vn
        self.V={}
        self.E={}
    def add_vertex(self,v):
        self.vnum+=1
        self.V[v]=False
        self.E[v]={}
    def add_edge(self,v1,v2):
        if not v1 in self.V:
            self.add_vertex(v1)
        if not v2 in self.V:
            self.add_vertex(v2)
        self.E[v1][v2]=1
        self.E[v2][v1]=1
    def dfs(self,v):
        self.V[v]=True
        for e in self.E[v]:
            if self.V[e]==False:
                self.dfs(e)
    def DFS(self):
        connum=0
        for e in self.V:
            if self.V[e]==False:
                connum+=1
                self.dfs(e)
        return connum
    def set_visited(self,v):
        self.V[v]=True
    def reset(self):
        for e in self.V:
            self.V[e]=False
N,M,K=map(int,input().split())
g=Graph()
for i in range(M):
    a,b=map(int,input().split())
    g.add_edge(a,b)
quest=list(map(int,input().split()))
result=[]
for e in quest:
    g.reset()
    g.set_visited(e)
    result.append(g.DFS()-1)
for e in result:
    print(e)

