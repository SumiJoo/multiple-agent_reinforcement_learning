import numpy as np
class Qlearning():
    def __init__(self,epsilon,ncol=12,nrow=4,action=4):
        self.Qnet=np.zeros((ncol,nrow,action))
        self.ncol=ncol
        self.nrow=nrow
        self.epsilon=epsilon
        self.action=action
    def take_action(self,x,y):
        if np.random.random()<self.epsilon:
            return np.random.randint(0,4)
        else:
            return np.argmax(self.Qnet[x][y])
    def update(self,x,y,action,reward,next_x,next_y):
        self.Qnet[x][y][action]=0.9*(reward+np.max(self.Qnet[next_x][next_y]))+0.1*self.Qnet[x][y][action]
    def print(self):
        #change=[[0,1],[0,-1],[-1,0],[1,0]]
        notion_act=['up','down','left','right']
        for j in range(4):
            for i in range(12):
                if j==3 and i in range(11):
                    print('cliff',end=' ')
                elif j==3 and i==11:
                    print('end')
                else:
                    print(notion_act[np.argmax(self.Qnet[i][j])],end=' ')
            print('\n')



