from PySide6 import QtWidgets, QtCore
from wom.GUI.PY import bta_Discharge_details
from wom.app_logic.db_func.db_bta import write_all_data_to_db_bta
from wom.app_logic.service_func import create_mkb_nmu_dict, add_mkb10_nmu
from wom.app_logic.writing.postprocessing.passport import update_patient_info
from wom.app_logic.writing.postprocessing.dis_details import update_after_dis_details  # noqa: E501


# Окно доп.данных для выписки (коды, услуги)
class Ui_Discharge_details(QtWidgets.QMainWindow,
                           bta_Discharge_details.Ui_MainWindow):
    def __init__(self, windows, d):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.windows = windows
        self.d = d

        self.mkb10, self.nmu = create_mkb_nmu_dict()

        self.set_connections()
        self.add_values_to_popup_lists()
        self.set_patient_info()
        self.insert_data_from_dictionary()

    def add_values_to_popup_lists(self):
        # добавление значений в выплывающие списки
        self.comboBoxPtMKB10_main.clear()
        self.comboBoxPtMKB10_main.addItems(list(self.mkb10.keys()))
        self.comboBoxPtNMU_code.clear()
        self.comboBoxPtNMU_code.addItems(list(self.nmu.keys()))

    def set_connections(self):
        # коннекты для кнопок
        self.pushButtonNotSaveExit.clicked.connect(self.exit)
        self.pushButtonSaveExit.clicked.connect(self.exit_and_save)
        self.pushButtonDischarge_and_close_history.clicked.connect(self.close_history)  # noqa: E501
        self.comboBoxPtMKB10_main.currentTextChanged.connect(self.change_mkb_label)  # noqa: E501
        self.comboBoxPtNMU_code.currentTextChanged.connect(self.change_nmu_label)  # noqa: E501

    def change_mkb_label(self):
        try:
            self.label_mkb.setText(
                self.mkb10[self.comboBoxPtMKB10_main.currentText()])
        except KeyError:
            self.label_mkb.setText('Не найден такой код МКБ-10')

    def change_nmu_label(self):
        try:
            self.label_nmu.setText(
                self.nmu[self.comboBoxPtNMU_code.currentText()])
        except KeyError:
            self.label_nmu.setText('Не найден такой код НМУ')

    def insert_data_from_dictionary(self):
        if 'ФИО_врача' in self.d:
            self.dateEditDischargeDate.setDate(QtCore.QDate.fromString(
                self.d['дата_выписки_план'], "dd.MM.yyyy"))
            self.dateEditDischargeDate_plan.setDate(QtCore.QDate.fromString(
                self.d['дата_выписки_план'], "dd.MM.yyyy"))
            self.comboBoxPtMKB10_main.setCurrentText(self.d['МКБ'])
            self.comboBoxPtNMU_code.setCurrentText(self.d['услуга'])
            self.dateEditPtAdmissionDay.setDate(QtCore.QDate.fromString(
                self.d['дата_поступления'], "dd.MM.yyyy"))
            self.timeEditPtAdmissionTime.setTime(QtCore.QTime.fromString(
                self.d['время_поступления'], "hh:mm"))
            self.comboBoxPtHoptitalisationType.setCurrentText(self.d['тип_стационара'])  # noqa: E501
            self.comboBoxTherapist.setCurrentText(self.d['ФИО_врача'])
            self.lineEdit_history_number.setText(self.d['номер_истории'])
            self.comboBox_department_head.setCurrentText(self.d['зав_отделением'])  # noqa: E501
            self.comboBox_referring_health_facility.setCurrentText(self.d['ЛПУ_кто_направил'])  # noqa: E501
            self.comboBoxGender.setCurrentText(self.d['пол'])
            self.lineEdit_room_number.setText(self.d['палата'])
            # время выписки по умолчанию
            self.timeEditDischargeTime.setTime(QtCore.QTime.fromString(
                "10:00", "hh:mm"))
        if 'вид_выбытия' in self.d:
            self.dateEditDischargeDate.setDate(QtCore.QDate.fromString(
                self.d['дата_выписки'], "dd.MM.yyyy"))
            self.timeEditDischargeTime.setTime(QtCore.QTime.fromString(
                self.d['время_выписки'], "hh:mm"))
            self.comboBoxDischargeData_1.setCurrentText(self.d['вид_выбытия'])
            self.comboBoxDischargeData_2.setCurrentText(self.d['характер_выписки'])  # noqa: E501
            self.comboBoxDischargeData_3.setCurrentText(self.d['итог_выписки'])

    def set_patient_info(self):
        # Заполнение Patient Info
        if 'patient_info' in self.d:
            self.label_Pt_info.setText(self.d['patient_info'])
        else:
            self.label_Pt_info.setText('Ошибка! Нет "patient_info" в словаре!')

    def write_to_dictionary(self):
        '''
        перезапись в словаре всех значений из виджетов на новые
        '''
        self.d['дата_выписки_план'] = self.dateEditDischargeDate_plan.dateTime().toString('dd.MM.yyyy')  # noqa: E501
        self.d['дата_выписки'] = self.dateEditDischargeDate.dateTime().toString('dd.MM.yyyy')  # noqa: E501
        self.d['время_выписки'] = self.timeEditDischargeTime.dateTime().toString('hh:mm')  # noqa: E501
        self.d['МКБ'] = self.comboBoxPtMKB10_main.currentText()
        self.d['услуга'] = self.comboBoxPtNMU_code.currentText()
        self.d['вид_выбытия'] = self.comboBoxDischargeData_1.currentText()
        self.d['характер_выписки'] = self.comboBoxDischargeData_2.currentText()
        self.d['итог_выписки'] = self.comboBoxDischargeData_3.currentText()
        self.d['дата_поступления'] = self.dateEditPtAdmissionDay.dateTime().toString('dd.MM.yyyy')  # noqa: E501
        self.d['время_поступления'] = self.timeEditPtAdmissionTime.dateTime().toString('hh:mm')  # noqa: E501
        self.d['тип_стационара'] = self.comboBoxPtHoptitalisationType.currentText()  # noqa: E501
        self.d['ФИО_врача'] = self.comboBoxTherapist.currentText()
        self.d['номер_истории'] = self.lineEdit_history_number.text()
        self.d['зав_отделением'] = self.comboBox_department_head.currentText()
        self.d['ЛПУ_кто_направил'] = self.comboBox_referring_health_facility.currentText()  # noqa: E501
        self.d['пол'] = self.comboBoxGender.currentText()
        self.d['палата'] = self.lineEdit_room_number.text()
        add_mkb10_nmu(self.d)
        update_patient_info(self.d)
        update_after_dis_details(self.d)

        # название отделения
        if self.d['тип_стационара'] == 'БТ - круглосуточный':
            self.d['название_отделения'] = '4102. Неврологическое отделение (Панфилова, 20)'  # noqa: E501
        elif self.d['тип_стационара'] == 'БТ - дневной':
            self.d['название_отделения'] = '4202. Неврологический дневной стационар'  # noqa: E501

    def exit_and_save(self):
        self.write_to_dictionary()
        write_all_data_to_db_bta(self.d)
        self.exit()

    def exit(self):
        self.hide()
        self.w = self.windows['bta']['patient_card'](self.windows, self.d)
        self.w.show()

    def close_history(self):
        if self.checkBox_dis.isChecked():
            self.d['status_act'] = False  # свидетельство, что пациент выписан
            # записываем новые данные в словарь
            self.write_to_dictionary()
            # записываем словарь в json-файл и обновляем БД
            write_all_data_to_db_bta(self.d)
            self.hide()
            self.w = self.windows['bta']['main_menu'](self.windows)
            self.w.show()
