

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
	cube(size = 1);
	translate(v = [0, 0, 20]) {
		difference() {
			color(c = [0, 0, 1, 1]) {
				union() {
					cylinder($fs = 1, h = 9.5000000000, r = 1.5850000000);
					translate(v = [0, 0, -2]) {
						cylinder($fs = 1, h = 2, r = 4);
					}
					translate(v = [0, 0, -8]) {
						cylinder($fs = 1, h = 6, r1 = 13.8500000000, r2 = 5);
					}
					translate(v = [0, 0, -28]) {
						cylinder($fs = 1, h = 20, r = 13.8500000000);
					}
				}
			}
			translate(v = [8, 0, -29]) {
				color(c = [1, 0, 0, 1]) {
					cylinder($fs = 1, h = 11, r = 1.5000000000);
				}
			}
			translate(v = [-8, 0, -29]) {
				color(c = [1, 0, 0, 1]) {
					cylinder($fs = 1, h = 11, r = 1.5000000000);
				}
			}
			translate(v = [0, 9.5000000000, -29]) {
				color(c = [1, 0, 0, 1]) {
					cylinder($fs = 1, h = 11, r = 1.5000000000);
				}
			}
			translate(v = [0, -9.5000000000, -29]) {
				color(c = [1, 0, 0, 1]) {
					cylinder($fs = 1, h = 11, r = 1.5000000000);
				}
			}
		}
	}
	rotate(a = 90, v = [0, 0, 1]) {
		rotate(a = 90, v = [1, 0, 0]) {
			translate(v = [0, 80, -15]) {
				difference() {
					color(c = [0, 1, 0, 1]) {
						cube(center = true, size = [28, 30, 8]);
					}
					translate(v = [0, 0, 2]) {
						cube(center = true, size = [32, 16, 5]);
					}
					translate(v = [0, 0, 2]) {
						cube(center = true, size = [12, 32, 5]);
					}
					translate(v = [0, -10, -10]) {
						cylinder(h = 34, r = 2);
					}
					translate(v = [0, 0, -10]) {
						cylinder(h = 34, r = 2);
					}
					translate(v = [0, 10, -10]) {
						cylinder(h = 34, r = 2);
					}
					rotate(a = 90, v = [0, 1, 0]) {
						translate(v = [0, 11, -16]) {
							cylinder(h = 34, r = 1);
						}
					}
					rotate(a = 90, v = [0, 1, 0]) {
						translate(v = [0, -11, -16]) {
							cylinder(h = 34, r = 1);
						}
					}
					rotate(a = 90, v = [1, 0, 0]) {
						translate(v = [-10, 0, -16]) {
							cylinder(h = 34, r = 2);
						}
					}
					rotate(a = 90, v = [1, 0, 0]) {
						translate(v = [10, 0, -16]) {
							cylinder(h = 34, r = 2);
						}
					}
				}
			}
		}
	}
	rotate(a = 90, v = [0, 0, 1]) {
		rotate(a = 90, v = [-1, 0, 0]) {
			translate(v = [0, -80, -15]) {
				difference() {
					color(c = [0, 1, 0, 1]) {
						cube(center = true, size = [28, 30, 8]);
					}
					translate(v = [0, 0, 2]) {
						cube(center = true, size = [32, 16, 5]);
					}
					translate(v = [0, 0, 2]) {
						cube(center = true, size = [12, 32, 5]);
					}
					translate(v = [0, -10, -10]) {
						cylinder(h = 34, r = 2);
					}
					translate(v = [0, 0, -10]) {
						cylinder(h = 34, r = 2);
					}
					translate(v = [0, 10, -10]) {
						cylinder(h = 34, r = 2);
					}
					rotate(a = 90, v = [0, 1, 0]) {
						translate(v = [0, 11, -16]) {
							cylinder(h = 34, r = 1);
						}
					}
					rotate(a = 90, v = [0, 1, 0]) {
						translate(v = [0, -11, -16]) {
							cylinder(h = 34, r = 1);
						}
					}
					rotate(a = 90, v = [1, 0, 0]) {
						translate(v = [-10, 0, -16]) {
							cylinder(h = 34, r = 2);
						}
					}
					rotate(a = 90, v = [1, 0, 0]) {
						translate(v = [10, 0, -16]) {
							cylinder(h = 34, r = 2);
						}
					}
				}
			}
		}
	}
	translate(v = [0, 0, 22]) {
		color(c = [1, 0, 0, 1]) {
			difference() {
				cylinder($fs = 1, h = 10, r = 6);
				cylinder($fs = 1, h = 5, r = 1.5850000000);
				translate(v = [0, 0, 5]) {
					cylinder($fs = 1, h = 5, r = 2);
				}
			}
		}
	}
	translate(v = [0, 0, 24]) {
		color(c = [0.5000000000, 0.5000000000, 0.5000000000, 1]) {
			cylinder($fs = 1, h = 200, r = 2);
		}
	}
	translate(v = [0, 0, 140]) {
		difference() {
			color(c = [1, 0, 0, 1]) {
				difference() {
					union() {
						cylinder($fs = 1, h = 3, r = 15.8500000000);
						translate(v = [-15, 10, 0]) {
							cylinder($fs = 1, h = 10, r = 4);
						}
						translate(v = [15, -10, 0]) {
							cylinder($fs = 1, h = 10, r = 4);
						}
						translate(v = [15, 10, 0]) {
							cylinder($fs = 1, h = 10, r = 4);
						}
						translate(v = [-15, -10, 0]) {
							cylinder($fs = 1, h = 10, r = 4);
						}
					}
					translate(v = [-15, 10, -1]) {
						cylinder($fs = 1, h = 12, r = 2);
					}
					translate(v = [15, -10, -1]) {
						cylinder($fs = 1, h = 12, r = 2);
					}
					translate(v = [15, 10, -1]) {
						cylinder($fs = 1, h = 12, r = 2);
					}
					translate(v = [-15, -10, -1]) {
						cylinder($fs = 1, h = 12, r = 2);
					}
				}
			}
			translate(v = [0, 0, -1]) {
				cylinder($fs = 1, h = 12, r = 2);
			}
			translate(v = [8, 0, -1]) {
				color(c = [1, 0, 0, 1]) {
					cylinder($fs = 1, h = 12, r = 1.5000000000);
				}
			}
			translate(v = [-8, 0, -1]) {
				color(c = [1, 0, 0, 1]) {
					cylinder($fs = 1, h = 12, r = 1.5000000000);
				}
			}
			translate(v = [0, 9.5000000000, -1]) {
				color(c = [1, 0, 0, 1]) {
					cylinder($fs = 1, h = 12, r = 1.5000000000);
				}
			}
			translate(v = [0, -9.5000000000, -1]) {
				color(c = [1, 0, 0, 1]) {
					cylinder($fs = 1, h = 12, r = 1.5000000000);
				}
			}
		}
	}
	translate(v = [0, 0, -10]) {
		difference() {
			color(c = [1, 1, 0, 1]) {
				difference() {
					union() {
						cylinder($fs = 1, h = 3, r = 15.8500000000);
						translate(v = [-15, 10, 0]) {
							cylinder($fs = 1, h = 10, r = 4);
						}
						translate(v = [15, -10, 0]) {
							cylinder($fs = 1, h = 10, r = 4);
						}
					}
					translate(v = [0, 0, 2]) {
						cylinder($fs = 1, h = 2, r = 13.8500000000);
					}
					translate(v = [-15, 10, 2]) {
						cylinder($fs = 1, h = 12, r = 2);
					}
					translate(v = [15, -10, 2]) {
						cylinder($fs = 1, h = 12, r = 2);
					}
				}
			}
			translate(v = [0, 0, -1]) {
				cylinder($fs = 1, h = 12, r = 2);
			}
			translate(v = [8, 0, -1]) {
				color(c = [1, 0, 0, 1]) {
					cylinder($fs = 1, h = 12, r = 1.5000000000);
				}
			}
			translate(v = [-8, 0, -1]) {
				color(c = [1, 0, 0, 1]) {
					cylinder($fs = 1, h = 12, r = 1.5000000000);
				}
			}
			translate(v = [0, 9.5000000000, -1]) {
				color(c = [1, 0, 0, 1]) {
					cylinder($fs = 1, h = 12, r = 1.5000000000);
				}
			}
			translate(v = [0, -9.5000000000, -1]) {
				color(c = [1, 0, 0, 1]) {
					cylinder($fs = 1, h = 12, r = 1.5000000000);
				}
			}
		}
	}
	translate(v = [-15, 10, 0]) {
		color(c = [0, 0, 0, 1]) {
			cylinder($fs = 1, h = 250, r = 2);
		}
	}
	translate(v = [-15, -10, 65]) {
		color(c = [0, 0, 0, 1]) {
			cylinder($fs = 1, h = 250, r = 2);
		}
	}
	translate(v = [15, 10, 65]) {
		color(c = [0, 0, 0, 1]) {
			cylinder($fs = 1, h = 250, r = 2);
		}
	}
	translate(v = [15, -10, 0]) {
		color(c = [0, 0, 0, 1]) {
			cylinder($fs = 1, h = 250, r = 2);
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
		ESC40W(),
		translate([0,0, 20])(A2212()),
		(rotate(90,[0,0,1]))(rotate(90,[1,0,0])(translate([0,80,-15])(SEAbracketSide()))),
		(rotate(90,[0,0,1]))(rotate(90,[-1,0,0])(translate([0,-80,-15])(SEAbracketSide()))),
		translate([0,0, 22])(ShaftAdapter3_17to4mm()),
		translate([0,0,24])(screwRodm4(200)),
		(translate([0,0, 140])(SEAtopCap())),
		translate([0,0, -10])(A2212Attachment()),
		translate([-15,10,0])(linearRod4mm()),
		translate([-15,-10,65])(linearRod4mm()),
		translate([15,10,65])(linearRod4mm()),
		translate([15,-10,0])(linearRod4mm()),
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
