# Connect-4-AI-project-
"AI Project for Connect 4 with search algorithms."
Connect 4 AI - Problem Modeling
1. State Space Representation:
The state space for the Connect 4 game consists of all possible board configurations, represented as a 6x7 grid, where each cell can be empty (0), occupied by Player 1 (1), or Player 2 (2). The total number of unique configurations is vast, but many configurations are not valid due to game rules.

2. Initial and Goal States:
Initial State: The board starts empty with all cells set to 0.
Goal State: The game ends when a player connects four of their pieces in a horizontal, vertical, or diagonal line.
3. Actions:
Players take turns choosing a column to drop a piece into. The piece will fall to the lowest empty row in the selected column.

4. Transition Function:
The transition occurs when a player places a piece into a column, which will fall to the lowest empty row within that column. The state is updated after every move.

5. Problem Size:
The game is played on a 6x7 board, so there are 42 cells. Each cell has three possible values, resulting in a large but manageable state space.

6. Modeling Assumptions:
Players take turns placing pieces into columns.
The game ends when a player connects four pieces.
There are no draws, and players alternate turns.
