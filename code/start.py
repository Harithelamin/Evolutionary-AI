from datetime import datetime
from email import policy
from time import time


def Gym():
    import gym
    import matplotlib.pyplot as plt
    env = gym.make("CartPole-v1")
    observation, info = env.reset(seed=42)

    for _ in range(1000):
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()
    env.close() 
    print(observation)
    plt.plot(observation, label='Obs')
    plt.legend()
    plt.show()

def Gym2():
    import gym
    from gym.envs import box2d
    env = gym.make("LunarLander-v2", render_mode="human")
    observation, info = env.reset(seed=42)
    for _ in range(1000):
        action = policy(observation)  # User-defined policy function
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()
    env.close() 





if __name__ == "__main__":
    print("we start the test", datetime.now().strftime("%D%M%Y%H:%M:%S"))
    Gym()
    Gym2()
