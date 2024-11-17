from heapq import heappop, heappush
from copy import deepcopy
from environment import coloringNinja
from Node import Node
from Heuristic import Heuristic

def a_star_search(environment, heuristic, heuristic_type=1, verbose=True):
    """
    Implements A* Search for the coloringNinja environment and returns the solution.
    The heuristic function (h) is used to estimate the distance to the goal.
    The cost to reach the node from the start is g(n).
    """
    root = Node.root(environment)  # Initialize with the full state, including palette and savings.

    # Check if the root node already meets the goal condition
    if root.state[:len(environment.line)] == environment.goalState:
        return {"actions": [], "total_cost": 0, "max_frontier": 1}

    frontier = []  # Priority Queue for A* (min-heap)
    print("cost: ", root.path_cost)
    root_h = heuristic.calculate(root, heuristic_type)
    root.heuristic = root_h
    heappush(frontier, (root.path_cost + root_h, root))  # f(n) = g(n) + h(n)
    explored = set()  # Track explored states
    max_frontier_size = 1  # Track the maximum frontier size

    while frontier:
        _, node = heappop(frontier)
        node_state_tuple = tuple(node.state)
        explored.add(node_state_tuple)  # Add the current state to the explored set

        # Update the environment state from the current node
        environment.line = list(node.state[:len(environment.line)])
        environment.agentPosition = node.state[len(environment.line)]
        environment.savings = node.state[len(environment.line) + 1]
        environment.paletteQuantity = dict(node.state[len(environment.line) + 2])

        # Print the current state of the environment
        if verbose:
            print("Current Line State:")
            environment.displayLineState()

        # Debug print for path cost (g(n)) and heuristic (h(n))
        print(f"Node Path Cost (g(n)): {node.path_cost}")
        print(f"Heuristic (h(n)): {heuristic.calculate(node, heuristic_type)}")
        
        # Check if the agent can purchase any palettes (if savings allow)
        for color in environment.paletteQuantity:
            if environment.paletteQuantity[color] == 0 and environment.savings >= environment.paletteCost:
                # Update palette quantity to 2 if savings are enough
                environment.paletteQuantity[color] = 2
                environment.savings -= environment.paletteCost
                print(f"Purchased {color} palette, new palette quantities: {environment.paletteQuantity}")

        # Update points and savings
        points = environment.points
        print(f"Updated Points: {points}, Savings: {environment.savings}")

        # Expand the node by generating actions based on the environment
        for action in ["color", "skip", "move left", "move right"]:  # Added 'skip' as an action
            child = Node.child(deepcopy(environment), node, action)  # Create child node directly from action
            child_state_tuple = tuple(child.state)

            if verbose:
                print(f"  Action: {action}, Child State: {child_state_tuple}")

            # Check if the child state is new
            if child_state_tuple not in explored and not any(child_state_tuple == item[1].state for item in frontier):
                # Check if the child is the goal
                if child.state[:len(environment.line)] == environment.goalState:
                    if verbose:
                        print("Goal state reached:", child.state[:len(environment.line)])
                    solution_result = solution(child)  # Call solution()

                    # Ensure the solution_result is a valid tuple before unpacking
                    if solution_result:  # Check if solution_result is not None
                        actions, total_cost = solution_result
                        print(f"Solution Total Cost: {total_cost}")
                        return {
                            "goal_state": environment.goalState,
                            "actions": actions,
                            "max_frontier": max_frontier_size,   
                            "total_cost": total_cost
                        }

                # Add the child to the frontier with its f(n) = g(n) + h(n)
                child_h = heuristic.calculate(child, heuristic_type)
                child.heuristic = child_h
                heappush(frontier, (child.path_cost + child_h, child))

        # Update the maximum frontier size
        max_frontier_size = max(max_frontier_size, len(frontier))  # Track the max size of frontier

    # Return failure if no solution is found
    return {"actions": None, "total_cost": float('inf'), "max_frontier": max_frontier_size, "goal_state": environment.goalState}

def solution(node):
    actions = []
    total_cost = 0

    while node.parent is not None:
        actions.append(node.action)
        total_cost += (node.path_cost + node.heuristic)
        print(f"Tracing Back: Action = {node.action}, Path Cost = {(node.path_cost + node.heuristic)}, Total Cost So Far = {total_cost}")
        node = node.parent

    actions.reverse()
    print(f"Final Solution Actions: {actions}, Total Cost: {total_cost}")

    # Ensure we return a valid tuple
    if actions and total_cost >= 0:
        return actions, total_cost
    return None  # Return None if the solution is invalid or empty

# Example usage
environment = coloringNinja(lineSize=6)
heuristic = Heuristic(environment)

a_star_search(environment, heuristic, heuristic_type=2, verbose=True)
