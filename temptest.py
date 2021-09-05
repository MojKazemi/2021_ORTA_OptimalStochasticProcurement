import numpy as np
import scipy.sparse as sp
import gurobipy as gp

m = gp.Model("matrix1")
val = np.array([1.0, 2.0, 3.0, -1.0, -1.0])
row = np.array([0, 0, 0, 1, 1])
col = np.array([0, 1, 2, 0, 1])

A = sp.csr_matrix((val, (row, col)), shape=(2, 3))
rhs = np.array([4.0, -1.0])

# Add constraints
m.addConstr(A @ x <= rhs, name="c")
print(C)