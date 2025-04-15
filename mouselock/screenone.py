import pyautogui
import screeninfo
import time

# Get the primary monitor
primary_monitor = screeninfo.get_monitors()[0]

# Set the boundaries for the primary monitor
min_x, min_y, max_x, max_y = primary_monitor.x - 1, primary_monitor.y - 1, primary_monitor.x + primary_monitor.width, primary_monitor.y + primary_monitor.height

while True:
    # Get the current mouse position
    x, y = pyautogui.position()

    # Check if the mouse is outside the boundaries of the primary monitor
    if x < min_x or x > max_x or y < min_y or y > max_y:
        # Move the mouse back to the primary monitor's center
        pyautogui.moveTo((min_x + max_x) // 2, (min_y + max_y) // 2)

    # Pause briefly to reduce CPU usage
    time.sleep(0.1)
