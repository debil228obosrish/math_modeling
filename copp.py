import math
from ClimateUtilities import *
import phys
import numpy as nm
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import patches
#from matplotlib import animation


#------------Constants and file data------------
# 
printswitch = True
printswitch = False
printswitch2 = True
#printswitch2 = False

ECCabsoluteMax = 0.9
ECCmax = 0.067      # maximum value for this run - 
                    # should not be greater than
                    # ECCabsoluteMax
#ECCmax = 0.9       # maximum value for this run - should not be greater 
                    # than
                    # ECCabsoluteMax
if  ECCmax >= ECCabsoluteMax: 
    ECCmax = ECCabsoluteMax

ECCdelta = 0.001    # interval for graph

eccentricity = nm.arange(0., ECCmax, ECCdelta, dtype=float)
semimajorA = 1.0        # astronomical unit =~ 150.000.000 km mean        
                        # distance Sun Earth
totalRadN0 = 1370.      # radiation of Sun at TOA in Watt/m**2
albedoEarth = 0.3       # presently albedo of Earth, geographically 
                        # constant
T = 365.25              # duration of one orbit around central celestial 
                        # body in days
                        # here: duration of one orbit of Earth around Sun
R = 6378100.0           # radius of Earth in meters

TOIdim = ECCmax/ECCdelta
TOI = nm.arange(0., TOIdim, dtype=float ) 
                    # total insolation at location of Earth summed over 1 
                    # year
deltaT = 500        # ms interval of moving


# now define various "functions" like:

def computeTOI( ee, semimajorAxis, radiationAtStar, alpha  ):

    aa = semimajorAxis  # semimajor axis of orbital ellipse
    N0 = radiationAtStar# radiation of start at position of star (r = 0)
    resultTOI = 2.*nm.pi*T*R**2*N0*alpha/(aa**2*math.sqrt(1 - ee**2))
    return resultTOI

#
#####################################################################
#
print "start of ellipticity and absorbed insolation"
#
#
# Start of programme here
#
#####################################################################

# compute the various TOIs dependant on eccentricity "ecc"
#
ii = 0
for ecc in eccentricity:
    if printswitch:   print 'TOI = ', computeTOI( ecc, semimajorA,     
        totalRadN0, albedoEarth ), '\n'
    TOI[ii] = computeTOI( ecc, semimajorA, totalRadN0, 1. - albedoEarth 
                )/10.0**19
    ii = ii + 1

# TOI is an array consisting of TOIs depending on eccemtricity "ecc" 

x = eccentricity

if printswitch: print 'TOI = ', TOI
##########################################################################
# almost the whole screen is filled with this plot ... :)
##########################################################################

Main = plt.figure(figsize=(15.0,15.0))  
Main.subplots_adjust(top=0.95, left=0.09, right=0.95, hspace=0.20)

##########################################################################
axFigTOI = Main.add_subplot(211)     # first subplot

# Plot ... TOI over ECC: 

if ECCmax < 0.07: 
    plt.axis([0,0.07,8.9,9.0]) 

plt.title( 'Absorbed Irradiation and Orbital Eccentricity for Planet 
            Earth\n' )
plt.ylabel( 'Absorbed total \nsolar irradiation \n[Watt] *10**19' )
plt.xlabel( 'Eccentricity "e"' )

plt.plot( x, TOI, 'r-' )  # 'x' and 'TOI' are also center of "mini-
                          # ellipse"

# Now enter an ellipse here on Subplot 211 (first subplot) which slides 
# along curve:

xcenter, ycenter = x[1],TOI[1]      # center of ellipse to start with
width = 0.0025                      # width of small ellipse
height = 0.01                       # height of small ellipse

def init():                         # in order to initialize animation
    e1 = patches.Ellipse((xcenter, ycenter), width, height,\
        angle=0.0, linewidth=2, fill=False )

    axFigTOI.add_patch(e1)
    e1.set_visible( False )         # do not show (if True then ellipse 
                                    # stays here
    return [e1]

def animateEllipse(i):

    xcenter = x[i]
    ycenter = TOI[i]
    e1 = patches.Ellipse( ( xcenter, ycenter ), width, height,\
                     angle = 0.0, linewidth = 2, fill = True )
    if i == 1:
        e1.set_visible( True )

    axFigTOI.add_patch(e1)
    if printswitch: print 'i = ', i
    return [e1]

anim = animation.FuncAnimation( Main, 
                                animateEllipse, 
                                init_func=init, 
                                frames= int( TOIdim ), 
                                interval=deltaT,
                                blit=True )

#########################################################################
# the second subplot in the first figure for size of ellipse depending on 
# ECC
#########################################################################

# we still have a problem to get the "patch" (Ellipse) into the 2nd 
# subplot ...


axFigEllipse = Main.add_subplot(212)

plt.title( 'Shape of an Ellipse due to eccentricity' )
plt.ylabel( 'Height of Ellipse' )
plt.xlabel( 'Constant Semi-major Axis' )
"""
# 
# create an ellipse with following parameters - to be changed later for 
# curve
#   values
#


xcenter2 = x[40]
ycenter2 = TOI[40]      # center of ellipse 2 to start with
width2 = 0.0125
height2 = 0.0115

ell2 = patches.Ellipse( ( xcenter2, ycenter2 ), width2, height2,\
      angle=0.0, linewidth=2, fill=False )

ell2.set_visible(True)
axFigEllipse.add_patch(ell2)

#"""
"""

def init212():                         # in order to initialize animation
    ell2 = patches.Ellipse((xcenter2, ycenter2), width2, height2,\
        angle=0.0, linewidth=2, fill=False )

    axFigEllipse.add_patch(ell2)
    ell2.set_visible( False )         # do not show (if True then ellipse 
                                      # stays here
    return [ell2]

def animateEllipse(jj):

    #xcenter2 = xcenter2 + jj/10**4
    #ycenter2 = ycenter2 + jj/10**4
    ell2 = patches.Ellipse((xcenter2, ycenter2), width2, height2,\
         angle=0.0, linewidth=2, fill=True, zorder=2)
    if jj == 1:
        ell2.set_visible(True)

    axFigEllipse.add_patch(ell2)

    return [ell2]



anim = animation.FuncAnimation( Main, animateEllipse, 
                               init_func=init212, 
                               frames=360, 
                               interval=20,
                               blit=True )


#anim = animation.FuncAnimation(figEllipse, animateEllipse,     
        init_func=init_Ellipse, interval=1, blit=True)
#"""
plt.show()