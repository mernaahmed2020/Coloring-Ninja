from tabulate import tabulate
import time
from IDS import iterative_deepening_search
from BFS import breadth_first_graph_search
from search_algorithm import run_ids_algorithm, run_bfs_algorithm
from environment import coloringNinja

def measure_performance(search_algorithm, problem, verbose=False):
    """
    Wrapper function to measure the time and space performance of a search algorithm.
    """
    # Start measuring time
    start_time = time.time()

    # Run the search algorithm, capturing the solution and max frontier size
    solution_result = search_algorithm(problem, verbose=verbose)

    # Measure elapsed time
    elapsed_time = time.time() - start_time

    # Unpack the result depending on the search algorithm's return format
    if isinstance(solution_result, tuple):
        # Unpack the tuple result from iterative_deepening_search or other search algorithms returning tuples
        solution_path, total_cost, explored, depth_limit = solution_result
        max_frontier_size = explored  # Calculate max frontier size from explored nodes
    else:
        # Handle cases where the result is a dictionary (e.g., from BFS, DFS)
        solution_path = solution_result.get("actions", None)
        total_cost = solution_result.get("total_cost", 0)
        max_frontier_size = solution_result.get("max_frontier", 0)

    return {
        'solution': solution_path,
        'cost': total_cost,
        'elapsed_time': elapsed_time,
        'max_frontier_size': max_frontier_size
    }

def print_comparison_table(performance_data):
    """
    Prints a comparison table for the performance of search algorithms.
    """
    headers = ["Algorithm", "Solution", "Cost", "Time (seconds)", "Max Frontier Size"]
    
    # Prepare the data for the table
    table_data = []
    for algorithm, data in performance_data.items():
        solution = ', '.join(data['solution']) if data['solution'] else "No solution found"
        table_data.append([algorithm, solution, data['cost'], f"{data['elapsed_time']:.4f}", data['max_frontier_size']])

    print(tabulate(table_data, headers=headers, tablefmt='grid'))