class Heuristic:
    def __init__(self, environment):
        self.environment = environment  

    def heuristic_1(self, node):
       
        #calculate based on the number of uncolored cells.

        uncolored_cells = sum(1.5 for cell in node.state[:len(node.state)//2] if cell == "uncolored")
        return uncolored_cells

    # def heuristic_2(self, node):
    #     """
    #     Heuristic 2: Calculate based on some other criteria. For example, the number of moves 
    #     the agent needs to make to complete the task (this is just an example).
    #     """
    #     # Ensure the agent's position is treated as an integer
    #     agent_position = node.state[len(node.state) - 3] 
    #     # Calculate the remaining distance to the goal
    #     remaining_distance_to_goal = abs(agent_position - len(self.environment.line) - 1)
    #     return remaining_distance_to_goal
    def heuristic_2(self, node):
    
    # Uncolored cells (weighted)
        uncolored_cells = sum(1.5 for cell in node.state[:len(node.state)//2] if cell == "uncolored")
        
        # Palette cost (if relevant)
        palette_cost_factor = 0.5 * len(node.state[len(node.state)//2 + 1:])  # You can adjust the factor based on how palette cost affects the state.
        
        return uncolored_cells + palette_cost_factor

    
    
    
    

    

    def calculate(self, node, heuristic_type=1):
        """
        Returns the heuristic value based on the type chosen.
        """
        if heuristic_type == 1:
            return self.heuristic_1(node)
        elif heuristic_type == 2:
            return self.heuristic_2(node)
        else:
            raise ValueError("Invalid heuristic type. Choose 1 or 2.")
        

