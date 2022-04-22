import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", type = float, help = "input for field of view (in degrees)", required = True)
parser.add_argument("-r", type = float, help = "radius of the area you want to view", required = True)
parser.add_argument("-v", default = False, action = "store_true", help = "enable verbose output")
parser.add_argument("-u", type = str, default = "units", help = "unit to use for radius and distance")
parser.add_argument("-d", type = int, default = 3, help = "amout of decimal places to output")
args = parser.parse_args()

def find_tan(f):
    global tan
    tan = math.tan(math.radians(args.f))
    
def needed_distance(r):
    global distance
    distance = r / tan

#function from 2016 stackoverflow lol
def truncate(distance, d) -> float:
    stepper = 10.0 ** d
    return math.trunc(stepper * distance) / stepper

find_tan(args.f)
needed_distance(args.r)
truncatedDistance = truncate(distance, args.d)

if args.v == True:
    print("FOV: " + str(args.f) + " degrees")
    print("Radius: " + str(args.r) + " " + args.u)
    print("tan(" + str(args.f) + "): " + str(tan))

print("You need to be " + str(truncatedDistance) + " " + args.u + " away")
