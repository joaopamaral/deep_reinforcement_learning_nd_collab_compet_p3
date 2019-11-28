[//]: # (Image References)

[image1]: https://user-images.githubusercontent.com/10624937/42135623-e770e354-7d12-11e8-998d-29fc74429ca2.gif "Trained Agent"
[image2]: https://user-images.githubusercontent.com/10624937/42135622-e55fb586-7d12-11e8-8a54-3c31da15a90a.gif "Soccer"

# Udacity Deep Reinforcement Learning Nanodegree

# Project 3: Collaboration and Competition

### Introduction

For this project, an agent is trained to work with the [Tennis](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Examples.md#tennis) environment.

![Trained Agent][image1]

In this environment, two agents control rackets to bounce a ball over a net. If an agent hits the ball over the net, it receives a reward of **+0.1**.  If an agent lets a ball hit the ground or hits the ball out of bounds, it receives a reward of **-0.01**.  Thus, the goal of each agent is to keep the ball in play.

- Agent Reward Function (independent):
  - +0.1 To agent when hitting ball over net.
  - -0.1 To agent who let ball hit their ground, or hit ball out of bounds.

The observation space consists of **8 variables** corresponding to the position and velocity of the ball and racket. Each agent receives its own, local observation.  **2 continuous** actions are available, corresponding to movement toward (or away from) the net, and jumping. 

- Behavior Parameters:
  - Vector Observation space: 
    - 8 variables corresponding to position and velocity of ball and racket.
  - Vector Action space: 
    - (Continuous) Size of 2, corresponding to movement toward net or away from net, and jumping.

### Multi Agent Learning

This environment works with two agents playing during an episode. Both agents have the same objective and this allows us to work with only one Agent model and use both agents interact with the environment to make the agent learn and improve our model.

### Solving the Environment

The task is episodic, and in order to solve the environment, your agents must get an average score of +0.5 (over 100 consecutive episodes, after taking the maximum over both agents). Specifically,

- After each episode, we add up the rewards that each agent received (without discounting), to get a score for each agent. This yields 2 (potentially different) scores. We then take the maximum of these 2 scores.
- This yields a single **score** for each episode.

The environment is considered solved, when the average (over 100 episodes) of those **scores** is at least `+0.5`.

### Getting Started

1. Download the environment from one of the links below.  You need only select the environment that matches your operating system:
    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Linux.zip)
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86_64.zip)
    
    (_For Windows users_) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

    (_For AWS_) If you'd like to train the agent on AWS (and have not [enabled a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md)), then please use [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Linux_NoVis.zip) to obtain the "headless" version of the environment.  You will **not** be able to watch the agent without enabling a virtual screen, but you will be able to train the agent.  (_To watch the agent, you should follow the instructions to [enable a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md), and then download the environment for the **Linux** operating system above._)

2. Place the file in the DRLND GitHub repository, in the `p3_collab-compet/` folder, and unzip (or decompress) the file. 

## Dependencies

To set up your python environment to run the code in this repository, follow the instructions below.

1. Create (and activate) a new environment with Python 3.6.

	- __Linux__ or __Mac__: 
	```bash
	conda create --name drlnd python=3.6
	source activate drlnd
	```
	- __Windows__: 
	```bash
	conda create --name drlnd python=3.6 
	activate drlnd
	```

2. Install all dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

3. Install Pytorch version 0.4.0 with your correct Cuda version (in my case, I'm using cuda 10.0).

```bash
conda install -n drlnd pytorch=0.4.0 cudatoolkit=10.0 -c pytorch
```

4 - Create an IPython kernel for the drlnd environment.

```bash
python -m ipykernel install --user --name drlnd --display-name "drlnd"
```

### Instructions

Follow the instructions in `Report.ipynb` to get started with training the agent!

### Result

In episode **941** (and after 30:01 minutes training in a local machine using GPU), the agent achieved the expected result 👍 (moving avg > 0.5).

![Result](assets/result_plot.png)

So let's see what happen to the agent:

| We started with a random agent  | After 941 episodes agents were able to play for a long time  |
|---|---|
| <img src="assets/random_agent.gif" width="400">  |  <img src="assets/trained_agent.gif" width="400"> |