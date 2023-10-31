#testrun to check why as the jupyter scripts displays the line below twice
# line of speaking: display(plotQtable(Qtable_frozenlake))  # <=========== todo: plot anpassen mit state & action beschreibung
# todo: how to plot display() in this script (in comparison to a jupyter NB)

import gym
import time
import matplotlib.pyplot as plt
import numpy as np
import random
from tqdm.notebook import trange
from gym.envs.toy_text.frozen_lake import generate_random_map
from IPython.display import clear_output, display

# env=gym.make('FrozenLake-v1', desc=generate_random_map(size=8)) #for random map

desc=["SFFF", "FHFH", "FFFH", "HFFG"] # modify for different environment: S=Start, F=Frozen, H=Hole, G=Goal
env=gym.make("FrozenLake-v1",map_name="4x4",desc=desc,is_slippery=False)

env.reset()
env.render()

def plotQtable(data=np.zeros((16,4))) :  # data = 2d array describing the actions/state correlation  
    clear_output(wait=True)
    fig, ax = plt.subplots()
    ax.table(cellText=data, loc='center')
    return fig
    # print(f"printed the display")   # debugging
    # display(fig, display_id="qtable")
    
def updateQtablePlot(Udata=np.zeros((16,4))):    # updates q-table, resets if no data is given
    fig, ax = plt.subplots()
    clear_output(wait=True)
    ax.table(cellText=Udata, loc='center')
    display(fig,display_id="qtable")

    
def epsilon_greedy_policy(Qtable, state, epsilon):
  """
  acting policy
  1. Generates random number between 0 & 1
  2. if number greater than epsilon -> exploitation (action with highest value to the current state) 
  3. else -> exploration (random action)
  """
  random_int = random.uniform(0,1)
  if random_int > epsilon:
    action = np.argmax(Qtable[state])
  else:
    action = env.action_space.sample()
  return action

def greedy_policy(Qtable, state):
  """
  updating policy
  """
  action = np.argmax(Qtable[state]) # the action that the agent should take in order to maximize its reward
  return action



state_space = env.observation_space.n
action_space = env.action_space.n
print(f"state: {state_space}, action: {action_space}")

Qtable_frozenlake = np.zeros((state_space, action_space)) # create a 16 x 4 Array for the q-table
# 16x4 so it has a value for every state/action-pair
display(plotQtable(Qtable_frozenlake))  # <=========== todo: plot anpassen mit state & action beschreibung
# each row represents a state from 0 to 15 (for a 4x4 map see variable "desc") and each column the actions right, left, up & down

while 1:
   continue