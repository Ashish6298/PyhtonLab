def is_valid(v, pos, path, graph): 
if not graph[path[pos - 1]][v]:
return False 
if v in path:
return False 
return True
def hamiltonian_cycle_util(graph, path, pos): 
if pos == len(graph):
if graph[path[pos - 1]][path[0]] == 1: 
return True
return False
for v in range(1, len(graph)):
if is_valid(v, pos, path, graph): 
path[pos] = v
if hamiltonian_cycle_util(graph, path, pos + 1): 
return True
path[pos] = -1
return False
def hamiltonian_cycle(graph): 
path = [-1] * len(graph) 
path[0] = 0
if not hamiltonian_cycle_util(graph, path, 1): 
print("No Hamiltonian cycle found.")
else:
print("Hamiltonian cycle found:", path)
def main():
n = int(input("Enter the number of nodes: ")) 
graph = [[0] * n for _ in range(n)]
print("Enter the adjacency matrix:") 
for i in range(n):
row = list(map(int, input().split())) 
for j in range(n):
graph[i][j] = row[j]
hamiltonian_cycle(graph)
if name == " main ": 
main()