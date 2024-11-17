import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self, game):  # Fixed the method name to `__init__`
        self.game = game
        # Create a color mapping for the emoji to valid matplotlib colors
        self.color_mapping = {
            "🍓": "red",
            "🐳": "blue",
            "🐸": "green",
            "🌸": "pink", 
            "uncolored": "white"
        }

    def visualize(self):
        """
        Visualize the current state of the line.
        """
        n = len(self.game.line)
        colors = []
        for i, cell in enumerate(self.game.line):
            # Use the color mapping to get a valid color
            colors.append(self.color_mapping.get(cell, "gray"))  # Default to gray for unknown colors

        fig, ax = plt.subplots(figsize=(n, 1))
        ax.set_xlim(0, n)
        ax.set_ylim(0, 1)

        # Draw cells
        for i, color in enumerate(colors):
            rect = plt.Rectangle((i, 0), 1, 1, facecolor=color, edgecolor="black")
            ax.add_patch(rect)
            # Highlight the agent position
            if i == self.game.agentPosition:
                ax.text(i + 0.5, 0.5, "A", color="black", ha="center", va="center", fontsize=14, fontweight="bold")

        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis("off")
        plt.show()
