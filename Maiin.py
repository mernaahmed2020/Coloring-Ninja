from environment import coloringNinja
from Node import Node
from BFS import breadth_first_graph_search
from DFS import depth_first_graph_search
from IDS import iterative_deepening_search
from UCS import uniform_cost_search
from Heuristic import Heuristic
from Greedy import greedy_best_first_search
from Astar import a_star_search
from HillClimbing import *
from simAnealing import *
from search_algorithm import *
import time
import psutil
import os

#======================== run ================================
def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024  

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
        
        total_cost = result.get("total_cost", "N/A")  
        print(f"Total Cost: {total_cost}")  

            
        print("==============================================================================================")
        
print_algorithm_summary(algorithm_results) 


 

print("==============================================================================================")



 

result_node, result_score, elapsed_time, memory_used = run_simulated_annealing()

print("==============================================================================================")


result_node, result_score, elapsed_time, memory_used = run_hill_climbing()








  