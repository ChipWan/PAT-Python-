class Graph:
    def __init__(self,vn=0):
        self.vnum=vn
        self.V=[0]*vn
        self.E=[[0]*vn for i in range(vn)]
    def add_edge(self,v1,v2):
        self.E[v1][v2]=1
        self.E[v2][v1]=1
    def dfs(self,v):
        self.V[v]=1
        for i in range(self.vnum):
            if self.E[v][i]==1 and self.V[i]==0:
                self.dfs(i)
    def DFS(self):
        connum=0
        for i in range(self.vnum):
            if self.V[i]==False:
                connum+=1
                self.dfs(i)
        return connum
    def set_visited(self,v):
        self.V[v]=1
    def reset(self):
        for i in range(self.vnum):
            self.V[i]=0
N,M,K=map(int,input().split())
g=Graph(N)
for i in range(M):
    a,b=map(int,input().split())
    g.add_edge(a-1,b-1)
quest=list(map(int,input().split()))
result=[]
for e in quest:
    g.reset()
    g.set_visited(e-1)
    result.append(g.DFS()-1)
for e in result:
    print(e)
exit(0)