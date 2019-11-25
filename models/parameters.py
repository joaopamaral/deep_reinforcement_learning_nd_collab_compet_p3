import torch

BUFFER_SIZE = int(1e5)      # replay buffer size
BATCH_SIZE = 128            # minibatch size
GAMMA = 0.99                # discount factor
TAU = 1e-3                  # for soft update of target parameters
LR_ACTOR = 4e-4             # learning rate of the actor
LR_CRITIC = 2e-4            # learning rate of the critic
WEIGHT_DECAY = 0            # L2 weight decay

LEARN_STEPS = 1             # Lear evey N steps
N_UPDATES = 1               # Number of updates that will be realize in learn step

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


def check_device():
    """Print the device"""
    print(f'Using device: {device}')
