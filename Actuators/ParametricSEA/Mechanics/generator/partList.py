from solid import *
from solid.utils import *  # Not required, but the utils module is useful

#configuration
head_rad = 2.65
head_height = 2.8

nut_height = 2.3
nut_rad = 3

m3_rad = 1.4

A2212_dia = 27.7

USD2RMB = 6.95
RMB2USD = 0.144

set_bom_headers("filamentUsage","link")

#parts
#! /usr/bin/env python
# -*- coding: utf-8 -*-


@bom_part("SpringHolderShellMiddleNut")
def SpringHolderShellMiddleNut():
	body = cube([20,12,14],True)
	centerHole = cube([10,12,10],True)
	m4Hole = cylinder(r=2,h=100,center=True)
	m4Hole.add_param('$fs', 1)  # rod smooth
	nutHole = cube((3.1,7.9,40),center=True)
	holder = difference()(
		body,
		translate([11,0,0])(centerHole),
		translate([-11,0,0])(centerHole),
		rotate(a=90,v=[1,0,0])(m4Hole),
		translate([0,0,0])(rotate(90,[0,0,1])(nutHole)),
	)
	return color([1,0,0, 1])(holder)



def sinusoidal_ring(rad=0.2, segments=148):
    outline = []
    z = 0.0
    for i in range(segments):
        angle = i * 360*10 / segments
        x = rad * cos(radians(angle))
        y = rad * sin(radians(angle))
        z = z + 0.2
        outline.append(Point3(x, y, z))
    return outline


def star(num_points=5, outer_rad=1.0, dip_factor=0.0):
    star_pts = []
    for i in range(2 * num_points):
        rad = outer_rad - i % 2 * dip_factor * outer_rad
        angle = radians(360 / (2 * num_points) * i)
        star_pts.append(Point3(rad * cos(angle), rad * sin(angle), 0))
    return star_pts


def extrude_example():

    # Note the incorrect triangulation at the two ends of the path.  This
    # is because star isn't convex, and the triangulation algorithm for
    # the two end caps only works for convex shapes.
    shape = star(num_points=5)
    path = sinusoidal_ring(rad=7.5)

    # If scale_factors aren't included, they'll default to
    # no scaling at each step along path.  Here, let's
    # make the shape twice as big at beginning and end of the path

    extruded = extrude_along_path(shape_pts=shape, path_pts=path)

    return extruded

@bom_part("MetalSpring")
def MetalSpring():
	helix = linear_extrude(height=100, center=True, convexity=100, twist=100, slices=100, scale=100)
	linear_extrude(height = 10, center = true, convexity = 10, twist = 5*360)
	translate([2, 0, 0])
	circle(r = 0.2);
	#helix.add_param('$fs', 1)  # rod smooth
	return helix #color([0,0,0,1])(helix)

@bom_part("SpringHolderShell")
def SpringHolderShell():
	spring_length = 32
	spring_width = 17
	shell_length = spring_length*2+14;
	body = cube([30,shell_length,10],True)
	centerHole = cube([19,shell_length-14,12],True)
	m4Hole = cylinder(r=2,h=100,center=True)
	m4Hole.add_param('$fs', 1)  # rod smooth
	nutHole = cube((3.1,7.9,12),center=True)
	nutHoleCutIn_x = 12.5
	pinHoleCutIn_x = 10

	holder = difference()(
		body,
		# nut holes left
		translate([-1*nutHoleCutIn_x,-30,0])(rotate(0,[1,0,0])(nutHole)),
		translate([-1*nutHoleCutIn_x,-20,0])(rotate(0,[1,0,0])(nutHole)),
		translate([-1*nutHoleCutIn_x,-10,0])(rotate(0,[1,0,0])(nutHole)),
		translate([-1*nutHoleCutIn_x,0,0])(rotate(0,[1,0,0])(nutHole)),
		translate([-1*nutHoleCutIn_x,10,0])(rotate(0,[1,0,0])(nutHole)),
		translate([-1*nutHoleCutIn_x,20,0])(rotate(0,[1,0,0])(nutHole)),
		translate([-1*nutHoleCutIn_x,30,0])(rotate(0,[1,0,0])(nutHole)),
		# pin holes left
		translate([pinHoleCutIn_x,30,0])(rotate(90,[0,1,0])(m4Hole)),
		translate([pinHoleCutIn_x,20,0])(rotate(90,[0,1,0])(m4Hole)),
		translate([pinHoleCutIn_x,10,0])(rotate(90,[0,1,0])(m4Hole)),
		translate([pinHoleCutIn_x,0,0])(rotate(90,[0,1,0])(m4Hole)),
		translate([pinHoleCutIn_x,-10,0])(rotate(90,[0,1,0])(m4Hole)),
		translate([pinHoleCutIn_x,-20,0])(rotate(90,[0,1,0])(m4Hole)),
		translate([pinHoleCutIn_x,-30,0])(rotate(90,[0,1,0])(m4Hole)),

		# nut holes right
		translate([1*nutHoleCutIn_x,-30,0])(rotate(0,[1,0,0])(nutHole)),
		translate([1*nutHoleCutIn_x,-20,0])(rotate(0,[1,0,0])(nutHole)),
		translate([1*nutHoleCutIn_x,-10,0])(rotate(0,[1,0,0])(nutHole)),
		translate([1*nutHoleCutIn_x,0,0])(rotate(0,[1,0,0])(nutHole)),
		translate([1*nutHoleCutIn_x,10,0])(rotate(0,[1,0,0])(nutHole)),
		translate([1*nutHoleCutIn_x,20,0])(rotate(0,[1,0,0])(nutHole)),
		translate([1*nutHoleCutIn_x,30,0])(rotate(0,[1,0,0])(nutHole)),
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
	m4HolePin = cylinder(h=30,r=2)
	m4HolePin.add_param('$fs', 1)
	distance = sqrt(pow(20,2)+pow(30,2))
	body = cube((distance+8,8,30),True)


	body = difference()(
		body,
		(translate([-distance/2.0,0, -2]))(m4HolePin),
		translate([distance/2.0,0, -2])(m4HolePin),
		(translate([0,10,-8]))(rotate(a=90,v=[1,0,0])(m4HolePin)),
	)
	return body

@bom_part("A2212 Attachment",price=0.2,print_time=32)
def A2212Attachment():
	
	# construction geometries 
	pinHolderOuter = cylinder(h=10,r=4)
	pinHolderOuter.add_param('$fs', 1)
	
	pinHolderInner = cylinder(h=12,r=2)
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
						)
	# pocket, main structure
	attachment = difference()(
						attachment,
						translate([0,0, 2])(motorInner),
						translate([-15,10, 2])(pinHolderInner),
						translate([15,-10, 2])(pinHolderInner),
						)
	attachment = color([1,1,0, 1])(attachment)
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

@bom_part("SEA sled side bracket",price=0.5,print_time=32)
def SEAbracketSide():
	bracket = cube((28,30,8),center=True)
	pocket1 = cube((32,16,5),True)
	pocket2 = cube((12,32,5),True)
	bracket = color([0,1,0, 1])(bracket)
	holePin = cylinder(h=34,r=2)
	holeLock = cylinder(h=34,r=1)
	bracket = difference()(
						(bracket),
						translate([0,0,2])(pocket1),
						translate([0,0,2])(pocket2),
						translate([0,-10,-10])(holePin),
						translate([0,0,-10])(holePin),
						translate([0,10,-10])(holePin),
						rotate(a=90,v=[0,1,0])(translate([0,11,-16])(holeLock)),
						rotate(a=90,v=[0,1,0])(translate([0,-11,-16])(holeLock)),
						rotate(a=90,v=[1,0,0])(translate([-10,0,-16])(holePin)),
						rotate(a=90,v=[1,0,0])(translate([10,0,-16])(holePin)),
						)
	return bracket

@bom_part("SEA 3d printed spring",price=0.2,print_time=32)
def printedSpring():
	sideCleranceOffset = 8
	sprindWidthCleranceOffset = 2
	nutHoleCutIn_x = 11
	pinHoleCutIn_x = 8
	springGap_y = 1
	springGap_x = 11
	bracket = cube((30,32,10),center=True)
	nutHole = cube((3.1,7.9,12),center=True)
	springSideClearance = cube((2,28,12),True)
	springWidthClearance = cube((springGap_x,springGap_y,12),True)
	springWidthFillet_r = (springGap_y/2.0)
	sprindWidthFillet = cylinder(h=4000,r=springWidthFillet_r)
	sprindWidthFillet.add_param('$fs', 0.1)

	holePin = cylinder(h=40,r=2)
	holePin.add_param('$fs', 1)

	springCutout = bracket
	for i in range(0,3):
			offset_y1 = 3+i*4;
			offset_y2 = 5+i*4;

			# spring clerance top
			springCutout = difference()(
				springCutout,
				# top
				translate([sprindWidthCleranceOffset*-1,offset_y1,0])(rotate(0,[0,0,1])(springWidthClearance)), # spring gap
				translate([sprindWidthCleranceOffset*-1+(springGap_x/2+springWidthFillet_r),offset_y1,-10])(rotate(0,[0,0,1])(sprindWidthFillet)), # spring gap fillet
				
				translate([sprindWidthCleranceOffset,offset_y2,0])(rotate(0,[0,0,1])(springWidthClearance)),
				translate([sprindWidthCleranceOffset-(springGap_x/2+springWidthFillet_r),offset_y2,-10])(rotate(0,[0,0,1])(sprindWidthFillet)),

				# bottom
				translate([sprindWidthCleranceOffset,offset_y1*-1,0])(rotate(0,[0,0,1])(springWidthClearance)), # spring gap
				translate([sprindWidthCleranceOffset-(springGap_x/2+springWidthFillet_r),offset_y1*-1,-10])(rotate(0,[0,0,1])(sprindWidthFillet)), # spring gap fillet
				
				translate([sprindWidthCleranceOffset*-1,offset_y2*-1,0])(rotate(0,[0,0,1])(springWidthClearance)),
				translate([sprindWidthCleranceOffset*-1+(springGap_x/2+springWidthFillet_r),offset_y2*-1,-10])(rotate(0,[0,0,1])(sprindWidthFillet)),

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
	
	pinHolderInner = cylinder(h=12,r=2)
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
def screwRodm4(len):
	rod = cylinder(h=len,r=2)
	rod.add_param('$fs', 1)  # rod smooth
	rod = color([0.5,0.5,0.5, 1])(rod)
	return rod

@bom_part("Fibre Glass Rod 4mm",(8*USD2RMB)/20)
def linearRod4mm():

	rod = cylinder(h=250,r=2)
	rod.add_param('$fs', 1)  # rod smooth
	rod = color([0,0,0, 1])(rod)

	return rod

def head():
	hx = cylinder(h=head_height, r=head_rad)
	hx.add_param('$fn', 6)  # make the nut hexagonal
	return hx

@bom_part("M3x16 Bolt", 0.12)
def m3_16(a=3):
	bolt_height = 16
	hx = cylinder(r=m3_rad, h=bolt_height)
	hx.add_param('$fs', 1)  # rod smooth
	m = union()(head(),translate([0, 0, -bolt_height])(hx))
	return m

@bom_part("M3x12 Bolt", 0.09)
def m3_12():
	bolt_height = 12
	hx = cylinder(r=m3_rad, h=bolt_height)
	hx.add_param('$fs', 1)  # rod smooth
	m = union()(head(),translate([0, 0, -bolt_height])(hx))
	return m

@bom_part("M3 Nut", 0.04)
def m3_nut():
	hx = cylinder(r=nut_rad, h=nut_height)
	hx.add_param('$fn', 6)  # make the nut hexagonal
	n = difference()(hx,translate([0, 0, -EPSILON])(cylinder(r=m3_rad, h=nut_height + 2 * EPSILON)))
	return n
