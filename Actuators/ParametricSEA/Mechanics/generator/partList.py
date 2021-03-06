from solid import *
from solid.utils import *  # Not required, but the utils module is useful

#configuration
LINEAR_ROD_CLEARANCE = 0.4
LINEAR_ROD_R = 2
LINEAR_ROD_WITH_CLEARANCE_R = LINEAR_ROD_R + LINEAR_ROD_CLEARANCE/2.0
LINEAR_ROD_LENGTH = 100

SCREW_CLEARANCE = 0.4
SCREW_ROD_R = 2
SCREW_ROD_WITH_CLEARANCE_R = SCREW_ROD_R + SCREW_CLEARANCE/2.0
NUT_CLEARANCE = 0.6
NUT_S = 7 + NUT_CLEARANCE
NUT_M = 3.2 + NUT_CLEARANCE
NUT_D = 4 + NUT_CLEARANCE

SPRING_R = 17/2.0
SPRING_H = 32 - 0

A2212_dia = 27.7

USD2RMB = 6.95
RMB2USD = 0.144

set_bom_headers("filamentUsage","link")

#parts
#! /usr/bin/env python
# -*- coding: utf-8 -*-


@bom_part("SpringHolderShellMiddleNut")
def SpringHolderShellMiddleNut():
	springfit = cylinder(r=9,h=4)
	body = cube([18,12,14],True)
	centerHole = cube([10,14,10],True)
	m4Hole = cylinder(r=SCREW_ROD_WITH_CLEARANCE_R,h=100,center=True)
	m4Hole.add_param('$fs', 1)  # rod smooth
	nutHole = cube((NUT_M,NUT_S,40),center=True)
	holder = difference()(
		body,
		translate([0,8,0])((rotate(a=90,v=[1,0,0]))(springfit)),
		translate([0,-8,0])((rotate(a=90,v=[-1,0,0]))(springfit)),
		rotate(a=90,v=[1,0,0])(m4Hole),
		translate([0,0,0])(rotate(90,[0,0,1])(nutHole)),
	)
	return color([1,0,0, 1])(holder)

@bom_part("Puller")
def Puller():
	springfit = cylinder(r=9,h=4)
	body = cube([14,20,10],True)
	#centerHole = cube([10,14,10],True)
	m4Hole = cylinder(r=SCREW_ROD_WITH_CLEARANCE_R,h=100,center=True)
	m4Hole.add_param('$fs', 1)  # rod smooth
	nutHole = cube((NUT_M,NUT_S,40),center=True)
	holder = difference()(
		body,
		translate([0,-4,0])(rotate(a=90,v=[0,0,0])(m4Hole)),
		rotate(a=90,v=[1,0,0])(m4Hole),
		translate([0,5,0])(rotate(90,[0,0,1])(nutHole)),
	)
	return color([1,0,0, 1])(holder)

@bom_part("SpringHolderShell")
def SpringHolderShell():
	springfit = cylinder(r=9,h=6)
	shell_length = SPRING_H*2+12;
	body = cube([32,shell_length,10],True)
	centerHole = cube([19,shell_length-14,12],True)
	m4Hole = cylinder(r=SCREW_ROD_WITH_CLEARANCE_R,h=100,center=True)
	m4Hole.add_param('$fs', 1)  # rod smooth
	nutHole = cube((NUT_M,NUT_S,12),center=True)
	nutHoleCutIn_x = 12.5
	pinHoleCutIn_x = 10

	holder = difference()(
		body,
		#spring pocket
		translate([0,SPRING_H+2,0])((rotate(a=90,v=[1,0,0]))(springfit)),
		translate([0,-1*(SPRING_H+2),0])((rotate(a=90,v=[-1,0,0]))(springfit)),

		# nut holes left
		#translate([-1*nutHoleCutIn_x,-30,0])(rotate(0,[1,0,0])(nutHole)),
		translate([-1*nutHoleCutIn_x,-20,0])(rotate(0,[1,0,0])(nutHole)),
		translate([-1*nutHoleCutIn_x,-10,0])(rotate(0,[1,0,0])(nutHole)),
		translate([-1*nutHoleCutIn_x,0,0])(rotate(0,[1,0,0])(nutHole)),
		translate([-1*nutHoleCutIn_x,10,0])(rotate(0,[1,0,0])(nutHole)),
		translate([-1*nutHoleCutIn_x,20,0])(rotate(0,[1,0,0])(nutHole)),
		#translate([-1*nutHoleCutIn_x,30,0])(rotate(0,[1,0,0])(nutHole)),
		# pin holes left
		#translate([pinHoleCutIn_x,30,0])(rotate(90,[0,1,0])(m4Hole)),
		translate([pinHoleCutIn_x,20,0])(rotate(90,[0,1,0])(m4Hole)),
		translate([pinHoleCutIn_x,10,0])(rotate(90,[0,1,0])(m4Hole)),
		translate([pinHoleCutIn_x,0,0])(rotate(90,[0,1,0])(m4Hole)),
		translate([pinHoleCutIn_x,-10,0])(rotate(90,[0,1,0])(m4Hole)),
		translate([pinHoleCutIn_x,-20,0])(rotate(90,[0,1,0])(m4Hole)),
		#translate([pinHoleCutIn_x,-30,0])(rotate(90,[0,1,0])(m4Hole)),

		# nut holes right
		#translate([1*nutHoleCutIn_x,-30,0])(rotate(0,[1,0,0])(nutHole)),
		translate([1*nutHoleCutIn_x,-20,0])(rotate(0,[1,0,0])(nutHole)),
		translate([1*nutHoleCutIn_x,-10,0])(rotate(0,[1,0,0])(nutHole)),
		translate([1*nutHoleCutIn_x,0,0])(rotate(0,[1,0,0])(nutHole)),
		translate([1*nutHoleCutIn_x,10,0])(rotate(0,[1,0,0])(nutHole)),
		translate([1*nutHoleCutIn_x,20,0])(rotate(0,[1,0,0])(nutHole)),
		#translate([1*nutHoleCutIn_x,30,0])(rotate(0,[1,0,0])(nutHole)),
		centerHole,
		rotate(a=90,v=[1,0,0])(m4Hole),
	)
	return color([0,1,0, 1])(holder)

@bom_part("ESC 40W",4.5*USD2RMB)
def ESC40W():
	return cube(1)

@bom_part("A2212",4.5*USD2RMB,filamentUsage=24,link="http://example.io/M3x16")
def A2212():

	rod = cylinder(h=9.5,r=3.17/2)
	rod.add_param('$fs', 1)  # rod smooth

	topCylinder = cylinder(h=2,r=4)
	topCylinder.add_param('$fs', 1)  # rod smooth

	top = cylinder(h=6,r2=5,r1=A2212_dia/2.0)
	top.add_param('$fs', 1)  # rod smooth

	body = cylinder(h=20,r=A2212_dia/2.0)
	body.add_param('$fs', 1)  # rod smooth

	m3HolePin = cylinder(h=11,r=1.5)
	m3HolePin.add_param('$fs', 1)
	m3HolePin = color([1,0,0, 1])(m3HolePin)
	a2212 = union()(
					rod,
					translate([0,0, -2])(topCylinder),
					translate([0,0, -8])(top),
					translate([0,0, -28])(body)
					)
	a2212 = color([0,0,1, 1])(a2212)
	a2212b = difference()(
						a2212,
						translate([8,0, -29])(m3HolePin),
						translate([-8,0, -29])(m3HolePin),
						translate([0,9.5, -29])(m3HolePin),
						translate([0,-9.5, -29])(m3HolePin)
						)
	return a2212b

@bom_part("Shaft Adapter 3.17:4",price=0.5,print_time=8, filament=24)
def ShaftAdapter3_17to4mm():
	body = cylinder(h=10,r=6)
	body.add_param('$fs', 1)  # rod smooth
	rod1 = cylinder(h=5,r=2)
	rod1.add_param('$fs', 1)  # rod smooth
	rod2 = cylinder(h=5,r=3.17/2)
	rod2.add_param('$fs', 1)  # rod smooth
	part = difference()(
						body,
						(rod2),
						translate([0,0,5])(rod1),
						)
	part = color([1,0,0, 1])(part)

	return part


@bom_part("TopPusher",price=0.2,print_time=32)
def TopPusher():
	holePin = cylinder(h=30,r=SCREW_ROD_WITH_CLEARANCE_R)
	holePin.add_param('$fs', 1)
	distance = sqrt(pow(20,2)+pow(32,2))
	body = cube((distance+8,8,20),True)

	body = difference()(
		body,
		(translate([-distance/2.0,0, -2]))(holePin),
		translate([distance/2.0,0, -2])(holePin),
		(translate([0,10,-2]))(rotate(a=90,v=[1,0,0])(holePin)),
	)
	return color(Brass)(body)

@bom_part("A2212 Attachment",price=0.2,print_time=32)
def A2212Attachment():
	
	holeLock = cylinder(h=50,r=1)
	# construction geometries 
	pinHolderOuter = cylinder(h=10,r=LINEAR_ROD_WITH_CLEARANCE_R+2)
	pinHolderOuter.add_param('$fs', 1)
	
	pinHolderInner = cylinder(h=12,r=LINEAR_ROD_WITH_CLEARANCE_R)
	pinHolderInner.add_param('$fs', 1)
	
	motorOuter = cube([32,26,2],True)

	motorInner = cylinder(h=2,r=SCREW_ROD_WITH_CLEARANCE_R+4)
	motorInner.add_param('$fs', 1)

	holePin = cylinder(h=12,r=1.5)
	holePin.add_param('$fs', 1)
	holePin = color([1,0,0, 1])(holePin)

	# pad, main structure
	attachment = union()(
						translate([0,0, 1])(motorOuter),
						translate([-16,-10, 0])(pinHolderOuter),
						translate([-16,10, 0])(pinHolderOuter),
						translate([16,-10, 0])(pinHolderOuter),
						translate([16,10, 0])(pinHolderOuter),
						)
	# pocket, main structure
	attachment = difference()(
						attachment,
						translate([0,0, 2])(motorInner),

						translate([8,8, -1])(pinHolderInner),
						translate([8,-8, -1])(pinHolderInner),
						translate([-8,8, -1])(pinHolderInner),
						translate([-8,-8, -1])(pinHolderInner),

						translate([-16,-10, 2])(pinHolderInner),
						translate([-16,10, 2])(pinHolderInner),
						translate([16,-10, 2])(pinHolderInner),
						translate([16,10, 2])(pinHolderInner),
						rotate(a=90,v=[0,1,0])(translate([-4,10,-28])(holeLock)),
						rotate(a=90,v=[0,1,0])(translate([-4,-10,-28])(holeLock)),
						)
	attachment = color([1,1,0, 1])(attachment)
	# holes for motor mounting
	attachment = difference()(
						attachment,
						translate([0,0,-1])(pinHolderInner),
						translate([8,0, -1])(holePin),
						translate([-8,0, -1])(holePin),
						translate([0,9.5, -1])(holePin),
						translate([0,-9.5, -1])(holePin)
						)
	return attachment

@bom_part("SEA sled side bracket",price=0.5,print_time=32)
def SEAbracketSide():
	bracket = cube((28,30,8),center=True)
	pocket1 = cube((32,16,5),True)
	pocket2 = cube((12,32,5),True)
	bracket = color([0,1,0, 1])(bracket)
	holePin = cylinder(h=34,r=LINEAR_ROD_WITH_CLEARANCE_R)
	holePin.add_param('$fs', 0.1)
	screwHolePin = cylinder(h=34,r=SCREW_ROD_WITH_CLEARANCE_R)
	screwHolePin.add_param('$fs', 0.1)
	holeLock = cylinder(h=34,r=1)
	holeLock.add_param('$fs', 0.1)
	bracket = difference()(
						(bracket),
						translate([0,0,2])(pocket1),
						translate([0,0,2])(pocket2),
						translate([0,-10,-10])(screwHolePin),
						translate([0,0,-10])(screwHolePin),
						translate([0,10,-10])(screwHolePin),
						rotate(a=90,v=[0,1,0])(translate([0,11,-16])(holeLock)),
						rotate(a=90,v=[0,1,0])(translate([0,-11,-16])(holeLock)),
						rotate(a=90,v=[1,0,0])(translate([-10,0,-16])(holePin)),
						rotate(a=90,v=[1,0,0])(translate([10,0,-16])(holePin)),
						)
	return color(Yellow)(bracket)

@bom_part("SEA 3d printed spring",price=0.2,print_time=32)
def printedSpring():
	sideCleranceOffset = 8
	springWidthCleranceOffset = 2
	nutHoleCutIn_x = 12
	pinHoleCutIn_x = 8
	springGap_y = 1
	springGap_x = 11
	bracket = cube((32,32,10),center=True)
	nutHole = cube((NUT_M,NUT_S,12),center=True)
	springSideClearance = cube((2,28,12),True)
	springWidthClearance = cube((springGap_x,springGap_y,12),True)
	springWidthFillet_r = (springGap_y/2.0)
	sprindWidthFillet = cylinder(h=4000,r=springWidthFillet_r)
	sprindWidthFillet.add_param('$fs', 0.1)

	holePin = cylinder(h=40,r=SCREW_ROD_WITH_CLEARANCE_R)
	holePin.add_param('$fs', 1)

	springCutout = bracket
	for i in range(0,3):
			offset_y1 = 3+i*4;
			offset_y2 = 5+i*4;

			# spring clerance top
			springCutout = difference()(
				springCutout,
				# top
				translate([springWidthCleranceOffset*-1,offset_y1,0])(rotate(0,[0,0,1])(springWidthClearance)), # spring gap
				translate([springWidthCleranceOffset*-1+(springGap_x/2+springWidthFillet_r),offset_y1,-10])(rotate(0,[0,0,1])(sprindWidthFillet)), # spring gap fillet
				
				translate([springWidthCleranceOffset,offset_y2,0])(rotate(0,[0,0,1])(springWidthClearance)),
				translate([springWidthCleranceOffset-(springGap_x/2+springWidthFillet_r),offset_y2,-10])(rotate(0,[0,0,1])(sprindWidthFillet)),

				# bottom
				translate([springWidthCleranceOffset,offset_y1*-1,0])(rotate(0,[0,0,1])(springWidthClearance)), # spring gap
				translate([springWidthCleranceOffset-(springGap_x/2+springWidthFillet_r),offset_y1*-1,-10])(rotate(0,[0,0,1])(sprindWidthFillet)), # spring gap fillet
				
				translate([springWidthCleranceOffset*-1,offset_y2*-1,0])(rotate(0,[0,0,1])(springWidthClearance)),
				translate([springWidthCleranceOffset*-1+(springGap_x/2+springWidthFillet_r),offset_y2*-1,-10])(rotate(0,[0,0,1])(sprindWidthFillet)),

			)
	bracket = springCutout
	spring = difference()(
						bracket,
						translate([0,20,0])(rotate(90,[1,0,0])(holePin)),

						# nut hole center
						translate([0,0,0])(rotate(90,[0,0,1])(nutHole)),

						# clearence left
						translate([sideCleranceOffset*-1,0,0])(rotate(0,[0,0,1])(springSideClearance)),
						# nut holes left
						translate([-1*nutHoleCutIn_x,10,0])(rotate(0,[1,0,0])(nutHole)),
						translate([-1*nutHoleCutIn_x,0,0])(rotate(0,[1,0,0])(nutHole)),
						translate([-1*nutHoleCutIn_x,-10,0])(rotate(0,[1,0,0])(nutHole)),
						# pin holes left
						translate([pinHoleCutIn_x,10,0])(rotate(90,[0,1,0])(holePin)),
						translate([pinHoleCutIn_x,0,0])(rotate(90,[0,1,0])(holePin)),
						translate([pinHoleCutIn_x,-10,0])(rotate(90,[0,1,0])(holePin)),

						# clearence right
						translate([sideCleranceOffset,0,0])(rotate(0,[0,0,1])(springSideClearance)),
						# nut holes right
						translate([nutHoleCutIn_x,10,0])(rotate(0,[1,0,0])(nutHole)),
						translate([nutHoleCutIn_x,0,0])(rotate(0,[1,0,0])(nutHole)),
						translate([nutHoleCutIn_x,-10,0])(rotate(0,[1,0,0])(nutHole)),
						# pin holes right
						translate([-1*pinHoleCutIn_x,10,0])(rotate(90,[0,-1,0])(holePin)),
						translate([-1*pinHoleCutIn_x,0,0])(rotate(90,[0,-1,0])(holePin)),
						translate([-1*pinHoleCutIn_x,-10,0])(rotate(90,[0,-1,0])(holePin)),
						)
	spring = color(([0.8,0,0.8]))(spring)
	return spring


@bom_part("SEA Top Cap",price=0.5,print_time=30)
def SEAtopCap():
	# construction geometries 
	pinHolderOuter = cylinder(h=10,r=4)
	pinHolderOuter.add_param('$fs', 1)
	
	pinHolderInner = cylinder(h=12,r=LINEAR_ROD_WITH_CLEARANCE_R)
	pinHolderInner.add_param('$fs', 1)
	
	motorOuter = cylinder(h=3,r=A2212_dia/2+2)
	motorOuter.add_param('$fs', 1)

	motorInner = cylinder(h=2,r=A2212_dia/2)
	motorInner.add_param('$fs', 1)

	m3HolePin = cylinder(h=12,r=1.5)
	m3HolePin.add_param('$fs', 1)
	m3HolePin = color([1,0,0, 1])(m3HolePin)

	# pad, main structure
	attachment = union()(
						motorOuter,
						translate([-15,10, 0])(pinHolderOuter),
						translate([15,-10, 0])(pinHolderOuter),
						translate([15,10, 0])(pinHolderOuter),
						translate([-15,-10, 0])(pinHolderOuter),
						)
	# pocket, main structure
	attachment = difference()(
						attachment,
						translate([-15,10, -1])(pinHolderInner),
						translate([15,-10, -1])(pinHolderInner),
						translate([15,10, -1])(pinHolderInner),
						translate([-15,-10, -1])(pinHolderInner),
						)
	attachment = color([1,0,0, 1])(attachment)
	# holes for motor mounting
	attachment = difference()(
						attachment,
						translate([0,0,-1])(pinHolderInner),
						translate([8,0, -1])(m3HolePin),
						translate([-8,0, -1])(m3HolePin),
						translate([0,9.5, -1])(m3HolePin),
						translate([0,-9.5, -1])(m3HolePin)
						)
	return attachment

@bom_part("Screw Rod m4",2)
def screwRod(len=LINEAR_ROD_LENGTH):
	rod = cylinder(h=len,r=SCREW_ROD_R)
	rod.add_param('$fs', 1)  # rod smooth
	rod = color([0.5,0.5,0.5, 1])(rod)
	return rod

@bom_part("Fibre Glass Rod 4mm",(8*USD2RMB)/20)
def linearRod(len=LINEAR_ROD_LENGTH):

	rod = cylinder(h=len,r=LINEAR_ROD_R)
	rod.add_param('$fs', 1)  # rod smooth
	rod = color([0,0,0, 1])(rod)

	return rod

#def head():
#	hx = cylinder(h=head_height, r=head_rad)
#	hx.add_param('$fn', 6)  # make the nut hexagonal
#	return hx
#
#@bom_part("M3x16 Bolt", 0.12)
#def m3_16(a=3):
#	bolt_height = 16
#	hx = cylinder(r=m3_rad, h=bolt_height)
#	hx.add_param('$fs', 1)  # rod smooth
#	m = union()(head(),translate([0, 0, -bolt_height])(hx))
#	return m
#
#@bom_part("M3x12 Bolt", 0.09)
#def m3_12():
#	bolt_height = 12
#	hx = cylinder(r=m3_rad, h=bolt_height)
#	hx.add_param('$fs', 1)  # rod smooth
#	m = union()(head(),translate([0, 0, -bolt_height])(hx))
#	return m
#
#@bom_part("M3 Nut", 0.04)
#def m3_nut():
#	hx = cylinder(r=nut_rad, h=nut_height)
#	hx.add_param('$fn', 6)  # make the nut hexagonal
#	n = difference()(hx,translate([0, 0, -EPSILON])(cylinder(r=m3_rad, h=nut_height + 2 * EPSILON)))
#	return n
#