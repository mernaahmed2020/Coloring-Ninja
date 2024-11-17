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
    completed_cells = sum(1 for cell in environment.line if cell != 0)
    return completed_cells

def hill_climbing(environment, verbose=False):

    current = Node.root(environment)
    current_score = evaluate(environment, current)

    if verbose:
        print("Initial state:")
        environment.displayLineState()
        print(f"Initial Score: {current_score}")

    start_time = time.time()
    frontier_size = 0

    while True:
       
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
            break

        current = next_state
        current_score = best_score

        if verbose:
            print("Moved to new state:")
            environment.displayLineState()
            print(f"New Score: {current_score}")
    end_time = time.time()
    execution_time = end_time - start_time

    if next_state is None:
        print("Goal state not reached.")
    else:
        print("Goal state reached.")

    print("Frontier Size:", frontier_size)
    print("Time taken:", execution_time, "seconds")
    print("Memory usage:")

    return current, current_score
 



# environment = coloringNinja()
# result_node, result_score = hill_climbing(environment, verbose=True)
