
from pulp import * 



model = LpProblem("Diet", LpMinimize)

# Define decision variables
e = LpVariable("eggs", 0, None, LpContinuous)
g = LpVariable("granola", 0, None, LpContinuous)
y = LpVariable("yogurt", 0, None, LpContinuous)
s = LpVariable("shrimp", 0, None, LpContinuous)
v = LpVariable("vegetables", 0, None, LpContinuous)


# Define Objective
model += 0.31*e + 0.5*g + 0.87*y + 1.86*s + v


# Define Constraints -- weekly
model += 70*e + 160*g + 100*y + 90*s + 120*v >= 14000 # calories
model += 70*e + 25*g + 60*y + 310*s + 860*v <= 35000 # sodium
model += 6*e + 4*g + 18*y + 22*s + 6*v >= 350 # protein
model += e + 0*g + 0*y + 0*s + 0*v >= 140 # vitamin D
model += 30*e + 30*g + 190*y + 50*s + 60*v >= 9100 # calcium
model += 0.9*e + 1.1*g + 0*y + 0*s + 1.6*v >= 126 # iron
model += 70*e + 150*g + 190*y + 125*s + 220*v >= 32900 # potassium

model.solve()

for v in model.variables():
    print(f"{v.name} = {v.varValue:.2f}")

print(f"Cost of Weekly Diet: ${value(model.objective):.2f}")