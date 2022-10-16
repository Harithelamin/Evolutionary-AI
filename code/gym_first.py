#https://www.gymlibrary.dev/
#pip install gym
#pip install --upgrade pip
#pip install gym[box2d]
#pip uninstall gym
#pip install gym[box2d]
#python.exe -m pip install --upgrade pip
#pip install gym[box2d] pygame      

from os import environ      
from gym.utils.env_checker import check_env
check_env(environ)

import gym
env = gym.make("LunarLander-v2", render_mode="human")
env.action_space.seed(42)

observation, info = env.reset(seed=42)

for _ in range(1000):
    observation, reward, terminated, truncated, info = env.step(env.action_space.sample())

    if terminated or truncated:
        observation, info = env.reset()

env.close()   