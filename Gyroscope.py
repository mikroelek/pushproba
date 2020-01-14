from sense_hat import SenseHat
import time
import globals
globals.init()
def gyro():
     sense=SenseHat()
     globals.pitch,globals.roll,globals.yaw=sense.get_accelerometer().values()
     globals.x,globals.y,globals.z=sense.get_accelerometer_raw().values()
     #globals.pitch=round(globals.pitch,0)
    # globals.roll=round(globals.roll,0)
    # globals.yaw=round(globals.yaw,0)
   # x=round(x,1)
  #  y=round(y,1)
   # z=round(z,1)
   # print("p:{0},r:{1},y:{2},x:{3},y:{4},z:{5}".format(pitch,roll,yaw,x,y,z))

