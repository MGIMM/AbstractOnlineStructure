from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any
import os
import pickle

@dataclass
class Entity:
    def __post_init__(self):
        self.attrs_ = {}

    def save(self, path):
        dirname = os.path.abspath(os.path.dirname(path))
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        
        with open(path, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def load(cls, path):
        return pickle.load(open(path, "rb"))
    
    def throw(self, err, msg):
        raise err(f"class {self.__class__.__name__}: {msg}")

    @property
    def attrs(self):
        return self.attrs_

@dataclass
class Base(Entity, ABC):
    def __post_init__(self):
        super().__post_init__()
    
    @classmethod
    def __init_subclass__(cls, *args, **kwargs):
        super().__init_subclass__(*args, **kwargs)

@dataclass
class AbstractAgent(Base):
    @abstractmethod
    def __call__(self, obs: Any) -> Any:
        """obs -> agent -> action"""
        ...

@dataclass
class AbstractEnv(Base):
    @abstractmethod
    def observation(self) -> Any:    
        ...

    @abstractmethod
    def step(self) -> Any:    
        ...

    @property
    @abstractmethod
    def state(self):
        ...

    @abstractmethod
    def update(self):    
        ...