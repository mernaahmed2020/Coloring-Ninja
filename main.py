from environment import coloringNinja
from Node import Node
from BFS import breadth_first_graph_search
from DFS import depth_first_graph_search
from IDS import iterative_deepening_search
from UCS import uniform_cost_search
from Heuristic import Heuristic
from Greedy import greedy_best_first_search
from Astar import a_star_search


# # # Initialize the environment
# # ninja_env = coloringNinja(lineSize=6)

# # # Create the root node from the environment instance
# # root = Node.root(ninja_env)

# # # Run IDS (Iterative Deepening Search)
# # actions, explored, max_depth = iterative_deepening_search(ninja_env, verbose=True)

# # # Display results
# # if actions is not None:  # Checking if a solution was found
# #     print("Solution found!")
# #     print("Actions:", actions)
# #    # Assuming cost is calculated somewhere in your code
# # else:
# #     print("No solution found.")

# # # Print the maximum frontier size encountered
# # print("Max Frontier Size:", max_depth)
# from environment import coloringNinja
# from Node import Node
# from BFS import breadth_first_graph_search

# # Initialize the environment
# ninja_env = coloringNinja(lineSize=7)

# # Create the root node from the environment instance
# root = Node.root(ninja_env)


# # Run BFS
# #result = depth_first_graph_search(ninja_env, verbose=True)

# # result=uniform_cost_search(ninja_env, verbose=True)

# # # Display results
# # if result["actions"] is not None:
# #     actions = result.get("actions")
# #     cost = result.get("total_cost")
# #     print("Solution found!")
# #     print("Actions:", actions)
# #     print("Total Cost:", cost)
   

# # else:
# #     print("No solution found.")

# # print("Max Frontier Size:", result["max_frontier"])

# actions, total_cost, max_frontier_size = uniform_cost_search(ninja_env)

# # Check if actions are found (solution exists)
# if actions is not None:
#     # print("Solution found!")
#     # print("Actions:", actions)
#     # print("Total Cost:", total_cost)
#     print(ninja_env.getState())
# else:
#     print("No solution found.")

# # Always print the maximum frontier size tracked during the search
# # print("Max Frontier Size:", max_frontier_size)
#environment = coloringNinja()

# Run Uniform Cost Search
# result = uniform_cost_search(ninja_env)

# # Print the results
# print(f"Actions: {result['actions']}")
# print(f"Total Cost: {result['total_cost']}")
# print(f"Maximum Frontier Size: {result['max_frontier']}")


#🔴🔴   🔴🔴 🔴🔴   🔴🔴 

ninja_env1 = coloringNinja(lineSize=6)
ninja_env2 = coloringNinja(lineSize=6)

heuristic1 = Heuristic(ninja_env1)
heuristic2 = Heuristic(ninja_env2)

#===============================================


#🔴🔴 FOR GREEDY 🔴🔴 



# def display_results(result, heuristic_type):
#     if result['actions'] is None:
#         print(f"Heuristic {heuristic_type} - No solution found.")
#     else:
#         print(f"Heuristic {heuristic_type} - Solution found!")
#         print(f"Actions taken: {result['actions']}")
#         print(f"Total cost: {result['total_cost']}")
#         print(f"Maximum frontier size during search: {result['max_frontier']}")

# # Run with Heuristic 1
# result_heuristic_1 = greedy_best_first_search(ninja_env1, heuristic1, heuristic_type=1)
# display_results(result_heuristic_1, heuristic_type=1)

# # Run with Heuristic 2
# result_heuristic_2 = greedy_best_first_search(ninja_env2, heuristic2, heuristic_type=2)
# display_results(result_heuristic_2, heuristic_type=2)



#🔴🔴 FOR A* 🔴🔴 

# Run A* Search with Heuristic 1
result_a_star_1 = a_star_search(ninja_env1, heuristic1, heuristic_type=1)

# Display results for A* Search with Heuristic 1
if result_a_star_1['actions'] is None:
    print("A* Heuristic 1 - No solution found.")
else:
    print("A* Heuristic 1 - Solution found!")
    print(f"Actions taken: {result_a_star_1['actions']}")
    print(f"Total cost: {result_a_star_1['total_cost']}")
    print(f"Maximum frontier size during search: {result_a_star_1['max_frontier']}")

# Run A* Search with Heuristic 2
result_a_star_2 = a_star_search(ninja_env2, heuristic2, heuristic_type=2)

# Display results for A* Search with Heuristic 2
if result_a_star_2['actions'] is None:
    print("A* Heuristic 2 - No solution found.")
else:
    print("A* Heuristic 2 - Solution found!")
    print(f"Actions taken: {result_a_star_2['actions']}")
    print(f"Total cost: {result_a_star_2['total_cost']}")
    print(f"Maximum frontier size during search: {result_a_star_2['max_frontier']}")
