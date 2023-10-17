import pyautogui
import time
import keyboard

# Specify the pixel coordinates (replace with your own)
x, y = 963, 457

while True:
    # If the 'q' key is pressed, break out of the loop
    if keyboard.is_pressed('q'):
        print('You pressed q, the script is stopping...')
        break

    # Get the color of the pixel at the specified location
    pixel_color = pyautogui.screenshot().getpixel((x, y))

    # If the pixel is green
    if pixel_color == (75, 219, 106):
        # Move the mouse to the location of the pixel and click
        pyautogui.moveTo(x, y)
        pyautogui.click()