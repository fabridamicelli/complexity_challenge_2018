# complexity_challenge_2018

Python code to run an agent based implementation of the game proposed in the 2018 edition of the Santa Fe Institute Complexity Challenge (https://www.complexityexplorer.org/challenges/2-spring-2018-complexity-challenge/submissions).

At each time step, each agent must decide to locate at one of three possible pools (investing options). 
These pools are called: stable, high, and low. 
Agents must choose their pool without knowing what the other agents have picked, and can only rely on 
information from prior time steps (in particular, each agent must make their choice knowing only the number
of agents (but not their identity) that located at each pool and each pool's payoff for all prior time steps). 
Agents are allowed to switch pools at the start of any time step, but to do so costs the agent a payment 
of tau (where 0 <= tau). Initial pool choice costs nothing.
