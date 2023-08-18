from PySide6 import QtWidgets, QtCore

from wom.GUI.PY.omr import omr_PatientPassportData
from wom.app_logic.create_docs import (creating_documents,
                                       open_folder_with_files)
from wom.app_logic.db_func.db_omr import (write_omr_table)
from wom.app_logic.writing.postprocessing\
    .passport import update_after_passport_data


# Окно паспортных данных пациента
class Ui_PatientPassportData(QtWidgets.QWidget,
                             omr_PatientPassportData.Ui_PatientPassportData):
    def __init__(self, windows, main_win, dictionary):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.windows = windows
        self.main_win = main_win
        self.d = dictionary

        msg = "World of Medicine - Отделение медицинской "\
              "реабилитации - Паспортные данные пациента"
        main_win.setWindowTitle(msg)
        objectTitleBar = main_win.titleBar
        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

        self.set_connections()
        self.insert_data_from_dictionary()
        self.set_styles()

    def onButtonMy(self):
        pass

    def set_connections(self):
        # коннекты для кнопок
        self.pushButtonPrintConsent.clicked.connect(self.create_consent)
        self.pushButtonAddRelative.clicked.connect(self.add_patient_relative)
        self.pushButtonNotSaveExit.clicked.connect(self.exit)
        self.pushButtonSaveExit.clicked.connect(self.exit_and_save)

    def insert_data_from_dictionary(self):
        # заполнение ячеек окна паспортных данных данными из словаря
        if 'имя' in self.d:
            self.surname.setText(self.d['фамилия'])
            self.name.setText(self.d['имя'])
            self.dadname.setText(self.d['отчество'])
            self.adress.setText(self.d['адрес'])
            self.phone.setText(self.d['телефон'])
            self.email.setText(self.d['электронная_почта'])
            self.passport.setText(self.d['паспорт'])
            self.polis_oms.setText(self.d['полис_ОМС'])
            self.snils.setText(self.d['СНИЛС'])
            self.dateEdit_birthday.setDate(QtCore.QDate.fromString(
                self.d['дата_рождения'], "dd.MM.yyyy"))
            self.comboBox_gender.setCurrentText(self.d['пол'])
            self.checkBox_signature_cant.setChecked(
                self.d.get('не_может_подписаться', False))
        update_after_passport_data(self.d)

    # функции для кнопок
    def create_consent(self):
        '''
        функция создает и открывает файл (.docx)
            с различными согласиями пациента
            с возможностью их редактирования
            и вывода на печать

        '''
        self.write_to_dictionary()

        self.bt_check = False
        if self.d['тип_стационара'] in {'БТ - круглосуточный', 'БТ - дневной'}:
            self.bt_check = True

        self.templates_consent = ['Согласие_перс_данные',
                                  'Согласие',
                                  'Уведомление']

        self.templates_consent_bta = ['Согласие_перс_данные',
                                      'Согласие',
                                      'Уведомление',
                                      'Согласие_БТА']

        if self.bt_check:
            creating_documents(self.d, self.templates_consent_bta)
        else:
            creating_documents(self.d, self.templates_consent)

        open_folder_with_files(self.d)

    def write_to_dictionary(self):
        '''
        перезапись в словаре всех значений из виджетов на новые
        '''
        self.d['фамилия'] = self.surname.text()
        self.d['имя'] = self.name.text()
        self.d['отчество'] = self.dadname.text()
        self.d['адрес'] = self.adress.text()
        self.d['телефон'] = self.phone.text()
        self.d['электронная_почта'] = self.email.text()
        self.d['паспорт'] = self.passport.text()
        self.d['полис_ОМС'] = self.polis_oms.text()
        self.d['СНИЛС'] = self.snils.text()
        self.d['дата_рождения'] = self.dateEdit_birthday\
            .dateTime().toString('dd.MM.yyyy')
        self.d['пол'] = self.comboBox_gender.currentText()
        self.d['не_может_подписаться'] = self\
            .checkBox_signature_cant.isChecked()

    def open_window(self, name):
        win = self.windows['Frameless']()
        win.setWidget(
            self.windows['omr'][name](
                windows=self.windows,
                main_win=win,
                dictionary=self.d))
        win.show()

    def add_patient_relative(self):
        self.write_to_dictionary()
        self.open_window('add_relative')
        self.main_win.close()

    def exit(self):
        self.open_window('patient_card')
        self.main_win.close()

    def exit_and_save(self):
        self.write_to_dictionary()
        write_omr_table(self.d)
        self.exit()

    def set_styles(self):
        pass
