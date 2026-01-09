import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QFormLayout,
    QGridLayout,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QComboBox,
    QCheckBox,
    QPushButton
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout Demo")

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        
        form_layout = QFormLayout()

        name_edit = QLineEdit()
        location_edit = QLineEdit()

        form_layout.addRow("Name:", name_edit)
        form_layout.addRow("Location:", location_edit)

        grid_layout = QGridLayout()

        combo = QComboBox()
        combo.addItems(["One", "Two", "Three"])

        checkbox = QCheckBox("On or off")


        ok_button = QPushButton("Ok")


        
        cancel_button = QPushButton("Cancel")

    
        grid_layout.addWidget(combo, 0, 0)

        grid_layout.addWidget(checkbox, 0, 1)

        
        grid_layout.addWidget(ok_button, 1, 0)
        grid_layout.addWidget(cancel_button, 1, 1)




        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(grid_layout)

        central_widget.setLayout(main_layout)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
