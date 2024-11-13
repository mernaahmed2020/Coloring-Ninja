class Problem:
    '''
    Abstract base class for problem formulation.
    It declares the expected methods to be used by a search algorithm.

    '''

    def __init__(self,enviroment):
        '''Constructor that initializes the problem. Typically used to setup the initial state and, if applicable, the goal state.'''
        self.enviroment = enviroment
        self.init_state = enviroment.getState()
        self.goalstate = enviroment.getGoalState()
        self.stateSpaceSize = stateSpaceSize
    

    def actions(self, state):
        '''Returns an iterable with the applicable actions to the given state.'''
        raise NotImplementedError

    def result(self, state, action):
        '''Returns the resulting state from applying the given action to the given state.'''
        raise NotImplementedError

    def goal_test(self, state):
        '''Returns whether or not the given state is a goal state.'''
        raise NotImplementedError

    def step_cost(self, state, action):
        '''Returns the step cost of applying the given action to the given state.'''
        raise NotImplementedError