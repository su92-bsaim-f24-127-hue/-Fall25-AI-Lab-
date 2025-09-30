tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['G'],
    'G': []
}
visited = []
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def dfs( self,start, goal):
        if goal not in visited:
            visited.append(start)
            for i in tree[start]:
               self.dfs(i, goal)
s= Stack()
s.dfs( 'A', 'G')
print(visited)           