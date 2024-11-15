from environment import coloringNinja
from Node import Node
from BFS import breadth_first_graph_search

# Initialize the environment
ninja_env = coloringNinja(lineSize=16)

# Create the root node from the environment instance
root = Node.root(ninja_env)

# Run BFS
solution, max_frontier = breadth_first_graph_search(ninja_env, verbose=True)

# Display results
if solution:
    actions, cost = solution
    print("Solution found!")
    print("Actions:", actions)
    print("Total Cost:", cost)
    
   
     # This will show the final state of the line
else:
    print("No solution found.")

print("Max Frontier Size:", max_frontier)
