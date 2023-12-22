from dataclasses import dataclass
from typing import Any, List
from .abstract import AbstractAgent, AbstractEnv


@dataclass
class Agent(AbstractAgent):
    def __call__(self, obs):
        return self.act(obs) if obs is not None else None

    def act(self, obs):
        ...
    
@dataclass
class PipelineAgent(Agent):
    agents:List

    def act(self, obs):
        actions = dict()
        for agent in self.agents:
            action = agent(obs)
            if action is not None:
                obs.update(action)
                actions.update(action)
        return actions

@dataclass
class Env(AbstractEnv):
    data_stream: Any = None

    def __post_init__(self):
        super().__post_init__()
        if self.data_stream is not None:
            self.iter_ = iter(self.data_stream)
        self.state_ = {}

    def observation(self):
        if self.data_stream is not None:
            self.state_.update(next(self.iter_))
        return self.state_ 
    
    def step(self):
        try:
            obs = self.observation()
            done = False
        except StopIteration:
            obs = None
            done = True
        return obs, done
    
    @property
    def state(self):
        return self.state_

    def update(self, action):
        if action is not None:
            self.state.update(action)

def train(agent, env):
    done = False
    while not done:
        obs, done = env.step()
        action = agent(obs)
        env.update(action)