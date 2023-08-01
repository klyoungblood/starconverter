#!/usr/bin/env python3

import math

hms = input ("Enter right ascension H M S, separated by spaces: ")
h,m,s=hms.split(' ')

rah=float(h)
ram=float(m)
ras=float(s)

dec = input ("Enter declination in D M S, separated by spaces: ")
d,m,s=dec.split(' ')

decdeg=float(d)
decmin=float(m)
decsec=float(s)

ly = input ("Ender distance from sol system in Light Years: ")

rho=float(ly)

# convert RA from HMS to degrees, then to radians

theta = math.radians((rah+ram/60.0+ras/3600.0) * 15.0)

# delincation is above or below equator,
# phi angle is angle off vertical axis
# convert declination to phi angle, in radians
phi = math.radians(90.0 - decdeg+decmin/60.0+decsec/3600.0)

# godot uses y=UP rather than Z=up
x = rho * math.sin(phi) * math.cos(theta)
y = rho * math.cos(theta)
z = rho * math.sin(phi) * math.sin(theta)

print (x, y, z)

input ("Press Enter to exit.")
