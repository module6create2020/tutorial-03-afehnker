import random
import pygame
import math


class Bubble:
    x = 0
    y = 0

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.dx = random.uniform(-1,1)
        self.dy = random.uniform(-1,1)
        self.color = color
        self.diameter = 50

    def __del__(self):
        print(self.identify()+" has been deleted")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.color == other.color

    def identify(self):
        return ("Bubble("+str(self.x)+","+str(self.y)+")")

    def move(self, x0, y0, xf, yf):
        self.x += self.dx
        self.y += self.dy
        if self.x<x0 and self.dx < 0:
            self.dx = - self.dx
        if self.y < y0 and self.dy < 0:
            self.dy = - self.dy
        if self.x > xf and self.dx > 0:
            self.dx = - self.dx
        if self.y > yf and self.dy > 0:
            self.dy = - self.dy

    def display(self, screen, font):
        pygame.draw.ellipse(screen, self.color, [[self.x, self.y], [50, 50]])
        text = font.render("!", True, (255, 255, 255))
        screen.blit(text, (self.x + 22, self.y + 12))

    def collide(self, other):
        dist_now = math.sqrt(math.pow(self.x-other.x,2)+math.pow(self.y-other.y,2))
        dist_next = math.sqrt(math.pow(self.x+self.dx-other.x-other.dx,2)+math.pow(self.y+self.dy-other.y-other.dy,2))
        minDist = (self.diameter + other.diameter) / 2

        if not(self is other) and dist_now < minDist and dist_next < dist_now:
            numerator = (self.dx - other.dx) * (self.x - other.x) + (self.dy - other.dy) * (self.y - other.y)
            denominator = math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2)
            temp1dx = self.dx - numerator / denominator * (self.x - other.x)
            temp1dy = self.dy - numerator / denominator * (self.y - other.y)
            temp2dx = other.dx - numerator / denominator * (other.x - self.x)
            temp2dy = other.dy - numerator / denominator * (other.y - self.y)

            self.dx = temp1dx
            self.dy = temp1dy
            other.dx = temp2dx
            other.dy = temp2dy



