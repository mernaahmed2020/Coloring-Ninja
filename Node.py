class Node:
    '''Node data structure for search space bookkeeping.'''

    def __init__(self, state, parent, action, path_cost, heuristic=0):
        '''Constructor for the node state with the required parameters.'''
        self.state = state 
        self.parent = parent  
        self.action = action  #move to reach this state
        self.path_cost = path_cost  #pallet cost for now
        self.heuristic = heuristic 
        self.totalCost = path_cost + heuristic  

    @classmethod
    def root(cls, init_state):
        '''Factory method to create the root node.'''
        return cls(init_state, None, None, 0)

    @classmethod
    def child(cls, problem, parent, action):
        '''Factory method to create a child node.'''
        newState = problem.result(parent.state, action)  #the next state
        path_cost = parent.path_cost + problem.step_cost(parent.state, action)  # path cost to reach the state
        heuristic = problem.heuristic(new_state)  ##for the heursitc
        return cls(newState, parent, action, path_cost, heuristic)


def solution(node):
    '''A method to extract the sequence of actions representing the solution from the goal node.'''
    actions = []
    cost = node.path_cost
    while node.parent is not None:
        actions.append(node.action)
        node = node.parent
    actions.reverse()
    return actions, cost
