Tree = {
    "a": ["b", "c"],
    "b": ["d", "e"],
    "c": ["f"],
    "d": [],
    "e": [],
    "f": ["g"],
    "g": []
}
def bfs(start, goal):
    visited = []
    q = [start]
    while q:
        n = q.pop(0)   
        if n not in visited:
            visited.append(n)
            if n == goal:  
                break
            for i in Tree[n]:
                if i not in visited:
                    q.append(i)
    return visited

print(bfs("a", "f"))