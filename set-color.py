import sys
from officelifx import BuildLight, Colors

if len(sys.argv) > 1:
    color = Colors.from_string(sys.argv[1])
else:
    color = Colors.GREEN

light = BuildLight()
light.set_color(color)