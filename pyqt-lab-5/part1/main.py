# keypad_main.py

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from passkey import Ui_Form

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initializeUI()
        self.show()

    def checkPasscode(self):
        entered_passcode = (
            self.ui.lineEdit_1.text()
            + self.ui.lineEdit_2.text()
            + self.ui.lineEdit_3.text()
            + self.ui.lineEdit_4.text()
        )
        if len(entered_passcode) == 4 and int(entered_passcode) == self.passcode:
            QMessageBox.information(
                self, "Верный пароль!", "Верный пароль!", QMessageBox.StandardButton.Ok
            )
            self.close()
        else:
            QMessageBox.warning(
                self,
                "Сообщение об ошибке",
                "Неверный пароль.",
                QMessageBox.StandardButton.Close,
            )
            self.ui.lineEdit_1.clear()
            self.ui.lineEdit_2.clear()
            self.ui.lineEdit_3.clear()
            self.ui.lineEdit_4.clear()
            self.ui.lineEdit_1.setFocus()

    def initializeUI(self):
        self.ui.lineEdit_1.setMaxLength(1)
        self.ui.lineEdit_1.setValidator(QIntValidator(0, 9))
        self.ui.lineEdit_1.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ui.lineEdit_2.setMaxLength(1)
        self.ui.lineEdit_2.setValidator(QIntValidator(0, 9))
        self.ui.lineEdit_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ui.lineEdit_3.setMaxLength(1)
        self.ui.lineEdit_3.setValidator(QIntValidator(0, 9))
        self.ui.lineEdit_3.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ui.lineEdit_4.setMaxLength(1)
        self.ui.lineEdit_4.setValidator(QIntValidator(0, 9))
        self.ui.lineEdit_4.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.passcode = 8618

        self.ui.pushButton_0.clicked.connect(lambda: self.numberClicked(self.ui.pushButton_0.text()))
        self.ui.pushButton_1.clicked.connect(lambda: self.numberClicked(self.ui.pushButton_1.text()))
        self.ui.pushButton_2.clicked.connect(lambda: self.numberClicked(self.ui.pushButton_2.text()))
        self.ui.pushButton_3.clicked.connect(lambda: self.numberClicked(self.ui.pushButton_3.text()))
        self.ui.pushButton_4.clicked.connect(lambda: self.numberClicked(self.ui.pushButton_4.text()))
        self.ui.pushButton_5.clicked.connect(lambda: self.numberClicked(self.ui.pushButton_5.text()))
        self.ui.pushButton_6.clicked.connect(lambda: self.numberClicked(self.ui.pushButton_6.text()))
        self.ui.pushButton_7.clicked.connect(lambda: self.numberClicked(self.ui.pushButton_7.text()))
        self.ui.pushButton_8.clicked.connect(lambda: self.numberClicked(self.ui.pushButton_8.text()))
        self.ui.pushButton_9.clicked.connect(lambda: self.numberClicked(self.ui.pushButton_9.text()))
        self.ui.pushButton_sharp.clicked.connect(self.checkPasscode)

    def numberClicked(self, text_value):
        if self.ui.lineEdit_1.text() == "":
            self.ui.lineEdit_1.setFocus()
            self.ui.lineEdit_1.setText(text_value)
            self.ui.lineEdit_1.repaint()
        elif self.ui.lineEdit_1.text() != "" and self.ui.lineEdit_2.text() == "":
            self.ui.lineEdit_2.setFocus()
            self.ui.lineEdit_2.setText(text_value)
            self.ui.lineEdit_2.repaint()
        elif (
            self.ui.lineEdit_1.text() != ""
            and self.ui.lineEdit_2.text() != ""
            and self.ui.lineEdit_3.text() == ""
        ):
            self.ui.lineEdit_3.setFocus()
            self.ui.lineEdit_3.setText(text_value)
            self.ui.lineEdit_3.repaint()
        elif (
            self.ui.lineEdit_1.text() != ""
            and self.ui.lineEdit_2.text() != ""
            and self.ui.lineEdit_3.text() != ""
            and self.ui.lineEdit_4.text() == ""
        ):
            self.ui.lineEdit_4.setFocus()
            self.ui.lineEdit_4.setText(text_value)
            self.ui.lineEdit_4.repaint()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Keypad = MainWindow()
    sys.exit(app.exec())
