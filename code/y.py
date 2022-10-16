env = gym.make("MountainCar-v0")
observation = env.reset() 

# Object's type in the action Space
print("The Action Space is an object of type: {0}\n".format(env.action_space))
# Shape of the action Space
print("The shape of the action space is: {0}\n".format(env.action_space.n))
# Object's type in the Observation Space
print("The Environment Space is an object of type: {0}\n".format(env.observation_space))
# Shape of the observation space
print("The Shape of the dimension Space are: {0}\n".format(env.observation_space.shape))
# The high and low values in the observation space
print("The High values in the observation space are {0}, the low values are {1}\n".format(
    env.observation_space.high, env.observation_space.low))
# Minimum and Maximum car position
print("The minimum and maximum car's position are: {0}, {1}\n".format(
    env.observation_space.low[0], env.observation_space.high[0]))
# Minimum and Maximum car velocity
print("The minimum and maximum car's velocity are: {0}, {1}\n".format(
    env.observation_space.low[1], env.observation_space.high[1]))
# Example of observation
print("The Observations at a given timestep are {0}\n".format(env.observation_space.sample()))