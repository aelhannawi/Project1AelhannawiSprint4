import CreateDataBase
import sqlite3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget


class show_window(QTableWidget):
    def __init__(self):
        super(show_window, self).__init__()
        self.TV_Movies_window()
        self.get_TV_data()

    def TV_Movies_window(self):
        self.setWindowTitle("Most popular TV shows sorted by rank")
        self.setGeometry(200, 50, 300, 400)
        self.setColumnWidth(0, 50)
        self.tv()

    def popular_tv_data(self):
        conn = sqlite3.connect('output/project1db.sqlite')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM MOST_POPULAR_TV_SHOWS ORDER BY rank')
        most_popular_TV_show_data = cur.fetchall()
        CreateDataBase.close_db(conn)
        self.tableWidget.setRowCount(len(most_popular_TV_show_data))
        row = 0
        for data in most_popular_TV_show_data:
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


class Up_Down_TV_Window(QTableWidget):
    def __init__(self):
        super(Up_Down_TV_Window, self).__init__()
        self.TV_Movies_window()
        self.up_down_pop_tv_data()

    def up_down_pop_tv_data(self):
        self.setWindowTitle("Most Popular TV Shows sorted by rank")
        self.setGeometry(200, 50, 300, 400)
        self.ColumnWidth(0, 50)
        self.show()

    def get_rank_up_down_pop_tv_data(self):
        conn = sqlite3.connect('output/project1db.sqlite')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM MOST_POPULAR_TV_SHOWS ORDER BY rank_up_down')
        most_popular_tv_data = cur.fetchall()
        CreateDataBase.close_db(conn)
        self.tableWidget.setRowCount(len(most_popular_tv_data))
        row = 0
        for data in most_popular_tv_data:
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


class Movie_Window(QTableWidget):
    def __init__(self):
        super(Movie_Window, self).__init__()
        self.setup_window()
        self.popular_movie_data()

    def movies_window(self):
        self.setWindowTitle("Most Popular Movies sorted by rank")
        self.setGeometry(200, 50, 300, 400)
        self.setColumnWidth(0, 50)
        self.show()

    def popular_movie_data(self):
        conn = sqlite3.connect('output/project1db.sqlite')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM MOST_POPULAR_MOVIES ORDER BY rank')
        most_popular_movie_data = cur.fetchall()
        CreateDataBase.close_db(conn)
        self.tableWidget.setRowCount(len(most_popular_movie_data))
        row = 0
        for data in most_popular_movie_data:
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


class Up_Down_Movie_Window(QTableWidget):
    def __init__(self):
        super(Up_Down_Movie_Window, self).__init__()
        self.setup_window()
        self.get_rank_up_down_pop_movie_data()

    def setup_window(self):
        self.setWindowTitle("Most Popular TV Shows sorted by rank")
        self.setGeometry(200, 50, 300, 400)
        self.setColumnWidth(0, 50)
        self.show()

    def get_rank_up_down_pop_movie_data(self):
        conn = sqlite3.connect('output/project1db.sqlite')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM MOST_POPULAR_MOVIES ORDER BY rank_up_down')
        most_popular_movie_data = cur.fetchall()
        CreateDataBase.close_db(conn)
        self.tableWidget.setRowCount(len(most_popular_movie_data))
        row = 0
        for data in most_popular_movie_data:
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
