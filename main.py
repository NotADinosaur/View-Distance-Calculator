import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", type = float, help = "input for field of view (in degrees)", required = True)
parser.add_argument("-r", type = float, help = "radius of the area you want to view", required = True)
parser.add_argument("-v", default = False, action = "store_true", help = "enable verbose output")
parser.add_argument("-u", type = str, default = "units", help = "unit to use for radius and distance")
args = parser.parse_args()

def aquire_tan(f):
    global tan
    tan = math.tan(math.radians(args.f))
    
def aquire_needed_distance(r):
    distance = r / tan
    print("You need to be " +str(distance) + " " + args.u + " away")

aquire_tan(args.f)

if args.v == True:
    print("FOV: " + str(args.f) + " degrees")
    print("Radius: " + str(args.r) + " " + args.u)
    print("tan(" + str(args.f) + "): " + str(tan))

aquire_needed_distance(args.r)
