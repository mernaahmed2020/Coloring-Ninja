from queue import PriorityQueue
from environment import coloringNinja
from Node import Node
from copy import deepcopy

def uniform_cost_search(environment, verbose=True):

    root = Node.root(environment)  # Initialize with full state, including palette and savings.

    # Check if the root node meets the goal condition
    if root.state[:len(environment.line)] == environment.goalState:
        return {"actions": [], "total_cost": 0, "max_frontier": 1}

    # Priority Queue for UCS (min-heap) to prioritize nodes with the lowest cost
    frontier = PriorityQueue()
    frontier.put((0, root))  # Insert the root node with a cost of 0
    explored = set()  # Track explored states
    frontier_states = set()  # Track states in the frontier
    max_frontier_size = 1  # Track the maximum frontier size

    def is_in_frontier(state):
        # Efficient lookup in frontier states set
        return state in frontier_states

    while not frontier.empty():
        # Pop the node with the lowest cost from the frontier
        current_cost, node = frontier.get()
        node_state_tuple = tuple(node.state)
        explored.add(node_state_tuple)  # Add the current state to the explored set

        # Update the environment state from the current node
        environment.line = list(node.state[:len(environment.line)])
        environment.agentPosition = node.state[len(environment.line)]
        environment.savings = node.state[len(environment.line) + 1]
        environment.paletteQuantity = dict(node.state[len(environment.line)+2])

        # Print the current state of the environment
        if verbose:
            print("Current Line State:")
            environment.displayLineState()

        # Check if the agent can purchase any palettes (if savings allow)
        for color in environment.paletteQuantity:
            if environment.paletteQuantity[color] == 0 and environment.savings >= environment.paletteCost:
                # Update palette quantity to 2 if savings are enough
                environment.paletteQuantity[color] = 2
                environment.savings -= environment.paletteCost  # Deduct the palette cost from savings
                if verbose:
                    print(f"Purchased {color} palette, new palette quantities: {environment.paletteQuantity}")
        
        # Update points and savings
        points = environment.points  # Assuming you update points based on the agent's actions
        
        if verbose:
            print(f"Updated Points: {points}, Savings: {environment.savings}")

        # Expand the node by generating actions based on the environment
        for action in ["color", "skip", "move left", "move right"]:  # Added 'skip' as an action
            child = Node.child(deepcopy(environment), node, action)  # Create child node directly from action
            child_state_tuple = tuple(child.state)

            if verbose:
                print(f"  Action: {action}, New Cost: {current_cost}, Child State: {child_state_tuple}")

            # Check if the child state is new and not in explored or frontier
            if child_state_tuple not in explored and not is_in_frontier(child_state_tuple):
                # Check if the child is the goal
                if child.state[:len(environment.line)] == environment.goalState:
                    if verbose:
                        print("Goal state reached:", child.state[:len(environment.line)])
                    solution_result = solution(child)  # Call solution()

                    # Ensure the solution_result is a valid tuple before unpacking
                    if solution_result:  # Check if solution_result is not None
                        actions, total_cost = solution_result
                        print(f"Total Cost: {total_cost}")
                        print(f"Max Frontier Size: {max_frontier_size}")

                        return {
                            "actions": actions,
                            "total_cost": total_cost,
                            "goal_state": environment.goalState,
                            "max_frontier": max_frontier_size,
                        }

                # Add the child to the frontier with its accumulated cost
                new_cost = current_cost + child.path_cost
                frontier.put((new_cost, child))
                frontier_states.add(child_state_tuple)  # Add state to frontier set

        # Update the maximum frontier size
        max_frontier_size = max(max_frontier_size, frontier.qsize())  # Track the max size of frontier

    # Return failure if no solution is found
    return {"actions": None, "total_cost": float('inf'), "max_frontier": max_frontier_size}

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

environment = coloringNinja(lineSize=6)
result = uniform_cost_search(environment, verbose=True)