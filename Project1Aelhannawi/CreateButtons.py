import CreateData
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QWidget


class createTVButtons(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("TV Sort Buttons")
        create_by_rank_button = QPushButton("Sorted by Rank", self)
        create_by_rank_button.clicked.connect(self.rank_shows_window)
        create_by_rank_up_down_button = QPushButton("Sorted by RankUpDown", self)
        create_by_rank_up_down_button.clicked.connect(self.rank_up_down_window)
        layout = QHBoxLayout()
        layout.stretch(1)
        layout.addWidget(create_by_rank_button)
        layout.addWidget(create_by_rank_up_down_button)
        v_layout = QVBoxLayout()
        v_layout.stretch(1)
        v_layout.addLayout(layout)
        self.Layout(v_layout)
        self.position(100, 100, 100, 150)
        self.show()

    def rank_shows_window(self):
        self.w = CreateData.show_window()
        self.w.show()

    def rank_up_down_window(self):
        self.w = CreateData.Up_Down_TV_Window()
        self.w.show()


class CreateMovieButtons(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("sort movies")
        create_by_rank_button = QPushButton("Sorted by Rank", self)
        create_by_rank_button.clicked.connect(self.rank_shows_window)
        create_by_rank_up_down_button = QPushButton("Sorted by RankUpDown", self)
        create_by_rank_up_down_button.clicked.connect(self.rank_up_down_window)
        layout = QHBoxLayout()
        layout.stretch(1)
        layout.addWidget(create_by_rank_button)
        layout.addWidget(create_by_rank_up_down_button)
        v_layout = QVBoxLayout()
        v_layout.stretch(1)
        v_layout.addLayout(layout)
        self.Layout(v_layout)
        self.position(100, 100, 100, 150)
        self.show()

    def rank_shows_window(self):
        self.w = CreateData.Movie_Window()
        self.w.show()

    def rank_up_down_window(self):
        self.w = CreateData.Up_Down_Movie_Window()
        self.w.show()
