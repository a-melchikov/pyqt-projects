import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtGui import QFont, QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(50, 50, 375, 675)
        self.setWindowTitle("Об авторе")
        self.setUpMainWindow()
        self.show()

    def createImageLabels(self):
        images = ["images/Фон.jpg",
                  "images/Фото.png"]
        for image in images:
            try:
                with open(image):
                    label = QLabel(self)
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap)
                    if image == "images/Фон.jpg":
                        label.setGeometry(0, 0, 375, 170)
                        label.setScaledContents(True)
                    if image == "images/Фото.png":
                        label.setGeometry(130, 10, 105, 150)
                        label.setScaledContents(True)
            except FileNotFoundError as error:
                print(f"Image not found.\nError: {error}")

    def buttonClicked(self):
        self.close()

    def showDetails(self):
        global about_label, details_button, detailed_description, short_description
        if about_label.text() == short_description:
            about_label.setText(detailed_description)
            details_button.setText("Скрыть")
        else:
            about_label.setText(short_description)
            details_button.setText("Подробнее")

    def setUpMainWindow(self):
        self.createImageLabels()

        user_label = QLabel(self)
        user_label.setText("Иван Петров")
        user_label.setFont(QFont("Arial", 16))
        user_label.move(120, 180)

        bio_label = QLabel(self)
        bio_label.setText("Биография")
        bio_label.setFont(QFont("Arial", 14))
        bio_label.move(15, 210)

        global about_label, detailed_description, short_description
        short_description = "Предприниматель \t\t\n\n"
        detailed_description = "Предприниматель "\
                               "Директор ООО АЛ-ТЕХ и ООО Дельфин "
        about_label = QLabel(self)
        about_label.setText(short_description)
        about_label.setWordWrap(True)
        about_label.move(15, 245)

        skills_label = QLabel(self)
        skills_label.setText("Умения")
        skills_label.setFont(QFont("Arial", 14))
        skills_label.move(15, 320)

        languages_label = QLabel(self)
        languages_label.setText("Python | C++ | SQL | 1C")
        languages_label.move(15, 345)

        experience_label = QLabel(self)
        experience_label.setText("Опыт")
        experience_label.setFont(QFont("Arial", 14))
        experience_label.move(15, 400)

        developer_label = QLabel(self)
        developer_label.setText("Директор ООО АЛ-ТЕХ")
        developer_label.move(15, 425)

        dev_dates_label = QLabel(self)
        dev_dates_label.setText("2010 - настоящее время")
        dev_dates_label.setFont(QFont("Arial", 10))
        dev_dates_label.move(15, 445)

        pizza_label = QLabel(self)
        pizza_label.setText("Директор ООО Дельфин")
        pizza_label.move(15, 475)

        pizza_dates_label = QLabel(self)
        pizza_dates_label.setText("2023 - настоящее время")
        pizza_dates_label.setFont(QFont("Arial", 10))
        pizza_dates_label.move(15, 495)

        global details_button
        details_button = QPushButton("Подробнее", self)
        details_button.move(50, 600)
        details_button.clicked.connect(self.showDetails)

        ok_button = QPushButton("ОК", self)
        ok_button.move(240, 600)
        ok_button.clicked.connect(self.buttonClicked)


# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
