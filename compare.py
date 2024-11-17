# from tabulate import tabulate
# import time
# from IDS import iterative_deepening_search
# from BFS import breadth_first_graph_search
# from search_algorithm import run_ids_algorithm, run_bfs_algorithm
# from environment import coloringNinja

# def measure_performance(search_algorithm, problem, verbose=False):

#     start_time = time.time()
#     solution_result = search_algorithm(problem, verbose=verbose)

   
#     elapsed_time = time.time() - start_time

#     if isinstance(solution_result, tuple):
#         solution_path, total_cost, explored, depth_limit = solution_result
#         max_frontier_size = explored 
#     else:
#         solution_path = solution_result.get("actions", None)
#         total_cost = solution_result.get("total_cost", 0)
#         max_frontier_size = solution_result.get("max_frontier", 0)

#     return {
#         'solution': solution_path,
#         'cost': total_cost,
#         'elapsed_time': elapsed_time,
#         'max_frontier_size': max_frontier_size
#     }

# def print_comparison_table(performance_data):
#     """
#     Prints a comparison table for the performance of search algorithms.
#     """
#     headers = ["Algorithm", "Solution", "Cost", "Time (seconds)", "Max Frontier Size"]
    
#     table_data = []
#     for algorithm, data in performance_data.items():
#         solution = ', '.join(data['solution']) if data['solution'] else "No solution found"
#         table_data.append([algorithm, solution, data['cost'], f"{data['elapsed_time']:.4f}", data['max_frontier_size']])

#     print(tabulate(table_data, headers=headers, tablefmt='grid'))