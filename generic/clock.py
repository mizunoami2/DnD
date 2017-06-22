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

def waitForStart(button, bgColor, fontColor, buttonPos):
    while True:
        event = pygame.event.poll()
        while event.type != MOUSEBUTTONUP:
            event = pygame.event.poll()
        if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] >= buttonPos[0] and event.pos[0] <= buttonPos[0] + button.get_width() and event.pos[1] >= buttonPos[1] and event.pos[1] <= buttonPos[1] + button.get_height():
            screen.fill(bgColor)
            button = drawButton("Pause", fontColor)
            screen.blit(button, buttonPos)
            return button

if __name__ == "__main__":
    SIZE = (150,150)
    time = int(sys.argv[1])
    seconds = time % 60
    time -= seconds
    warning = pygame.mixer.Sound("Warning.wav")
    timeout = pygame.mixer.Sound("TimeOut.wav")
    minutes = time / 60
    bgColor = (255,255,0)
    fontColor = (0,0,0)
    textPos = (40,25)
    buttonPos = (35,75)
    screen = pygame.display.set_mode(SIZE)
    screen.fill(bgColor)
    dummy = sys_font.render(str(minutes).rjust(2, '0') + ':' + str(seconds).rjust(2, '0'), 0, fontColor)
    screen.blit(dummy, textPos)
    pygame.display.set_caption('Countdown Clock')
    button = drawButton("Start", fontColor)
    screen.blit(button, buttonPos)
    pygame.display.flip()
    running = False
    while not running:
        button = waitForStart(button, bgColor, fontColor, buttonPos)
        running = True
    while minutes > 0 or seconds > 0:
        screen.fill(bgColor)
        dummy = sys_font.render(str(minutes).rjust(2, '0') + ':' + str(seconds).rjust(2, '0'), 0, fontColor)
        screen.blit(dummy, textPos)
        screen.blit(button, buttonPos)
        pygame.display.flip()
        pygame.time.wait(1000)
        if seconds == 0:
            minutes -= 1
            seconds = 59
        else:
            seconds -= 1
            if minutes == 1 and seconds == 0:
                warning.play()
        event = pygame.event.poll()
        while event.type != NOEVENT and event.type != MOUSEBUTTONUP:
            event = pygame.event.poll()
        if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] >= buttonPos[0] and event.pos[0] <= buttonPos[0] + button.get_width() and event.pos[1] >= buttonPos[1] and event.pos[1] <= buttonPos[1] + button.get_height():
            screen.fill(bgColor)
            button = drawButton("Start", fontColor)
            screen.blit(button, buttonPos)
            dummy = sys_font.render(str(minutes).rjust(2, '0') + ':' + str(seconds).rjust(2, '0'), 0, fontColor)
            screen.blit(dummy, textPos)
            running = False
            pygame.display.flip()
        while not running:
            button = waitForStart(button, bgColor, fontColor, buttonPos)
            running = True
    timeout.play()
    screen.fill(bgColor)
    dummy = sys_font.render(str(minutes).rjust(2, '0') + ':' + str(seconds).rjust(2, '0'), 0, fontColor)
    screen.blit(dummy, textPos)
    pygame.display.flip()
    pygame.time.wait(5000)