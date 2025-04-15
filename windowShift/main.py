import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QColor, QPalette, QBrush, QMouseEvent

class WhiteScreenApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the screen dimensions to 1920x1080
        self.screen_width, self.screen_height = 1920, 1080
        self.setGeometry(0, 0, self.screen_width, self.screen_height)

        # Create the white screen label
        self.white_screen_label = QLabel(self)
        self.white_screen_label.setGeometry(QRect(0, 0, self.screen_width, self.screen_height))
        self.white_screen_label.setAutoFillBackground(True)
        palette = self.white_screen_label.palette()
        palette.setBrush(QPalette.Background, QBrush(QColor(255, 255, 255)))
        self.white_screen_label.setPalette(palette)

        # Create the "Move" button
        self.move_button = QPushButton("Move", self)
        self.move_button.setGeometry(QRect(10, 10, 100, 30))
        self.move_button.clicked.connect(self.move_to_second_monitor)

    def move_to_second_monitor(self):
        # Get information about available monitors
        available_monitors = QApplication.screens()

        if len(available_monitors) < 2:
            print("You need at least two monitors to move the screen.")
            return

        # Get the geometry of the second monitor
        second_monitor_geometry = available_monitors[1].geometry()

        # Move the window to the second monitor
        self.setGeometry(second_monitor_geometry)

        # Set the "Move" button's click event to move back to the first monitor
        self.move_button.clicked.disconnect(self.move_to_second_monitor)
        self.move_button.clicked.connect(self.move_to_first_monitor)

    def move_to_first_monitor(self):
        # Get information about available monitors
        available_monitors = QApplication.screens()

        # Get the geometry of the first monitor
        first_monitor_geometry = available_monitors[0].geometry()

        # Move the window back to the first monitor
        self.setGeometry(first_monitor_geometry)

        # Set the "Move" button's click event to move to the second monitor
        self.move_button.clicked.disconnect(self.move_to_first_monitor)
        self.move_button.clicked.connect(self.move_to_second_monitor)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WhiteScreenApp()
    window.show()
    sys.exit(app.exec_())
