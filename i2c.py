#import modules
from smbus2 import SMBus
import time

bus = SMBus(1)

DEVICE_ADDRESS = 0x23
CONTINUOUS_H_RES = 0x10

def configure():
  print("Configure")
  bus.write_byte(DEVICE_ADDRESS, CONTINUOUS_H_RES) # Set mode
  time.sleep(.01) # sleep 10ms
  print("Done configure")

def read():
  print("Read")
  level = -1.0

  # Get two bytes
  measurement = bus.read_i2c_block_data(DEVICE_ADDRESS, CONTINUOUS_H_RES, 2)
  print(f"Measurement: {measurement}")
  level = measurement[0] << 8 | measurement[1]

  if (level != -1.0):
    # Convert to lux
    level /= 2.4

  print(f"level: {level}")
  return level

try:
  configure()
  while 1:
    val = read()
    if(val < 20): print("too dark")
    elif(val < 70): print("medium")
    elif(val < 500): print("bright")
    else: print("too bright")
    time.sleep(0.75)

except KeyboardInterrupt:
  print("\nProgram Exited Cleanly")
except Exception as e:
  print(e);
