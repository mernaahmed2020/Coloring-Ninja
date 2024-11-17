import networkx as nx
import matplotlib.pyplot as plt
from heapq import heappop, heappush
from copy import deepcopy
from environment import coloringNinja
from Node import Node
from Heuristic import Heuristic

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

def a_star_search(environment, heuristic, heuristic_type=1, verbose=True):
    """
    Implements A* Search for the coloringNinja environment and returns the solution.
    """
    root = Node.root(environment)  # Initialize with the full state, including palette and savings.

    # Initialize the search tree graph
    G = nx.DiGraph()  # Directed graph for search tree

    # Add root node to the graph
    G.add_node(tuple(root.state), cost=root.path_cost, heuristic=root.heuristic)

    # Check if the root node already meets the goal condition
    if root.state[:len(environment.line)] == environment.goalState:
        draw_search_tree(G)
        return {"actions": [], "total_cost": 0, "max_frontier": 1}

    frontier = []  # Priority Queue for A* (min-heap)
    root_h = heuristic.calculate(root, heuristic_type)
    root.heuristic = root_h
    heappush(frontier, (root.path_cost + root_h, root))  # f(n) = g(n) + h(n)
    explored = set()  # Track explored states
    max_frontier_size = 1  # Track the maximum frontier size

    while frontier:
        _, node = heappop(frontier)
        node_state_tuple = tuple(node.state)
        explored.add(node_state_tuple)  # Add the current state to the explored set

        # Update the environment state from the current node
        environment.line = list(node.state[:len(environment.line)])
        environment.agentPosition = node.state[len(environment.line)]
        environment.savings = node.state[len(environment.line) + 1]
        environment.paletteQuantity = dict(node.state[len(environment.line) + 2])

        # Expand the node by generating actions based on the environment
        for action in ["color", "skip", "move left", "move right"]:  # Added 'skip' as an action
            child = Node.child(deepcopy(environment), node, action)  # Create child node directly from action
            child_state_tuple = tuple(child.state)

            # Add child node and edge to the graph
            G.add_node(child_state_tuple, cost=child.path_cost, heuristic=child.heuristic)
            G.add_edge(node_state_tuple, child_state_tuple, action=action)

            if child_state_tuple not in explored and not any(child_state_tuple == item[1].state for item in frontier):
                # Check if the child is the goal
                if child.state[:len(environment.line)] == environment.goalState:
                    solution_result = solution(child)  # Call solution()

                    # Draw the search tree
                    draw_search_tree(G)

                    if solution_result:  # Check if solution_result is not None
                        actions, total_cost = solution_result
                        return {
                            "goal_state": environment.goalState,
                            "actions": actions,
                            "max_frontier": max_frontier_size,
                            "total_cost": total_cost
                        }

                # Add the child to the frontier with its f(n) = g(n) + h(n)
                child_h = heuristic.calculate(child, heuristic_type)
                child.heuristic = child_h
                heappush(frontier, (child.path_cost + child_h, child))

        # Update the maximum frontier size
        max_frontier_size = max(max_frontier_size, len(frontier))  # Track the max size of frontier

    # Draw the search tree even if no solution is found
    draw_search_tree(G)

    # Return failure if no solution is found
    return {"actions": None, "total_cost": float('inf'), "max_frontier": max_frontier_size, "goal_state": environment.goalState}

def solution(node):
    actions = []
    total_cost = 0

    while node.parent is not None:
        actions.append(node.action)
        total_cost += (node.path_cost + node.heuristic)
        node = node.parent

    actions.reverse()

    if actions and total_cost >= 0:
        return actions, total_cost
    return None  # Return None if the solution is invalid or empty

# Example usage
# environment = coloringNinja(lineSize=2)
# heuristic = Heuristic(environment)

# a_star_search(environment, heuristic, heuristic_type=2, verbose=True)
