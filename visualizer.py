# import networkx as nx
# import matplotlib.pyplot as plt
# from Node import Node

# class SearchTreeVisualizer:
#     def __init__(self, environment, goal_state=None):
#         """
#         Initializes the visualizer with the environment and optional goal state.
        
#         :param environment: The environment object that contains the current state.
#         :param goal_state: The optional goal state to stop visualization at.
#         """
#         self.environment = environment
#         self.goal_state = goal_state
#         self.graph = nx.DiGraph()  # Directed graph to show the search tree

#     def visualize_search_tree(self):
#         """
#         Visualizes the search tree starting from the root node to the goal state (if provided).
#         """
#         start_node = Node.root(self.environment)
#         current_node = start_node

#         # Traverse the search tree (backtrack from the goal state)
#         while current_node:
#             self.graph.add_node(str(current_node.state))  # Add node with the state as identifier

#             # Add edge from parent to current node with action as edge label
#             if current_node.parent:
#                 self.graph.add_edge(str(current_node.parent.state), str(current_node.state), action=current_node.action)

#             # Stop if we've reached the goal node (optional)
#             if self.goal_state and current_node.state == self.goal_state:
#                 break

#             current_node = current_node.parent  # Move to the parent node (backtracking)

#         # Draw the graph
#         self._draw_graph()

#     def _draw_graph(self):
#         """
#         Draw the graph using NetworkX and Matplotlib.
#         """
#         pos = nx.spring_layout(self.graph)  # Layout for positioning the nodes
#         nx.draw(self.graph, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=8, font_weight="bold")
#         edge_labels = nx.get_edge_attributes(self.graph, 'action')
#         nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        
#         plt.title("Search Tree Visualization")
#         plt.show()
