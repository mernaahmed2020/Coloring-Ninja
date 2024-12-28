import numpy as np
from collections import defaultdict
from environment import coloringNinja

class QLearningAgent:
    def __init__(self, environment, alpha=0.1, gamma=0.9, epsilon=0.5):
        self.env = environment
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.Q = defaultdict(float)
        self.actions = ["move_left", "move_right", "color"]

    def get_state_key(self, state):
        # Convert state to a hashable key for Q-table
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
        # Check if the current state matches the goal state
        goal_state = self.env.getGoalState()
        return state == goal_state

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

                self.learn(state, action, reward, next_state)

                q_key = self.get_state_key(state) + (action,)
                print(f"Q-value Update: Q[{q_key}] = {self.Q[q_key]}")

                state = next_state
                rewards += reward
                steps += 1

                # Check if the current state is terminal or step limit is reached
                if self.is_terminal(state):
                    print("Goal State Reached! Ending Episode.")
                    done = True
                elif steps >= step_limit:
                    print(f"Step limit of {step_limit} reached. Ending Episode.")
                    done = True

            # Decay epsilon after each episode
            self.epsilon = max(0.1, self.epsilon * 0.99)

            print(f"Episode {episode+1} Summary: Total Rewards: {rewards}, Steps: {steps}, Final Epsilon: {self.epsilon}")


# Initialize and train the Q-learning agent
ninja = coloringNinja()
q_agent = QLearningAgent(ninja)
q_agent.train(episodes=500)
