import pygame

import handler

from pygame.locals import *
from constants import *

class Game:
  def __init__(self):
    # Resolution.
    self.xRes = XRES
    self.yRes = YRES

    # Contains variables that are consistant across all handlers,
    # and indeed the current handler.
    self.handler = None

    # Might not be required in the new input handling system
    # self.crossHandlerKeys = list()

    # PyGame variables..
    self.screen = None
    self.run = True