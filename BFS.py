from collections import deque
from environment import coloringNinja
from Node import Node

def breadth_first_graph_search(environment, verbose=False):
    """
    Implements BFS for the coloringNinja environment using the Node class.
    """
    root = Node.root(environment)  # Now, it gets the full state including palette

    if root.state[:len(environment.line)] == environment.goalState:
        return solution(root), 1

    frontier = deque([root])  # Initialize the frontier with the root node
    explored = set()  # To track explored states
    max_frontier_size = 1  # To track maximum frontier size

    if verbose:
        print(f"Initial Frontier: {[node.state for node in frontier]}")

    while frontier:
        node = frontier.popleft()  # Dequeue the first node
        
        # Convert state to a hashable type before adding to explored
        explored.add(tuple(node.state))  # Use tuple for immutability

        # Expand the node by iterating over possible actions
        for action in ["color", "move left", "move right"]:
            child = Node.child(environment, node, action)

            # Convert child state to tuple for comparison
            if tuple(child.state) not in explored and child not in frontier:
                if child.state[:len(environment.line)] == environment.goalState:  # Goal test
                    print("final line:")
                    print(child.state[:len(environment.line)])
                    return solution(child), max_frontier_size  # Return solution and stats
                frontier.append(child)  # Add child to the frontier

        max_frontier_size = max(max_frontier_size, len(frontier))

        if verbose:
            print(f"Frontier: {[node.state for node in frontier]}")
            print(f"Explored: {explored}")

    return None, max_frontier_size  # No solution found
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

