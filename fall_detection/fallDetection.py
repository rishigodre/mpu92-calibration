import time
from mpu9250_i2c import *
time.sleep(0.5)
#
#############################
# Strings for Units/Labs
#############################
#
imu_devs   = ["ACCELEROMETER"]
imu_labels = ["x-dir","y-dir","z-dir"]
imu_units  = ["g","g","g"]

while True:
    ##################################
    # Reading and Printing IMU values
    ##################################
    #
    try:
        ax,ay,az,extra = mpu6050_conv() # read and convert mpu6050 data
    except:
        continue

    netG = (ax*ax + ay*ay + az*az)**0.5

    print(netG + " - net G")

    time.sleep(0.01)

