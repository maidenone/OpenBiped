#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from solid import *
from solid.utils import *
from partList import *

use_3dp_spring = False


#SLED_POS = -26 
SLED_POS = 0
#SLED_POS = 30

# select parts for 3drinted spring or for "steel springs"
spring = None
if use_3dp_spring:
	spring = printedSpring(),
else:
	spring = union()(
			SpringHolderShellMiddleNut(),
			SpringHolderShell(),
			translate([0,-5,0])((rotate(a=90,v=[1,0,0]))(color(Black))(springGenerator())),
			translate([0,5,0])((rotate(a=90,v=[-1,0,0]))(color(Black))(springGenerator())),
		)

def assemble():
	return union()(
		# spring selected according to config
		(translate([0,-1*SLED_POS,0]))(spring),
		#translate([0,-1.5,0])((rotate(90,[-1,0,0]))(color(Stainless)(nut('m4')))),

		# common parts
		(rotate(180,[0.5,0,0.5])(translate([0,SLED_POS+0,-16])(SEAbracketSide()))),
		(rotate(180,[-0.5,0,0.5])(translate([0,SLED_POS+0,-16])(SEAbracketSide()))),
		translate([0,-60,0])((rotate(a=90,v=[-1,0,0]))(screwRod(120))),
		
		#translate([-10,10,0])((rotate(180,[-0.5,0,0.5]))(color(Stainless)(screw('m4',10)))),
		#translate([-11,10,0])((rotate(180,[-0.5,0,0.5]))(color(Stainless)(nut('m4')))),
		
		#translate([-10,-10,0])((rotate(180,[-0.5,0,0.5]))(color(Stainless)(screw('m4',10)))),
		#translate([-11,-10,0])((rotate(180,[-0.5,0,0.5]))(color(Stainless)(nut('m4')))),

		# Motor assembly
		(rotate(90,[1,0,0]))(translate([0,0, -70])(A2212())),
		(rotate(90,[1,0,0]))(translate([0,0, -65])(ShaftAdapter3_17to4mm())),
		(rotate(90,[-1,0,0]))(translate([0,0,-146-SLED_POS])(A2212Attachment())),
		(rotate(90,[1,0,0]))(translate([0,0, -100])(A2212Attachment())),
		(rotate(90,[-1,0,0]))(translate([0,0, -60])(A2212Attachment())),
		(translate([0,-156-SLED_POS,])(Puller())),
		# rails back
		(rotate(90,[1,0,0]))(translate([16,-10,-98])(linearRod(160))),
		(rotate(90,[1,0,0]))(translate([-16,10,-98])(linearRod(160))),

		# rails front
		(rotate(90,[1,0,0]))(translate([16,10,-15+SLED_POS])(linearRod(160))),
		(rotate(90,[1,0,0]))(translate([-16,-10,-15+SLED_POS])(linearRod(160))),
		
		#(rotate(32,[0,-1,0]))((rotate(90,[-1,0,0]))(translate([0,0,-140])(TopPusher()))),
		#JUST FOR BOM, NO MODEL YET
		ESC40W(),
	)

if __name__ == '__main__':
	out_dir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
	file_out = os.path.join(out_dir, 'SEA.scad')
	a = assemble()
	bom = bill_of_materials()
	print("%(__file__)s: SCAD file written to: \n%(file_out)s" % vars())
	print(bom)
	scad_render_to_file(a, file_out)
