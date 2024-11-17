import time
import math
import random
from visualizer import Visualizer
from environment import coloringNinja
from Node import Node
import matplotlib.pyplot as plt


def generate_neighbors(environment, node):
    neighbors = []
    for action in ["color", "move left", "move right"]:
        neighbor = Node.child(environment, node, action)
        neighbors.append(neighbor)
    return neighbors

def evaluate(environment, node):
    completed_cells = sum(1 for cell in environment.line if cell != 0)
    return completed_cells


def simulated_annealing(environment, initial_temp=100, cooling_rate=0.95, verbose=False):
   
    # visualizer = Visualizer(environment)

   
    current = Node.root(environment)
    current_score = evaluate(environment, current)
    temperature = initial_temp

    if verbose:
        #print("Initial state:")
        environment.displayLineState()
        print(f"Initial Score: {current_score}, Temperature: {temperature}")

    start_time = time.time()
    frontier_size = 0
    iteration = 0  

    fig, ax = plt.subplots(figsize=(len(environment.line), 1))
    ax.set_xlim(0, len(environment.line))
    ax.set_ylim(0, 1)
    ax.axis("off")

    while temperature > 0.1:  
      
        # visualizer.visualize()  

        neighbors = generate_neighbors(environment, current)
        next_state = random.choice(neighbors)

   
        environment.line = list(next_state.state[:len(environment.line)])
        environment.agentPosition = next_state.state[len(environment.line)]
        environment.savings = next_state.state[len(environment.line) + 1]
        environment.paletteQuantity = dict(next_state.state[len(environment.line) + 2])

        next_score = evaluate(environment, next_state)

  
        if next_score > current_score or random.random() < math.exp((next_score - current_score) / temperature):
            current = next_state
            current_score = next_score

            if verbose:
                print("Accepted new state:")
                environment.displayLineState()
                print(f"New Score: {current_score},  Temperature: {temperature}")

    
        temperature *= cooling_rate
        frontier_size = len(neighbors)
        iteration += 1 
        
    print("Final State:")
    print(f"Final State: {environment.line}")   
         

       # plt.pause(0.05)  

    end_time = time.time()
    execution_time = end_time - start_time

    print("Frontier Size:", frontier_size)
    print(f"Execution Time: {execution_time:.2f} seconds") 
    return current, current_score
    

 
# environment = coloringNinja()  
# result_node, result_score = simulated_annealing(environment, verbose=True)
