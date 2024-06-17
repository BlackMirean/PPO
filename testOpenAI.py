import gym

env1 = gym.make('CartPole-v1', render_mode='human')

for i_episode in range(20):
    observation = env1.reset()
    for t in range(200):
        env1.render()
        print(observation)
        action = env1.action_space.sample()
        observation, reward, done, info, _ = env1.step(action)
        if done:
            print("Episode finished after{} timesteps".format(t + 1))
            break
