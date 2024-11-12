class coloringNinja():
    def __init__(self,size=8,paletteCost=3,points=5,paletteQuantitiy=5):
        self.size = size
        self.colorList = ["red","blue","green","pink"]
        self.paletteCost = paletteCost
        self.paletteQuantity=paletteQuantitiy
        self.pionts=points
        self.savings=0
        self.grid = [["uncolored" for _ in range(size)]for _ in range(size)]
        self.agentPosition = ((0),(0))
        self.moves = 0
        
        self.initialState= self.getState()
        self.goalState = self.getGoalState()
        
    def getState(self):
        
        return[row[:] for row in self.grid] # making a copy of the current state (intialy all uncolcored)
        
        
    def getGoalState(self):  
        
        goal= [["uncolored" for _ in range(self.size)]for _ in range(self.size)]
        
        for row in range(self.size):
            for column in range(self.size):
                color_index = (row + column ) % len(self.colorList)
                goal[row][column] = self.colorList[color_index]
            
        return goal      




    def printGoalState(self):
        print("Goal state:")
        for row in self.goalState:
            print(row)
        print()

    def coloringPencil(self):
        # a function that colors the cells and check the adjecnt cells also check if is goal state
        #transition function
        return"color"
    
    def moves(self):
        return"move"
        # moves the agent around the grid (v=could be splitted into 4 functions)
    
    
            

game = coloringNinja(size=8)  
game.printGoalState()  

        # can add action values ex: up = -3 down -1 
      