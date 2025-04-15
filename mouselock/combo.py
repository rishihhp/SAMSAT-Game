from pynput.mouse import Controller
import screeninfo
import time

# Get the list of available monitors
screen_list = screeninfo.get_monitors()

# Create mouse controllers for each mouse device
mouse1 = Controller()
mouse2 = Controller()

# Assuming you have at least two screens and two mice
if len(screen_list) >= 2:
    screen1 = screen_list[0]
    screen2 = screen_list[1]
else:
    print("At least two screens are required.")
    exit()

# Set the boundaries for each screen
screen1_bounds = (screen1.x - 1, screen1.y - 1, screen1.x + screen1.width, screen1.y + screen1.height)
screen2_bounds = (screen2.x - 1, screen2.y - 1, screen2.x + screen2.width, screen2.y + screen2.height)

while True:
    # Get the current positions of both mice
    x1, y1 = mouse1.position
    x2, y2 = mouse2.position

    # Check if mouse 1 is outside the boundaries of screen 1
    if x1 < screen1_bounds[0] or x1 > screen1_bounds[2] or y1 < screen1_bounds[1] or y1 > screen1_bounds[3]:
        # Move mouse 1 back to screen 1
        mouse1.position = ((screen1_bounds[0] + screen1_bounds[2]) // 2, (screen1_bounds[1] + screen1_bounds[3]) // 2)

    # Check if mouse 2 is outside the boundaries of screen 2
    if x2 < screen2_bounds[0] or x2 > screen2_bounds[2] or y2 < screen2_bounds[1] or y2 > screen2_bounds[3]:
        # Move mouse 2 back to screen 2
        mouse2.position = ((screen2_bounds[0] + screen2_bounds[2]) // 2, (screen2_bounds[1] + screen2_bounds[3]) // 2)

    # Pause briefly to reduce CPU usage
    time.sleep(0.1)
