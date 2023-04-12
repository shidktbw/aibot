# NeuralCraftAim

**NeuralCraftAim** is a neural network that knows how to play PvP (1.8.9) in Minecraft.


![YEEE(1)](https://user-images.githubusercontent.com/112849918/231447464-296e6b45-82d8-429e-8d84-913d5d7e0713.gif)
This neural network detects objects using YOLOv8 and uses pyautogui to aim at players and start clicking LMB

If you want to improve the neural network, you need to improve the model's dataset. Currently, my model (layers.pt) is built on just 80 images (which is very little)


# Usage:
*  Your window will probably have a different name than "Minecraft". Therefore, you should replace  [here](https://github.com/shidktbw/NeuralCraftAim/blob/main/main.py#L8) with the name of your Minecraft window.
*  To change the model, click [here](https://github.com/shidktbw/NeuralCraftAim/blob/main/main.py#L8).
* Also, if you want to switch to PvP on version 1.12.2, you should add a small delay before clicking [here](https://github.com/shidktbw/NeuralCraftAim/blob/main/main.py#L41).

# Credits:
 *   [ultralytics](https://github.com/ultralytics/ultralytics)
