#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 00:38:09 2018

@author: fabrizio
"""
import random
        
class Board(object):

    def __init__(self, pools, agents, tau=1, time_steps=100):
        '''
        pools: list of Pool objects
        agents: list of Agent objects
        tau: cost of switching pool (>0)
        time_steps: number of iterations (int)
        '''
        self.pools = pools
        self.agents = agents
        self.tau = tau
        self.time_steps = time_steps
    
    def assign_agents_random(self):
        '''start board game with agents randomly placed in the pools'''
        for agent in self.agents:
            pool = random.choice(self.pools)
            pool.add_agent(agent)
         
    def update_pools(self):
        '''choose the new pool affiliation for all the agents'''
        for agent in self.agents:
            new_pool = agent.pick_pool(self.pools)
            old_pool = agent.current_pool
            if new_pool != old_pool:
                old_pool.remove_agent(agent)
                new_pool.add_agent(agent)
                agent.pool_switches_history.append(1)
                
    def update_payment(self):
        for pool in self.pools:
            pool.pay_to_agents()                
               
    def run_game(self):
        for step in range(self.time_steps):
            self.update_pools()
            self.update_payment()