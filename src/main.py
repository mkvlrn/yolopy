"""heyo."""

import sys

from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

from heyo.stuff import my_balls


class MyApp(QWidget):
    """My App."""

    def __init__(self) -> None:
        """Init."""
        super().__init__()
        self.setWindowTitle("My PyQt6 App")
        self.setGeometry(100, 100, 300, 150)

        self.label = QLabel("Click the button", self)
        self.button = QPushButton("Greet", self)
        self.button.clicked.connect(self.say_hello)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def say_hello(self) -> None:
        """Say hello."""
        text: str = my_balls() + "" + "yellow"
        self.label.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
