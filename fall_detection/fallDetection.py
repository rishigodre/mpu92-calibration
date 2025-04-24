import time
t0 = time.time()
start_bool = False # boolean for connection
while (time.time()-t0)<5: # wait for 5-sec to connect to IMU
    try:
        from mpu9250_i2c import *
        start_bool = True # True for forthcoming loop
        break
    except:
        continue
#############################
# Main Loop to Test IMU
#############################
#
oldG = 1
while True:
    if start_bool==False: # make sure the IMU was started
        print("IMU not Started, Check Wiring") # check wiring if error
        break
    try:
        ax,ay,az,wx,wy,wz = mpu6050_conv() # read and convert mpu6050 data
    except:
        continue
    netG = ax * ax + ay * ay + az * az
    netG = netG ** 0.5
    jerkMag = (netG - oldG) / (0.001)

    if jerkMag > 1500:
        print("fall!!")

    time.sleep(0.001) # wait between prints

