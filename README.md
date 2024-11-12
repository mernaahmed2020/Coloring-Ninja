# ColoringNinja-AI-project-
1. Problem Modeling: 
o State Space Representation: An 8x8 grid. Each cell can be colored with one of four colors (red, blue, pink, mint) and no adjacent cells should be the same color.  
 o Initial and Goal States: Initial state: the board is empty and the goal state: all board is colored and  no adjacent cells have the same color. 
o Actions: the agent can move to color one cell at a time
 
o Transition function:
 Update the game state and  detect a win or when there are no available moves (two adjacent cells will be the same color)

2. Modeling Assumptions: 
O colors are limited and each color palette has a cost (5 coins)
. on coloring a cell correctly the agent collects 5 coins 
4. Heuristic Search: 
o Define two heuristic functions suitable for the problem:
Calculate the difference between the goal and the current state


—> penalty for buying extra color pallets : phase 2
  


