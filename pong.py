#!/usr/bin/python
#-*- coding:utf-8 -*-

#---------------------------------------------------------
# Modulos
#---------------------------------------------------------
import pygame, sys, time
import pygame._view
from pygame.locals import *

#---------------------------------------------------------
# Inicio de Pygame
#---------------------------------------------------------
pygame.init()

#---------------------------------------------------------
# Leer jugadores
#---------------------------------------------------------
with open(".pl") as o:
	pls = o.read()

#---------------------------------------------------------
# Variables
#---------------------------------------------------------
fps = 60
timeP = 0
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)
pl1, pl2 = (pls.split(":")[0], pls.split(":")[1])
ballX, ballY = (50, 50)
ballDX, ballDY = (5, 5)
palaX, palaY = (50, 250)
pala2X, pala2Y = (740, 250)
palaDY, pala2DY = (5, 5)
points1, points2 = (0, 0)
pointsTotals = int(pls.split(":")[2])
typeLetter = pygame.font.SysFont("arial", 96)
typeLetter2 = pygame.font.SysFont("arial", 24)

#---------------------------------------------------------
# Pnatalla del juego (SURFACE)
#---------------------------------------------------------
screen = pygame.display.set_mode((800, 600), 0)
pygame.display.set_caption("PING PONG")

#---------------------------------------------------------
# Funciones
#---------------------------------------------------------
def pause():
	wait = True
	while wait:
		for e in pygame.event.get():
			if e.type == QUIT:
				pygame.quit()
				sys.exit()
			if e.type == KEYDOWN:
				wait = False
				if e.key == K_ESCAPE:
					pygame.quit()
					sys.exit()

def showInfo():
	screen.fill((0, 0, 0))
	mens1 = "P O N G"
	mens2 = "Pulsa una tecla para comenzar"
	txt1 = typeLetter.render(mens1, True, AMARILLO)
	txt2 = typeLetter2.render(mens2, True, BLANCO)
	screen.blit(txt1, (50, 250, 200, 100))
	screen.blit(txt2, (450, 292, 350, 30))
	pygame.display.update()
	pause()

def drawPlay():
	screen.fill((0, 0, 0))
	pygame.draw.circle(screen, AZUL, (ballX, ballY), 6, 0)
	pygame.draw.rect(screen, BLANCO, (palaX, palaY, 10, 50))
	pygame.draw.rect(screen, BLANCO, (pala2X, pala2Y, 10, 50))

	for i in range(10):
		pygame.draw.rect(screen, ROJO, (398, 10+60*i, 4, 30))
	
	mark1 = typeLetter.render(str(points1), True, BLANCO)
	mark2 = typeLetter.render(str(points2), True, BLANCO)
	screen.blit(mark1, (300, 20, 50, 50))
	screen.blit(mark2, (450, 20, 50, 50))

	pygame.display.update()

def seeWin():
	if points1 == pointsTotals:
		win = pl1
	else:
		win = pl2
	mensW1 = "Ganador:"
	mensW2 = win
	mensW3 = "Pulsa una tecla para continuar"
	txt = typeLetter.render(mensW1, True, BLANCO)
	txt2 = typeLetter.render(mensW2, True, AMARILLO)
	txt3 = typeLetter2.render(mensW3, True, BLANCO)
	screen.blit(txt, (75, 75, 600, 100))
	screen.blit(txt2, (200, 170, 600, 100))
	screen.blit(txt3, (400, 300, 350, 30))
	pygame.display.update()
	time.sleep(2)
	pause()
#---------------------------------------------------------
# Inicio del Juego
#---------------------------------------------------------
pygame.mouse.set_visible(False)
showInfo()

while True:
	#---------------------------------------------------------
	# Velocidad de juego
	#---------------------------------------------------------
	if pygame.time.get_ticks() - timeP < 1000 / fps:
		continue
	timeP = pygame.time.get_ticks()

	#---------------------------------------------------------
	# Eventos
	#---------------------------------------------------------
	for e in pygame.event.get():
		if e.type == QUIT:
			pygame.quit()
			sys.exit()
		if e.type == KEYDOWN:
			if e.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
	
	#---------------------------------------------------------
	# Mover la pelota
	#---------------------------------------------------------
	dif1 = ballY - palaY
	if ballX == palaX + 10 and dif1 >= 0 and dif1 <= 50:
		ballDX = -ballDX
	dif2 = ballY - pala2Y
	if ballX == pala2X and dif2 >= 0 and dif2 <= 50:
		ballDX = -ballDX
	if ballY < 5 or ballY > 595:
		ballDY = -ballDY
	
	ballX += ballDX
	ballY += ballDY

	#---------------------------------------------------------
	# Mover las palas
	#---------------------------------------------------------
	keyPress = pygame.key.get_pressed()

	## Jugador 1
	if keyPress[K_s]:
		palaY += palaDY
	if keyPress[K_w]:
		palaY -= palaDY
	
	if palaY < 0:
		palaY = 0
	if palaY > 550:
		palaY = 550
	
	## Jugador 2
	if keyPress[K_DOWN]:
		pala2Y += pala2DY
	if keyPress[K_UP]:
		pala2Y -= pala2DY
	
	if pala2Y < 0:
		pala2Y = 0
	if pala2Y > 550:
		pala2Y = 550
	
	#---------------------------------------------------------
	# Puntos
	#---------------------------------------------------------
	if ballX > 800 or ballX < 0:
		time.sleep(0.75)
		palaY = 250
		pala2Y = 250
		if ballX > 800:
			points1 += 1
		else:
			points2 += 1
		ballX = 400
		ballDX = -ballDX
		if points1 == pointsTotals or points2 == pointsTotals:
			screen.fill((0, 0, 0))
			seeWin()
			points1 = 0
			points2 = 0
			showInfo()
	
	#---------------------------------------------------------
	# Dibujar el juego
	#---------------------------------------------------------
	drawPlay()