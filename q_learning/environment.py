class CliffEnv():
    def __init__(self):
        self.ncol=12
        self.nrow=4
        self.x=0
        self.y=3


    def step(self,action):
        reward=0
        done=False
        change=[[0,1],[0,-1],[-1,0],[1,0]]
        self.x=max(0,min(self.ncol-1,self.x+change[action][0]))
        self.y=max(0,min(self.nrow-1,self.y+change[action][1]))
        reward-=1
        if self.y==self.nrow-1:
            done=True
            if self.x!=self.ncol-1:
                reward-=100
           


        return self.x,self.y,reward,done

    def reset(self):
        self.x=0
        self.y=0
        return self.x,self.y
    def get(self):
        return self.x,self.y