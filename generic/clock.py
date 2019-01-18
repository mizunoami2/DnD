#!/usr/bin/env python
import pygame
import sys
from pygame.locals import *

pygame.init()
sys_font = pygame.font.SysFont("tlwgtypist", 20, bold=True)

def drawButton(string, fontColor):
	fake = pygame.Surface((len(string) * 15, 25))
	fake.fill((255,255,255))
	pygame.draw.rect(fake, (255,0,255), fake.get_rect(), 3)
	dummy = sys_font.render(string, 0, fontColor)
	fake.blit(dummy, (5, 0))
	return fake

def waitForStart(button1, buttonPos1, button2, bottonPos2, bgColor, fontColor):
	while True:
		event = pygame.event.poll()
		while event.type != MOUSEBUTTONUP:
			event = pygame.event.poll()
		if (event.type == MOUSEBUTTONUP and event.button == 1 and 
			 ((event.pos[0] >= buttonPos1[0] and event.pos[0] <= buttonPos1[0] + button1.get_width() and event.pos[1] >= buttonPos1[1] and event.pos[1] <= buttonPos1[1] + button1.get_height()) or
			  (event.pos[0] >= buttonPos2[0] and event.pos[0] <= buttonPos2[0] + button2.get_width() and event.pos[1] >= buttonPos2[1] and event.pos[1] <= buttonPos2[1] + button2.get_height()))):
			screen.fill(bgColor)
			if event.pos[0] >= buttonPos1[0] and event.pos[0] <= buttonPos1[0] + button1.get_width() and event.pos[1] >= buttonPos1[1] and event.pos[1] <= buttonPos1[1] + button1.get_height():
				button1 = drawButton("Pause", fontColor)
				screen.blit(button1, buttonPos1)
				butt =1 
			else:
				button2 = drawButton("Pause", fontColor)
				screen.blit(button2, buttonPos2)
				butt = 2
			return button1, button2, butt 

if __name__ == "__main__":
	#Argument 1, the only argument, is number of seconds the timer should run
	SIZE = (300,150)
	time = int(sys.argv[1])
	seconds1 = time % 60
	seconds2 = time % 60
	time -= seconds1
	warning = pygame.mixer.Sound("Warning.wav")
	timeout = pygame.mixer.Sound("TimeOut.wav")
	minutes1 = int(time / 60)
	minutes2 = minutes1
	bgColor = (255,255,0)
	fontColor = (0,0,0)
	textPos1 = (40, 25)
	buttonPos1 = (35, 75)
	textPos2 = (190, 25)
	buttonPos2 = (185, 75)
	screen = pygame.display.set_mode(SIZE)
	screen.fill(bgColor)

	dummy = sys_font.render(str(minutes1).rjust(2, '0') + ':' + str(seconds1).rjust(2, '0'), 0, fontColor)
	screen.blit(dummy, textPos1)
	dummy = sys_font.render(str(minutes2).rjust(2, '0') + ':' + str(seconds2).rjust(2, '0'), 0, fontColor)
	screen.blit(dummy, textPos2)

	pygame.display.set_caption('Countdown Clock')
	button1 = drawButton("Start", fontColor)
	button2 = drawButton("Start", fontColor)
	screen.blit(button1, buttonPos1)
	screen.blit(button2, buttonPos2)

	pygame.display.flip()
	running = False
	while not running:
		button1, button2, butt = waitForStart(button1, buttonPos1, button2, buttonPos2, bgColor, fontColor)
		running = True
		while (minutes1 > 0 or seconds1 > 0) and (minutes2 > 0 or seconds2 > 0):
			screen.fill(bgColor)
			dummy = sys_font.render(str(minutes1).rjust(2, '0') + ':' + str(seconds1).rjust(2, '0'), 0, fontColor)
			screen.blit(dummy, textPos1)
			dummy = sys_font.render(str(minutes2).rjust(2, '0') + ':' + str(seconds2).rjust(2, '0'), 0, fontColor)
			screen.blit(dummy, textPos2)

			screen.blit(button1, buttonPos1)
			screen.blit(button2, buttonPos2)

			pygame.display.flip()
			pygame.time.wait(1000)
			if butt == 1:
				if seconds1 == 0:
					minutes1 -= 1
					seconds1 = 59
				else:
					seconds1 -= 1
					if minutes1 == 1 and seconds1 == 0:
						warning.play()
			else:
				if seconds2 == 0:
					minutes2 -= 1
					seconds2 = 59
				else:
					seconds2 -= 1
					if minutes2 == 1 and seconds2 == 0:
						warning.play()
			event = pygame.event.poll()
			while event.type != NOEVENT and event.type != MOUSEBUTTONUP:
				event = pygame.event.poll()

			#This part is complex and dumb, I need a better way to check multiple buttons, but for only two buttons it's...workable
			if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] >= buttonPos1[0] and event.pos[0] <= buttonPos1[0] + button1.get_width() and event.pos[1] >= buttonPos1[1] and event.pos[1] <= buttonPos1[1] + button1.get_height():
				screen.fill(bgColor)
				if butt == 1:
					button1 = drawButton("Start", fontColor)
					running = False
				else:
					button2 = drawButton("Start", fontColor)
					button1 = drawButton("Pause", fontColor)
					butt = 1
				screen.blit(button1, buttonPos1)
				screen.blit(button2, buttonPos2)
				dummy = sys_font.render(str(minutes1).rjust(2, '0') + ':' + str(seconds1).rjust(2, '0'), 0, fontColor)
				screen.blit(dummy, textPos1)
				dummy = sys_font.render(str(minutes2).rjust(2, '0') + ':' + str(seconds2).rjust(2, '0'), 0, fontColor)
				screen.blit(dummy, textPos2)
				pygame.display.flip()
			if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] >= buttonPos2[0] and event.pos[0] <= buttonPos2[0] + button2.get_width() and event.pos[1] >= buttonPos2[1] and event.pos[1] <= buttonPos2[1] + button2.get_height():
				screen.fill(bgColor)
				if butt == 2:
					button2 = drawButton("Start", fontColor)
					running = False
				else:
					button1 = drawButton("Start", fontColor)
					button2 = drawButton("Pause", fontColor)
					butt = 2
				screen.blit(button1, buttonPos1)
				screen.blit(button2, buttonPos2)
				dummy = sys_font.render(str(minutes1).rjust(2, '0') + ':' + str(seconds1).rjust(2, '0'), 0, fontColor)
				screen.blit(dummy, textPos1)
				dummy = sys_font.render(str(minutes2).rjust(2, '0') + ':' + str(seconds2).rjust(2, '0'), 0, fontColor)
				screen.blit(dummy, textPos2)
				pygame.display.flip()
			while not running:
				button1, button2, butt = waitForStart(button1, buttonPos1, button2, buttonPos2, bgColor, fontColor)
				running = True
		timeout.play()
		screen.fill(bgColor)
		dummy = sys_font.render(str(minutes1).rjust(2, '0') + ':' + str(seconds1).rjust(2, '0'), 0, fontColor)
		screen.blit(dummy, textPos1)
		dummy = sys_font.render(str(minutes2).rjust(2, '0') + ':' + str(seconds2).rjust(2, '0'), 0, fontColor)
		screen.blit(dummy, textPos2)	    
		pygame.display.flip()
		pygame.time.wait(5000)