class coloringNinja():
    def __init__(self, lineSize=6, paletteCost=3, points=1, paletteQuantitiy=2):
        self.size = lineSize
        self.colorList = ["🍓", "🐳", "🐸", "🌸"]
        self.paletteCost = paletteCost
        self.paletteQuantity = {color: paletteQuantitiy for color in self.colorList}
        self.points = points
        self.savings = 0
        self.line = ["uncolored"] * lineSize
        self.agentPosition = 0
        self.moves = 0

        self.initialState = self.getState()
        self.goalState = self.getGoalState()

    def displayLineState(self):
               
                print("Current line state:")
                for index, cell in enumerate(self.line):
                    marker = "🔲" if cell == "uncolored" else "✅"
                    print(f"Position {index+1}: {cell} {marker}")
                print(f"Agent Position: {self.agentPosition}")
                print(f"Savings: {self.savings}, Points: {self.points}")
                print(f"Palette Quantities: {self.paletteQuantity}")

    def getState(self):
        return self.line, self.agentPosition, self.savings

    def getGoalState(self):
        goal = ["uncolored"] * self.size
        for pos in range(self.size):
            goal[pos] = self.getColorForPosition(pos)
            
        return tuple(goal)

    def getColorForPosition(self, pos):
        
        if (pos+1) % 2 == 0:
            return "🍓"
        elif (pos+1) % 3 == 0:
            return "🐸"
        elif (pos+1) % 5 == 0:
            return "🐳"
        
        return "🌸"

    def isGoal(self):
         return self.line == self.goalState

    def printGoalState(self):
        print("Goal state:", self.goalState)

    def colorCells(self):
        if self.line[self.agentPosition] == "uncolored":
            color = self.getColorForPosition(self.agentPosition)
            # print(f"Attempting to color position {self.agentPosition} with {color}")

            if self.paletteQuantity[color] > 0:
                self.line[self.agentPosition] = color
                self.paletteQuantity[color] -= 1
                self.savings += self.points
            else:  
                if self.savings >= self.paletteCost:
                    self.savings -= self.paletteCost
                    self.paletteQuantity[color] = 2 
                    self.line[self.agentPosition] = color
                    self.paletteQuantity[color] -= 1
                    self.savings += self.points
                else:  
                    print(f"Skipped cell at {self.agentPosition} due to insufficient resources.")
                    return False 
            return True 
        return None  

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
            return False
        

    def getActions(self, direction):
        actions = []
        skipped_positions = []
        print(f"Generating actions from state: {self.line}, agentPosition: {self.agentPosition}, palette: {self.paletteQuantity}")


        while "uncolored" in self.line:
            success = self.colorCells()
            if success:
                color = self.line[self.agentPosition]
                actions.append(("color", color))
            elif success is False: 
                skipped_positions.append(self.agentPosition)
                actions.append(("skipped", self.agentPosition))
                print(f"Invalid move at position {self.agentPosition}, skipped.")

          
            if not self.moveAgent(direction):
                if skipped_positions:  
                    self.agentPosition = skipped_positions.pop(0)
                    print(f"Revisiting skipped cell at position {self.agentPosition}.")
                    continue
                else:  
                    break

        return actions

    
    
ninja = coloringNinja()
ninja.printGoalState()



