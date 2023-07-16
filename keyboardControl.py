from djitellopy import tello
import keyPress as keypress
from time import sleep
import cv2

keypress.init()
tello = tello.Tello()
tello.connect()
tello.streamon()
print(tello.get_battery())

screen_width = 640
screen_height = 480

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 30
    if keypress.getKey("LEFT"):
        lr = -speed
    elif keypress.getKey("RIGHT"):
        lr = speed
    if keypress.getKey("UP"):
        fb = speed
    elif keypress.getKey("DOWN"):
        fb = -speed
    if keypress.getKey("w"):
        ud = speed
    elif keypress.getKey("s"):
        ud = -speed
    if keypress.getKey("a"):
        yv = -speed
    elif keypress.getKey("d"):
        yv = speed
    if keypress.getKey("q"):
        tello.land()
        sleep(3)
    if keypress.getKey("e"):
        tello.takeoff()
    return [lr, fb, ud, yv]



while True:
    frame = tello.get_frame_read().frame
    frame = cv2.resize(frame, (screen_width, screen_height))


    cv2.imshow("Tello Drone", frame)

    vals = getKeyboardInput()
    tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)


cv2.destroyAllWindows()
tello.streamoff()
tello.land()