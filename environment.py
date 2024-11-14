class coloringNinja():
    def __init__(self,size=8,paletteCost=3,points=5,paletteQuantitiy=5):
        self.size = size
        self.colorList = ["red","blue","green","pink"]
        self.paletteCost = paletteCost
        self.paletteQuantity={color : paletteQuantitiy for color in self.colorList}
        self.points=points
        self.savings=0
        self.grid = [["uncolored" for _ in range(size)]for _ in range(size)]
        self.agentPosition = (0,0)
        self.moves = 0
        
        
        self.initialState= self.getState()
        self.goalState = self.getGoalState()
        
    def getState(self):
        
        gridTuple = tuple(tuple(row) for row in self.grid)
        return(gridTuple,self.agentPosition,self.savings)
        
        
    def getGoalState(self):  
        
        goal= [["uncolored" for _ in range(self.size)]for _ in range(self.size)]
        
        for row in range(self.size):
            for column in range(self.size):
                color_index = (row + column ) % len(self.colorList)
                goal[row][column] = self.colorList[color_index]
            
        return tuple(tuple(row) for row in goal)    # i changed it to a tuble instead of i list to ensure that it wont change by acciedeint 


    def isGoal(self):
        return self.getState() == self.getGoalState()

    def printGoalState(self):
        print("Goal state:")
        for row in self.goalState:
            print(row)
        print()

    #check the adjecnt cells
    def isAdjacent(row,column,color):
                    #can cause a problem if out of boundry
        adjecntCells = [(row,column-1),(row,column+1),(row-1,column),(row+1,column)]
        for r,c in adjecntCells:
            #fixing the boundry problem
            if 0 <= r < self.size and 0 <= c < self.size:
                if self.grid[r][c] == color:
                    print(f"can't color due to adjecncy constarint! at ({r},{c})")
                        
                    return False
        return True
        
        
        
        
    # a function that colors the cells and also check if is goal state
    def coloringPencil(self,row,column,direction,color):
        if self.grid[row][column] != "uncolored":
            return False
        
        if not self.isAdjacent(self,row,column,color):
            return False
                   
            #check  the quantity of palette      
        if  self.paletteQuantity[color] == 0:              
            self.buyPalette(color)
                
                        
        if self.paletteQuantity[color] == 0:
            print("no enough savings! moving to next position")
            self.movingAgent(direction)
            return False    
                        
                    
                     
                     #color the cell and updates savings and qantitity   
        self.grid[row][column] = color
        self.paletteQuantity[color] -= 1
        self.savings += self.points
                    
        self.agentPosition=(row,column)
                        
        print(f"colored cell{self.agentPosition} with {color}")
        if self.isGoal():
            return True               
                    
        self.movingAgent(direction)

                    
           
    
    def movingAgent(self,direction):
        row, column = self.agentPosition
        if direction == "up" and row > 0:
            self.agentPosition = (row-1,column)
        elif direction =="down" and row <(self.size-1):
            self.agentPosition = (row+1,column)
        elif direction =="right" and column < (self.size-1):
            self.agentPosition = (row,column+1)
        elif direction== "left" and column >0:
            self.agentPosition = (row,column-1)
        else:
            print("Invaild move")            
        
        self.moves += 1
        print(f"agent moved to {self.agentPosition}") 
         # can add action values ex: up = -3 down -1  
              
    def buyPalette(self,color):
        if self.savings >= self.paletteCost:
            self.savings -= self.paletteCost
            self.paletteQuantity[color] += 1 
            
            print(f"restoked {color} palette")
            return True
        else:
            print("no enough savings! moving to next position")
            return False
              
        
    def getActions(self):
        actions=[]
        row,column = self.agentPosition
        directions = ["up","down","right","left"]
        for direction in directions:
            if direction =="up" and row >0:
                actions.append()
            elif direction == "down" and row < (self.size- 1):
                actions.append(("move", "down"))
            elif direction == "right" and column <(self.size- 1):
                actions.append(("move", "right"))
            elif direction == "left" and column >0:
                actions.append(("move", "left"))           

        if self.grid[row][column] =="uncolored":
            for color in self.colorList:
                if self.isAdjacent(row, column, color) and self.paletteQuantity[color] >0:
                    
                    actions.append(("color", color))
        
        return actions           
game = coloringNinja(size=8)  
game.printGoalState()  

        

