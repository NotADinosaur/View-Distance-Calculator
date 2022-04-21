import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", type = float, help = "input for field of view (in degrees)", required = True)
parser.add_argument("-r", type = float, help = "radius of the area you want to view", required = True)
args = parser.parse_args()

print("FOV: " + str(args.f) + " degrees")
print("Radius: " + str(args.r) + " units")

def aquire_tan(f):
    global tan
    tan = math.tan(math.radians(args.f))
    print(tan)

def aquire_needed_distance(r):
    distance = r / tan
    print("You need to be " +str(distance) + " units away")

aquire_tan(args.f)
aquire_needed_distance(args.r)
