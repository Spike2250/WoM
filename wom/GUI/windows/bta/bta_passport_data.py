from PySide6 import QtWidgets, QtCore
from wom.GUI.PY import bta_PatientPassportData
from wom.app_logic.db_func.db_bta import write_all_data_to_db_bta


# Окно паспортных данных
class Ui_PatientPassportData(QtWidgets.QMainWindow,
                             bta_PatientPassportData.Ui_PatientPassportData):
    def __init__(self, windows, d):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.windows = windows
        self.d = d

        self.set_connections()
        self.insert_data_from_dictionary()

    def set_connections(self):
        self.pushButtonNotSaveExit.clicked.connect(self.return_to_card)
        self.pushButtonSaveExit.clicked.connect(self.exit_and_save)
        self.pushButtonHelp.clicked.connect(self.open_help)

    def return_to_card(self):
        self.hide()
        self.w = self.windows['bta']['patient_card'](self.windows, self.d)
        self.w.show()

    def exit_and_save(self):
        self.write_to_dictionary()
        write_all_data_to_db_bta(self.d)
        self.return_to_card()

    def open_help(self):
        pass

    def insert_data_from_dictionary(self):
        # заполнение ячеек окна паспортных данных данными из словаря
        if 'имя' in self.d:
            # lineEdit's
            self.surname.setText(self.d['фамилия'])
            self.name.setText(self.d['имя'])
            self.dadname.setText(self.d['отчество'])
            self.adress.setText(self.d['адрес'])
            self.phone.setText(self.d['телефон'])
            self.email.setText(self.d['электронная_почта'])
            self.passport.setText(self.d['паспорт'])
            self.polis_oms.setText(self.d['полис_ОМС'])
            self.snils.setText(self.d['СНИЛС'])
            # dateEdit
            self.dateEdit_birthday.setDate(
                QtCore.QDate.fromString(self.d['дата_рождения'], "dd.MM.yyyy"))
            # comboBox
            self.comboBox_gender.setCurrentText(self.d['пол'])
            # checkBox
            self.checkBox_signature_cant.setChecked(self.d['не_может_подписаться'])

    def write_to_dictionary(self):
        # lineEdit's
        self.d['фамилия'] = self.surname.text()
        self.d['имя'] = self.name.text()
        self.d['отчество'] = self.dadname.text()
        self.d['адрес'] = self.adress.text()
        self.d['телефон'] = self.phone.text()
        self.d['электронная_почта'] = self.email.text()
        self.d['паспорт'] = self.passport.text()
        self.d['полис_ОМС'] = self.polis_oms.text()
        self.d['СНИЛС'] = self.snils.text()
        # dateEdit
        self.d['дата_рождения'] = self.dateEdit_birthday.dateTime().toString('dd.MM.yyyy')
        # comboBox
        self.d['пол'] = self.comboBox_gender.currentText()
        # checkBox
        self.d['не_может_подписаться'] = self.checkBox_signature_cant.isChecked()

        # добавление надписей, при невозможнссти пациента поставить подпись
        if self.d['не_может_подписаться']:
            self.d['нмпп'] = 'не может подписаться'
            self.d['нмпп_дата_поступления'] = self.d['дата_поступления']
            self.d['нмпп_дата_выписки'] = self.d['дата_выписки']
            self.d['нмпп_ФИО_врача'] = self.d['ФИО_врача']
            self.d['нмпп_зав_отделением'] = self.d['зав_отделением']
