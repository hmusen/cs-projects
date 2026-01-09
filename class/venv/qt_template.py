from PyQt6 import QtCore 
from PyQt6 import QtWidgets as qtw

# import PyQt6.QtCore as qtc
# import PyQt6.QtGui as qtg

# Subclass QMainWindow to customise your application's main window
class MainWindow(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Awesome App')

        layout = qtw.QVBoxLayout()

        self.label = qtw.QLabel("Widget Demo")
        layout.addWidget(self.label)

        self.label2 = qtw.QComboBox()
        self.label2.addItems(['One','Two'])
        layout.addWidget(self.label2)

        self.check = qtw.QCheckBox(text="Choose this")
        layout.addWidget(self.check)

        self.check2 = qtw.QCheckBox(text="and this?")
        layout.addWidget(self.check2)

        self.line_edit = qtw.QLineEdit("Type here", self)
        layout.addWidget(self.line_edit)

        self.radio = qtw.QRadioButton(text="This one?")
        self.radio2 = qtw.QRadioButton(text="Or this one?")
        layout.addWidget(self.radio)
        layout.addWidget(self.radio2)


        self.slider = qtw.QSlider()
        self.slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        layout.addWidget(self.slider)

        self.button = qtw.QPushButton(text='Ok')
        layout.addWidget(self.button)

        self.button = qtw.QPushButton(text='Cancel')
        layout.addWidget(self.button)


        
        
        widget = qtw.QWidget()
        widget.setLayout(layout)
        
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = qtw.QApplication([])

window = MainWindow()
window.show()

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event 
# loop has stopped.