#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 00:33:41 2018

@author: fabrizio
"""
import numpy as np
from matplotlib import pyplot as plt

from pools import Pool
from agents import RandomAgent, LowAgent, HighAgent, StableAgent
from board import Board

###########    Simulation only with RandomAgents (sanity check)   ###########

# Define basic parameters
NUM_AGENTS = 99
TOTAL_TIME = 100
TAU = 0.5  # switching cost

# Create pool & agents
pools = [Pool('low'), Pool('stable'), Pool('high')]
agents = [RandomAgent() for _ in range(NUM_AGENTS)]

# Set board and run
board = Board(pools, agents, tau=TAU, time_steps=TOTAL_TIME)        
board.assign_agents_random()
board.run_game()        

        

###########    Plot and save results      ###########
plt.style.use('ggplot')  # just aesthetics

# Plot pools statistics
plt.figure(figsize=(16,8))

plt.subplot(231)
plt.title('pools occupation history')
plt.xlabel('steps')
plt.ylabel('# agents')
for pool in pools:
    plt.plot(pool.occupation_history, label=pool.type)
# Plot prediction (assuming only presence of RandomAgents)
plt.axhline(y=NUM_AGENTS/3, color='green', linestyle='--', linewidth=5,
            label='theoretical expectation')
plt.legend()


plt.subplot(232)
plt.title('pools payoff history')
plt.xlabel('steps')
plt.ylabel('payoff')
for pool in pools:
    plt.plot(pool.payoffs_history, 'o', label=pool.type)
plt.legend()


plt.subplot(233)
plt.title('pools payoff history')
plt.xlabel('payoff')
plt.ylabel('frequency')
for pool in pools:
    plt.hist(pool.payoffs_history, 
             histtype='step', 
             linewidth=3,
             label=pool.type)
plt.legend()


plt.subplot(234)
plt.title('total payoff per agent')
plt.xlabel('payoff')
plt.ylabel('frequency')
plt.hist([agent.coins for agent in agents])
# Prediction
E_coins_per_agent = ((120/NUM_AGENTS) + 1) * TOTAL_TIME / 3 
plt.axvline(x=E_coins_per_agent, color='green', linestyle='--', linewidth=5,
            label='theoretical expectation')
plt.legend()


plt.subplot(235)
plt.title('total payoff-cost per agent')
plt.xlabel('balance')
plt.ylabel('frequency')
payoffs = np.array([agent.coins for agent in agents]) 
costs = np.array([agent.pool_switches for agent in agents]) * TAU
balance = payoffs - costs 
plt.hist(balance)


# Prediction
plt.subplot(236)
plt.title('total number of switches per agent')
plt.xlabel('# switches')
plt.ylabel('frequency')
plt.hist([agent.pool_switches for agent in agents])
# Prediction
plt.axvline(x=2 * TOTAL_TIME / 3, color='green', linestyle='--', linewidth=5,
            label='theoretical prediction')
plt.legend()

plt.tight_layout()
plt.savefig('random_agents')
plt.close()
