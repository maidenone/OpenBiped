

union() {
	rotate(a = 90, v = [1, 0, 0]) {
		translate(v = [0, 80, 0]) {
			color(c = [0.8000000000, 0, 0.8000000000]) {
				difference() {
					cube(center = true, size = [30, 32, 10]);
					translate(v = [0, 20, 0]) {
						rotate(a = 90, v = [1, 0, 0]) {
							cylinder(h = 40, r = 2);
						}
					}
					translate(v = [-1, 3, 0]) {
						rotate(a = 0, v = [0, 0, 1]) {
							cube(center = true, size = [8, 1, 12]);
						}
					}
					translate(v = [1, 5, 0]) {
						rotate(a = 0, v = [0, 0, 1]) {
							cube(center = true, size = [8, 1, 12]);
						}
					}
					translate(v = [-1, 7, 0]) {
						rotate(a = 0, v = [0, 0, 1]) {
							cube(center = true, size = [8, 1, 12]);
						}
					}
					translate(v = [1, 9, 0]) {
						rotate(a = 0, v = [0, 0, 1]) {
							cube(center = true, size = [8, 1, 12]);
						}
					}
					translate(v = [-1, 11, 0]) {
						rotate(a = 0, v = [0, 0, 1]) {
							cube(center = true, size = [8, 1, 12]);
						}
					}
					translate(v = [1, 13, 0]) {
						rotate(a = 0, v = [0, 0, 1]) {
							cube(center = true, size = [8, 1, 12]);
						}
					}
					translate(v = [0, 0, 0]) {
						rotate(a = 90, v = [0, 0, 1]) {
							cube(center = true, size = [3.1000000000, 7.9000000000, 12]);
						}
					}
					translate(v = [1, -3, 0]) {
						rotate(a = 0, v = [0, 0, 1]) {
							cube(center = true, size = [8, 1, 12]);
						}
					}
					translate(v = [-1, -5, 0]) {
						rotate(a = 0, v = [0, 0, 1]) {
							cube(center = true, size = [8, 1, 12]);
						}
					}
					translate(v = [1, -7, 0]) {
						rotate(a = 0, v = [0, 0, 1]) {
							cube(center = true, size = [8, 1, 12]);
						}
					}
					translate(v = [-1, -9, 0]) {
						rotate(a = 0, v = [0, 0, 1]) {
							cube(center = true, size = [8, 1, 12]);
						}
					}
					translate(v = [1, -11, 0]) {
						rotate(a = 0, v = [0, 0, 1]) {
							cube(center = true, size = [8, 1, 12]);
						}
					}
					translate(v = [-1, -13, 0]) {
						rotate(a = 0, v = [0, 0, 1]) {
							cube(center = true, size = [8, 1, 12]);
						}
					}
					translate(v = [-7, 0, 0]) {
						rotate(a = 0, v = [0, 0, 1]) {
							cube(center = true, size = [4, 28, 12]);
						}
					}
					translate(v = [-11, 10, 0]) {
						rotate(a = 0, v = [1, 0, 0]) {
							cube(center = true, size = [3.1000000000, 7.9000000000, 12]);
						}
					}
					translate(v = [-11, 0, 0]) {
						rotate(a = 0, v = [1, 0, 0]) {
							cube(center = true, size = [3.1000000000, 7.9000000000, 12]);
						}
					}
					translate(v = [-11, -10, 0]) {
						rotate(a = 0, v = [1, 0, 0]) {
							cube(center = true, size = [3.1000000000, 7.9000000000, 12]);
						}
					}
					translate(v = [5, 10, 0]) {
						rotate(a = 90, v = [0, 1, 0]) {
							cylinder(h = 40, r = 2);
						}
					}
					translate(v = [5, 0, 0]) {
						rotate(a = 90, v = [0, 1, 0]) {
							cylinder(h = 40, r = 2);
						}
					}
					translate(v = [5, -10, 0]) {
						rotate(a = 90, v = [0, 1, 0]) {
							cylinder(h = 40, r = 2);
						}
					}
					translate(v = [7, 0, 0]) {
						rotate(a = 0, v = [0, 0, 1]) {
							cube(center = true, size = [4, 28, 12]);
						}
					}
					translate(v = [11, 10, 0]) {
						rotate(a = 0, v = [1, 0, 0]) {
							cube(center = true, size = [3.1000000000, 7.9000000000, 12]);
						}
					}
					translate(v = [11, 0, 0]) {
						rotate(a = 0, v = [1, 0, 0]) {
							cube(center = true, size = [3.1000000000, 7.9000000000, 12]);
						}
					}
					translate(v = [11, -10, 0]) {
						rotate(a = 0, v = [1, 0, 0]) {
							cube(center = true, size = [3.1000000000, 7.9000000000, 12]);
						}
					}
					translate(v = [-5, 10, 0]) {
						rotate(a = 90, v = [0, -1, 0]) {
							cylinder(h = 40, r = 2);
						}
					}
					translate(v = [-5, 0, 0]) {
						rotate(a = 90, v = [0, -1, 0]) {
							cylinder(h = 40, r = 2);
						}
					}
					translate(v = [-5, -10, 0]) {
						rotate(a = 90, v = [0, -1, 0]) {
							cylinder(h = 40, r = 2);
						}
					}
				}
			}
		}
	}
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
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

from solid import *
from solid.utils import *  # Not required, but the utils module is useful
from partList import *

def assemble():
	return union()(
		(rotate(90,[1,0,0])(translate([0,80,0])(printedSpring()))),
#		ESC40W(),
#		translate([0,0, 20])(A2212()),
#		(rotate(90,[0,0,1]))(rotate(90,[1,0,0])(translate([0,80,-15])(SEAbracketSide()))),
#		(rotate(90,[0,0,1]))(rotate(90,[-1,0,0])(translate([0,-80,-15])(SEAbracketSide()))),
#		translate([0,0, 22])(ShaftAdapter3_17to4mm()),
#		translate([0,0,24])(screwRodm4(200)),
#		(translate([0,0, 140])(SEAtopCap())),
#		translate([0,0, -10])(A2212Attachment()),
#		translate([-15,10,0])(linearRod4mm()),
#		translate([-15,-10,65])(linearRod4mm()),
#		translate([15,10,65])(linearRod4mm()),
#		translate([15,-10,0])(linearRod4mm()),
	)

if __name__ == '__main__':
	out_dir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
	file_out = os.path.join(out_dir, 'SEA.scad')
	a = assemble()
	bom = bill_of_materials()
	print("%(__file__)s: SCAD file written to: \n%(file_out)s" % vars())
	print(bom)
	scad_render_to_file(a, file_out) 
 
************************************************/
