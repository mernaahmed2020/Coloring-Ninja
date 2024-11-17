import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
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

def depth_first_graph_search(environment, verbose=False):
    """
    Implements DFS for the coloringNinja environment and returns the solution.
    """
    root = Node.root(environment)  # Initialize with full state, including palette and savings.

    # Initialize the search tree graph
    G = nx.DiGraph()  # Directed graph for search tree

    # Check if the root node meets the goal condition
    if root.state[:len(environment.line)] == environment.goalState:
        return {"goal_state": root.state[:len(environment.line)], "actions": [], "total_steps": 0, "max_frontier": 1}

    frontier = [root]  # Initialize the frontier with a stack
    explored = set()  # Track explored states
    max_frontier_size = 1  # Track the maximum frontier size

    if verbose:
        print(f"Initial Frontier: {[node.state for node in frontier]}")

    while frontier:
        node = frontier.pop()  # Pop the last node (LIFO)
        explored.add(tuple(node.state))  # Add the current state to the explored set

        # Add the current node and its state to the graph G
        G.add_node(tuple(node.state))
        if node.parent:
            G.add_edge(tuple(node.parent.state), tuple(node.state), action=node.action)

        # Update the environment state from the current node
        environment.line = list(node.state[:len(environment.line)])
        environment.agentPosition = node.state[len(environment.line)]
        environment.savings = node.state[len(environment.line) + 1]
        environment.paletteQuantity = dict(node.state[len(environment.line)+2])

        # Print the current state of the environment
        print("Current Line State:")
        environment.displayLineState()

        # Check if the agent can purchase any palettes (if savings allow)
        for color in environment.paletteQuantity:
            if environment.paletteQuantity[color] == 0 and environment.savings >= environment.paletteCost:  # Palette cost is environment.paletteCost
                # Update palette quantity to 2 if savings are enough
                environment.paletteQuantity[color] = 2
                environment.savings -= environment.paletteCost  # Deduct the palette cost from savings
                print(f"Purchased {color} palette, new palette quantities: {environment.paletteQuantity}")
        
        # Update points and savings
        points = environment.points  # Assuming you update points based on the agent's actions
        print(f"Updated Points: {points}, Savings: {environment.savings}")
        
        # Expand the node by iterating over possible actions
        for action in ["color", "skip", "move left", "move right"]:
            child = Node.child(environment, node, action)

            # Convert state to tuple for exploration tracking
            child_state_tuple = tuple(child.state)

            # Check if the child state is new
            if child_state_tuple not in explored and child not in frontier:
                # Check if the child is the goal
                if child.state[:len(environment.line)] == environment.goalState:
                    if verbose:
                        print("Goal state reached:")
                        print(child.state[:len(environment.line)])

                    # Extract the solution (actions and cost)
                    actions, total_steps = solution(child)

                    # Draw the search tree after finding the solution
                    draw_search_tree(G)

                    # Return the result including the goal state
                    return {
                        "goal_state": child.state[:len(environment.line)],  # Add the goal state here
                        "actions": actions,
                        "total_steps": total_steps,
                        "max_frontier": max_frontier_size
                    }

                # Add the child to the frontier (stack)
                frontier.append(child)

        # Update the maximum frontier size
        max_frontier_size = max(max_frontier_size, len(frontier))

        if verbose:
            print(f"Frontier: {[node.state for node in frontier]}")

    # Return when no solution is found
    return {"goal_state": None, "actions": None, "total_cost": None, "max_frontier": max_frontier_size}

def solution(node):
    """
    Constructs the path of actions and calculates the total cost from the root to the goal state.
    """
    actions = []  # To store the sequence of actions

    # Traverse back to the root from the goal node
    while node.parent is not None:
        actions.append(node.action)  # Append the action leading to this node
        node = node.parent

    actions.reverse()  # Reverse to get the correct order
    total_steps = len(actions)
    return actions, total_steps


# Example usage
# environment = coloringNinja(lineSize=3)
# result = depth_first_graph_search(environment, verbose=True)

# Note: The search tree will be drawn after finding a solution, or when the search ends.
