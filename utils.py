# def solution(goal_node):
#     """
#     Extracts the solution path and total cost from the goal node.
    
#     :param goal_node: The goal Node object containing the solution path.
#     :return: A tuple containing a list of actions to reach the goal and the total cost.
#     """
#     actions = []
#     total_cost = goal_node.path_cost
#     current_node = goal_node

#     # Traverse the path from the goal node to the root node
#     while current_node.parent is not None:
#         actions.insert(0, current_node.action)  # Insert actions in reverse order (from root to goal)
#         current_node = current_node.parent

#     return actions, total_cost