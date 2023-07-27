import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if current_dist > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

def find_optimal_route(graph, start, destination):
    distances = dijkstra(graph, start)
    if distances[destination] == float('inf'):
        return None
    route = []
    node = destination

    while node != start:
        route.append(node)
        neighbors = graph[node]
        min_distance = float('inf')
        next_node = None
        for neighbor, weight in neighbors.items():
            if distances[neighbor] + weight == distances[node] and distances[neighbor] < min_distance:
                min_distance = distances[neighbor]
                next_node = neighbor
        if next_node is None or next_node in route:
            return None
        node = next_node

    route.append(start)
    route.reverse()
    return route

# Get user input for the graph
graph = {}
num_edges = int(input("Enter the number of edges in the graph: "))
print("Enter the edges in the format 'node1 node2 weight':")
for _ in range(num_edges):
    edge = input().split()
    node1, node2, weight = edge[0], edge[1], int(edge[2])
    if node1 not in graph:
        graph[node1] = {}
    if node2 not in graph:
        graph[node2] = {}
    graph[node1][node2] = weight
    graph[node2][node1] = weight

# Get user input for the start and destination nodes
start_node = input("Enter the start node: ")
destination_node = input("Enter the destination node: ")

# Find the optimal route
route = find_optimal_route(graph, start_node, destination_node)

# Print the result
if route is None:
    print("No route found.")
else:
    print("Optimal route:", route)
    
    
#     OUTPUT
#     Enter the number of edges in the graph: 7
# Enter the edges in the format 'node1 node2 weight':
# A B 3
# B C 4
# C E 6
# A D 7
# D E 4
# D C 5
# B D 2
# Enter the start node: A
# Enter the destination node: E
# Optimal route: ['A', 'B', 'D', 'E']