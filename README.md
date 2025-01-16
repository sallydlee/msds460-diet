# The Diet Problem Revisited
For this assignment, linear programming concepts were used to solve the classic diet problem. I selected 5 food items I routinely eat as variables and used the current recommended dietary allowances from the U.S. Food and Drug Administration as constraints. I'm looking to minimize the cost of my weekly diet while maintaining recommended levels of nutrition.

## Setting Up the Problem

The variables and their constaints are shown in the table below. The last row showing the costs per serving sets up the objective.
![](https://raw.githubusercontent.com/sallydlee/msds460-diet/refs/heads/main/misc/constraint%20table.PNG)

## Solving the Problem

The optimization model recommended consuming 140 eggs, 151.67 servings of granola, 1.84 servings of yogurt, and no shrimp or vegetables for a weekly cost of $120.84. The `pulp` library in Python was used to solve the diet problem. The code can be found in `diet solution.py`. 

Additional constraints were then added to increase the variety and practicality of the model. The code can be found in `modified diet solution.py`. For more details on what the constraints were, please see part 4 of my write-up located in the repository.

## Solving with AI

ChatGPT was used to verify the solution and validate its ability to solve the optimization problem. ChatGPT generated Python code which was compared to the code used to solve the problem on my own. The entire conversation and prompts can be read in the `ChatGPT conversation.txt` file.
