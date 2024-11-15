from environment import coloringNinja
from Node import Node

def iterative_deepening_search(environment, max_depth=float('inf'), verbose=False):
    """
    Implements IDS for the coloringNinja environment using the Node class.
    """
    if max_depth == float('inf'):
        max_depth = 1000 
    for depth_limit in range(1, max_depth + 1):  # Increment depth limit from 1 to max_depth
        print(f"Depth limit: {depth_limit}")  # Optionally print depth limit
        result, explored = depth_limited_search(environment, depth_limit, verbose)
        if result is not None:
            return result,explored,depth_limit  # Return result if goal is found

    return None, 0,0 # Return None if no solution found within max_depth

def depth_limited_search(environment, depth_limit, verbose=False):
    """
    Performs a depth-limited search (DFS with depth limit) on the coloringNinja environment.
    """
    root = Node.root(environment)  # Get the full state including palette

    if root.state[:len(environment.line)] == environment.goalState:
        return solution(root), 1  # Return solution if the initial state is the goal

    frontier = [(root, 0)]  # Initialize the frontier with the root node (node, depth)
    explored = set()  # To track explored states
    max_frontier = len(frontier)  # Track maximum frontier size

    if verbose:
        print(f"Initial Frontier: {[node.state for node, _ in frontier]}")

    while frontier:
        node, depth = frontier.pop()  # Pop the last node and its depth from the stack
        
        if depth > depth_limit:  # Skip nodes deeper than the current depth limit
            continue

        # Convert state to a hashable type before adding to explored
        explored.add(tuple(node.state))  # Use tuple for immutability

        # Expand the node by iterating over possible actions
        for action in ["color", "move left", "move right"]:
            child = Node.child(environment, node, action)

            # Convert child state to tuple for comparison
            if tuple(child.state) not in explored and (child, depth + 1) not in frontier:
                if child.state[:len(environment.line)] == environment.goalState:  # Goal test
                    print("final line:")
                    print(child.state[:len(environment.line)])
                    return solution(child), len(explored)  # Return solution and stats

                frontier.append((child, depth + 1))  # Add child to the frontier with incremented depth
                
        max_frontier = max(max_frontier, len(frontier))

        if verbose:
            print(f"Frontier: {[node.state for node, _ in frontier]}")
            print(f"Explored: {explored}")

    return None, len(explored) # No solution found

def solution(node):
    """
    Backtracks from the goal node to root to generate the solution path and cost.
    """
    actions = []
    current_node = node
    while current_node.parent is not None:
        actions.append(current_node.action)  # Add the action that led to the current node
        current_node = current_node.parent
    actions.reverse()  # Reverse the list to get the actions from root to goal
    return actions, current_node.path_cost,
