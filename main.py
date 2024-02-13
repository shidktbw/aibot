from ultralytics import YOLO
import pygetwindow as gw
import pyautogui
import numpy as np
import cv2
import os


class GameWindow:
    def __init__(self, title):
        self.game_win = gw.getWindowsWithTitle(title)[0]

    def capture_screen(self, capture_width=800, capture_height=600):
        screen = np.array(pyautogui.screenshot())

        win_left, win_top = self.game_win.topleft
        win_width, win_height = self.game_win.size

        start_x = win_left + (win_width - capture_width) // 2
        start_y = win_top + (win_height - capture_height) // 2

        cropped = screen[start_y:start_y+capture_height, start_x:start_x+capture_width]
        cropped = cv2.cvtColor(cropped, cv2.COLOR_RGB2BGR)

        return cropped, win_left, win_top

class Detect:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect_objects(self, image):
        predictions = self.model.predict(image, conf=0.4, show=True, show_labels=True, show_conf=True, line_width=2, device='cpu')
        boxes = predictions[0].boxes
        names = predictions[0].names

        return boxes, names

def aim_and_click(boxes, win_left, win_top):
    if boxes.xyxy.shape[0] != 0:
        xyxy = boxes.xyxy[0]
        x_center = (xyxy[0] + xyxy[2]) / 2
        y_center = (xyxy[1] + xyxy[3]) / 2

        pyautogui.moveTo(int(x_center + win_left), int(y_center + win_top))
        pyautogui.click()
  #     pyautogui sucks 

def main():
    os.system('cls')
    game_window = GameWindow("Minecraft")
    model = Detect('players.pt')

    while True:
        cropped, win_left, win_top = game_window.capture_screen()
        boxes, names = model.detect_objects(cropped)
        aim_and_click(boxes, win_left, win_top)

if __name__ == "__main__":
    main()  
