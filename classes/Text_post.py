import  pygame
from classes.Post import *
from constants import *

class Text_post(Post):
    def __init__(self,text,text_color,background_color,username, location, description, likes_counter):
        super().__init__(username, location, description, likes_counter)
        self.background_color = background_color
        self.text_color = text_color
        self.text = text

    def display(self, screen):
        screen.blit(self.background_color)
        screen.blit(self.text)
        super(screen)