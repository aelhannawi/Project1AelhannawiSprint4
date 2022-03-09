from PyQt5.QtWidgets import QApplication
import GUI
import sys


def display_data():
    app = QApplication(sys.argv)
    my_window = GUI.MainWindow()
    print(my_window)
    sys.exit(app.exec())


def main():
    display_data()


if __name__ == '__main__':
    main()
