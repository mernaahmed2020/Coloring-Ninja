class coloringNinja():
    def __init__(self, lineSize=16, paletteCost=3, points=1, paletteQuantitiy=2):
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
        if self.line == self.goalState:
            print("goal raeched")

    def printGoalState(self):
        print("Goal state:", self.goalState)

    def colorCells(self):
        # Only try to color if the cell is uncolored
        if self.line[self.agentPosition] == "uncolored":
            color = self.getColorForPosition(self.agentPosition)
            
            # Debugging print to show the current color attempt
            print(f"Coloring position {self.agentPosition} with {color}")  
            
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
        while self.agentPosition < len(self.line) or "uncolored" in self.line:
            self.colorCells()
            color = self.line[self.agentPosition]
            if color != "uncolored":  # coloring successful
                actions.append(("color", color))
            else:
                print(f"Skipping cell at {self.agentPosition} - No coloring done")

            # Move the agent based on the direction
            success = self.moveAgent(direction)
            if success:
                actions.append(("moved", direction))
            else:
                actions.append(("invalid move", direction))
            
            # If the agent reaches the end of the line and there are uncolored cells, loop back to the beginning
            if self.agentPosition == len(self.line) - 1 and "uncolored" in self.line:
                print("End of line reached. Looping back to the start.")
                self.agentPosition = 0

        return actions

    
    
ninja = coloringNinja()
ninja.printGoalState()


# def test_color_cells():
#     ninja = coloringNinja(lineSize=32, paletteQuantitiy=2)  # Extended line size for position 24
#     ninja.agentPosition = 24  # Start at position 24 for testing

#     # Try to color the cells and check the results
#     ninja.colorCells()  # Should color position 24 ("blue")
#     assert ninja.line[24] == "blue", f"Expected 'blue' at position 24, but got {ninja.line[24]}"
#     assert ninja.paletteQuantity["blue"] == 1, f"Expected 1 'blue' palette, but got {ninja.paletteQuantity['blue']}"
    
#     print("Color cells test passed!")

# test_color_cells()

# test_color_cells()


# def run_tests():

#     test_color_cells()


# run_tests()


    