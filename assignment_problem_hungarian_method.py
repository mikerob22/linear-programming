import numpy as np
from scipy.optimize import linear_sum_assignment

# There are n people who need to be assigned to n jobs, one person per job.
# The cost of assigning person i to job j is C[i,j].
# Find an assignment that minimizes the total cost.


# Cost matrix with values C[i][j]
cost_matrix = np.array([[9, 2, 7, 8],
                        [6, 4, 3, 7],
                        [5, 8, 1, 8],
                        [7, 6, 9, 4]])

row_i, col_j = linear_sum_assignment(cost_matrix)

optimal_assessment = col_j

total_cost = cost_matrix[row_i, col_j].sum()

# index of each row 1-4
print("Index of each row of row i is optimal value pattern", optimal_assessment)
print('Total assignment cost is', total_cost)
