import matplotlib.pyplot as plt
import numpy as np
import subprocess as sp

class Dis:
    def __init__(self) -> None:
        self.unit = {"mm" :0.001, "cm" :0.01, "m" :1, "km": 1000}
        pass


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

    def printRelative(self):
        deg = np.degrees(np.arctan2(self.y,self.x))
        print("The final destination is ",end='')
        if -22.5 <= deg <=22.5:
            print("E",end=' ')
        elif 22.5 <= deg <=67.5:
            print("NE",end=' ')
        elif 67.5 <= deg <=112.5:
            print("N",end=' ')
        elif 112.5 <= deg <=157.5:
            print("NW",end=' ')
        elif 157.5 <= deg <=180 or -180 <= deg <= -157.5:
            print("W",end=' ')
        elif -157.5 <= deg <= -112.5:
            print("SW",end=' ')
        elif -112.5 <= deg <= -67.5:
            print("S",end=' ')
        else:
            print("SE",end=' ')
        print("of the Starting point")
        
        pass

def main():
    v = vector()

    commands = []
    dis = Dis()
    print("Enter distance and direction (\"0 0\"to stop):\n(press ENTER after every command)")
    while True:
        try:
            distance,direction = input().split()
        except:
            print("INVALID INPUT")
            continue
        # print(distance,direction)
        direction = direction.upper()
        if distance == '0':
            break
        index = next((i for i, c in enumerate(distance) if not c.isdigit()), None)

        if index is None:
            raise ValueError

        distance_str, unit = distance[:index], distance[index:].lower()

        try:
            print(distance_str,unit)
            distance = float(distance_str)
            distance *= dis.unit[unit]
        except Exception as e:
            print(f"{e} INVALID DISTANCE")
            continue
        if(direction not in ["N","NE","NW","E","W","S","SE","SW"]):
            print("INVALID DIRECTION")
            continue

        commands.append((distance, direction))

    tmp = sp.call('clear', shell=True)

    for distance,direction in commands:
        v.AddDistance(distance,direction)

    # v.printCoord()
    v.printRelative()
    v.plot_movement()

if __name__ == "__main__":
    main()