import sys
from officelifx import CeilingLights

lights = CeilingLights()

def run_instr(instr):
    if instr == "on":
        lights.on()
    elif instr == "off":
        lights.off()
    elif instr == "day":
        lights.day()
    elif instr == "night":
        lights.night()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_instr(sys.argv[1])
    else:
        print('Provide a command: [on, off, day, night]')