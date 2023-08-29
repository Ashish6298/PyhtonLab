def optCost(freq, i, j):
if j < i:
return 0 
if j == i:
return freq[i]
fsum = Sum(freq, i, j)
Min = 999999999999
for r in range(i, j + 1):
cost = (optCost(freq, i, r - 1) + 
optCost(freq, r + 1, j))
if cost < Min:
Min = cost
return Min + fsum
def optimalSearchTree(keys, freq, n):
return optCost(freq, 0, n - 1)
def Sum(freq, i, j): 
s = 0
for k in range(i, j + 1): 
s += freq[k]
return s
if name == ' main ':
keys = input("Enter keys separated by spaces: ").split()
freq = list(map(float, input("Enter corresponding probabilities: ").split()))
n = len(keys)
print("Cost of Optimal BST is", 
optimalSearchTree(keys, freq, n))
