from environment import coloringNinja
from Node import Node
from BFS import breadth_first_graph_search
from DFS import depth_first_graph_search
from IDS import iterative_deepening_search
from UCS import uniform_cost_search
from Heuristic import Heuristic
from Greedy import greedy_best_first_search
from Astar import a_star_search
from compare import print_comparison_table, measure_performance
from search_algorithm import *
import time
import psutil
import os

#======================== run ================================


algorithms = [("DFS", run_dfs_algorithm), ("BFS", run_bfs_algorithm),("IDS", run_ids_algorithm),("UCS",run_ucs_algorithm),("Greedy with H1",run_greedy_algorithm1),("Greedy with H2",run_greedy_algorithm2),("A*1",run_a_star1),("A*2",run_a_star2)]
algorithm_results=[]
for name, algorithm in algorithms:

     
    result,elapsed_time, memory_used = algorithm() 
    
    
    if result is not None:
    

    
        goal_state = result.get("goal_state")
        actions = result["actions"]
        max_frontier = result["max_frontier"]
        
        total_cost = result.get("total_cost", None) if name in ["UCS", "Greedy with H1","Greedy with H2", "A*1","A*2"] else None



        algorithm_results.append({
            "name": name,
            "goal_state": goal_state,
            "actions": actions,
            "max_frontier": max_frontier,
            "time": elapsed_time,
            "memory_used":memory_used,
            "total_cost":total_cost
        })
        
        
    else:
       print(f"{name} found no solution.")
       

def print_algorithm_summary(algorithm_results):
    for result in algorithm_results:
        print("==============================================================================================")
        print(f"{result['name']} Solution found!")
        print(f"Goal state reached:\n{result['goal_state']}")
        print(f"Actions: {result['actions']}")
        print(f"Max Frontier Size: {result['max_frontier']}")
        print(f"{result['name']} time: {result['time']:.3f} sec")
        print(f"{result['name']} memory_used: {result['memory_used']:.2f} MB")
        
        total_cost = result.get("total_cost", "N/A")  # Handle missing cost with a default value
        print(f"Total Cost: {total_cost}")  # This will handle missing total_cost properly

            
        print("==============================================================================================")
        
print_algorithm_summary(algorithm_results) 



# performance_data = {}
# if dfs_result is not None:
#         # dfs_performance = measure_performance(depth_first_graph_search, ninja_env_dfs, verbose=True)
#         performance_data['DFS'] = dfs_performance

#     #  print_comparison_table(performance_data)
# if result["actions"] is not None:
#     print("Solution found!")
#     print("Actions:", result["actions"])
  
# else:
#     print("No solution found.")
# print("Maximum Frontier Size:", result["max_frontier"])

  