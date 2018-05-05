class Graph:
    def __init__(self):
        self.edge={}
        self.vertex={}
    def clear(self):
        for e in self.vertex:
            e[1]=False
    def add_vertex(self,item_v):
        self.vertex[item_v]=False
        self.edge[item_v]=[]
    def add_edge(self,item_e1,item_e2,value):
        if not item_e1 in self.vertex:
            self.add_vertex(item_e1)
        if not item_e2 in self.vertex:
            self.add_vertex(item_e2)
        flag=True
        for e in self.edge[item_e1]:
            if e[0]==item_e2:
               e[1]+=value
               flag=False
        if flag:
            self.edge[item_e1].append([item_e2,value])
    def dfs(self,start,result):
        result.append(start)
        self.vertex[start]=True
        for e in self.edge[start]:
            if (not e[0] in result) and(self.vertex[e[0]]==False):
                self.dfs(e[0],result)
    def gang_dfs(self,start):
        result=[]
        self.dfs(start,result)
        for e in self.vertex:
            if not e in result:
                for x in self.edge[e]:
                    if x[0] in result:
                       self.dfs(e,result)
        return result

#if __name__=='__main__'
g=Graph()
N,M=map(int,input().split())
for i in range(N):
    x=input().split()
    a,b=x[0],x[1]
    c=int(x[2])
    g.add_edge(a,b,c)

totalgang=0
ganglist=[]
for e in g.vertex:
    if not g.vertex[e]:
        tmp=g.gang_dfs(e)
        if len(tmp)>2:
            result={}
            for index in tmp:
                result[index]=0
            for x in tmp:
               for y in g.edge[x]:
                    result[x]+=y[1]
                    result[y[0]]+=y[1]
            total=sum(list(result.values()))/2.0
            if total>M:
                totalgang+=1
                maxtmp=0
                maxkey=''
                for e in result:
                    if result[e]>maxtmp:
                        maxtmp=result[e]
                        maxkey=e
                ganglist.append(maxkey+' '+str(len(result)))
print(totalgang)
for e in ganglist:
    print(e)
                