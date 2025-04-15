import pygame
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"  # Position the window at the top-left corner of the screen

pygame.init()

# Set the width and height of each window
window_width = 1440
window_height = 1024

# Get the width and height of each monitor
monitor_info = pygame.display.Info()
monitor_width = monitor_info.current_w
monitor_height = monitor_info.current_h

# Calculate the total width for the window spanning two monitors
total_width = window_width * 2
height = window_height

# Create the Pygame window
window = pygame.display.set_mode((total_width, height), pygame.NOFRAME)

# Set the position of the window to span across two monitors
window_position = ((monitor_width - total_width) // 2, (monitor_height - height) // 2)
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{window_position[0]}, {window_position[1]}"

# Load the "Start.png" image
image_path = os.path.join("img", "Start.png")
start_image = pygame.image.load(image_path)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255, 255, 255))  # Fill the window with white color

    # Blit the "Start.png" image onto the left half of the window
    window.blit(start_image, (0, 0))

    # Blit the "Start.png" image onto the right half of the window
    window.blit(start_image, (window_width, 0))

    pygame.display.flip()  # Update the display

pygame.quit()
