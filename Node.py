from environment import coloringNinja
from copy import deepcopy

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=None, heuristic=0):
        self.state = state  # Tuple containing line, agent position, savings, and palette
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.heuristic = heuristic

    def __lt__(self, other):
        if self.path_cost is None or other.path_cost is None:
            return False  # Don't compare if one of them doesn't have path_cost
        return self.path_cost < other.path_cost

    def __hash__(self):
        return hash(tuple(self.state))

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    @staticmethod
    def root(environment):
        line, agentPosition, savings = environment.getState()
        palette = tuple(environment.paletteQuantity.items())
        state = (*line, agentPosition, savings, palette)
        return Node(state,path_cost=0)

    @staticmethod
    def child(environment, parent_node, action,action_cost=0):
        *line, agentPosition, savings, palette = parent_node.state
        palette = dict(palette)

        # Reconstruct the environment state
        new_env = deepcopy(environment)
        new_env.line = list(line)
        new_env.agentPosition = agentPosition
        new_env.savings = savings
        new_env.paletteQuantity = palette

        # Perform the action
        if action == "color":
            new_env.colorCells()
        elif action == "skip":
            pass
        elif action == "move left":
            new_env.moveAgent("left")
        elif action == "move right":
            new_env.moveAgent("right")

        # Create the new state after the action
        new_state = (
            *new_env.line,
            new_env.agentPosition,
            new_env.savings,
            tuple(new_env.paletteQuantity.items()),
        )
        
        
        if parent_node.path_cost is not None:
            new_path_cost = parent_node.path_cost + action_cost
        else:
            new_path_cost = None  # If no path_cost is used, set it to None
        return Node(new_state, parent_node, action, new_env.points)


