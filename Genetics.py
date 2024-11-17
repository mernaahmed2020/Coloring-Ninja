import random
import time

from environment import coloringNinja
from Node import Node

def initialize_population(environment, population_size):
    population = []
    for _ in range(population_size):
        line = [random.choice(list(environment.paletteCosts.keys())) for _ in range(len(environment.line))]
        agent_position = random.randint(0, len(environment.line) - 1)
        palette_quantity = {k: random.randint(0, 10) for k in environment.paletteCosts.keys()}
        individual = [line, agent_position, palette_quantity] 
        population.append(individual)
    return population

def evaluate(environment, individual):
    line, agent_position, palette_quantity = individual
    goal_state = ('🌸', '🍓', '🐸', '🍓', '🐳', '🍓')  
    similarity = sum(1 for i, cell in enumerate(line) if cell == goal_state[i])
    completed_cells = sum(1 for cell in line if cell != 0)
    penalties = sum(1 for color, quantity in palette_quantity.items() if quantity < 0)
    return similarity - penalties  

def select_parents(population, fitness_scores):
    parents = []
    for _ in range(len(population) // 2):
        tournament = random.sample(list(zip(population, fitness_scores)), k=3)
        winner = max(tournament, key=lambda x: x[1])[0]
        parents.append(winner)
    return parents

def crossover(parents, population_size):
    offspring = []
    while len(offspring) < population_size:
        parent1, parent2 = random.sample(parents, 2)
        crossover_point = random.randint(0, len(parent1[0]) - 1)
        child_line = parent1[0][:crossover_point] + parent2[0][crossover_point:]
        child_agent_position = random.choice([parent1[1], parent2[1]])
        child_palette_quantity = {
            k: (parent1[2][k] + parent2[2][k]) // 2 for k in parent1[2].keys()
        }
        offspring.append([child_line, child_agent_position, child_palette_quantity])  
    return offspring

def mutate(offspring, mutation_rate):
    for i in range(len(offspring)):
        if random.random() < mutation_rate:
            individual = offspring[i]
            mutation_point = random.randint(0, len(individual[0]) - 1)
            individual[0][mutation_point] = random.choice(list(individual[2].keys()))  
            individual[1] = random.randint(0, len(individual[0]) - 1)
            key_to_mutate = random.choice(list(individual[2].keys()))
            individual[2][key_to_mutate] += random.randint(-2, 2)
            individual[2][key_to_mutate] = max(0, individual[2][key_to_mutate])

    return offspring


def genetic_algorithm(environment, population_size=20, generations=50, mutation_rate=0.1, verbose=False):

    if not hasattr(environment, 'paletteCosts'):
        environment.paletteCosts = {
            "🍓": 7,  
            "🐳": 5,
            "🐸": 2,
            "🌸": 1,
        }

    population = initialize_population(environment, population_size)

    for generation in range(generations):
        fitness_scores = [evaluate(environment, individual) for individual in population]

        if verbose:
            print(f"Generation {generation}: Best Fitness = {max(fitness_scores)}")

        parents = select_parents(population, fitness_scores)

        offspring = crossover(parents, population_size)

        offspring = mutate(offspring, mutation_rate)

        population = offspring

        best_individual = population[fitness_scores.index(max(fitness_scores))]
        # visualizer = Visualizer(environment)
        environment.line = best_individual[0]  
        environment.agentPosition = best_individual[1]  
        # visualizer.visualize()  


    best_fitness = max(fitness_scores)
    best_individual = population[fitness_scores.index(best_fitness)]
    

    # visualizer = Visualizer(environment)
    environment.line = best_individual[0]  
    environment.agentPosition = best_individual[1] 
    # visualizer.visualize() 
    
    return best_individual, best_fitness



environment = coloringNinja() 
start_time = time.time()

best_individual, best_fitness = genetic_algorithm(environment, population_size=20, generations=20, mutation_rate=0.1, verbose=True)

end_time = time.time()  
execution_time = end_time - start_time 

line = best_individual[0]  
agent_position = best_individual[1]  
palette_quantity = best_individual[2]  

print(f"Best Individual Line: {line}")
print(f"Agent Position: {agent_position}")
print(f"Palette Quantities: {palette_quantity}")
print(f"Best Fitness Score: {best_fitness}")
print(f"Execution Time: {execution_time:.2f} seconds")