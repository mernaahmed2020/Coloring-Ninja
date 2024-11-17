import networkx as nx
import matplotlib.pyplot as plt
from environment import coloringNinja
from Node import Node

# def draw_search_tree(G):
#     pos = nx.spectral_layout(G)  # Using the spectral layout for node positioning
#     plt.figure(figsize=(12, 8))
#     nx.draw(G, pos, with_labels=True, node_size=2000, node_color="pink", font_size=10, font_weight="bold", edge_color="gray")
#     edge_labels = nx.get_edge_attributes(G, 'action')
#     nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
#     plt.title("Search Tree")
#     plt.show()

def iterative_deepening_search(environment, max_depth=float('inf'), verbose=False):
    """
    Implements IDS for the coloringNinja environment using the Node class.
    """
    if max_depth == float('inf'):
        max_depth = 50 
    
   
    # G = nx.DiGraph()  # Directed graph for search tree
    
    for depth_limit in range(1, max_depth + 1):  
        if verbose:
            print(f"Depth limit: {depth_limit}")
        
        result, explored, max_frontier = depth_limited_search(environment, depth_limit, verbose)
        if result is not None:
            actions, total_steps = result
            return {
                "goal_state": environment.goalState,
                "actions": result[0],
                "total_steps": total_steps,
                "max_frontier": max_frontier,
                "depth_limit_reached": depth_limit,
            }
    
  
    return {
        "goal_state": None,
        "actions": None,
        "total_steps": None,
        "max_frontier": 0,
        "depth_limit_reached": max_depth,
    }


def depth_limited_search(environment, depth_limit, verbose=False, G=None):
    root = Node.root(environment) 

    if root.state[:len(environment.line)] == environment.goalState:
        return solution(root), 1, 1

    frontier = [(root, 0)]  
    explored = set() 
    max_frontier = len(frontier)  

    if verbose:
        print(f"Initial Frontier: {[node.state for node, _ in frontier]}")

    while frontier:
        node, depth = frontier.pop()
        
        if depth > depth_limit:
            continue  

        explored.add(tuple(node.state))  
       
        # G.add_node(tuple(node.state))
        # if node.parent:
        #     G.add_edge(tuple(node.parent.state), tuple(node.state), action=node.action)

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

    return None, len(explored), max_frontier  

def solution(node):
    """
    Backtracks from the goal node to root to generate the solution path and cost.
    """
    actions = []
    current_node = node

    while current_node.parent is not None:
        actions.append(current_node.action)
        current_node = current_node.parent
    
    actions.reverse()  
    total_steps = len(actions)
    return actions, total_steps
# environment = coloringNinja(lineSize=2)
# result = iterative_deepening_search(environment, verbose=True)