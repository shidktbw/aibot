from ultralytics import YOLO
import cv2
import numpy as np
import pyautogui
import pygetwindow as gw
from mouse import Mouse
import os

os.system('cls')
#ur window 
game_win = gw.getWindowsWithTitle("Minecraft")[0] 

# model
model = YOLO('best.pt')



def capture():
    #main capture
    screen = np.array(pyautogui.screenshot())
    
    #calc size
    win_left, win_top = game_win.topleft
    win_width, win_height = game_win.size

    capture_width, capture_height = 800, 600  # so, its capture zone (px)

    # $ize window for our capture
    start_x = win_left + (win_width - capture_width) // 2
    start_y = win_top + (win_height - capture_height) // 2
 
    #cut our window to our zone window
    cropped = screen[start_y:start_y+capture_height, start_x:start_x+capture_width]

    # rbg to bgr
    cropped = cv2.cvtColor(cropped, cv2.COLOR_RGB2BGR)

    #settings for model
    predictions = model.predict(cropped, conf=0.4, show=True, show_labels=True, show_conf=True, line_width=2, device='cpu') #conf = 0.3 cuz idc abt dataset    
 
    # get info abt size/name/etc
    boxes = predictions[0].boxes
    names = predictions[0].names

    #making sure we have even one object
    if boxes.xyxy.shape[0] != 0:
        xywh = boxes.xywh[0]  #get info about xywh
        xyxy = boxes.xyxy[0]  #get info about xyxy
        
        #get center of object
        x_center = (xyxy[0] + xyxy[2]) / 2
        y_center = (xyxy[1] + xyxy[3]) / 2
        
        # aim xD
        pyautogui.moveTo(int(x_center + win_left), int(y_center + win_top))
        pyautogui.click()

   # else:
    #    print("No objects detected")
    
    return cropped

# whileeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
while True:
    cropped = capture()



