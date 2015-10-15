import datetime
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class ClientReq(QtWidgets.QWidget):
    def __init__(self, client_ids):
        super().__init__()

        self.client_ids = client_ids

        self.initUI()

    def initUI(self):
        # self.setGeometry(500, 200, 850, 420)

        # --- TOP LEFT CORNER ---
        client_rec_no_label = QtWidgets.QLabel('Client record number :')
        self.client_name_edit = QtWidgets.QLabel()

        self.client_rec_no_edit = QtWidgets.QComboBox()
        self.client_rec_no_edit.setEditable(False)
        self.client_rec_no_edit.currentTextChanged.connect(self._client_changed)
        self.client_rec_no_edit.addItems(self.client_ids.keys())
        # comboBox.setSizePolicy(QtGui.QSizePolicy.Expanding,
        #         QtGui.QSizePolicy.Preferred)
        client_name_label = QtWidgets.QLabel('Client name :')
        event_type_label = QtWidgets.QLabel('Event type :')
        self.event_type_edit = QtWidgets.QLineEdit()
        description_label = QtWidgets.QLabel('Description :')
        self.description_edit = QtWidgets.QTextEdit()

        to_layout = QtWidgets.QHBoxLayout()
        from_layout = QtWidgets.QHBoxLayout()
        from_label = QtWidgets.QLabel('From :')
        to_label = QtWidgets.QLabel('To :')
        self.from_date = QtWidgets.QDateEdit(datetime.date.today())
        self.to_date = QtWidgets.QDateEdit(datetime.date.today())
        to_layout.addWidget(from_label)
        to_layout.addWidget(self.from_date)
        from_layout.addWidget(to_label)
        from_layout.addWidget(self.to_date)

        top_left_layout = QtWidgets.QGridLayout()
        top_left_layout.addWidget(client_rec_no_label, 0, 0)
        top_left_layout.addWidget(self.client_rec_no_edit, 0, 1)
        top_left_layout.addWidget(client_name_label, 1, 0)
        top_left_layout.addWidget(self.client_name_edit, 1, 1)
        top_left_layout.addWidget(event_type_label, 2, 0)
        top_left_layout.addWidget(self.event_type_edit, 2, 1)
        top_left_layout.addWidget(description_label, 3, 0)
        top_left_layout.addWidget(self.description_edit, 3, 1)
        top_left_layout.addLayout(from_layout, 4, 0)
        top_left_layout.addLayout(to_layout, 4, 1)

        # --- TOP RIGHT CORNER ---
        exp_no_label = QtWidgets.QLabel('Expected number :')
        self.exp_no_edit = QtWidgets.QLineEdit()
        planned_budget_label = QtWidgets.QLabel('Planned budget :')
        self.planned_budget_edit = QtWidgets.QLineEdit()

        top_right_layout = QtWidgets.QGridLayout()
        top_right_layout.addWidget(exp_no_label, 0, 0)
        top_right_layout.addWidget(self.exp_no_edit, 0, 1)
        top_right_layout.addWidget(planned_budget_label, 1, 0)
        top_right_layout.addWidget(self.planned_budget_edit, 1, 1)

        # --- CENTER ---
        decorations_group = QtWidgets.QGroupBox("Decorations")
        decorations_layout = QtWidgets.QHBoxLayout()
        self.decorations_edit = QtWidgets.QTextEdit()
        decorations_layout.addWidget(self.decorations_edit)
        decorations_group.setLayout(decorations_layout)

        filming_group = QtWidgets.QGroupBox("Filming/Photos")
        filming_layout = QtWidgets.QHBoxLayout()
        self.filming_edit = QtWidgets.QTextEdit()
        filming_layout.addWidget(self.filming_edit)
        filming_group.setLayout(filming_layout)

        poster_group = QtWidgets.QGroupBox("Posters/Art Work")
        poster_layout = QtWidgets.QHBoxLayout()
        self.poster_edit = QtWidgets.QTextEdit()
        poster_layout.addWidget(self.poster_edit)
        poster_group.setLayout(poster_layout)

        food_group = QtWidgets.QGroupBox("Food/Drinks")
        food_layout = QtWidgets.QHBoxLayout()
        self.food_edit = QtWidgets.QTextEdit()
        food_layout.addWidget(self.food_edit)
        food_group.setLayout(food_layout)

        music_group = QtWidgets.QGroupBox("Music")
        music_layout = QtWidgets.QHBoxLayout()
        self.music_edit = QtWidgets.QTextEdit()
        music_layout.addWidget(self.music_edit)
        music_group.setLayout(music_layout)

        computer_group = QtWidgets.QGroupBox("Computer-Related Issues")
        computer_layout = QtWidgets.QHBoxLayout()
        self.computer_edit = QtWidgets.QTextEdit()
        computer_layout.addWidget(self.computer_edit)
        computer_group.setLayout(computer_layout)

        center_layout = QtWidgets.QGridLayout()
        center_layout.addLayout(top_left_layout, 0, 0)
        center_layout.addLayout(top_right_layout, 0, 1)
        center_layout.addWidget(decorations_group, 1, 0)
        center_layout.addWidget(food_group, 1, 1)
        center_layout.addWidget(filming_group, 2, 0)
        center_layout.addWidget(music_group, 2, 1)
        center_layout.addWidget(poster_group, 3, 0)
        center_layout.addWidget(computer_group, 3, 1)

        # --- BOTTOM ---
        other_label = QtWidgets.QLabel("Other needs :")
        self.other_edit = QtWidgets.QTextEdit()

        bottom_layout = QtWidgets.QHBoxLayout()
        bottom_layout.addWidget(other_label)
        bottom_layout.addWidget(self.other_edit)

        # --- MAIN ----
        title_label = QtWidgets.QLabel("Client Request Details")
        submit_button = QtWidgets.QPushButton("Submit")
        submit_button.clicked.connect(self.onSubmit)
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(title_label)
        main_layout.addLayout(center_layout)
        main_layout.addLayout(bottom_layout)
        main_layout.addWidget(submit_button)
        main_layout.setAlignment(title_label, Qt.AlignHCenter)

        self.setLayout(main_layout)
        self.show()

    def _client_changed(self, text):
        self.client_name_edit.setText(self.client_ids[text])

    def onSubmit(self):
        from view.mediator import get_mediator
        m = get_mediator()
        m.create_client_req(self.client_rec_no_edit.currentText() ,self.event_type_edit.text(), self.description_edit.toPlainText(), self.from_date.text(),
                            self.to_date.text(), self.exp_no_edit.text(),
                            self.planned_budget_edit.text(), self.decorations_edit.toPlainText(),
                            self.filming_edit.toPlainText(), self.poster_edit.toPlainText(),
                            self.food_edit.toPlainText(), self.music_edit.toPlainText(),
                            self.computer_edit.toPlainText(), self.other_edit.toPlainText())