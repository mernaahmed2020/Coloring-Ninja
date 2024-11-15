class coloringNinja():
    def __init__(self, lineSize=8, paletteCost=3, points=1, paletteQuantitiy=5):
        self.size = lineSize
        self.colorList = ["red", "blue", "green", "pink"]
        self.paletteCost = paletteCost
        self.paletteQuantity = {color: paletteQuantitiy for color in self.colorList}
        self.points = points
        self.savings = 0
        self.line = ["uncolored"] * lineSize
        self.agentPosition = 0
        self.moves = 0

        self.initialState = self.getState()
        self.goalState = self.getGoalState()

    def getState(self):
        return self.line, self.agentPosition, self.savings

    def getGoalState(self):
        goal = ["uncolored"] * self.size
        for pos in range(self.size):
            goal[pos] = self.getColorForPosition(pos)
        return tuple(goal)

    def getColorForPosition(self, pos):
        
        if (pos+1) % 2 == 0:
            return "red"
        elif (pos+1) % 3 == 0:
            return "green"
        elif (pos+1) % 5 == 0:
            return "blue"
        
        return "pink"

    def isGoal(self):
        return self.line == self.goalState

    def printGoalState(self):
        print("Goal state:", self.goalState)

    def colorCells(self):
        # Only try to color if the cell is uncolored
        if self.line[self.agentPosition] == "uncolored":
            color = self.getColorForPosition(self.agentPosition)
            
            # Debugging print to show the current color attempt
            print(f"Coloring position {self.agentPosition} with {color}")  

            # If the agent doesn't have the color in the palette, check if they can buy it
            if self.paletteQuantity[color] == 0:
                print(f"Skipping {color} at position {self.agentPosition} - No palette available")
                return self.line
            
            if self.paletteQuantity[color] > 0:  # Can color normally
                self.line[self.agentPosition] = color
                self.paletteQuantity[color] -= 1
                self.savings += self.points
            else:  # Refilling the palette if the agent doesn't have enough savings
                if self.savings >= self.paletteCost:
                    self.savings -= self.paletteCost
                    self.paletteQuantity[color] = 5  # Refill palette
                    self.line[self.agentPosition] = color
                    self.paletteQuantity[color] -= 1
                    self.savings += self.points
                else:
                    print(f"Not enough savings to color cell at position {self.agentPosition}")
        return self.line


    def moveAgent(self, direction):
        if direction == "left" and self.agentPosition > 0:
            self.agentPosition -= 1
            self.moves += 1
            return True
        elif direction == "right" and self.agentPosition < len(self.line) - 1:
            self.agentPosition += 1
            self.moves += 1
            return True
        else:
            print("Invalid move")
            return False

    def getActions(self, direction):
        actions = []
        while self.agentPosition < len(self.line):
            
            if self.line[self.agentPosition] == "uncolored":
                self.colorCells() 
                color = self.line[self.agentPosition]
                if color != "uncolored":  #coloring successful
                    actions.append(("color", color))
                else:
                    print(f"Skipping cell at {self.agentPosition} - No coloring done")
        
            success = self.moveAgent(direction)
            if success:
                actions.append(("moved", direction))
            else:
                actions.append(("invalid move", direction))

            return actions
    
    
ninja = coloringNinja()
ninja.printGoalState()