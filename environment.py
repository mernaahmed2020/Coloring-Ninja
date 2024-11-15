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
        if self.line[self.agentPosition] == "uncolored":
            color = self.getColorForPosition(self.agentPosition)
            print(f"Coloring position {self.agentPosition} with {color}")  #debugging 
            if self.paletteQuantity[color] > 0:
                self.line[self.agentPosition] = color
                self.paletteQuantity[color] -= 1
                self.savings += self.points
            else:
                if self.savings >= self.paletteCost:
                    self.savings -= self.paletteCost
                    self.paletteQuantity[color] = 5  # refill palette
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
    
# Test 1: Low Palette Quantity, High Palette Cost, Low Savings
print("Test 1: Low Palette Quantity, High Palette Cost, Low Savings")
env1 = coloringNinja(paletteQuantitiy=1, paletteCost=5, points=1)
env1.savings = 1  # Low savings to test behavior
print("\nInitial State:")
print("Line:", env1.line)
print("Agent Position:", env1.agentPosition)
print("Savings:", env1.savings)
print("Goal state:", env1.goalState)
env1.getActions("right")  # Try to color and move
print("\nFinal state:")
print("Line:", env1.line)
print("Agent Position:", env1.agentPosition)
print("Savings:", env1.savings)

# Test 2: High Palette Quantity, Low Palette Cost, High Savings
print("\nTest 2: High Palette Quantity, Low Palette Cost, High Savings")
env2 = coloringNinja(paletteQuantitiy=5, paletteCost=1, points=1)
env2.savings = 10  # High savings
print("\nInitial State:")
print("Line:", env2.line)
print("Agent Position:", env2.agentPosition)
print("Savings:", env2.savings)
env2.getActions("right")  # Try to color and move
print("\nFinal state:")
print("Line:", env2.line)
print("Agent Position:", env2.agentPosition)
print("Savings:", env2.savings)

# Test 3: No Palette Quantity, No Savings
print("\nTest 3: No Palette Quantity, No Savings")
env3 = coloringNinja(paletteQuantitiy=0, paletteCost=3, points=1)
env3.savings = 0  # No savings
print("\nInitial State:")
print("Line:", env3.line)
print("Agent Position:", env3.agentPosition)
print("Savings:", env3.savings)
env3.getActions("right")  # Try to color and move
print("\nFinal state:")
print("Line:", env3.line)
print("Agent Position:", env3.agentPosition)
print("Savings:", env3.savings)

# Test 4: High Palette Quantity, Zero Palette Cost, High Savings
print("\nTest 4: High Palette Quantity, Zero Palette Cost, High Savings")
env4 = coloringNinja(paletteQuantitiy=5, paletteCost=0, points=1)
env4.savings = 10  # High savings, no cost
print("\nInitial State:")
print("Line:", env4.line)
print("Agent Position:", env4.agentPosition)
print("Savings:", env4.savings)
env4.getActions("right")  # Try to color and move
print("\nFinal state:")
print("Line:", env4.line)
print("Agent Position:", env4.agentPosition)
print("Savings:", env4.savings)

# Test 5: Low Palette Quantity, Moderate Palette Cost, High Savings
print("\nTest 5: Low Palette Quantity, Moderate Palette Cost, High Savings")
env5 = coloringNinja(paletteQuantitiy=2, paletteCost=3, points=1)
env5.savings = 5  # High savings
print("\nInitial State:")
print("Line:", env5.line)
print("Agent Position:", env5.agentPosition)
print("Savings:", env5.savings)
env5.getActions("right")  # Try to color and move
print("\nFinal state:")
print("Line:", env5.line)
print("Agent Position:", env5.agentPosition)
print("Savings:", env5.savings)
