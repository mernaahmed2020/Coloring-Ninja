from queue import PriorityQueue
from environment import coloringNinja
from Node import Node
from copy import deepcopy
import networkx as nx
import matplotlib.pyplot as plt

def uniform_cost_search(environment, verbose=True):

    root = Node.root(environment) 

    
    if root.state[:len(environment.line)] == environment.goalState:
        return {"actions": [], "total_cost": 0, "max_frontier": 1}

    frontier = PriorityQueue()
    frontier.put((0, root))  
    explored = set() 
    frontier_states = set() 
    max_frontier_size = 1 

    
    # G = nx.DiGraph()

    def is_in_frontier(state):
       
        return state in frontier_states

    while not frontier.empty():
       
        current_cost, node = frontier.get()
        node_state_tuple = tuple(node.state)
        explored.add(node_state_tuple)  
       
        environment.line = list(node.state[:len(environment.line)])
        environment.agentPosition = node.state[len(environment.line)]
        environment.savings = node.state[len(environment.line) + 1]
        environment.paletteQuantity = dict(node.state[len(environment.line)+2])


        if verbose:
            print("Current Line State:")
            environment.displayLineState()

       
        for color in environment.paletteQuantity:
            if environment.paletteQuantity[color] == 0 and environment.savings >= environment.paletteCost:
               
                environment.paletteQuantity[color] = 2
                environment.savings -= environment.paletteCost  
                if verbose:
                    print(f"Purchased {color} palette, new palette quantities: {environment.paletteQuantity}")

      
        points = environment.points  

        if verbose:
            print(f"Updated Points: {points}, Savings: {environment.savings}")

     
        for action in ["color", "skip", "move left", "move right"]: 
            child = Node.child(deepcopy(environment), node, action)  
            child_state_tuple = tuple(child.state)

            if verbose:
                print(f"  Action: {action}, New Cost: {current_cost}, Child State: {child_state_tuple}")

           
            if child_state_tuple not in explored and not is_in_frontier(child_state_tuple):
                
                if child.state[:len(environment.line)] == environment.goalState:
                    if verbose:
                        print("Goal state reached:", child.state[:len(environment.line)])
                    solution_result = solution(child)  

                  
                    if solution_result:  
                        actions, total_cost = solution_result
                        print(f"Total Cost: {total_cost}")
                        print(f"Max Frontier Size: {max_frontier_size}")

                      
                        # draw_search_tree(G)

                        return {
                            "actions": actions,
                            "total_cost": total_cost,
                            "goal_state": environment.goalState,
                            "max_frontier": max_frontier_size,
                        }

              
                new_cost = current_cost + child.path_cost
                frontier.put((new_cost, child))
                frontier_states.add(child_state_tuple)  

               
                # G.add_edge(tuple(node.state), tuple(child.state), action=action)

       
        max_frontier_size = max(max_frontier_size, frontier.qsize())  
    
    # draw_search_tree(G)
    return {"actions": None, "total_cost": float('inf'), "max_frontier": max_frontier_size}

def solution(node):
    actions = []
    total_cost = 0

    while node.parent is not None:
        actions.append(node.action)
        total_cost += node.path_cost
        node = node.parent

    actions.reverse()

    if actions and total_cost >= 0:
        return actions, total_cost
    return None

# def draw_search_tree(G):
#     pos = nx.spectral_layout(G) 
#     plt.figure(figsize=(12, 8))
#     nx.draw(G, pos, with_labels=True, node_size=2000, node_color="pink", font_size=10, font_weight="bold", edge_color="gray")
#     edge_labels = nx.get_edge_attributes(G, 'action')
#     nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
#     plt.title("Search Tree")
#     plt.show()


