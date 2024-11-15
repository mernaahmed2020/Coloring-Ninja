from environment import coloringNinja
from Node import Node
from BFS import breadth_first_graph_search

# Initialize the environment
ninja_env = coloringNinja(lineSize=7)

# Create the root node from the environment instance
root = Node.root(ninja_env)


# Run BFS
result = breadth_first_graph_search(ninja_env, verbose=True)

# Display results
if result["actions"] is not None:
    actions = result.get("actions")
    cost = result.get("total_cost")
    print("Solution found!")
    print("Actions:", actions)
    print("Total Cost:", cost)
    print(ninja_env.getState())

else:
    print("No solution found.")

print("Max Frontier Size:", result["max_frontier"])