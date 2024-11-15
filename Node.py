from environment import coloringNinja
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state  # This will be a tuple containing the environment state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    @staticmethod
    def root(environment):
        # Get the environment's state (line, agentPosition, savings)
        line, agentPosition, savings = environment.getState()
        palette = tuple(environment.paletteQuantity.items())  # Include palette state (color quantities)
        
        # Combine all parts of the state
        state = (*line, agentPosition, savings, palette)  # Complete state with line, position, savings, and palette
        
        return Node(state)  # Return the node with the full state

    @staticmethod
    def child(environment, parent_node, action):
        # Unpack the state correctly
        *line, agentPosition, savings, palette = parent_node.state  # Use *line to handle the rest of the state
        
        # Convert palette back to a dictionary
        palette = dict(palette)
        
        # Create a new environment object
        new_env = coloringNinja()  # Create a new environment instance
        new_env.line = list(line)  # Copy the state
        new_env.agentPosition = agentPosition
        new_env.savings = savings
        new_env.paletteQuantity = palette  # Restore the palette

        # Perform the action
        if action == "color":
            new_env.colorCells()
        elif action == "move left":
            new_env.moveAgent("left")
        elif action == "move right":
            new_env.moveAgent("right")

        # Create a new state for the child node
        new_state = (*new_env.line, new_env.agentPosition, new_env.savings, tuple(new_env.paletteQuantity.items()))
        return Node(new_state, parent_node, action)
