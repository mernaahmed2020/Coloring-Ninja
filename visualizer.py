# from shutil import get_terminal_size
# terminal_width, _ = get_terminal_size()

# _visualizers = {}

# def _default_visualizer(_, state):
#     '''Generic visualizer for unknown problems.'''
#     print(state)

# class Visualizer:
#     '''Visualization and printing functionality encapsulation.'''

#     def __init__(self, problem):
#         '''Constructor with the problem to visualize.'''
#         self.problem = problem
#         self.counter = 0

#     def visualize(self, frontier):
#         '''Visualizes the frontier at every step.'''
#         self.counter += 1
#         print(f'Frontier at step {self.counter}')
#         for node in frontier:
#             print()
#             _visualizers.get(type(self.problem), _default_visualizer)(self.problem, node.state)
#         print('-' * terminal_width)