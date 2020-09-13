class Solution:
    def minimumCost(self,N ,connections):
        if len(connections)< N -1:
            print("No")
        connections.sort(key = lambda a : a[2])
        parent = [i for i in range(N)]

        def find(x):
            if x!= parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        res , e, k = 0, 0, 0
        while e<N-1:
            u,v,w = connections[k]
