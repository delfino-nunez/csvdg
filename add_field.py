from PyQt5.QtWidgets import (QDialog, QDialogButtonBox, QGridLayout, QLabel, QLineEdit, 
QComboBox)
from PyQt5.QtCore import pyqtSlot

class AddField(QDialog):
    '''
    Display Custom Add Field Dialog
    '''

    def __init__(self, *args, **kwargs):
        '''
        Initialize dialog
        '''

        super(AddField, self).__init__(*args, **kwargs)

        self.setWindowTitle('Add new CSV field')

        self.init_gui()
    
    def init_gui(self):
        '''
        Setup the GUI
        '''

        field_name_lbl = QLabel('Name:')
        field_name_txt = QLineEdit()
        field_name_txt.setPlaceholderText('Enter field name')

        field_type_lbl = QLabel('Type')
        self.field_type_list = QComboBox(self)
        combo_box_items = ['-- Select Type --', 
                           'String', 
                           'Number', 
                           'Date', 
                           'Boolean'
                           ]
        self.field_type_list.addItems(combo_box_items)
        self.field_type_list.currentIndexChanged.connect(self.selectFieldType)

        QButton = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QButton)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QGridLayout()

        self.layout.addWidget(field_name_lbl,0,0)
        self.layout.addWidget(field_name_txt,0,1)
        self.layout.addWidget(field_type_lbl,1,0)
        self.layout.addWidget(self.field_type_list,1,1)
        self.layout.addWidget(self.buttonBox,2,1)

        self.setLayout(self.layout)

    def selectFieldType(self):
        '''
        Based on field type add new fields
        '''
        print(self.field_type_list.currentText())
