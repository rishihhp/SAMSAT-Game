import pyautogui
import screeninfo
import time

# Get the details of screen 2
screen_list = screeninfo.get_monitors()
if len(screen_list) > 1:
    screen2 = screen_list[1]  # Assuming screen 2 is the second monitor in the list
else:
    print("Screen 2 not found.")
    exit()

# Set the boundaries for screen 2
min_x, min_y, max_x, max_y = screen2.x - 1, screen2.y - 1, screen2.x + screen2.width, screen2.y + screen2.height

while True:
    # Get the current mouse position
    x, y = pyautogui.position()

    # Check if the mouse is outside the boundaries of screen 2
    if x < min_x or x > max_x or y < min_y or y > max_y:
        # Move the mouse back to the center of screen 2
        pyautogui.moveTo((min_x + max_x) // 2, (min_y + max_y) // 2)

    # Pause briefly to reduce CPU usage
    time.sleep(0.1)
