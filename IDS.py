import networkx as nx
import matplotlib.pyplot as plt
from environment import coloringNinja
from Node import Node

def draw_search_tree(G):
    """
    Draw the search tree using a spectral layout.
    """
    pos = nx.spectral_layout(G)  # Using the spectral layout for node positioning
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="pink", font_size=10, font_weight="bold", edge_color="gray")
    edge_labels = nx.get_edge_attributes(G, 'action')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Search Tree")
    plt.show()

def iterative_deepening_search(environment, max_depth=float('inf'), verbose=False):
    """
    Implements IDS for the coloringNinja environment using the Node class.
    """
    if max_depth == float('inf'):
        max_depth = 50  # Default maximum depth if not specified
    
    # Initialize the search tree graph
    G = nx.DiGraph()  # Directed graph for search tree
    
    for depth_limit in range(1, max_depth + 1):  # Increment depth limit from 1 to max_depth
        if verbose:
            print(f"Depth limit: {depth_limit}")
        
        result, explored, max_frontier = depth_limited_search(environment, depth_limit, verbose, G)
        if result is not None:
            actions, total_steps = result
            # Draw the search tree after finding the solution
            draw_search_tree(G)
            return {
                "goal_state": environment.goalState,
                "actions": result[0],
                "total_steps": total_steps,
                "max_frontier": max_frontier,
                "depth_limit_reached": depth_limit,
            }
    
    # No solution found within the depth limit
    return {
        "goal_state": None,
        "actions": None,
        "total_steps": None,
        "max_frontier": 0,
        "depth_limit_reached": max_depth,
    }


def depth_limited_search(environment, depth_limit, verbose=False, G=None):
    """
    Performs a depth-limited search (DFS with depth limit) on the coloringNinja environment.
    """
    root = Node.root(environment)  # Get the initial state including palette

    if root.state[:len(environment.line)] == environment.goalState:
        return solution(root), 1, 1  # Solution found at the root, frontier size is 1

    frontier = [(root, 0)]  # Stack with (node, depth)
    explored = set()  # Track explored states
    max_frontier = len(frontier)  # Track maximum frontier size

    if verbose:
        print(f"Initial Frontier: {[node.state for node, _ in frontier]}")

    while frontier:
        node, depth = frontier.pop()  # Pop the last node and its depth
        
        if depth > depth_limit:
            continue  # Skip nodes deeper than the depth limit

        explored.add(tuple(node.state))  # Add state to explored set

        # Add the current node and its state to the graph G
        G.add_node(tuple(node.state))
        if node.parent:
            G.add_edge(tuple(node.parent.state), tuple(node.state), action=node.action)

        for action in ["color", "move left", "move right"]:
            child = Node.child(environment, node, action)

            if tuple(child.state) not in explored and (child, depth + 1) not in frontier:
                if child.state[:len(environment.line)] == environment.goalState:
                    if verbose:
                        print("Final line:", child.state[:len(environment.line)])
                    return solution(child), len(explored), max_frontier

                frontier.append((child, depth + 1))
                max_frontier = max(max_frontier, len(frontier))

        if verbose:
            print(f"Frontier: {[node.state for node, _ in frontier]}") 
            print(f"Explored: {len(explored)} states")

    return None, len(explored), max_frontier  # No solution found

def solution(node):
    """
    Backtracks from the goal node to root to generate the solution path and cost.
    """
    actions = []
    current_node = node

    while current_node.parent is not None:
        actions.append(current_node.action)
        current_node = current_node.parent
    
    actions.reverse()  # Reverse the list to show actions from root to goal
    total_steps = len(actions)
    return actions, total_steps
# environment = coloringNinja(lineSize=2)
# result = iterative_deepening_search(environment, verbose=True)