import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox, QPushButton
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QMainWindow

from .automate import automate


class Dialog(QDialog):
    """Dialog."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Learn with Shin app")
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()
        self.directory = QLineEdit()
        self.output_name = QLineEdit()
        formLayout.addRow("Resources Directory:", self.directory)
        formLayout.addRow("Output File Name:", self.output_name)
        dlgLayout.addLayout(formLayout)

        btn = QPushButton("Execute my project")

        btn.clicked.connect(
            lambda: self.run(self.directory.text(), self.output_name.text())
        )

        dlgLayout.addWidget(btn)

        self.setLayout(dlgLayout)

    def run(self, directory: str, output_name: str = "result.csv"):
        print(directory, output_name)
        automate(directory, output_name)


def main():
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()