import matplotlib.pyplot as plt
import numpy as np
import subprocess as sp

class vector:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.CalAngle = {
                            "E":(1.0,0),
                            "NE":(1/np.sqrt(2),1/np.sqrt(2)),
                            "N":(0,1.0),
                            "NW":(-1/np.sqrt(2),1/np.sqrt(2)),
                            "W":(-1.0,0),
                            "SW":(-1/np.sqrt(2),-1/np.sqrt(2)),
                            "SE":(1/np.sqrt(2),-1/np.sqrt(2)),
                            "S":(0,-1.0)
                        }
        self.path = [[0],[0]]
        pass
    
    def AddDistance(self,distance, direction):
        angle = self.CalAngle[direction] 
        self.x += distance * angle[0]
        self.y += distance * angle[1]
        self.path[0].append(self.x)
        self.path[1].append(self.y)


    def printCoord(self):
        print(self.x, self.y)
        print(self.path)


    def plot_movement(self):
        
        plt.plot(self.path[0], self.path[1], marker='o', linestyle='-',zorder = 1)
        plt.scatter(self.path[0][0], self.path[1][0], color='red', label='Starting Point',zorder = 2)
        plt.scatter(self.path[0][-1], self.path[1][-1], color='green', label='Last Point',zorder = 2)
        plt.legend()
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('2D Movement Plot')
        plt.grid(True)
        plt.show()

def main():
    v = vector()

    commands = []

    while True:
        distance = float(input("Enter distance (0 to stop): "))
        if distance == 0:
            break
        print()
        direction = input("Enter direction (N, NE, E, SE, S, SW, W, NW): ").upper()
        # print()
        tmp = sp.call('clear', shell=True)
        commands.append((distance, direction))

    tmp = sp.call('clear', shell=True)

    for distance,direction in commands:
        v.AddDistance(distance,direction)

    # v.printCoord()
    v.plot_movement()

if __name__ == "__main__":
    main()