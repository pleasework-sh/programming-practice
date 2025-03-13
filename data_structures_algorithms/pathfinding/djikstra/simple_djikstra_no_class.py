# Define the graph as an adjacency matrix

graph = [
    [0, 2, 4, 1, 0, 0], #1
    [2, 0, 0, 3, 10, 0], #2
    [4, 0, 0, 2, 0, 5], #3
    [1, 3, 2, 0, 7, 0], #4
    [0, 10, 0, 7, 0, 3], #5
    [0, 0, 5, 0, 3, 0] #6
]

num_nodes = len(graph)
start_node = 0

end_nodes = [1, 2, 3, 4, 5]

dist = [float('inf')] * num_nodes
dist[start_node] = 0
visited = [False] * num_nodes

def get_min(dist, visited):
    min_dist = float('inf')
    min_node = -1
    for i in range(num_nodes):
        print(f"Current value of i {i}")
        print(f"Current value of visited[i] {visited[i]}")
        print(f"Current dist[i] {dist[i]}")
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            min_node = i
    return min_node

for _ in range(num_nodes):
    current_node = get_min(dist, visited)
    visited[current_node] = True

    for neighbor in range(num_nodes):
        print(f"Current value of neighbor {neighbor}")
        print(f"Current value of graph[current_node][neighbor] {graph[current_node][neighbor]}")
        if graph[current_node][neighbor] > 0:
            if dist[current_node] + graph[current_node][neighbor] < dist[neighbor]:
                dist[neighbor] = dist[current_node] + graph[current_node][neighbor]

optimal_paths = []
for end_node in end_nodes:
    path = [end_node]
    while path[-1] != start_node:
        for neighbor in range(num_nodes):
            if graph[path[-1]][neighbor] > 0 and dist[neighbor] + graph[path[-1]][neighbor] == dist[path[-1]]:
                path.append(neighbor)
                break
    path.reverse()
    optimal_paths.append(path)

for i, path in enumerate(optimal_paths, start=2):
    print(f"Optimal path from node 1 to node {i}: {path}, Total distance: {dist[i-1]}")
