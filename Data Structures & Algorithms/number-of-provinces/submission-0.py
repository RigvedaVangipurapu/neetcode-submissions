class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected[0]) #number of vertices
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(i1): #function to find a node's parent
            print('finding ', i1, 'parent')
            res = i1

            while res!= parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            print('found - ',res)
            return res

        def union(i1 , i2):
            print('unioning',i1,i2)
            pi1 , pi2 = find(i1) , find(i2) #indices of parents
            
            if pi1 == pi2:
                return 0 # 0 unions happened

            else:
                if rank[pi1] >= rank[pi2]:
                    parent[pi2] = pi1 
                    rank[pi2] += 1
                    print ('unioned into' ,pi1)
                    return 1
                else:
                    parent[pi1] = pi2
                    rank[pi1] += 1
                    print ('unioned into', pi2)
                    return 1


        cities = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    print(i,j)
                    cities -= union(i,j)
        return cities











        