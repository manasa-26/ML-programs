import numpy as np
# Initialize the Q-table to a 5x5 matrix of zeros:
Q = np.zeros([5, 5])
# Set the gamma parameter and alpha:
gamma = 0.8
alpha = 0.9
# Define the reward matrix:
R = np.array([[0, 0, 0, 0, 100],
              [0, 0, 0, 100, -100],
              [0, 0, 0, 100, -100],
              [0, 100, 100, 100, 100],
              [100, -100, -100, 100, 100]])
# Training phase:
for episode in range(100):
    # Randomly pick a state:
    state = np.random.randint(0, 5)
    while state != 4: # While the goal state has not been reached...
        # Select any action from the current state:
        action = np.random.randint(0, 5)
        # Update the Q-value for the current state-action pair:
        Q[state, action] = R[state, action] + gamma * max(Q[action, :])
        # Update the current state:
        state = action
# Normalize the Q-table:
Q /= np.max(Q)
print(Q)
