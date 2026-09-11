import pygame

pygame.init()
window = pygame.display.set_mode((500,500))
color = (255, 192, 203)  

pygame.draw.rect(window, color, pygame.Rect(10, 10, 10, 10))
pygame.display.flip()

pygame.time.wait(3000)
pygame.quit()