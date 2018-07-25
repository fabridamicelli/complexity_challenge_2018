#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 15:21:52 2018

@author: fabrizio
"""
import random


class Pool:

    def __init__(self, pool_type=None):
        assert pool_type in ['low', 'stable', 'high']
        self.type = pool_type
        self.agents = []
        # Track pool number of agents and payoffs
        self.occupation_history = []
        self.payoffs_history = []

    def __contains__(self, agent):
        '''check if agent is in Pool with "in" operator'''
        return agent in self.agents

    def __len__(self):
        '''define len(Pool) as number of agents in it'''
        return len(self.agents)

    def add_agent(self, agent):
        self.agents.append(agent)
        agent.current_pool = self

    def remove_agent(self, agent):
        self.agents.remove(agent)
        agent.current_pool = None

    @property
    def payout(self):
        if self.type == 'low':
            payoff = 40/len(self.agents)
            return payoff if random.random() < 0.5 else 0

        elif self.type == 'stable':
            return 1

        elif self.type == 'high':
            payoff = 80/len(self.agents)
            return payoff if random.random() < 0.25 else 0

    def pay_to_agents(self):
        payment = self.payout
        for agent in self.agents:
            agent.coins_history.append(payment)
        # Track pool record
        self.payoffs_history.append(payment)
        self.occupation_history.append(len(self.agents))
