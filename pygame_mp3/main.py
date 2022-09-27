import pygame
pygame.init() #iniciando pygame
pygame.mixer.music.load('Marília Mendonça - Supera (Ao Vivo).mp3') #carregando a musica
pygame.mixer.music.play() # iniciando musica
pygame.event.wait() # esperar o evento terminar para encerrar