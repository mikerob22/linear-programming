# Import the PuLP library
import pulp

# Define the number of tasks and resources
num_tasks = 4
num_resources = 4

# Define the costs matrix (can be profit matrix if maximizing)
costs = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

# Create a binary LP problem
assignment_lp = pulp.LpProblem("Assignment Problem", pulp.LpMinimize)

# Define decision variables
x = [[pulp.LpVariable(f"x{i}{j}", cat=pulp.LpBinary) for j in range(num_resources)] for i in range(num_tasks)]

# Define objective function
assignment_lp += pulp.lpSum(costs[i][j] * x[i][j] for i in range(num_tasks) for j in range(num_resources))

# Add constraints: each task is assigned to exactly one resource
for i in range(num_tasks):
    assignment_lp += pulp.lpSum(x[i][j] for j in range(num_resources)) == 1

# Add constraints: each resource is assigned to at most one task
for j in range(num_resources):
    assignment_lp += pulp.lpSum(x[i][j] for i in range(num_tasks)) <= 1

# Solve the problem
assignment_lp.solve()

# Print the solution
print("Solution:")
for i in range(num_tasks):
    for j in range(num_resources):
        if pulp.value(x[i][j]) == 1:
            print(f"Task {i+1} is assigned to Resource {j+1} with cost {costs[i][j]}")

# Print the total cost
print("Total cost:", pulp.value(assignment_lp.objective))
