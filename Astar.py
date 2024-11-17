from queue import PriorityQueue
from environment import coloringNinja
from Node import Node
from copy import deepcopy
from Heuristic import Heuristic

def a_star_search(environment, heuristic, heuristic_type=1, verbose=True):
    root = Node.root(environment)  # Initialize with full state, including palette and savings.

    # Check if the root node meets the goal condition
    if root.state[:len(environment.line)] == environment.goalState:
        return {"actions": [], "total_cost": 0, "max_frontier": 1}

    # Priority Queue for A* (min-heap) to prioritize nodes based on the f(n) value
    frontier = PriorityQueue()
    f_value = root.path_cost + heuristic.calculate(root, heuristic_type)  # f(n) = g(n) + h(n)
    frontier.put((f_value, root))  # Insert the root node with its f(n) value
    explored = set()  # Track explored states
    max_frontier_size = 1  # Track the maximum frontier size

    def is_in_frontier(frontier, state):
        return any(state == item[1].state for item in frontier.queue)

    # Memoize the heuristic function for efficiency
    heuristic_fn = memoize(heuristic.calculate, 'h')

    while not frontier.empty():
        # Pop the node with the lowest f(n) value from the frontier
        current_f_value, node = frontier.get()
        node_state_tuple = tuple(node.state)
        explored.add(node_state_tuple)  # Add the current state to the explored set

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

        # Expand the node by generating actions based on the environment
        for action in ["color", "skip", "move left", "move right"]:  # Added 'skip' as an action
            child = Node.child(deepcopy(environment), node, action)  # Create child node directly from action
            child_state_tuple = tuple(child.state)

            if verbose:
                print(f"  Action: {action}, Child State: {child_state_tuple}")

            # Check if the child state is new
            if child_state_tuple not in explored and not is_in_frontier(frontier, child_state_tuple):
                # Check if the child is the goal
                if child.state[:len(environment.line)] == environment.goalState:
                    if verbose:
                        print("Goal state reached:", child.state[:len(environment.line)])
                    solution_result = solution(child)  # Call solution()

                    # Ensure the solution_result is a valid tuple before unpacking
                    if solution_result:  # Check if solution_result is not None
                        actions, total_cost = solution_result
                        return {
                            "goal_state": environment.goalState,
                            "actions": actions,
                            "max_frontier": max_frontier_size,   
                            "total_cost": total_cost}
                
                # Use memoized heuristic calculation
                new_f_value = child.path_cost + heuristic_fn(child, heuristic_type)
                frontier.put((new_f_value, child))

        # Update the maximum frontier size
        max_frontier_size = max(max_frontier_size, frontier.qsize())  # Track the max size of frontier

    # Return failure if no solution is found
    return {"actions": None, "total_cost": float('inf'), "max_frontier": max_frontier_size, "goal_state": environment.goalState}

def solution(node):
    actions = []
    total_cost = 0

    while node.parent is not None:
        actions.append(node.action)
        total_cost += node.path_cost
        node = node.parent

    actions.reverse()
    
    # Ensure we return a valid tuple
    if actions and total_cost >= 0:
        return actions, total_cost
    return None  # Return None if the solution is invalid or empty

def memoize(fn, attr_name):
    """Memoizes function results by storing them in an attribute of the problem object."""
    cache = {}

    def memoized_fn(node, heuristic_type):
        if node not in cache:
            cache[node] = fn(node, heuristic_type)
        return cache[node]

    return memoized_fn
