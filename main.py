from ultralytics import YOLO
import cv2
import numpy as np
import pyautogui
import pygetwindow as gw

#ur window
game_win = gw.getWindowsWithTitle("Minecraft")[0] 

# model
model = YOLO(r"Players.pt")

# Capture and process the screenshot
def capture_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)

    win_left, win_top = game_win.topleft
    win_width, win_height = game_win.size

    cropped = screenshot[win_top:win_top+win_height, win_left:win_left+win_width]
    cropped = cv2.cvtColor(cropped, cv2.COLOR_RGB2BGR)
    predictions = model.predict(cropped, conf=0.2, show=True, show_labels=True, show_conf=True, save=False, save_txt=False, save_crop=False, line_thickness=2) #conf = 0.2 because i didn't bother with the dataset
    print(predictions[0].boxes.numpy)
    
    # Get the boxes object
    boxes = predictions[0].boxes

    # Check if it is not empty
    if boxes.boxes.shape[0] != 0:
        # Get xywh coordinates and convert to xyxy
        xywh = boxes.xywh[0]  
        xyxy = boxes.xyxy[0]
        
        # Find the center player
        x_center = (xyxy[0] + xyxy[2]) / 2
        y_center = (xyxy[1] + xyxy[3]) / 2
        
        # aim xD
        pyautogui.moveTo(int(x_center + win_left), int(y_center + win_top))
        pyautogui.click()

    else:
        print("No objects detected")
    
    return cropped

# whileeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
while True:
    cropped = capture_screenshot()


cv2.destroyAllWindows()
