import pygame as pg

class Pelota:
    def __init__(self, x, y, vx, vy, color, tamano):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.tamano = tamano

        self.imagen = pg.Surface((self.tamano, self.tamano))
        self.imagen.fill(self.color)

  
    
    @property
    def right(self):
        rect = pg.Rect(self.x, self.y, self.tamano, self.tamano)
        return rect.right
    
    @property
    def left(self):
        rect = pg.Rect(self.x, self.y, self.tamano, self.tamano)
        return rect.left

    @property
    def top(self):
        rect = pg.Rect(self.x, self.y, self.tamano, self.tamano)
        return rect.top

    @property
    def bottom(self):
        rect = pg.Rect(self.x, self.y, self.tamano, self.tamano)
        return rect.bottom