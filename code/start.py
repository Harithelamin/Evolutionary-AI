
from datetime import datetime


def Gym1():
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
    from email import policy
    import gym
    env = gym.make("LunarLander-v2", render_mode="human")
    observation, info = env.reset(seed=42)
    for _ in range(1000):
        action = policy(observation)  # User-defined policy function
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            observation, info = env.reset()
    env.close()

def Gym3():
    import gym
    import gnwrapper
    env = gnwrapper.Monitor(gym.make('CartPole-v1'))         
    obs = env.reset()
    for _ in range(100):
        o, r, d, i = env.step(env.action_space.sample())
        if d:
            env.reset()
    env.display()
if __name__ == "__main__":
    print("we start the test", datetime.now().strftime("%D%M%Y%H:%M:%S"))
    Gym3()
