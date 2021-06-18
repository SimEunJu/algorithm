class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for _from, _to in sorted(tickets):
            graph[_from].append(_to)
        
        result = []
        def findDfs(_from):
            while graph[_from]:
                findDfs(graph[_from].pop(0))
            
            result.append(_from)
                
                
        findDfs("JFK")
        return result[::-1]
        
