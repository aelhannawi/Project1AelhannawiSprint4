import CreateButtons
import CreateData
import CreateDataBase
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QTableWidget,\
    QPushButton, QMessageBox, QVBoxLayout, QWidget

class ShowWindow(QTableWidget):
    def __init__(self):
        super(ShowWindow, self).__init__()
        self.setup_window()
        self.get_pop_tv_data()

    def setup_window(self):
        self.setWindowTitle("Most Popular TV Shows")
        self.setColumnWidth(0, 50)
        self.show()

    def get_pop_tv_data(self):
        conn = sqlite3.connect('output/imdb_db.sqlite')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM MOST_POPULAR_TV_SHOWS')
        raw_most_popular_tv_data = cur.fetchall()
        CreateDataBase.close_db(conn)
        self.tableWidget.setRowCount(len(raw_most_popular_tv_data))
        row = 0
        for data in raw_most_popular_tv_data:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(data['id']))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data['rank'])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data['rank_up_down'])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(data['title']))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(data['full_title']))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(data['year']))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(data['crew']))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(data['imdb_rating'])))
            self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(str(data['imdb_rating_count'])))
            row = row + 1


class MovieWindow(QTableWidget):
    def __init__(self):
        super(MovieWindow, self).__init__()
        ##loadUi("imdbDBTest.ui", self)
        self.setup_window()
        self.get_popular_movie_data()

    def setup_window(self):
        self.Title("Show Most Popular Movies")
        self.Width(0, 50)
        self.show()

    def get_popular_movie_data(self):
        conn = sqlite3.connect('output/project1db.sqlite')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM MOST_POPULAR_MOVIES')
        raw_most_popular_movie_data = cur.fetchall()
        CreateDataBase.close_db(conn)
        self.tableWidget.setRowCount(len(raw_most_popular_movie_data))
        row = 0
        for data in raw_most_popular_movie_data:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(data['id']))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data['rank'])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data['rank_up_down'])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(data['title']))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(data['full_title']))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(data['year']))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(data['crew']))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(data['imdb_rating'])))
            self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(str(data['imdb_rating_count'])))
            row = row + 1

    def rank_shows_window(self):
        self.w = CreateData.show_window()
        self.w.show()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("Home Page")
        update_button = QPushButton("Update Now", self)
        update_button.clicked.connect(self.update_data)
        pop_tv_button = QPushButton("Most Popular TV Shows List", self)
        pop_tv_button.clicked.connect(self.shows_window)
        pop_movie_button = QPushButton("Most Popular Movies List", self)
        pop_movie_button.clicked.connect(self.movies_window)
        layout = QHBoxLayout()
        layout.stretch(1)
        layout.addWidget(update_button)
        layout.addWidget(pop_tv_button)
        layout.addWidget(pop_movie_button)
        v_layout = QVBoxLayout()
        v_layout.stretch(1)
        v_layout.addLayout(layout)
        self.setLayout(v_layout)
        self.setGeometry(300, 300, 300, 150)
        self.show()

    def update_data(self):
        CreateDataBase.main()
        message_box = QMessageBox(self)
        message_box.setText("imDB data updated.")
        message_box.show()

    def shows_window(self):
        self.w = ShowWindow()
        self.sort = CreateButtons.createTVButtons()
        self.w.show()
        self.sort.show()

    def movies_window(self):
        self.w = MovieWindow()
        self.sort = CreateButtons.CreateMovieButtons()
        self.w.show()
