import pygame
import sys
import math

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255,0,0)

def is_point_inside_circle(point, circle_center, circle_radius):
    x, y = point
    center_x, center_y = circle_center
    distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
    return distance < circle_radius

def is_position_open(position, place, ind):

    if ind == -1:
        for i in place.emptyPos:
            if is_point_inside_circle(position,place.star_points[i], 40):
                return i,None


    if ind % 2 == 0:
        neighbors = [ind + 1, ind - 1]
    else:
        neighbors = [ind + 1, ind - 1, ind + 2, ind - 2]

    if place.current_player == "Vulture":
        killPlace = [(ind + 3)%10, (ind -3)%10]

        l = (ind + 1)%2
        if killPlace[0] in place.emptyPos and (killPlace[0] - 1 - l)%10 not in place.emptyPos and is_point_inside_circle(position,place.star_points[killPlace[0]], 40):
            place.emptyPos.append((killPlace[0] - 1 - l)%10)
            for crow in place.crows:
                if crow.ind == (killPlace[0] - 1- l)%10: 
                    place.crows.remove(crow)
                    place.killCount+=1
            return killPlace[0],None
        if killPlace[1] in place.emptyPos and (killPlace[1] + 1 + l)%10 not in place.emptyPos and is_point_inside_circle(position,place.star_points[killPlace[1]], 40):
            place.emptyPos.append((killPlace[1] + 1 + l)%10)
            for crow in place.crows:
                if crow.ind == (killPlace[1] + 1 + l)%10: 
                    place.crows.remove(crow)
                    
                    place.killCount+=1
            return killPlace[1],None
            

    for neighbor in neighbors:
        if neighbor%10 in place.emptyPos and is_point_inside_circle(position,place.star_points[neighbor%10], 40):

            return neighbor%10,None

        for crow in place.crows:
            if is_point_inside_circle(position,(crow.x,crow.y), 40):
                return -1, (crow if place.current_player == 'Crow' else place.vulture)


        continue


    return -1,None

class Board:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.center_x = width // 2
        self.center_y = height // (100/40) #35
        self.outer_radius = .3 * height
        self.inner_radius = self.outer_radius * (math.tan(math.radians(18)))

        self.star_points = []
        self.vertex_circles = []  # To store the positions of circles at the vertices
        self.outer_circles = []   # To store the positions of circles at the outer edges

        self.calculate_points()

    def calculate_points(self):
        for i in range(5):
            outer_angle = math.radians(90 + i * 360 / 5)
            inner_angle = math.radians(90 + (i + 0.5) * 360 / 5)

            outer_x = self.center_x + self.outer_radius * math.cos(outer_angle)
            outer_y = self.center_y - self.outer_radius * math.sin(outer_angle)

            inner_x = self.center_x + self.inner_radius * math.cos(inner_angle)
            inner_y = self.center_y - self.inner_radius * math.sin(inner_angle)

            self.star_points.extend([(int(outer_x), int(outer_y)), (int(inner_x), int(inner_y))])


            self.vertex_circles.append((int(inner_x), int(inner_y)))
            self.outer_circles.append((int(outer_x), int(outer_y)))
            
    def display(self, screen):
        pygame.draw.polygon(screen, black, self.star_points, 2)
        pygame.draw.polygon(screen, black, self.vertex_circles, 2)
        # pygame.draw.circle(screen, black, self.outer_circles, 2)
        
        for inner_x, inner_y in self.star_points:
            pygame.draw.circle(screen, black, (int(inner_x), int(inner_y)), 10)
            pygame.draw.circle(screen, black, (int(inner_x), int(inner_y)), 40, 1)  # Adjust the radius as needed

class Crow:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.selected = False
        self.ind = -1

    def move(self, destination):
        self.x, self.y = destination

    def display(self, screen):
        pygame.draw.circle(screen, blue, (self.x, self.y), 35)

class Vulture:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ind = -1


    def move(self, destination):
        self.x, self.y = destination

    def display(self, screen):
        pygame.draw.circle(screen, red, (self.x, self.y), 35)

class Place:
    def __init__(self, star_points, width, height):
        self.star_points = star_points
        self.crows = [Crow(x, height - 50) for x in range(80, 80 + 7 * 80, 80)]
        self.vulture = Vulture(width - 80, height - 50)
        self.width = width
        self.height = height
        self.current_player = 'Crow'  # Initial player
        self.emptyPos = [0,1,2,3,4,5,6,7,8,9]
        self.killCount = 0
        self.CrowOnBoard = 0



    def Draw(self, screen):
        for crow in self.crows:
            crow.display(screen)
        self.vulture.display(screen)

    def switch_player(self):
        self.current_player = 'Vulture' if self.current_player == 'Crow' else 'Crow'

class Game:
    def __init__(self) -> None:
        
        pygame.init()
        self.width, self.height = 1000, 1000
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Star Pentagram Board")

        self.board = Board(self.width, self.height)
        self.place = Place(self.board.star_points, self.width, self.height)
        self.selected = None
        self.winner = None

    def canMoveVulture(self):
        vul = self.place.vulture
        ind = vul.ind
        if vul.ind == -1:
            return True

        if ind % 2 == 0:
            neighbors = [ind + 1, ind - 1]
        else:
            neighbors = [ind + 1, ind - 1, ind + 2, ind - 2]
        
        killPlace = [(ind + 3)%10, (ind -3)%10]
        for neighbor in  neighbors:
            if neighbor%10 in self.place.emptyPos: return True
        for kill in killPlace:
            if kill%10 in self.place.emptyPos: return True

    def gameLogic(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                destination = (mouse_x, mouse_y)
                k,temp = is_position_open(destination, self.place,self.selected.ind)
                if k != -1:
                    if self.selected.ind != -1: 
                        self.place.emptyPos.append(self.selected.ind)
                    self.place.emptyPos.remove(k)
                    self.selected.move(self.place.star_points[k])
                    # self.selected.Draw(self.screen)
                    self.selected.ind = k
                    self.place.switch_player()
                self.selected = temp
            if self.place.killCount > 3:
                self.winner = "Vulture"
                self.selected = None
                return
            elif not self.canMoveVulture():
                self.winner = "Crow"
                self.selected = None
                return
            
    def SetGame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    click = (mouse_x, mouse_y)
                    if self.place.current_player == 'Crow':

                        for crow in self.place.crows:
                            if is_point_inside_circle(click, (crow.x, crow.y), 35):
                                # crow.selected = True
                                if self.place.CrowOnBoard == 7:
                                    self.selected = crow
                                elif crow.ind == -1:
                                    self.selected = crow
                                    self.place.CrowOnBoard += 1
                                break

                    elif self.place.current_player == 'Vulture':
                        if is_point_inside_circle(click, (self.place.vulture.x, self.place.vulture.y), 35):

                            self.selected = self.place.vulture

                while self.selected:
                    self.gameLogic()

                if self.winner:
                    return

            self.screen.fill(white)
            self.board.display(self.screen)
            self.place.Draw(self.screen)
            pygame.display.flip()
        
    def mainMenu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.SetGame()
                        if self.winner: self.displayWinScreen()
                    elif event.key == pygame.K_2:
                        pygame.quit()
                        sys.exit()

            self.screen.fill(white)
            self.drawMainMenu()
            pygame.display.flip()

    def drawMainMenu(self):
        font = pygame.font.Font(None, 36)
        draw_text = lambda text, x, y: self.screen.blit(font.render(text, True, (0, 0, 0)), (x, y))

        draw_text("Main Menu", self.width // 2 - 80, self.height // 4)
        draw_text("1. Start Game", self.width // 2 - 60, self.height // 2)
        draw_text("2. Exit", self.width // 2 - 60, self.height // 2 + 50)

    def displayWinScreen(self):
        font = pygame.font.Font(None, 100)
        draw_text = lambda text, x, y: self.screen.blit(font.render(text, True, (255, 215, 0)), (x, y))
        self.screen.fill(white)
        self.board.display(self.screen)
        self.place.Draw(self.screen)
        WIN = True
        self.place = Place(self.board.star_points, self.width, self.height)
        while WIN:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                        WIN = False
                        break
                        

            winner_text = f"{self.winner} wins!"
            draw_text(winner_text, self.width // (100/40) , self.height // (100/40))
            pygame.display.flip()
        
        self.winner = None
        # pygame.time.delay(3000) 

if __name__ == "__main__":
    game = Game()
    game.mainMenu()
