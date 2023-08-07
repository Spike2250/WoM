from PySide6 import QtWidgets
from wom.GUI.PY.bta import bta_Diagnosis
from wom.app_logic.db_func.db_bta import write_all_data_to_db_bta
from wom.app_logic.writing.postprocessing.diagnosis import update_after_diagnosis  # noqa: E501


# Окно диагноза
class Ui_Diagnosis(QtWidgets.QMainWindow,
                   bta_Diagnosis.Ui_MainWindow):
    def __init__(self, windows, d):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.windows = windows
        self.d = d

        self.set_connections()
        self.set_patient_info()
        self.insert_data_from_dictionary()
        self.activate_VAS_boxes()

    def set_patient_info(self):
        # Заполнение Patient Info
        if 'patient_info' in self.d:
            self.label_Pt_info.setText(self.d['patient_info'])
        else:
            self.label_Pt_info.setText('Ошибка! Нет "patient_info" в словаре!')

    def set_connections(self):
        # коннекты кнопок
        self.pushButtonNotSaveExit.clicked.connect(self.exit)
        self.pushButtonSaveExit.clicked.connect(self.exit_and_save)
        # коннекты событий
        self.checkBoxPainCheck.stateChanged.connect(self.activate_VAS_boxes)

    def activate_VAS_boxes(self):
        if self.checkBoxPainCheck.isChecked():
            self.comboBoxDiagnosisFS_VAS_1.setEnabled(True)
            self.comboBoxDiagnosisFS_VAS_2.setEnabled(True)
        else:
            self.comboBoxDiagnosisFS_VAS_1.setEnabled(False)
            self.comboBoxDiagnosisFS_VAS_2.setEnabled(False)
            self.comboBoxDiagnosisFS_VAS_1.setCurrentText('0')
            self.comboBoxDiagnosisFS_VAS_2.setCurrentText('0')

    def insert_data_from_dictionary(self):
        # заполнение данных, если они уже есть
        if 'Основной_диагноз' in self.d:
            self.plainTextEditPtDiagnosisMain.setPlainText(self.d['Основной_диагноз'])  # noqa: E501
            self.plainTextEditPtDiagnosisConcomitant.setPlainText(self.d['Сопутствующий_диагноз'])  # noqa: E501
            self.comboBoxDiagnosisFS_RRS_1.setCurrentText(self.d['ШРМ'])
            self.comboBoxDiagnosisFS_mRs_1.setCurrentText(self.d['mRs'])
            self.comboBoxDiagnosisFS_IMR_1.setCurrentText(self.d['IMR'])
            self.comboBoxDiagnosisFS_Hauser_1.setCurrentText(self.d['хаузер'])
            self.comboBoxDiagnosisFS_VAS_1.setCurrentText(self.d['VAS'])
            self.checkBoxPainCheck.setChecked(self.d['наличие_боли'])
            self.comboBoxDiagnosisFS_RRS_2.setCurrentText(self.d['ШРМ_вып'])
            self.comboBoxDiagnosisFS_mRs_2.setCurrentText(self.d['mRs_вып'])
            self.comboBoxDiagnosisFS_IMR_2.setCurrentText(self.d['IMR_вып'])
            self.comboBoxDiagnosisFS_Hauser_2.setCurrentText(self.d['хаузер_вып'])  # noqa: E501
            self.comboBoxDiagnosisFS_VAS_2.setCurrentText(self.d['VAS_вып'])
        elif 'Сопутствующий_диагноз' in self.d:
            self.plainTextEditPtDiagnosisConcomitant.setPlainText(self.d['Сопутствующий_диагноз'])  # noqa: E501

        if 'NIHSS' in self.d:
            self.comboBoxDiagnosisFS_NIHSS.setCurrentText(self.d['NIHSS'])

    def write_to_dictionary(self):
        '''
        '''
        self.d['Основной_диагноз'] = self.plainTextEditPtDiagnosisMain.toPlainText()  # noqa: E501
        self.d['Сопутствующий_диагноз'] = self.plainTextEditPtDiagnosisConcomitant.toPlainText()  # noqa: E501
        self.d['ШРМ'] = self.comboBoxDiagnosisFS_RRS_1.currentText()
        self.d['mRs'] = self.comboBoxDiagnosisFS_mRs_1 .currentText()
        self.d['IMR'] = self.comboBoxDiagnosisFS_IMR_1.currentText()
        self.d['хаузер'] = self.comboBoxDiagnosisFS_Hauser_1.currentText()
        self.d['VAS'] = self.comboBoxDiagnosisFS_VAS_1.currentText()
        self.d['наличие_боли'] = self.checkBoxPainCheck.isChecked()
        self.d['ШРМ_вып'] = self.comboBoxDiagnosisFS_RRS_2.currentText()
        self.d['mRs_вып'] = self.comboBoxDiagnosisFS_mRs_2.currentText()
        self.d['IMR_вып'] = self.comboBoxDiagnosisFS_IMR_2.currentText()
        self.d['хаузер_вып'] = self.comboBoxDiagnosisFS_Hauser_2.currentText()
        self.d['VAS_вып'] = self.comboBoxDiagnosisFS_VAS_2.currentText()
        self.d['NIHSS'] = self.comboBoxDiagnosisFS_NIHSS.currentText()
        update_after_diagnosis(self.d)

    def exit_and_save(self):
        self.write_to_dictionary()
        write_all_data_to_db_bta(self.d)
        self.exit()

    def exit(self):
        self.hide()
        self.w = self.windows['bta']['patient_card'](self.windows, self.d)
        self.w.show()
