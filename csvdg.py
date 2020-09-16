import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QGridLayout, QHBoxLayout,
QLabel, QLineEdit, QPushButton,
QFileDialog, QListWidget, QListWidgetItem)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, pyqtSlot
from add_field import AddField

class dgGUI(QMainWindow):
    ''' 
    Data Generator GUI class definition 
    '''
    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        self.window_width = 600
        self.window_height = 500

        self.window_title = 'Data Generator'

        self.file_name = ''

        self.init_UI()

    def init_UI(self):
        '''
        Initialize the window and display its contents to the screen
        '''
        self.setMinimumSize(self.window_width,self.window_height)
        self.setWindowTitle(self.window_title)

        self.setup_widgets()

        self.show()

    def setup_widgets(self):
        '''
        Set up the widgets and layouts for interface
        '''
        file_location_label = QLabel('File:')
        self.file_location_edit = QLineEdit()
        self.file_location_edit.textChanged.connect(self.set_filename)
        
        file_location_btn = QPushButton('...')
        file_location_btn.setToolTip('Select the file location.')
        file_location_btn.clicked.connect(self.set_save_file_name)

        add_field_btn = QPushButton('Add Field...')
        add_field_btn.clicked.connect(self.show_add_field_dialog)
        add_field_btn.setToolTip('Add a new field to the list.')
        add_field_btn.setIcon(QIcon('resources/add_col.png'))
        add_field_btn.setIconSize(QSize(30,30))

        del_field_btn = QPushButton('Remove Field')
        del_field_btn.setToolTip('Remove the selected field.')
        del_field_btn.setIcon(QIcon('resources/remove_col.png'))
        del_field_btn.setIconSize(QSize(30,30))
        self.field_list = QListWidget()

        grid_layout = QGridLayout()
        btn_layout = QHBoxLayout()

        btn_layout.addWidget(add_field_btn)
        btn_layout.addWidget(del_field_btn)

        grid_layout.addWidget(file_location_label,0,0)
        grid_layout.addWidget(self.file_location_edit,0,1)
        grid_layout.addWidget(file_location_btn,0,2)
        grid_layout.addLayout(btn_layout,1,0,1,3)
        grid_layout.addWidget(self.field_list,2,0,1,3)
        
        main_widget = QWidget()
        main_widget.setLayout(grid_layout)
        self.setCentralWidget(main_widget)
    
    def set_filename(self):
        '''
        Set global file_name value
        '''
        self.file_name = self.file_location_edit.text()

    def set_save_file_name(self):
        '''
        Set the filename based on the value selected from the dialog window
        '''
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.AnyFile)
        self.file_name, _= file_dialog.getSaveFileName(self, 'Filename location','','CSV Files (*.csv);;All Files(*.*)')

        if self.file_name:
            self.file_location_edit.setText(self.file_name)
    
    @pyqtSlot()
    def show_add_field_dialog(self):
        '''
        Display Add new field dialog
        '''
        add_field_dlg = AddField(self)
        if add_field_dlg.exec_():
            print('Added')
        else:
            print('Not added')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = dgGUI()
    sys.exit(app.exec_())

