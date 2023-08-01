from PySide6 import QtWidgets
from wom.GUI.PY import bta_Neur_status
from wom.app_logic.db_func.db_st_neur_templates import (read_db_neur_template_list,  # noqa: E501
                                                        read_db_neur_template_data,  # noqa: E501
                                                        insert_neur_template_into_db,  # noqa: E501
                                                        update_neur_template_db)  # noqa: E501
from wom.app_logic.db_func.db_bta import write_all_data_to_db_bta
from wom.app_logic.writing.postprocessing.neur_st import update_after_neur_st


# Окно неврологического статуса
class Ui_Status_neurology(QtWidgets.QMainWindow,
                          bta_Neur_status.Ui_MainWindow):
    def __init__(self, windows, d):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.windows = windows
        self.d = d

        self.set_connections()
        self.set_templates_list()
        self.set_patient_info()
        self.insert_data_from_dictionary()

    def set_connections(self):
        # коннекты кнопок
        self.pushButtonNotSaveExit.clicked.connect(self.exit)
        self.pushButtonSaveExit.clicked.connect(self.exit_and_save)
        self.pushButtonAddNewTemplate.clicked.connect(
            self.add_new_template_neur_st)
        self.pushButton_push_temp.clicked.connect(
            self.push_active_template)

    def set_templates_list(self):
        # список шаблонов
        self.templates_list = read_db_neur_template_list()
        self.comboBoxNeuralStTemplate.clear()
        if len(self.templates_list) <= 1:
            self.comboBoxNeuralStTemplate.addItem(self.templates_list[0])
        else:
            self.comboBoxNeuralStTemplate.addItems(self.templates_list)

    def set_patient_info(self):
        # Заполнение Patient Info
        if 'patient_info' in self.d:
            self.label_Pt_info.setText(self.d['patient_info'])
        else:
            self.label_Pt_info.setText('Ошибка! Нет "patient_info" в словаре!')

    def insert_data_from_dictionary(self):
        # заполенение данных, если они уже есть
        if 'Неврологический_статус' in self.d:
            # Общие
            self.comboBoxNS_Conscious.setCurrentText(self.d['Сознание'])
            self.comboBoxNS_GCS.setCurrentText(self.d['ШКГ'])
            self.comboBoxNS_RASS.setCurrentText(self.d['RASS'])
            self.comboBoxNS_Contact.setCurrentText(self.d['Контакт'])
            self.comboBoxNS_Orientation.setCurrentText(self.d['Ориентирование'])  # noqa: E501
            self.comboBoxNS_MeningealSymp_1.setCurrentText(self.d['Менингеальные_1'])  # noqa: E501
            self.comboBoxNS_MeningealSymp_2.setCurrentText(self.d['Менингеальные_2'])  # noqa: E501
            self.comboBoxNS_MeningealSymp_3.setCurrentText(self.d['Менингеальные_3'])  # noqa: E501
            self.comboBoxNS_Speech_1.setCurrentText(self.d['Речь_1'])
            self.comboBoxNS_Speech_2.setCurrentText(self.d['Речь_2'])
            self.comboBoxNS_Speech_3.setCurrentText(self.d['Речь_3'])
            self.comboBoxNS_PelvicFuntion.setCurrentText(self.d['ФТО'])
            # ЧМН
            self.comboBoxNS_4MN_1_Smell.setCurrentText(self.d['обоняние'])
            self.comboBoxNS_4MN_2_VisualAcuity.setCurrentText(self.d['острота_зрения'])  # noqa: E501
            self.comboBoxNS_4MN_2_Fields.setCurrentText(self.d['поля_зрения'])
            self.comboBoxNS_4MN_2_Pupils.setCurrentText(self.d['зрачки'])
            self.comboBoxNS_4MN_2_Accomodation.setCurrentText(self.d['аккомодация'])  # noqa: E501
            self.comboBoxNS_4MN_2_Photoreaction.setCurrentText(self.d['фотореакция'])  # noqa: E501
            self.comboBoxNS_4MN_2_Convergension.setCurrentText(self.d['конвергенция'])  # noqa: E501
            self.comboBoxNS_4MN_346_EyeballMove.setCurrentText(self.d['движения_гл_яблок'])  # noqa: E501
            self.comboBoxNS_4MN_346_EyeballParesis.setCurrentText(self.d['парез_глазодвиг'])  # noqa: E501
            self.comboBoxNS_4MN_346_Ptosis.setCurrentText(self.d['птоз'])
            self.comboBoxNS_4MN_346_Nystagmus.setCurrentText(self.d['нистагм'])
            self.comboBoxNS_4MN_5_FaceSensitivity.setCurrentText(self.d['V_пара'])  # noqa: E501
            self.comboBoxNS_4MN_5_Branches.setCurrentText(self.d['V_пара_Ветви'])  # noqa: E501
            self.comboBoxNS_4MN_5_Zelder.setCurrentText(self.d['V_пара_Зельдер'])  # noqa: E501
            self.comboBoxNS_4MN_7_Symmetry.setCurrentText(self.d['VII_пара'])
            self.comboBoxNS_4MN_7_Other.setCurrentText(self.d['VII_пара_дополнение'])  # noqa: E501
            self.comboBoxNS_4MN_8_Hearing.setCurrentText(self.d['слух'])
            self.comboBoxNS_4MN_8_CentralVertigo.setCurrentText(self.d['центр_головокружение'])  # noqa: E501
            self.comboBoxNS_4MN_910_Phonation.setCurrentText(self.d['фонация'])
            self.comboBoxNS_4MN_910_SoftPalate.setCurrentText(self.d['мягкое_небо'])  # noqa: E501
            self.comboBoxNS_4MN_910_Swallowing.setCurrentText(self.d['глотание'])  # noqa: E501
            self.comboBoxNS_4MN_910_Food.setCurrentText(self.d['питание'])
            self.comboBoxNS_4MN_910_Dysarthria.setCurrentText(self.d['дизартрия'])  # noqa: E501
            self.comboBoxNS_4MN_910_Dysarthria_power.setCurrentText(self.d['дизартрия_степень'])  # noqa: E501
            self.comboBoxNS_4MN_11.setCurrentText(self.d['XI_пара'])
            self.comboBoxNS_4MN_12.setCurrentText(self.d['XII_пара'])
            # Движение, координация
            self.comboBoxNS_Moving_limbs.setCurrentText(self.d['движ_конечности'])  # noqa: E501
            self.comboBoxNS_Moving_joints.setCurrentText(self.d['движ_суставы'])  # noqa: E501
            self.comboBoxNS_Moving_spine.setCurrentText(self.d['движ_позвоночник'])  # noqa: E501
            self.comboBoxNS_MRC_R_A_P.setCurrentText(self.d['MRC_R_A_P'])
            self.comboBoxNS_MRC_R_A_D.setCurrentText(self.d['MRC_R_A_D'])
            self.comboBoxNS_MRC_R_L_P.setCurrentText(self.d['MRC_R_L_P'])
            self.comboBoxNS_MRC_R_L_D.setCurrentText(self.d['MRC_R_L_D'])
            self.comboBoxNS_MRC_L_A_P.setCurrentText(self.d['MRC_L_A_P'])
            self.comboBoxNS_MRC_L_A_D.setCurrentText(self.d['MRC_L_A_D'])
            self.comboBoxNS_MRC_L_L_P.setCurrentText(self.d['MRC_L_L_P'])
            self.comboBoxNS_MRC_L_L_D.setCurrentText(self.d['MRC_L_L_D'])
            self.comboBoxNS_MuscleTonus_1.setCurrentText(self.d['мышечный_тонус_1'])  # noqa: E501
            self.comboBoxNS_MuscleTonus_2.setCurrentText(self.d['мышечный_тонус_2'])  # noqa: E501
            self.comboBoxNS_Ash_R_A_P.setCurrentText(self.d['Ash_R_A_P'])
            self.comboBoxNS_Ash_R_A_D.setCurrentText(self.d['Ash_R_A_D'])
            self.comboBoxNS_Ash_R_L_P.setCurrentText(self.d['Ash_R_L_P'])
            self.comboBoxNS_Ash_R_L_D.setCurrentText(self.d['Ash_R_L_D'])
            self.comboBoxNS_Ash_L_A_P.setCurrentText(self.d['Ash_L_A_P'])
            self.comboBoxNS_Ash_L_A_D.setCurrentText(self.d['Ash_L_A_D'])
            self.comboBoxNS_Ash_L_L_P.setCurrentText(self.d['Ash_L_L_P'])
            self.comboBoxNS_Ash_L_L_D.setCurrentText(self.d['Ash_L_L_D'])
            self.comboBoxNS_Arms_reflex_1.setCurrentText(self.d['рефлексы_руки_1'])  # noqa: E501
            self.comboBoxNS_Arms_reflex_2.setCurrentText(self.d['рефлексы_руки_2'])  # noqa: E501
            self.comboBoxNS_Legs_reflex_1.setCurrentText(self.d['рефлексы_ноги_1'])  # noqa: E501
            self.comboBoxNS_Legs_reflex_2.setCurrentText(self.d['рефлексы_ноги_2'])  # noqa: E501
            self.comboBoxNS_Pathology_reflex.setCurrentText(self.d['патологические_рефлексы'])  # noqa: E501
            self.comboBoxNS_MuscleTrofic.setCurrentText(self.d['трофика_мышц'])
            self.comboBoxNS_Sensitivity_1.setCurrentText(self.d['чувствительность_1'])  # noqa: E501
            self.comboBoxNS_Sensitivity_2.setCurrentText(self.d['чувствительность_2'])  # noqa: E501
            self.plainTextEditNS_Sensitivity.setPlainText(self.d['чувствительность_текст'])  # noqa: E501
            self.comboBoxNS_Coordination_1.setCurrentText(self.d['координация_1'])  # noqa: E501
            self.comboBoxNS_Coordination_2.setCurrentText(self.d['координация_2'])  # noqa: E501
            self.plainTextEditNS_Coordination.setPlainText(self.d['координация_текст'])  # noqa: E501
            self.comboBoxNS_Extrapyramid_1.setCurrentText(self.d['экстрапирамидные_1'])  # noqa: E501
            self.comboBoxNS_Extrapyramid_2.setCurrentText(self.d['экстрапирамидные_2'])  # noqa: E501
            self.comboBoxNS_Extrapyramid_3.setCurrentText(self.d['экстрапирамидные_3'])  # noqa: E501
            self.comboBoxNS_EpilepticStatus.setCurrentText(self.d['эпилептический_статус'])  # noqa: E501
            # функциональный статус
            self.comboBoxNS_FuncStatus_common.setCurrentText(self.d['функциональный_статус'])  # noqa: E501
            self.comboBoxNS_FuncStatus_walking.setCurrentText(self.d['ходьба'])
            self.comboBoxNS_FuncStatus_walking_type.setCurrentText(self.d['походка'])  # noqa: E501
            self.comboBoxNS_FuncStatus_motorics.setCurrentText(self.d['мелкая_моторика'])  # noqa: E501
            self.comboBoxNS_FuncStatus_dressing.setCurrentText(self.d['одевание'])  # noqa: E501
            self.comboBoxNS_FuncStatus_stairway.setCurrentText(self.d['подъем_по_лестнице'])  # noqa: E501
            self.comboBoxNS_FuncStatus_eating.setCurrentText(self.d['прием_пищи'])  # noqa: E501
            self.comboBoxNS_FuncStatus_writing.setCurrentText(self.d['письмо'])
            self.comboBoxNS_FuncStatus_reading.setCurrentText(self.d['чтение'])
            self.plainTextEditNS_FuncStatus.setPlainText(self.d['функциональный_статус_дополнение'])  # noqa: E501
            self.plainTextEditNS_other.setPlainText(self.d['NS_дополнение'])

    def write_to_dictionary(self):
        self.d['Сознание'] = self.comboBoxNS_Conscious.currentText()
        self.d['ШКГ'] = self.comboBoxNS_GCS.currentText()
        self.d['RASS'] = self.comboBoxNS_RASS.currentText()
        self.d['Контакт'] = self.comboBoxNS_Contact.currentText()
        self.d['Ориентирование'] = self.comboBoxNS_Orientation.currentText()
        self.d['Менингеальные_1'] = self.comboBoxNS_MeningealSymp_1.currentText()  # noqa: E501
        self.d['Менингеальные_2'] = self.comboBoxNS_MeningealSymp_2.currentText()  # noqa: E501
        self.d['Менингеальные_3'] = self.comboBoxNS_MeningealSymp_3.currentText()  # noqa: E501
        self.d['Речь_1'] = self.comboBoxNS_Speech_1.currentText()
        self.d['Речь_2'] = self.comboBoxNS_Speech_2.currentText()
        self.d['Речь_3'] = self.comboBoxNS_Speech_3.currentText()
        self.d['ФТО'] = self.comboBoxNS_PelvicFuntion.currentText()
        # ЧМН
        self.d['обоняние'] = self.comboBoxNS_4MN_1_Smell.currentText()
        self.d['острота_зрения'] = self.comboBoxNS_4MN_2_VisualAcuity.currentText()  # noqa: E501
        self.d['поля_зрения'] = self.comboBoxNS_4MN_2_Fields.currentText()
        self.d['зрачки'] = self.comboBoxNS_4MN_2_Pupils.currentText()
        self.d['аккомодация'] = self.comboBoxNS_4MN_2_Accomodation.currentText()  # noqa: E501
        self.d['фотореакция'] = self.comboBoxNS_4MN_2_Photoreaction.currentText()  # noqa: E501
        self.d['конвергенция'] = self.comboBoxNS_4MN_2_Convergension.currentText()  # noqa: E501
        self.d['движения_гл_яблок'] = self.comboBoxNS_4MN_346_EyeballMove.currentText()  # noqa: E501
        self.d['парез_глазодвиг'] = self.comboBoxNS_4MN_346_EyeballParesis.currentText()  # noqa: E501
        self.d['птоз'] = self.comboBoxNS_4MN_346_Ptosis.currentText()
        self.d['нистагм'] = self.comboBoxNS_4MN_346_Nystagmus.currentText()
        self.d['V_пара'] = self.comboBoxNS_4MN_5_FaceSensitivity.currentText()
        self.d['V_пара_Ветви'] = self.comboBoxNS_4MN_5_Branches.currentText()
        self.d['V_пара_Зельдер'] = self.comboBoxNS_4MN_5_Zelder.currentText()
        self.d['VII_пара'] = self.comboBoxNS_4MN_7_Symmetry.currentText()
        self.d['VII_пара_дополнение'] = self.comboBoxNS_4MN_7_Other.currentText()  # noqa: E501
        self.d['слух'] = self.comboBoxNS_4MN_8_Hearing.currentText()
        self.d['центр_головокружение'] = self.comboBoxNS_4MN_8_CentralVertigo.currentText()  # noqa: E501
        self.d['фонация'] = self.comboBoxNS_4MN_910_Phonation.currentText()
        self.d['мягкое_небо'] = self.comboBoxNS_4MN_910_SoftPalate.currentText()  # noqa: E501
        self.d['глотание'] = self.comboBoxNS_4MN_910_Swallowing.currentText()
        self.d['питание'] = self.comboBoxNS_4MN_910_Food.currentText()
        self.d['дизартрия'] = self.comboBoxNS_4MN_910_Dysarthria.currentText()
        self.d['дизартрия_степень'] = self.comboBoxNS_4MN_910_Dysarthria_power.currentText()  # noqa: E501
        self.d['XI_пара'] = self.comboBoxNS_4MN_11.currentText()
        self.d['XII_пара'] = self.comboBoxNS_4MN_12.currentText()
        # Движение, координация
        self.d['движ_конечности'] = self.comboBoxNS_Moving_limbs.currentText()
        self.d['движ_суставы'] = self.comboBoxNS_Moving_joints.currentText()
        self.d['движ_позвоночник'] = self.comboBoxNS_Moving_spine.currentText()
        self.d['MRC_R_A_P'] = self.comboBoxNS_MRC_R_A_P.currentText()
        self.d['MRC_R_A_D'] = self.comboBoxNS_MRC_R_A_D.currentText()
        self.d['MRC_R_L_P'] = self.comboBoxNS_MRC_R_L_P.currentText()
        self.d['MRC_R_L_D'] = self.comboBoxNS_MRC_R_L_D.currentText()
        self.d['MRC_L_A_P'] = self.comboBoxNS_MRC_L_A_P.currentText()
        self.d['MRC_L_A_D'] = self.comboBoxNS_MRC_L_A_D.currentText()
        self.d['MRC_L_L_P'] = self.comboBoxNS_MRC_L_L_P.currentText()
        self.d['MRC_L_L_D'] = self.comboBoxNS_MRC_L_L_D.currentText()
        self.d['мышечный_тонус_1'] = self.comboBoxNS_MuscleTonus_1.currentText()  # noqa: E501
        self.d['мышечный_тонус_2'] = self.comboBoxNS_MuscleTonus_2.currentText()  # noqa: E501
        self.d['Ash_R_A_P'] = self.comboBoxNS_Ash_R_A_P.currentText()
        self.d['Ash_R_A_D'] = self.comboBoxNS_Ash_R_A_D.currentText()
        self.d['Ash_R_L_P'] = self.comboBoxNS_Ash_R_L_P.currentText()
        self.d['Ash_R_L_D'] = self.comboBoxNS_Ash_R_L_D.currentText()
        self.d['Ash_L_A_P'] = self.comboBoxNS_Ash_L_A_P.currentText()
        self.d['Ash_L_A_D'] = self.comboBoxNS_Ash_L_A_D.currentText()
        self.d['Ash_L_L_P'] = self.comboBoxNS_Ash_L_L_P.currentText()
        self.d['Ash_L_L_D'] = self.comboBoxNS_Ash_L_L_D.currentText()
        self.d['рефлексы_руки_1'] = self.comboBoxNS_Arms_reflex_1.currentText()
        self.d['рефлексы_руки_2'] = self.comboBoxNS_Arms_reflex_2.currentText()
        self.d['рефлексы_ноги_1'] = self.comboBoxNS_Legs_reflex_1.currentText()
        self.d['рефлексы_ноги_2'] = self.comboBoxNS_Legs_reflex_2.currentText()
        self.d['патологические_рефлексы'] = self.comboBoxNS_Pathology_reflex.currentText()  # noqa: E501
        self.d['трофика_мышц'] = self.comboBoxNS_MuscleTrofic.currentText()
        self.d['чувствительность_1'] = self.comboBoxNS_Sensitivity_1.currentText()  # noqa: E501
        self.d['чувствительность_2'] = self.comboBoxNS_Sensitivity_2.currentText()  # noqa: E501
        self.d['чувствительность_текст'] = self.plainTextEditNS_Sensitivity.toPlainText()  # noqa: E501
        self.d['координация_1'] = self.comboBoxNS_Coordination_1.currentText()
        self.d['координация_2'] = self.comboBoxNS_Coordination_2.currentText()
        self.d['координация_текст'] = self.plainTextEditNS_Coordination.toPlainText()  # noqa: E501
        self.d['экстрапирамидные_1'] = self.comboBoxNS_Extrapyramid_1.currentText()  # noqa: E501
        self.d['экстрапирамидные_2'] = self.comboBoxNS_Extrapyramid_2.currentText()  # noqa: E501
        self.d['экстрапирамидные_3'] = self.comboBoxNS_Extrapyramid_3.currentText()  # noqa: E501
        self.d['эпилептический_статус'] = self.comboBoxNS_EpilepticStatus.currentText()  # noqa: E501
        # функциональный статус
        self.d['функциональный_статус'] = self.comboBoxNS_FuncStatus_common.currentText()  # noqa: E501
        self.d['ходьба'] = self.comboBoxNS_FuncStatus_walking.currentText()
        self.d['походка'] = self.comboBoxNS_FuncStatus_walking_type.currentText()  # noqa: E501
        self.d['мелкая_моторика'] = self.comboBoxNS_FuncStatus_motorics.currentText()  # noqa: E501
        self.d['одевание'] = self.comboBoxNS_FuncStatus_dressing.currentText()
        self.d['подъем_по_лестнице'] = self.comboBoxNS_FuncStatus_stairway.currentText()  # noqa: E501
        self.d['прием_пищи'] = self.comboBoxNS_FuncStatus_eating.currentText()
        self.d['письмо'] = self.comboBoxNS_FuncStatus_writing.currentText()
        self.d['чтение'] = self.comboBoxNS_FuncStatus_reading.currentText()
        self.d['функциональный_статус_дополнение'] = self.plainTextEditNS_FuncStatus.toPlainText()  # noqa: E501
        self.d['NS_дополнение'] = self.plainTextEditNS_other.toPlainText()

        update_after_neur_st(self.d, 'первичный')

    def exit_and_save(self):
        self.write_to_dictionary()
        write_all_data_to_db_bta(self.d)
        self.exit()

    def exit(self):
        self.hide()
        self.w = self.windows['bta']['patient_card'](self.windows, self.d)
        self.w.show()

    def add_new_template_neur_st(self):
        new_template_name = self.lineEdit_new_template_name.text()
        # проверяем не пустое ли имя нового шаблона
        if new_template_name != '':
            # проверяем есть ли уже шаблон с таким именем
            if new_template_name not in self.templates_list:
                # формируем кортеж с данными нового шаблона
                template_new = (
                    self.lineEdit_new_template_name.text(),
                    self.comboBoxNS_Conscious.currentText(),
                    self.comboBoxNS_GCS.currentText(),
                    self.comboBoxNS_RASS.currentText(),
                    self.comboBoxNS_Contact.currentText(),
                    self.comboBoxNS_Orientation.currentText(),
                    self.comboBoxNS_MeningealSymp_1.currentText(),
                    self.comboBoxNS_MeningealSymp_2.currentText(),
                    self.comboBoxNS_MeningealSymp_3.currentText(),
                    self.comboBoxNS_Speech_1.currentText(),
                    self.comboBoxNS_Speech_2.currentText(),
                    self.comboBoxNS_Speech_3.currentText(),
                    self.comboBoxNS_PelvicFuntion.currentText(),
                    self.comboBoxNS_4MN_1_Smell.currentText(),
                    self.comboBoxNS_4MN_2_VisualAcuity.currentText(),
                    self.comboBoxNS_4MN_2_Fields.currentText(),
                    self.comboBoxNS_4MN_2_Pupils.currentText(),
                    self.comboBoxNS_4MN_2_Accomodation.currentText(),
                    self.comboBoxNS_4MN_2_Photoreaction.currentText(),
                    self.comboBoxNS_4MN_2_Convergension.currentText(),
                    self.comboBoxNS_4MN_346_EyeballMove.currentText(),
                    self.comboBoxNS_4MN_346_EyeballParesis.currentText(),
                    self.comboBoxNS_4MN_346_Ptosis.currentText(),
                    self.comboBoxNS_4MN_346_Nystagmus.currentText(),
                    self.comboBoxNS_4MN_5_FaceSensitivity.currentText(),
                    self.comboBoxNS_4MN_5_Branches.currentText(),
                    self.comboBoxNS_4MN_5_Zelder.currentText(),
                    self.comboBoxNS_4MN_7_Symmetry.currentText(),
                    self.comboBoxNS_4MN_7_Other.currentText(),
                    self.comboBoxNS_4MN_8_Hearing.currentText(),
                    self.comboBoxNS_4MN_8_CentralVertigo.currentText(),
                    self.comboBoxNS_4MN_910_Phonation.currentText(),
                    self.comboBoxNS_4MN_910_SoftPalate.currentText(),
                    self.comboBoxNS_4MN_910_Swallowing.currentText(),
                    self.comboBoxNS_4MN_910_Food.currentText(),
                    self.comboBoxNS_4MN_910_Dysarthria.currentText(),
                    self.comboBoxNS_4MN_910_Dysarthria_power.currentText(),
                    self.comboBoxNS_4MN_11.currentText(),
                    self.comboBoxNS_4MN_12.currentText(),
                    self.comboBoxNS_Moving_limbs.currentText(),
                    self.comboBoxNS_Moving_joints.currentText(),
                    self.comboBoxNS_Moving_spine.currentText(),
                    self.comboBoxNS_MRC_R_A_P.currentText(),
                    self.comboBoxNS_MRC_R_A_D.currentText(),
                    self.comboBoxNS_MRC_R_L_P.currentText(),
                    self.comboBoxNS_MRC_R_L_D.currentText(),
                    self.comboBoxNS_MRC_L_A_P.currentText(),
                    self.comboBoxNS_MRC_L_A_D.currentText(),
                    self.comboBoxNS_MRC_L_L_P.currentText(),
                    self.comboBoxNS_MRC_L_L_D.currentText(),
                    self.comboBoxNS_MuscleTonus_1.currentText(),
                    self.comboBoxNS_MuscleTonus_2.currentText(),
                    self.comboBoxNS_Ash_R_A_P.currentText(),
                    self.comboBoxNS_Ash_R_A_D.currentText(),
                    self.comboBoxNS_Ash_R_L_P.currentText(),
                    self.comboBoxNS_Ash_R_L_D.currentText(),
                    self.comboBoxNS_Ash_L_A_P.currentText(),
                    self.comboBoxNS_Ash_L_A_D.currentText(),
                    self.comboBoxNS_Ash_L_L_P.currentText(),
                    self.comboBoxNS_Ash_L_L_D.currentText(),
                    self.comboBoxNS_Arms_reflex_1.currentText(),
                    self.comboBoxNS_Arms_reflex_2.currentText(),
                    self.comboBoxNS_Legs_reflex_1.currentText(),
                    self.comboBoxNS_Legs_reflex_2.currentText(),
                    self.comboBoxNS_Pathology_reflex.currentText(),
                    self.comboBoxNS_MuscleTrofic.currentText(),
                    self.comboBoxNS_Sensitivity_1.currentText(),
                    self.comboBoxNS_Sensitivity_2.currentText(),
                    self.plainTextEditNS_Sensitivity.toPlainText(),
                    self.comboBoxNS_Coordination_1.currentText(),
                    self.comboBoxNS_Coordination_2.currentText(),
                    self.plainTextEditNS_Coordination.toPlainText(),
                    self.comboBoxNS_Extrapyramid_1.currentText(),
                    self.comboBoxNS_Extrapyramid_2.currentText(),
                    self.comboBoxNS_Extrapyramid_3.currentText(),
                    self.comboBoxNS_EpilepticStatus.currentText(),
                    self.comboBoxNS_FuncStatus_common.currentText(),
                    self.comboBoxNS_FuncStatus_walking.currentText(),
                    self.comboBoxNS_FuncStatus_walking_type.currentText(),
                    self.comboBoxNS_FuncStatus_motorics.currentText(),
                    self.comboBoxNS_FuncStatus_dressing.currentText(),
                    self.comboBoxNS_FuncStatus_stairway.currentText(),
                    self.comboBoxNS_FuncStatus_eating.currentText(),
                    self.comboBoxNS_FuncStatus_writing.currentText(),
                    self.comboBoxNS_FuncStatus_reading.currentText(),
                    self.plainTextEditNS_FuncStatus.toPlainText(),
                    self.plainTextEditNS_other.toPlainText()
                )
                # записываем новый шаблон
                insert_neur_template_into_db(template_new)
            else:
                # такое имя шаблона уже есть
                # уточняем желание перезаписать данные
                ''''''
                # формируем кортеж с данными нового шаблона
                template_new = (
                    self.comboBoxNS_Conscious.currentText(),
                    self.comboBoxNS_GCS.currentText(),
                    self.comboBoxNS_RASS.currentText(),
                    self.comboBoxNS_Contact.currentText(),
                    self.comboBoxNS_Orientation.currentText(),
                    self.comboBoxNS_MeningealSymp_1.currentText(),
                    self.comboBoxNS_MeningealSymp_2.currentText(),
                    self.comboBoxNS_MeningealSymp_3.currentText(),
                    self.comboBoxNS_Speech_1.currentText(),
                    self.comboBoxNS_Speech_2.currentText(),
                    self.comboBoxNS_Speech_3.currentText(),
                    self.comboBoxNS_PelvicFuntion.currentText(),
                    self.comboBoxNS_4MN_1_Smell.currentText(),
                    self.comboBoxNS_4MN_2_VisualAcuity.currentText(),
                    self.comboBoxNS_4MN_2_Fields.currentText(),
                    self.comboBoxNS_4MN_2_Pupils.currentText(),
                    self.comboBoxNS_4MN_2_Accomodation.currentText(),
                    self.comboBoxNS_4MN_2_Photoreaction.currentText(),
                    self.comboBoxNS_4MN_2_Convergension.currentText(),
                    self.comboBoxNS_4MN_346_EyeballMove.currentText(),
                    self.comboBoxNS_4MN_346_EyeballParesis.currentText(),
                    self.comboBoxNS_4MN_346_Ptosis.currentText(),
                    self.comboBoxNS_4MN_346_Nystagmus.currentText(),
                    self.comboBoxNS_4MN_5_FaceSensitivity.currentText(),
                    self.comboBoxNS_4MN_5_Branches.currentText(),
                    self.comboBoxNS_4MN_5_Zelder.currentText(),
                    self.comboBoxNS_4MN_7_Symmetry.currentText(),
                    self.comboBoxNS_4MN_7_Other.currentText(),
                    self.comboBoxNS_4MN_8_Hearing.currentText(),
                    self.comboBoxNS_4MN_8_CentralVertigo.currentText(),
                    self.comboBoxNS_4MN_910_Phonation.currentText(),
                    self.comboBoxNS_4MN_910_SoftPalate.currentText(),
                    self.comboBoxNS_4MN_910_Swallowing.currentText(),
                    self.comboBoxNS_4MN_910_Food.currentText(),
                    self.comboBoxNS_4MN_910_Dysarthria.currentText(),
                    self.comboBoxNS_4MN_910_Dysarthria_power.currentText(),
                    self.comboBoxNS_4MN_11.currentText(),
                    self.comboBoxNS_4MN_12.currentText(),
                    self.comboBoxNS_Moving_limbs.currentText(),
                    self.comboBoxNS_Moving_joints.currentText(),
                    self.comboBoxNS_Moving_spine.currentText(),
                    self.comboBoxNS_MRC_R_A_P.currentText(),
                    self.comboBoxNS_MRC_R_A_D.currentText(),
                    self.comboBoxNS_MRC_R_L_P.currentText(),
                    self.comboBoxNS_MRC_R_L_D.currentText(),
                    self.comboBoxNS_MRC_L_A_P.currentText(),
                    self.comboBoxNS_MRC_L_A_D.currentText(),
                    self.comboBoxNS_MRC_L_L_P.currentText(),
                    self.comboBoxNS_MRC_L_L_D.currentText(),
                    self.comboBoxNS_MuscleTonus_1.currentText(),
                    self.comboBoxNS_MuscleTonus_2.currentText(),
                    self.comboBoxNS_Ash_R_A_P.currentText(),
                    self.comboBoxNS_Ash_R_A_D.currentText(),
                    self.comboBoxNS_Ash_R_L_P.currentText(),
                    self.comboBoxNS_Ash_R_L_D.currentText(),
                    self.comboBoxNS_Ash_L_A_P.currentText(),
                    self.comboBoxNS_Ash_L_A_D.currentText(),
                    self.comboBoxNS_Ash_L_L_P.currentText(),
                    self.comboBoxNS_Ash_L_L_D.currentText(),
                    self.comboBoxNS_Arms_reflex_1.currentText(),
                    self.comboBoxNS_Arms_reflex_2.currentText(),
                    self.comboBoxNS_Legs_reflex_1.currentText(),
                    self.comboBoxNS_Legs_reflex_2.currentText(),
                    self.comboBoxNS_Pathology_reflex.currentText(),
                    self.comboBoxNS_MuscleTrofic.currentText(),
                    self.comboBoxNS_Sensitivity_1.currentText(),
                    self.comboBoxNS_Sensitivity_2.currentText(),
                    self.plainTextEditNS_Sensitivity.toPlainText(),
                    self.comboBoxNS_Coordination_1.currentText(),
                    self.comboBoxNS_Coordination_2.currentText(),
                    self.plainTextEditNS_Coordination.toPlainText(),
                    self.comboBoxNS_Extrapyramid_1.currentText(),
                    self.comboBoxNS_Extrapyramid_2.currentText(),
                    self.comboBoxNS_Extrapyramid_3.currentText(),
                    self.comboBoxNS_EpilepticStatus.currentText(),
                    self.comboBoxNS_FuncStatus_common.currentText(),
                    self.comboBoxNS_FuncStatus_walking.currentText(),
                    self.comboBoxNS_FuncStatus_walking_type.currentText(),
                    self.comboBoxNS_FuncStatus_motorics.currentText(),
                    self.comboBoxNS_FuncStatus_dressing.currentText(),
                    self.comboBoxNS_FuncStatus_stairway.currentText(),
                    self.comboBoxNS_FuncStatus_eating.currentText(),
                    self.comboBoxNS_FuncStatus_writing.currentText(),
                    self.comboBoxNS_FuncStatus_reading.currentText(),
                    self.plainTextEditNS_FuncStatus.toPlainText(),
                    self.plainTextEditNS_other.toPlainText(),
                    self.lineEdit_new_template_name.text()
                )
                # обновляем шаблон
                update_neur_template_db(template_new)
        else:
            # имя шаблона пустое
            pass

        self.lineEdit_new_template_name.setText('')
        self.templates_list = read_db_neur_template_list()
        self.comboBoxNeuralStTemplate.clear()
        if len(self.templates_list) <= 1:
            self.comboBoxNeuralStTemplate.addItem(self.templates_list[0])
        else:
            self.comboBoxNeuralStTemplate.addItems(self.templates_list)

    def push_active_template(self):
        '''
        '''
        template_name = self.comboBoxNeuralStTemplate.currentText()
        # читаем данные шаблона по имени
        tpl = read_db_neur_template_data([template_name])
        if tpl is None:
            pass
        else:
            # вставляем полученные данные в нужные ячейки
            self.comboBoxNS_Conscious.setCurrentText(tpl[0])
            self.comboBoxNS_GCS.setCurrentText(tpl[1])
            self.comboBoxNS_RASS.setCurrentText(tpl[2])
            self.comboBoxNS_Contact.setCurrentText(tpl[3])
            self.comboBoxNS_Orientation.setCurrentText(tpl[4])
            self.comboBoxNS_MeningealSymp_1.setCurrentText(tpl[5])
            self.comboBoxNS_MeningealSymp_2.setCurrentText(tpl[6])
            self.comboBoxNS_MeningealSymp_3.setCurrentText(tpl[7])
            self.comboBoxNS_Speech_1.setCurrentText(tpl[8])
            self.comboBoxNS_Speech_2.setCurrentText(tpl[9])
            self.comboBoxNS_Speech_3.setCurrentText(tpl[10])
            self.comboBoxNS_PelvicFuntion.setCurrentText(tpl[11])
            self.comboBoxNS_4MN_1_Smell.setCurrentText(tpl[12])
            self.comboBoxNS_4MN_2_VisualAcuity.setCurrentText(tpl[13])
            self.comboBoxNS_4MN_2_Fields.setCurrentText(tpl[14])
            self.comboBoxNS_4MN_2_Pupils.setCurrentText(tpl[15])
            self.comboBoxNS_4MN_2_Accomodation.setCurrentText(tpl[16])
            self.comboBoxNS_4MN_2_Photoreaction.setCurrentText(tpl[17])
            self.comboBoxNS_4MN_2_Convergension.setCurrentText(tpl[18])
            self.comboBoxNS_4MN_346_EyeballMove.setCurrentText(tpl[19])
            self.comboBoxNS_4MN_346_EyeballParesis.setCurrentText(tpl[20])
            self.comboBoxNS_4MN_346_Ptosis.setCurrentText(tpl[21])
            self.comboBoxNS_4MN_346_Nystagmus.setCurrentText(tpl[22])
            self.comboBoxNS_4MN_5_FaceSensitivity.setCurrentText(tpl[23])
            self.comboBoxNS_4MN_5_Branches.setCurrentText(tpl[24])
            self.comboBoxNS_4MN_5_Zelder.setCurrentText(tpl[25])
            self.comboBoxNS_4MN_7_Symmetry.setCurrentText(tpl[26])
            self.comboBoxNS_4MN_7_Other.setCurrentText(tpl[27])
            self.comboBoxNS_4MN_8_Hearing.setCurrentText(tpl[28])
            self.comboBoxNS_4MN_8_CentralVertigo.setCurrentText(tpl[29])
            self.comboBoxNS_4MN_910_Phonation.setCurrentText(tpl[30])
            self.comboBoxNS_4MN_910_SoftPalate.setCurrentText(tpl[31])
            self.comboBoxNS_4MN_910_Swallowing.setCurrentText(tpl[32])
            self.comboBoxNS_4MN_910_Food.setCurrentText(tpl[33])
            self.comboBoxNS_4MN_910_Dysarthria.setCurrentText(tpl[34])
            self.comboBoxNS_4MN_910_Dysarthria_power.setCurrentText(tpl[35])
            self.comboBoxNS_4MN_11.setCurrentText(tpl[36])
            self.comboBoxNS_4MN_12.setCurrentText(tpl[37])
            self.comboBoxNS_Moving_limbs.setCurrentText(tpl[38])
            self.comboBoxNS_Moving_joints.setCurrentText(tpl[39])
            self.comboBoxNS_Moving_spine.setCurrentText(tpl[40])
            self.comboBoxNS_MRC_R_A_P.setCurrentText(tpl[41])
            self.comboBoxNS_MRC_R_A_D.setCurrentText(tpl[42])
            self.comboBoxNS_MRC_R_L_P.setCurrentText(tpl[43])
            self.comboBoxNS_MRC_R_L_D.setCurrentText(tpl[44])
            self.comboBoxNS_MRC_L_A_P.setCurrentText(tpl[45])
            self.comboBoxNS_MRC_L_A_D.setCurrentText(tpl[46])
            self.comboBoxNS_MRC_L_L_P.setCurrentText(tpl[47])
            self.comboBoxNS_MRC_L_L_D.setCurrentText(tpl[48])
            self.comboBoxNS_MuscleTonus_1.setCurrentText(tpl[49])
            self.comboBoxNS_MuscleTonus_2.setCurrentText(tpl[50])
            self.comboBoxNS_Ash_R_A_P.setCurrentText(tpl[51])
            self.comboBoxNS_Ash_R_A_D.setCurrentText(tpl[52])
            self.comboBoxNS_Ash_R_L_P.setCurrentText(tpl[53])
            self.comboBoxNS_Ash_R_L_D.setCurrentText(tpl[54])
            self.comboBoxNS_Ash_L_A_P.setCurrentText(tpl[55])
            self.comboBoxNS_Ash_L_A_D.setCurrentText(tpl[56])
            self.comboBoxNS_Ash_L_L_P.setCurrentText(tpl[57])
            self.comboBoxNS_Ash_L_L_D.setCurrentText(tpl[58])
            self.comboBoxNS_Arms_reflex_1.setCurrentText(tpl[59])
            self.comboBoxNS_Arms_reflex_2.setCurrentText(tpl[60])
            self.comboBoxNS_Legs_reflex_1.setCurrentText(tpl[61])
            self.comboBoxNS_Legs_reflex_2.setCurrentText(tpl[62])
            self.comboBoxNS_Pathology_reflex.setCurrentText(tpl[63])
            self.comboBoxNS_MuscleTrofic.setCurrentText(tpl[64])
            self.comboBoxNS_Sensitivity_1.setCurrentText(tpl[65])
            self.comboBoxNS_Sensitivity_2.setCurrentText(tpl[66])
            self.plainTextEditNS_Sensitivity.setPlainText(tpl[67])
            self.comboBoxNS_Coordination_1.setCurrentText(tpl[68])
            self.comboBoxNS_Coordination_2.setCurrentText(tpl[69])
            self.plainTextEditNS_Coordination.setPlainText(tpl[70])
            self.comboBoxNS_Extrapyramid_1.setCurrentText(tpl[71])
            self.comboBoxNS_Extrapyramid_2.setCurrentText(tpl[72])
            self.comboBoxNS_Extrapyramid_3.setCurrentText(tpl[73])
            self.comboBoxNS_EpilepticStatus.setCurrentText(tpl[74])
            self.comboBoxNS_FuncStatus_common.setCurrentText(tpl[75])
            self.comboBoxNS_FuncStatus_walking.setCurrentText(tpl[76])
            self.comboBoxNS_FuncStatus_walking_type.setCurrentText(tpl[77])
            self.comboBoxNS_FuncStatus_motorics.setCurrentText(tpl[78])
            self.comboBoxNS_FuncStatus_dressing.setCurrentText(tpl[79])
            self.comboBoxNS_FuncStatus_stairway.setCurrentText(tpl[80])
            self.comboBoxNS_FuncStatus_eating.setCurrentText(tpl[81])
            self.comboBoxNS_FuncStatus_writing.setCurrentText(tpl[82])
            self.comboBoxNS_FuncStatus_reading.setCurrentText(tpl[83])
            self.plainTextEditNS_FuncStatus.setPlainText(tpl[84])
            self.plainTextEditNS_other.setPlainText(tpl[85])
