import numpy as np
import random 
from random import randint

class EnvGrid(object):

    def __init__(self):
        super(EnvGrid , self).__init__()

        self.grid = [
            [0 , 0 , 1] ,
            [0 , -1 , 0] , 
            [0 , 0 , 0] 
        ]

        #Position start
        self.y = 2
        self.x = 0

        #Action
        self.actions = [
            [-1 , 0] , #Up
            [1 , 0] , #down
            [0 , -1] , #left
            [0 , 1] #Right
        ]

    def reset(self):
       self.y = 2
       self.x = 0

       return (self.y * 2 + self.x + 1)
    
    def step(self , action):
        self.y = max(0 , min(self.y + self.actions[action][0] , 2))
        self.x = max(0 , min(self.x + self.actions[action][1] , 2))

        return (self.y * 3 + self.x + 1) , self.grid[self.y][self.x]
    
    def show(self):

        print('--------------------------------')
        y = 0
        for line in self.grid:
            x = 0
            for pt in line:
                print("%s\t" % (pt if y != self.y or x != self.x else 'X'))
                x +=1
            y += 1
            print("")

    def over(self):
        return self.grid[self.y][self.x] == 1
    

def take_actions(st , Q , eps):
    if random.uniform(0 , 1) < eps:
        action = randint(0 , 3)
    else:
        action = np.argmax(Q[st])
    return action

if __name__ == '__main__':
    env = EnvGrid()
    st = env.reset()

    Q = [
        [0 , 0 , 0 , 0],
        [0 , 0 , 0 , 0],
        [0 , 0 , 0 , 0],
        [0 , 0 , 0 , 0],
        [0 , 0 , 0 , 0],
        [0 , 0 , 0 , 0],
        [0 , 0 , 0 , 0],
        [0 , 0 , 0 , 0],
        [0 , 0 , 0 , 0],
        [0 , 0 , 0 , 0]    
    ]

    for _ in range(100):
        #Reset game
        st = env.reset()
        while not env.over():
            env.show()
            at = int(input("--"))
            #at = take_actions(st , 0 , 0.1)

            stp1 , r = env.step(at)
            print("s" , stp1)
            print("r" , r)

            #atp1 = take_actions(stp1 , 0 , 0.0)
            #Q[st][at] = Q[st][at] + 0.1 * (r + 0.9 * Q[stp1][atp1] - Q[st][at])

        st = stp1

    for s in range(1 , 10):
        print(s , Q[s])

