import numpy as np
from collections import defaultdict
from environment import coloringNinja
import networkx as nx
import matplotlib.pyplot as plt


class QLearningAgent:
    def __init__(self, environment, alpha=0.1, gamma=0.9, epsilon=0.5):
        self.env = environment
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.Q = defaultdict(float)
        self.actions = ["move_left", "move_right", "color"]
        self.transitions = [] 

    def get_state_key(self, state):
       
        return (tuple(state[0]), state[1], state[2])

    def choose_action(self, state, epsilon_greedy=True):
        if epsilon_greedy and np.random.rand() < self.epsilon:
            return np.random.choice(self.actions)
        else:
            q_values = [self.Q[self.get_state_key(state) + (action,)] for action in self.actions]
            return self.actions[np.argmax(q_values)]

    def learn(self, state, action, reward, next_state):
        q_key = self.get_state_key(state) + (action,)
        next_q_key = self.get_state_key(next_state) + (self.choose_action(next_state, epsilon_greedy=False),)
        self.Q[q_key] += self.alpha * (reward + self.gamma * self.Q[next_q_key] - self.Q[q_key])

    def is_terminal(self, state):
        
        goal_state = self.env.getGoalState()
        return state == goal_state

    def print_q_table(self, sorted_by_value=False, top_n=None):
        if sorted_by_value:
            
            sorted_q_table = sorted(self.Q.items(), key=lambda item: item[1], reverse=True)
            if top_n:
                sorted_q_table = sorted_q_table[:top_n]
            for key, value in sorted_q_table:
                print(f"Q[{key}] = {value}")
        else:
           
            for key, value in self.Q.items():
                print(f"Q[{key}] = {value}")

    def train(self, episodes=50, step_limit=50):
        for episode in range(episodes):
            print(f"\n=== Starting Episode {episode+1} ===")
            state = self.env.initialState
            done = False
            rewards = 0
            steps = 0
            while not done:
                print(f"\nCurrent State: {state}")
                
                action = self.choose_action(state)
                print(f"Chosen Action: {action}, Epsilon: {self.epsilon}")
                if action == "move_left":
                    next_state, success = self.env.moveAgent("left")
                    reward = self.env.getReward("move", success)
                elif action == "move_right":
                    next_state, success = self.env.moveAgent("right")
                    reward = self.env.getReward("move", success)
                elif action == "color":
                    next_state, success = self.env.colorCells()
                    if success:
                        reward = self.env.getReward("color", True)
                    else:
                        reward = self.env.getReward("skipped", False)
                print(f"Action Result - Next State: {next_state}, Success: {success}, Reward: {reward}")
                
                self.transitions.append((state, action, next_state))
                
                self.learn(state, action, reward, next_state)
                q_key = self.get_state_key(state) + (action,)
                print(f"Q-value Update: Q[{q_key}] = {self.Q[q_key]}")
                state = next_state
                rewards += reward
                steps += 1
              
                if self.is_terminal(state):
                    print("Goal State Reached! Ending Episode.")
                    done = True
                elif steps >= step_limit:
                    print(f"Step limit of {step_limit} reached. Ending Episode.")
                    done = True
          
            print(f"\n=== Q-Table Summary after Episode {episode+1} ===")
            self.print_q_table(sorted_by_value=True, top_n=5)
           
            self.epsilon = max(0.1, self.epsilon * 0.99)
            print(f"Episode {episode+1} Summary: Total Rewards: {rewards}, Steps: {steps}, Final Epsilon: {self.epsilon}")
        
        # self.draw_search_tree()

    # def draw_search_tree(self):
      
    #     G = nx.DiGraph()
    #     for state, action, next_state in self.transitions:
          
    #         state_key = self.get_state_key(state)
    #         next_state_key = self.get_state_key(next_state)
    #         G.add_node(state_key)
    #         G.add_node(next_state_key)
    #         G.add_edge(state_key, next_state_key, action=action)

       
    #     pos = nx.spring_layout(G)  
    #     plt.figure(figsize=(12, 8))
    #     nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold", edge_color="gray")
    #     edge_labels = nx.get_edge_attributes(G, 'action')
    #     nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    #     plt.title("Q-Learning Search Tree")
    #     plt.show()



ninja = coloringNinja()
q_agent = QLearningAgent(ninja)
q_agent.train(episodes=500)
