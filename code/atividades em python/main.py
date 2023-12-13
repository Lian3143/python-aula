import pygame

pygame.init()
pygame.mixer.music.load('ex03.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

#OBS: NÃO CONSEGUI FAZER FUNCIONAR NO VISUAL, APENAS NO PYCHARM