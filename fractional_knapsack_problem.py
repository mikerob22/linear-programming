# This model will assume it can take whole items and
# fractions other items that can be carried in the knapsack

from gekko import GEKKO

item = ['item 1', 'item 2', 'item 3', 'item 4']
weight = [2, 5, 10, 5]
value = [20, 30, 50, 10]

items = len(item)

# Create model
model = GEKKO()

# Variables
x = model.Array(model.Var, len(item), lb=0, ub=1, integer=True)

# Objective function
model.Maximize(model.sum([value[i] * x[i] for i in range(items)]))

# Constraint
limit = 16
model.Equation(model.sum([weight[i] * x[i] for i in range(items)]) <= limit)

model.solve()

# Report the solution

print()
for i in range (items):
    print("%s = %f" % (item[i], x[i].value[0]))

# convert maximum to minimum
print("Objective = %f" % (-model.options.objfcnval))

print('The model found the optimal solution by taking the following amounts of items.')
