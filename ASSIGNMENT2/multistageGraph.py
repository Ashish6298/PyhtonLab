def multistage_graph(graph, stages): 
n = len(graph)
cost = [float('inf')] * n 
parent = [0] * n
cost[n - 1] = 0
for i in range(n - 2, -1, -1): 
for j in range(n):
if graph[i][j] != float('inf'):
if cost[i] > graph[i][j] + cost[j]: 
cost[i] = graph[i][j] + cost[j] 
parent[i] = j
path = [0]
current_stage = 0
while current_stage < len(stages) - 1: 
next_stage = stages[current_stage + 1] 
next_node = parent[path[-1]]
while next_node < next_stage: 
path.append(next_node) 
next_node = parent[next_node]
current_stage += 1
path.append(n - 1) 
return path, cost[0]
def main():
n = int(input("Enter the number of nodes: ")) 
graph = [[float('inf')] * n for _ in range(n)]
for i in range(n):
neighbors = list(map(float, input(f"Enter distances for neighbors of node {i}: ").split())) 
for j, distance in enumerate(neighbors):
graph[i][j] = distance
num_stages = int(input("Enter the number of stages: "))
stages = list(map(int, input("Enter the number of nodes in each stage: ").split()))
if stages[0] != 1 or stages[-1] != 1:
print("First and last stages must have only one node.") 
return
path, min_cost = multistage_graph(graph, stages) 
print("Shortest path:", " -> ".join(map(str, path))) 
print("Minimum cost:", min_cost)
if name == " main ": 
main()