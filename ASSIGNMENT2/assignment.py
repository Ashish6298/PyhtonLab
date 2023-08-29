import numpy as np
from scipy.optimize import linear_sum_assignment
def solve_assignment(cost_matrix):
row_ind, col_ind = linear_sum_assignment(cost_matrix) 
total_cost = cost_matrix[row_ind, col_ind].sum() 
assignment = list(zip(row_ind, col_ind))
return total_cost, assignment
def main():
n = int(input("Enter the number of workers/tasks: ")) 
cost_matrix = np.zeros((n, n))
print("Enter the cost matrix:") 
for i in range(n):
row = list(map(int, input().split())) 
cost_matrix[i] = row
total_cost, assignment = solve_assignment(cost_matrix)
print("Optimal assignment:") 
for worker, task in assignment:
print(f"Worker {worker} assigned to Task {task}")
print("Total cost:", total_cost)
if name == " main ": 
main()