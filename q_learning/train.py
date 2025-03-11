from environment import CliffEnv
from q_learning import Qlearning
import copy
import numpy as np
import matplotlib.pyplot as plt

model=Qlearning(epsilon=0.1)
env_=CliffEnv()
total_epi=10000
total_rewardss=[]
for i in range(int(total_epi/10)):
    rewardss=[]
    for j in range(10):
        env_.reset()
        rewards=0
        done=False
        while done is not True:
            x,y=env_.get()
            action=model.take_action(x,y)
            next_x,next_y,reward,done=env_.step(action)
            rewards+=reward
            model.update(x,y,action,reward,next_x,next_y)
        rewardss.append(rewards)
    total_rewardss.append(np.mean(rewardss))
model.print()
plt.plot(list(range(len(total_rewardss))),total_rewardss)
plt.show()





















