class Heuristic:
    def __init__(self, environment):
        self.environment = environment  

    def heuristic_1(self, node):
       
        

        uncolored_cells = sum(1.5 for cell in node.state[:len(node.state)//2] if cell == "uncolored")
        return uncolored_cells

   
    def heuristic_2(self, node):
    
   
        uncolored_cells = sum(1.5 for cell in node.state[:len(node.state)//2] if cell == "uncolored")
        
    
        palette_cost_factor = 0.5 * len(node.state[len(node.state)//2 + 1:]) 
        
        return uncolored_cells + palette_cost_factor

    
    

    def calculate(self, node, heuristic_type=1):
      
        if heuristic_type == 1:
            return self.heuristic_1(node)
        elif heuristic_type == 2:
            return self.heuristic_2(node)
        else:
            raise ValueError("Invalid heuristic type. Choose 1 or 2.")
        

