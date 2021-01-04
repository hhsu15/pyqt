import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

from automate import automate


def greeting():
    """Slot function."""
    if msg.text():
        msg.setText("")
    else:
        msg.setText("Welcome to Learn With Shin!!!")


def run():
    automate()


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Learn with shin app")
layout = QVBoxLayout()

btn = QPushButton("Greet")
btn.clicked.connect(greeting)  # Connect clicked to greeting()

btn2 = QPushButton("Execute my project")
btn2.clicked.connect(run)

layout.addWidget(btn)
layout.addWidget(btn2)
msg = QLabel("")
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())