import random
import time
from environment import coloringNinja
from Node import Node

def generate_neighbors(environment, node):
    neighbors = []
    for action in ["color", "move left", "move right"]:
        neighbor = Node.child(environment, node, action)
        neighbors.append(neighbor)
    return neighbors

def evaluate(environment, node):
    completed_cells = sum(1 for cell in environment.line if cell != "uncolored")
    return completed_cells

def hill_climbing(environment, verbose=False):

    #visualizer = Visualizer(environment)
    
    current = Node.root(environment)
    current_score = evaluate(environment, current)

    if verbose:
        print("Initial state:")
        environment.displayLineState()
        print(f"Initial Score: {current_score}")

    start_time = time.time()
    frontier_size = 0

    while True:
        #visualizer.visualize()

        neighbors = generate_neighbors(environment, current)
        frontier_size = len(neighbors)
        next_state = None
        best_score = current_score

        for neighbor in neighbors:
            environment.line = list(neighbor.state[:len(environment.line)])
            environment.agentPosition = neighbor.state[len(environment.line)]
            environment.savings = neighbor.state[len(environment.line) + 1]
            environment.paletteQuantity = dict(neighbor.state[len(environment.line) + 2])

            score = evaluate(environment, neighbor)
            if score > best_score:
                best_score = score
                next_state = neighbor

        if next_state is None:   
            if verbose:
                print("Reached local maximum.")
                print("Goal state not reached.")
            break  

        current = next_state
        current_score = best_score

     
        environment.line = list(current.state[:len(environment.line)])
        environment.agentPosition = current.state[len(environment.line)]
        environment.savings = current.state[len(environment.line) + 1]
        environment.paletteQuantity = dict(current.state[len(environment.line) + 2])

        if verbose:
            print("Moved to new state:")
            environment.displayLineState()
            print(f"New Score: {current_score}")

    end_time = time.time()
    execution_time = end_time - start_time

    print("Frontier Size:", frontier_size)
    print("Time taken:", execution_time, "seconds")


    return current, current_score

# environment = coloringNinja()
# result_node, result_score = hill_climbing(environment, verbose=True)
