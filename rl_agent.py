import numpy as np

class RLAgent:
    def __init__(self):
        self.q_table = {}
        self.alpha = 0.1   # learning rate
        self.gamma = 0.9   # discount factor

    def get_q(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def update(self, state, action, reward):
        current_q = self.get_q(state, action)

        new_q = current_q + self.alpha * (reward - current_q)

        self.q_table[(state, action)] = new_q

    def rank_actions(self, state, actions):
        scored = [(a, self.get_q(state, i)) for i, a in enumerate(actions)]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [x[0] for x in scored]