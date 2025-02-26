import  pygame
from  constants import  *
from classes.Post import Post

class Imagepost(Post):
    def __init__(self, image, username, location, description, likes_counter):
        super().__init__(username, location, description, likes_counter)
        self.image = image
        image=pygame.transform.scale(image,(40,70))

    def load_image(self,image):
        pygame.image.load(self.image)


    def display(self, screen):
        screen.blit(self.image)
        super(screen)

