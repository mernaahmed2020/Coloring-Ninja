from environment import coloringNinja
from Node import Node
class Visualizer:
    """Visualizer for the Coloring Ninja problem."""

    def _init_(self, problem):
        """Initialize with the problem to visualize."""
        self.problem = problem
        self.counter = 0

    def visualize(self, frontier):
        """Visualize the frontier at each step."""
        self.counter += 1
        print(f"\nFrontier at step {self.counter}:")
        for node in frontier:
            print("\nNode State:")
            self.visualize_state(node.state)
        print("-" * 80)

    def visualize_state(self, state):
        """Visualizes a single state."""
        line, agent_position, savings, palette = state[:-3], state[-3], state[-2], dict(state[-1])
        print("Line State:")
        for idx, cell in enumerate(line):
            marker = "🔲" if cell == "uncolored" else "✅"
            agent = "🤖" if idx == agent_position else "   "
            print(f"{idx+1}: {cell} {marker} {agent}")

        print(f"Agent Position: {agent_position + 1}")
        print(f"Savings: {savings}")
        print(f"Palette Quantities: {palette}")
        print("-" * 40)

