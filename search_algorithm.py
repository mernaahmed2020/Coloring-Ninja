from IDS import iterative_deepening_search
from environment import coloringNinja
from BFS import breadth_first_graph_search
from DFS import depth_first_graph_search
from Astar import a_star_search
from Greedy import greedy_best_first_search
from UCS import uniform_cost_search
import time
import psutil
import os
from Heuristic import *


def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024  




def run_ids_algorithm():
   

    ninja_env = coloringNinja(lineSize=6) 

   
    print("\nRun IDS ")
    
    before_memory = get_memory_usage()
    start_time = time.time()
    
    ids_result = iterative_deepening_search(ninja_env, verbose=False)
    
    elapsed_time = time.time() - start_time
    after_memory = get_memory_usage()  
    memory_used = after_memory - before_memory
    
    if ids_result is not None:
        print("IDS Solution found!")
        print("Actions:", ids_result.get("actions"))
        print("Goal State:", ids_result.get("goal_state"))  
        print("Max Frontier Size:", ids_result.get("max_frontier")) 
    else:
        print("IDS No solution found.")

    return ids_result,elapsed_time,memory_used

def run_bfs_algorithm():
    ninja_env = coloringNinja(lineSize=6)  
    print("\nRun BFS")
    before_memory = get_memory_usage()
    start_time = time.time()    
    bfs_result = breadth_first_graph_search(ninja_env, verbose=False)
    elapsed_time = time.time() - start_time
    after_memory = get_memory_usage()  
    memory_used = after_memory - before_memory    

    if bfs_result is not None:
        print("BFS Solution found!")
        print("Actions:", bfs_result.get("actions")) 
        print("Goal State:", bfs_result.get("goal_state")) 
        print("Max Frontier Size:", bfs_result.get("max_frontier")) 
    else:
        print("BFS No solution found.")

    return bfs_result,elapsed_time,memory_used

def run_dfs_algorithm():
 
   
    ninja_env = coloringNinja(lineSize=6) 

    
    print("\nRun DFS ")
    
    before_memory = get_memory_usage()
    start_time = time.time()   
    dfs_result = depth_first_graph_search(ninja_env, verbose=False)
    elapsed_time = time.time() - start_time
    after_memory = get_memory_usage()  
    memory_used = after_memory - before_memory

    if dfs_result is not None:
        print("DFS Solution found!")
        print("Actions:", dfs_result.get("actions"))  
        print("Goal State:", dfs_result.get("goal_state")) 
        print("Max Frontier Size:", dfs_result.get("max_frontier")) 
    else:
        print("DFS No solution found.")

    return dfs_result,elapsed_time,memory_used



def run_ucs_algorithm():
   
  
    ninja_env = coloringNinja(lineSize=6) 
    print("\nRun UCS ")
    before_memory = get_memory_usage()
    start_time = time.time()   
    ucs_result = uniform_cost_search(ninja_env, verbose=False)
    elapsed_time = time.time() - start_time
    after_memory = get_memory_usage()  
    memory_used = after_memory - before_memory
    
    

    if isinstance(ucs_result, dict): 
        print("UCS Solution found!")
        print("Actions:", ucs_result.get("actions")) 
        print("Total cost:", ucs_result.get("total_cost"))   
        print("Goal State:", ucs_result.get("goal_state")) 
        print("Max Frontier Size:", ucs_result.get("max_frontier"))  
    else:
        print("UCS No solution found.")
    
        print(f"Error: {ucs_result}")    

    return ucs_result,elapsed_time,memory_used








def run_a_star1():
    
   
    ninja_env1 = coloringNinja(lineSize=6)  
    heuristic1 = Heuristic(ninja_env1)

    print("\nRun A* with Heuristic 1")
    before_memory1 = get_memory_usage()
    start_time1 = time.time()

    result_a_star1 = a_star_search(ninja_env1, heuristic1, heuristic_type=1)

    elapsed_time1 = time.time() - start_time1
    after_memory1 = get_memory_usage()  
    memory_used1 = after_memory1 - before_memory1

  
    if result_a_star1['actions'] is None:
        print("A* Heuristic 1 - No solution found.")
    else:
        print("A* Heuristic 1 - Solution found!")
        print(f"Actions taken: {result_a_star1['actions']}")
        print(f"Total cost: {result_a_star1['total_cost']}")
        print(f"Maximum frontier size during search: {result_a_star1['max_frontier']}")

    print(f"A* Heuristic 1 - Time: {elapsed_time1:.3f} seconds")
    print(f"A* Heuristic 1 - Memory used: {memory_used1:.2f} MB")

    return result_a_star1, memory_used1, elapsed_time1


def run_a_star2():

   
    ninja_env2 = coloringNinja(lineSize=6) 
    heuristic2 = Heuristic(ninja_env2)

    print("\nRun A* with Heuristic 2")
    before_memory2 = get_memory_usage()
    start_time2 = time.time()

    result_a_star2 = a_star_search(ninja_env2, heuristic2, heuristic_type=2)

    elapsed_time2 = time.time() - start_time2
    after_memory2 = get_memory_usage()  
    memory_used2 = after_memory2 - before_memory2
    if result_a_star2['actions'] is None:
        print("A* Heuristic 2 - No solution found.")
    else:
        print("A* Heuristic 2 - Solution found!")
        print(f"Actions taken: {result_a_star2['actions']}")
        print(f"Total cost: {result_a_star2['total_cost']}")
        print(f"Maximum frontier size during search: {result_a_star2['max_frontier']}")

    print(f"A* Heuristic 2 - Time: {elapsed_time2:.3f} seconds")
    print(f"A* Heuristic 2 - Memory used: {memory_used2:.2f} MB")

    return result_a_star2, memory_used2, elapsed_time2

def run_greedy_algorithm1():
    """
    Runs the Greedy algorithm with Heuristic 1 and returns results along with performance metrics.
    """
    ninja_env1 = coloringNinja(lineSize=6) 
    heuristic1 = Heuristic(ninja_env1)

    print("\nRun Greedy with Heuristic 1")
    before_memory = get_memory_usage()
    start_time = time.time()

    result_greedy1 = greedy_best_first_search(ninja_env1, heuristic1, heuristic_type=1)

    elapsed_time = time.time() - start_time
    after_memory = get_memory_usage()
    memory_used = after_memory - before_memory

    if result_greedy1['actions'] is None:
        print("Greedy Heuristic 1 - No solution found.")
    else:
        print("Greedy Heuristic 1 - Solution found!")
        print(f"Actions taken: {result_greedy1['actions']}")
        print(f"Total cost: {result_greedy1['total_cost']}")
        print(f"Maximum frontier size during search: {result_greedy1['max_frontier']}")

    print(f"Greedy Heuristic 1 - Time: {elapsed_time:.3f} seconds")
    print(f"Greedy Heuristic 1 - Memory used: {memory_used:.2f} MB")

    return result_greedy1, elapsed_time, memory_used


def run_greedy_algorithm2():
    ninja_env2 = coloringNinja(lineSize=6)  
    heuristic2 = Heuristic(ninja_env2)

    print("\nRun Greedy with Heuristic 2.")
    before_memory = get_memory_usage()
    start_time = time.time()

    result_greedy2 = greedy_best_first_search(ninja_env2, heuristic2, heuristic_type=2)

    elapsed_time = time.time() - start_time
    after_memory = get_memory_usage()
    memory_used = after_memory - before_memory

    if result_greedy2['actions'] is None:
        print("Greedy Heuristic 2 - No solution found.")
    else:
        print("Greedy Heuristic 2 - Solution found!")
        print(f"Actions taken: {result_greedy2['actions']}")
        print(f"Total cost: {result_greedy2['total_cost']}")
        print(f"Maximum frontier size during search: {result_greedy2['max_frontier']}")

    print(f"Greedy Heuristic 2 - Time: {elapsed_time:.3f} seconds")
    print(f"Greedy Heuristic 2 - Memory used: {memory_used:.2f} MB")

    return result_greedy2, elapsed_time, memory_used
