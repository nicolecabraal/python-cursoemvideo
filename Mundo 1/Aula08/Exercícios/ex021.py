#Faça um programa em python que abra e reproduza o áudio de um arquivo MP3. 

import pygame

#Inicializando o mixer do pygame

pygame.mixer.init()

#Carregando o arquivo mp3

pygame.mixer.music.load('F:\Estudo\PROGRAMAÇÃO\python-guanabara\Mundo 1\Aula08\Exercícios\ex021.MP3')

#Reproduzindo o audio

pygame.mixer.music.play()

#Mantem o programa ativo enquanto o audio estiver tocando

input('Pressione Enter para parar a reprodução...')
pygame.mixer.music.stop()