class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        d = {}
        self.n = len(tickets)
        for ticket in tickets:
            if ticket[0] in d.keys():
                d[ticket[0]][ticket[1]] = d[ticket[0]].get(ticket[1], 0) + 1
            else:
                d[ticket[0]] = {}
                d[ticket[0]][ticket[1]] = 1
        self.itin = ["JFK"]
        self.dfs("JFK", d)
        return self.itin
        
    def dfs(self, cur, d):
        if len(self.itin) == self.n + 1:
            return True
        if cur in d.keys():
            for city in sorted(d[cur]):
                if d[cur][city] > 0:
                    d[cur][city] -= 1
                    self.itin = self.itin + [city]
                    if self.dfs(city, d):
                        return True
                    d[cur][city] += 1
                    self.itin = self.itin[: -1]
            return False
