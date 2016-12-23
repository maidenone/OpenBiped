#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Basic shape with several repeated parts, demonstrating the use of
# solid.utils.bill_of_materials()
#
# Basically:
#   -- Define every part you want in the Bill of Materials in a function
#   -- Use the 'bom_part' decorator ahead of the definition of each part's function
#           e.g.:
# @bom_part()
# def my_part():
#     pass
#   -- Optionally, you can add a description and a per-unit cost to the
#       decorator invocations.
#
#   -- To generate the bill of materials, call solid.utils.bill_of_materials()
#
#       -ETJ 08 Mar 2011

import os
import sys
import pygame

if __name__ == '__main__':
	(width, height) = (512, 512)
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption('visulizer')
	running = True
	clock = pygame.time.Clock()

	i = 0
	while running:
		clock.tick(5)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		os.system("openscad --preview --camera=0,0,0,"+str(i)+","+str(0)+","+str(i)+",500 --imgsize=512,512 SEA.scad  -o SEA.png")
		image = pygame.image.load("SEA.png")
		screen.blit(image,(0,0))
		pygame.display.flip()
		i += 10
		i = i%1080