class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        start = k
        #convert the times list to a graph
        graph = defaultdict(list)

        for u , v, w in times:
            graph[u].append([v,w])

        print(graph)
        
        #initialize a minheap to store the shortest distance
        hq = [[0,start]]

        #initialize a dict that has each edge and min distance from start
        visited = {}

        while hq:
            w1 , u = heapq.heappop(hq)
            print('checking',u,w1)
            print('now heap is ', hq)

            if u in visited:
                continue

            visited[u] = w1

            for v , w2 in graph[u]:
                if v not in visited:
                    heapq.heappush(hq,[ w1+w2, v])

        
        for u ,v,w in times:
            if u not in visited:
                visited[u] = -1

        ans =  max(visited.values()) if -1 not in visited.values() and len(visited) == n else -1
        print(visited)
        return ans




