import math
import pygame

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255,0,0)

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
