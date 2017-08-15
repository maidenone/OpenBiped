#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from solid import *
from solid.utils import *
from partList import *
from solid.partLib import *
use_3dp_spring = False


#sled_pos = -26 
sled_pos = 0
#sled_pos = 30

# select parts for 3drinted spring or for "steel springs"
spring = None
if use_3dp_spring:
	spring = printedSpring(),
else:
	spring = union()(
			SpringHolderShellMiddleNut(),
			SpringHolderShell(),
			translate([0,-5,0])((rotate(a=90,v=[1,0,0]))(color(Black))(springGenerator(length=SPRING_H-2))),
			translate([0,5,0])((rotate(a=90,v=[-1,0,0]))(color(Black))(springGenerator(length=SPRING_H-2))),
		)

def SEA(sled_pos=0):
	return union()(
		# spring selected according to config
		(translate([0,-1*sled_pos,0]))(spring),
		#translate([0,-1.5,0])((rotate(90,[-1,0,0]))(color(Stainless)(nut('m4')))),

		# common parts
		(rotate(180,[0.5,0,0.5])(translate([0,sled_pos+0,-16])(SEAbracketSide()))),
		(rotate(180,[-0.5,0,0.5])(translate([0,sled_pos+0,-16])(SEAbracketSide()))),
		translate([0,-60,0])((rotate(a=90,v=[-1,0,0]))(screwRod(120))),
		
		#translate([-10,10,0])((rotate(180,[-0.5,0,0.5]))(color(Stainless)(screw('m4',10)))),
		#translate([-11,10,0])((rotate(180,[-0.5,0,0.5]))(color(Stainless)(nut('m4')))),
		
		#translate([-10,-10,0])((rotate(180,[-0.5,0,0.5]))(color(Stainless)(screw('m4',10)))),
		#translate([-11,-10,0])((rotate(180,[-0.5,0,0.5]))(color(Stainless)(nut('m4')))),

		# Motor assembly
		(rotate(90,[1,0,0]))(translate([0,0, -70])(A2212())),
		(rotate(90,[1,0,0]))(translate([0,0, -65])(ShaftAdapter3_17to4mm())),
		(rotate(90,[-1,0,0]))(translate([0,0,-146-sled_pos])(A2212Attachment())),
		(rotate(90,[1,0,0]))(translate([0,0, -100])(A2212Attachment())),
		(rotate(90,[-1,0,0]))(translate([0,0, -64])(A2212Attachment())),
		(translate([0,-156-sled_pos,])(Puller())),
		# rails back
		(rotate(90,[1,0,0]))(translate([16,-10,-98])(linearRod(160))),
		(rotate(90,[1,0,0]))(translate([-16,10,-98])(linearRod(160))),

		# rails front
		(rotate(90,[1,0,0]))(translate([16,10,-15+sled_pos])(linearRod(160))),
		(rotate(90,[1,0,0]))(translate([-16,-10,-15+sled_pos])(linearRod(160))),
		
		#(rotate(32,[0,-1,0]))((rotate(90,[-1,0,0]))(translate([0,0,-140])(TopPusher()))),
		#JUST FOR BOM, NO MODEL YET
		ESC40W(),
	)

#case = difference()(
#		up(0)(cube((60,42,14),True)),
#		up(2.5)(cube((62,14,11),True)),
#		up(5)(cube((52,50,5),True)),
#		)

case = difference()(
		union()(
			left(8)(cube((20,42,14),True)),
			translate((-35,19.5,-2))(cube((34,3,10),True)),
			translate((-35,-19.5,-2))(cube((34,3,10),True)),
			),
		up(0)(cube((62,14,10),True)),
		right(12)(cube((56,39.5,11.5),True)),
		#up(5)(cube((52,50,5),True)),
		)

#case = union()(
#		case,
#		translate((-38,19,-2))(cube((24,4,10),True)),
#		translate((-38,-19,-2))(cube((24,4,10),True)),
#		)

pin = cylinder(r=2.05,h=100)
pin.add_param('$fs', 1)
case = difference()(
		case,
		translate([-46,-50,-2])(rot_z_to_y(pin)),
	)

base = union()(
		down(2)(cube((52,33,10),True)),
		#translate([0,-50,0])(rot_z_to_y(pin)),
	)

base = difference()(
	base,
	translate([-16,-6,-4])(cube((10,14,10),True)),
	translate([0,-50,0])(rot_z_to_y(pin)),
	cube([100,3*5,3],True),
	scale(1.05)((color(Red)(rot_z_to_y(translate([5,0,1.2])(servo()))))),
	back(0)(cube((48,30,8),True)),
	translate([20,-10,-10])(pin),
	translate([-20,10,-10])(pin),
	)
if __name__ == '__main__':
	out_dir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
	file_out = os.path.join(out_dir, 'SEA.scad')
	a = union()(
		(color(Transparent)(base)),
		translate([24,40,0])(case),
		#translate([-2,0,46])(rot_z_to_neg_x(color(Blue)(up(0)(cube((56,38,11),True))))),
		#translate([-2,0,46])(rot_z_to_neg_x(case)),
		#(SEA(sled_pos)),
	)
	bom = bill_of_materials()
	print("%(__file__)s: SCAD file written to: \n%(file_out)s" % vars())
	print(bom)
	scad_render_to_file(a, file_out)
