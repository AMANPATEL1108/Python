from collections import deque, defaultdict

def GraphChallenge(strArr):
    n = int(strArr[0])
    graph = defaultdict(list)
    start = strArr[1]
    end = strArr[n]
    
    # Build the graph
    for i in range(1, n + 1):
        graph[strArr[i]] = []

    for i in range(n + 1, len(strArr)):
        edge = strArr[i].split('-')
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # BFS to find the shortest path
    queue = deque([start])
    parent = {}
    visited = set([start])
    
    while queue:
        current = queue.popleft()
        
        if current == end:
            # Reconstruct the path
            path = []
            while current:
                path.append(current)
                current = parent.get(current)
            path.reverse()
            return "-".join(path)
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current
    
    return "-1"  # No path found

# Test the function with the given example
input_data = ["5", "A", "B", "C", "D", "F", "A-B", "A-C", "B-C", "C-D", "D-F"]
print(GraphChallenge(input_data))
