#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from solid import *
from solid.utils import *
from partList import *

use_3dp_spring = False

spring = None


# select parts for 3drinted spring or for "steel springs"
if use_3dp_spring:
	spring = printedSpring(),
else:
	spring = union()(
			SpringHolderShellMiddleNut(),
			SpringHolderShell(),
			translate([0,-5,0])((rotate(a=90,v=[1,0,0]))(extrude_example())),
			translate([0,5,0])((rotate(a=90,v=[-1,0,0]))(extrude_example())),
		)

def assemble():
	return union()(
		# spring selected according to config
		spring,

		# common parts
		(rotate(180,[0.5,0,0.5])(translate([0,0,-15])(SEAbracketSide()))),
		(rotate(180,[-0.5,0,0.5])(translate([0,0,-15])(SEAbracketSide()))),
		translate([0,-100,0])((rotate(a=90,v=[-1,0,0]))(screwRodm4(200))),
		
		# Motor assembly
		(rotate(90,[1,0,0]))(translate([0,0, -110])(A2212())),
		(rotate(90,[1,0,0]))(translate([0,0, -105])(ShaftAdapter3_17to4mm())),
		(rotate(90,[1,0,0]))(translate([0,0, -140])(A2212Attachment())),
		
		# rails back
		(rotate(90,[1,0,0]))(translate([15,-10,-140])(screwRodm4(250))),
		(rotate(90,[1,0,0]))(translate([-15,10,-140])(screwRodm4(250))),

		# rails front
		(rotate(90,[1,0,0]))(translate([15,10,-15])(screwRodm4(250))),
		(rotate(90,[1,0,0]))(translate([-15,-10,-15])(screwRodm4(250))),

		(rotate(90,[1,0,0]))((translate([0,0, 100])(SEAtopCap()))),
		#translate([-15,10,0])(linearRod4mm()),
		#translate([-15,-10,65])(linearRod4mm()),
		#translate([15,10,65])(linearRod4mm()),
		#translate([15,-10,0])(linearRod4mm()),
		
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
