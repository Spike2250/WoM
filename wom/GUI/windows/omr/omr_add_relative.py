from PySide6 import QtWidgets

from wom.GUI.PY.omr import omr_AddRelative
from wom.app_logic.create_docs import (open_folder_with_files,
                                       creating_documents)
from wom.app_logic.db_func.db_omr import write_omr_table
from wom.app_logic.writing.postprocessing\
    .add_relative import update_after_add_relative


# Окно добавления родственников
class Ui_AddRelative(QtWidgets.QWidget,
                     omr_AddRelative.Ui_AddRelative):
    def __init__(self, windows, main_win, dictionary, from_add_patient=False):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.windows = windows
        self.main_win = main_win
        self.d = dictionary
        self.from_add_patient = from_add_patient

        self.set_connections()
        self.insert_data_from_dictionary()

    def set_connections(self):
        # коннекты для кнопок
        self.pushButtonPrintRelativePass\
            .clicked.connect(self.create_relative_pass)
        self.pushButtonNotSaveExit\
            .clicked.connect(self.exit)
        self.pushButtonSaveExit\
            .clicked.connect(self.exit_and_save)

    def insert_data_from_dictionary(self):
        self.labelPassportData.setText(self.d['patient_info'])
        # заполнение ячеек окна данными из словаря
        if 'родс_фио' in self.d:
            self.lineEditPtRelativeFullName\
                .setText(self.d['родс_фио'])
            self.lineEditPtRelativePhone\
                .setText(self.d['родс_телефон'])
            self.lineEditPtRelativePassportNumber\
                .setText(self.d['родс_паспорт'])
            self.lineEditPtRelativeKinship\
                .setText(self.d['родс_родство'])

            self.lineEditPtRelativeFullName_2\
                .setText(self.d['родс_фио_2'])
            self.lineEditPtRelativePhone_2\
                .setText(self.d['родс_телефон_2'])
            self.lineEditPtRelativePassportNumber_2\
                .setText(self.d['родс_паспорт_2'])
            self.lineEditPtRelativeKinship_2\
                .setText(self.d['родс_родство_2'])

            self.lineEditPtRelativeFullName_3\
                .setText(self.d['родс_фио_3'])
            self.lineEditPtRelativePhone_3\
                .setText(self.d['родс_телефон_3'])
            self.lineEditPtRelativePassportNumber_3\
                .setText(self.d['родс_паспорт_3'])
            self.lineEditPtRelativeKinship_3\
                .setText(self.d['родс_родство_3'])

            self.lineEditPtRelativeFullName_4\
                .setText(self.d['родс_фио_4'])
            self.lineEditPtRelativePhone_4\
                .setText(self.d['родс_телефон_4'])
            self.lineEditPtRelativePassportNumber_4\
                .setText(self.d['родс_паспорт_4'])
            self.lineEditPtRelativeKinship_4\
                .setText(self.d['родс_родство_4'])

    # функции для кнопок
    def create_relative_pass(self):
        '''
        '''
        self.write_to_dictionary()
        creating_documents(self.d, ['Пропуск_для_посещения'])
        open_folder_with_files(self.d)

    def write_to_dictionary(self):
        '''
        перезапись в словаре всех значений из виджетов на новые
        '''
        self.d['родс_фио'] = self\
            .lineEditPtRelativeFullName.text()
        self.d['родс_телефон'] = self\
            .lineEditPtRelativePhone.text()
        self.d['родс_паспорт'] = self\
            .lineEditPtRelativePassportNumber.text()
        self.d['родс_родство'] = self\
            .lineEditPtRelativeKinship.text()

        self.d['родс_фио_2'] = self\
            .lineEditPtRelativeFullName_2.text()
        self.d['родс_телефон_2'] = self\
            .lineEditPtRelativePhone_2.text()
        self.d['родс_паспорт_2'] = self\
            .lineEditPtRelativePassportNumber_2.text()
        self.d['родс_родство_2'] = self\
            .lineEditPtRelativeKinship_2.text()

        self.d['родс_фио_3'] = self\
            .lineEditPtRelativeFullName_3.text()
        self.d['родс_телефон_3'] = self\
            .lineEditPtRelativePhone_3.text()
        self.d['родс_паспорт_3'] = self\
            .lineEditPtRelativePassportNumber_3.text()
        self.d['родс_родство_3'] = self\
            .lineEditPtRelativeKinship_3.text()

        self.d['родс_фио_4'] = self\
            .lineEditPtRelativeFullName_4.text()
        self.d['родс_телефон_4'] = self\
            .lineEditPtRelativePhone_4.text()
        self.d['родс_паспорт_4'] = self\
            .lineEditPtRelativePassportNumber_4.text()
        self.d['родс_родство_4'] = self\
            .lineEditPtRelativeKinship_4.text()

        update_after_add_relative(self.d)

    def exit_and_save(self):
        self.write_to_dictionary()
        write_omr_table(self.d)
        self.exit()

    def exit(self, win_name='passport'):
        if self.from_add_patient:
            win_name = 'add_new_patient'
        win = self.windows['Frameless']()
        win.setWidget(
            self.windows['omr'][win_name](
                windows=self.windows,
                main_win=win,
                dictionary=self.d))
        win.show()
        self.main_win.close()
