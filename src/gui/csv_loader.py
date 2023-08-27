from PySide6.QtWidgets import QFileDialog, QPushButton, QVBoxLayout, QWidget


class CSVLoaderWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setup_open_file()

        layout = QVBoxLayout()
        layout.addWidget(self.load_csv_button)
        self.setLayout(layout)

    def setup_open_file(self):
        self.load_csv_button = QPushButton("Carregar CSV")
        self.load_csv_button.clicked.connect(self.get_filename)

    def get_filename(self):
        filters = "Comma Separated Values (*.csv);;"
        filename, selected_filter = QFileDialog.getOpenFileName(self, filter=filters)
        print(f"Filename: {filename}\n Filter: {selected_filter}")
