#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 00:37:22 2018

@author: fabrizio
"""
import random

class Agent(object):

    def __init__(self, initial_pool=None):
        self.coins_history = []
        self.pool_switches_history = []
        self.current_pool = initial_pool
    
    @property    
    def coins(self):
        '''total number of coins accumulated'''    
        return sum(self.coins_history)
        
    @property
    def pool_switches(self):
        '''total number of switches'''
        return sum(self.pool_switches_history)
        
        
class RandomAgent(Agent):
    '''Strategy: pick a pool each time with uniform probability'''
    def pick_pool(self, pools):
        return random.choice(pools)
        

class LowAgent(Agent):
    '''Strategy: pick always the low pool'''
    def pick_pool(self, pools):
        for pool in pools:
            if pool.type == 'low':
                return pool
                 

class StableAgent(Agent):
    '''
    Strategy: pick always in the stable pool
    '''
    def pick_pool(self, pools):
        for pool in pools:
            if pool.type == 'stable':
                return pool
                
                
class HighAgent(Agent):
    '''
    Strategy: pick always in the stable pool
    '''
    def pick_pool(self, pools):
        for pool in pools:
            if pool.type == 'high':
                return pool











        
        