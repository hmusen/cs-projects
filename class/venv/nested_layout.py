from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QLabel,
    QComboBox
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Awesome App')

        # Main layout
        layout = QVBoxLayout()

        # Nested layouts
        nested_layout = QHBoxLayout()
        form_layout = QHBoxLayout()

        # Buttons
        btn1 = QPushButton("Button 1")
        btn2 = QPushButton("Button 2")
        btn3 = QPushButton("Button 3")
        btn4 = QPushButton("Button 4")

        nested_layout.addWidget(btn1)
        nested_layout.addWidget(btn2)
        nested_layout.addWidget(btn3)
        nested_layout.addWidget(btn4)

        # Line edit
        line_label1 = QLabel("Line 1:")
        line_edit = QLineEdit("Question")

        line_label2 = QLabel("Line 2:")
        combo = QComboBox()
        combo.addItems(["One", "Two", "Three"])
        
        form_layout = QVBoxLayout()

        form_layout.addWidget(line_label1)
        form_layout.addWidget(line_edit)
        
        form_layout.addWidget(line_label2)
        form_layout.addWidget(combo)

        # Add layouts to main layout
        layout.addLayout(nested_layout)
        layout.addLayout(form_layout)

        # Central widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
