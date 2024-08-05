from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
import sys


class SimpleApp(QWidget):
    """A simple PyQt5 GUI application."""

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a label and button
        label = QLabel('Hello, PyQt5!', self)
        button = QPushButton('Click Me', self)
        button.clicked.connect(self.on_click)

        # Create a vertical layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)

        # Set the layout for the main window
        self.setLayout(layout)
        self.setWindowTitle('Simple PyQt5 App')
        self.show()

    def on_click(self):
        """Handle button click event."""
        print("Button clicked!")


def main():
    app = QApplication(sys.argv)
    window = SimpleApp()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
