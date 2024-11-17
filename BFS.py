import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
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

def breadth_first_graph_search(environment, verbose=False):
    
    root = Node.root(environment) 

    
    # G = nx.DiGraph()  # Directed graph for search tree

   
    if root.state[:len(environment.line)] == environment.goalState:
        return {"actions": [], "total_steps": 0, "max_frontier": 1}

    frontier = deque([root]) 
    explored = set() 
    max_frontier_size = 1  

    if verbose:
        print(f"Initial Frontier: {[node.state for node in frontier]}")

    while frontier:
        node = frontier.popleft() 
        explored.add(tuple(node.state))  

       
        # G.add_node(tuple(node.state))
        # if node.parent:
        #     G.add_edge(tuple(node.parent.state), tuple(node.state), action=node.action)

       
        environment.line = list(node.state[:len(environment.line)])
        environment.agentPosition = node.state[len(environment.line)]
        environment.savings = node.state[len(environment.line) + 1]
        environment.paletteQuantity = dict(node.state[len(environment.line)+2])

       
        print("Current Line State:")
        environment.displayLineState()

        for color in environment.paletteQuantity:
            if environment.paletteQuantity[color] == 0 and environment.savings >= environment.paletteCost:  
                
                environment.paletteQuantity[color] = 2
                environment.savings -= environment.paletteCost  
                print(f"Purchased {color} palette, new palette quantities: {environment.paletteQuantity}")
        
       
        points = environment.points 
        print(f"Updated Points: {points}, Savings: {environment.savings}")
        
       
        for action in ["color", "skip", "move left", "move right"]:
            child = Node.child(environment, node, action)

           
            child_state_tuple = tuple(child.state)

        
            if child_state_tuple not in explored and child not in frontier:
               
                if child.state[:len(environment.line)] == environment.goalState:
                    if verbose:
                        print("Goal state reached:")
                        print(child.state[:len(environment.line)])
                    
                   
                    actions, total_steps = solution(child)

                    
                    # draw_search_tree(G)

                    return {
                        "goal_state": child.state[:len(environment.line)],
                        "actions": actions,
                        "total_steps": total_steps,
                        "max_frontier": max_frontier_size,
                    }

                frontier.append(child)

        
        max_frontier_size = max(max_frontier_size, len(frontier))

        if verbose:
            print(f"Frontier: {[node.state for node in frontier]}")

   
    return {"actions": None, "total_cost": None, "max_frontier": max_frontier_size}

def solution(node):
    actions = [] 

    
    while node.parent is not None:
        actions.append(node.action)  
        node = node.parent

    actions.reverse() 
    total_steps = len(actions)
    return actions, total_steps


# environment = coloringNinja(lineSize=2)
# result = breadth_first_graph_search(environment, verbose=True)
