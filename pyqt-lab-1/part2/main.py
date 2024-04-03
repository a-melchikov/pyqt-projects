import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap
class MainWindow(QWidget):
     def __init__(self):
         super().__init__()
         self.initializeUI()
     def initializeUI(self):
         """Настройте графический интерфейс приложения."""
         self.setGeometry(100, 100, 350, 380)
         self.setWindowTitle("Пример QLabel")
         self.setUpMainWindow()
         self.show()
     def setUpMainWindow(self):
         """Создайте QLabel для отображения в главном окне."""
         hello_label = QLabel(self)
         hello_label.setText("Привет!")
         hello_label.move(155, 15)
         image = "images/Земля.jpg"
         try:
             with open(image):
                 world_label = QLabel(self)
                 pixmap = QPixmap(image)
                 pixmap = pixmap.scaled(300, 300)
                 world_label.setPixmap(pixmap)
                 world_label.move(25, 40)
         except FileNotFoundError as error:
             print(f"Image not found.\nError: {error}")


if __name__ == '__main__':
     app = QApplication(sys.argv)
     window = MainWindow()
     sys.exit(app.exec())