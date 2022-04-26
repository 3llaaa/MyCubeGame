import pygame

pygame.init()

#set up the game display
window = pygame.display.set_mode(600, 400)
pygame.display.set_caption("Ella's game")

Yellow = (237, 229, 145)
White = (255, 255, 255)
greenbutdifferent = (12, 28, 74)
purplebutdifferent = (36, 12, 74)
bluebutdifferent = (128, 176, 232)

speed = 5

cubeX = 250
cubeY = 250
cubeSize = 20

run = True

cubeSize = 20
food = [random.randrange(1,500)random.randrange(1,500), 10, 10]
Bfood = [random.randrange(1,500),random.randrange(1,500), 10, 10]