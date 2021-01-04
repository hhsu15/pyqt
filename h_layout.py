import sys

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("My Box Layout")

layout = QHBoxLayout()
layout.addWidget(QPushButton("left"))
layout.addWidget(QPushButton("center"))
layout.addWidget(QPushButton("right"))

window.setLayout(layout)

window.show()

sys.exit(app.exec_())
