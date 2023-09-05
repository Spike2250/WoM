import ast
from PySide6 import QtWidgets
from PySide6.QtWidgets import QPushButton

from wom.GUI.PY.omr import omr_PatientCard
from wom.app_logic.writing.postprocessing.passport import update_patient_info
from wom.app_logic.writing.diaries.gen import creating_diaries
from wom.app_logic.worklist_data_processing import refresh_worklist_data
from wom.app_logic.create_docs import (list_created_docs,
                                       open_folder_with_files,
                                       creating_documents
                                       )
from wom.app_logic.db_func.db_omr import write_all_data_to_db_omr
from wom.app_logic.db_func.bucket_func import upload_history_to_yandex_cloud_bucket  # noqa: E501
from wom.styles_qss.main_styles import (style_true_button as style_True,
                                        button_other,
                                        label_style_diabet,
                                        label_style_b20,
                                        label_style_act,
                                        label_style_dis,
                                        label_style_ln)


# Окно карты пациента
class Ui_PatientCard(QtWidgets.QWidget,
                     omr_PatientCard.Ui_omr_patient_card):
    def __init__(self, user_info, windows, main_win, dictionary):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.user_info = user_info
        self.windows = windows
        self.main_win = main_win
        self.d = dictionary

        # self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки

        msg = "World of Medicine - Отделение медицинской "\
              "реабилитации - Медицинская карта пациента"
        main_win.setWindowTitle(msg)
        objectTitleBar = main_win.titleBar
        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

        self.set_connections()
        self.update_descriptions()

        self.check_data_blocks()
        self.check_created_docs()

        self.set_styles()

        self.create_diaries_table()
        self.update_diaries_table()

        # проверяем возможности словаря
        # - полноту для создания документов
        self.check_possible()

    def onButtonMy(self):
        pass

    def set_connections(self):
        # коннекты для кнопок
        self.pushButtonOpenPtPassportData\
            .clicked.connect(self.open_passport_data_window)
        self.pushButtonOpenPtNeuralStatusAdm\
            .clicked.connect(self.open_neurology_status_admission)
        self.pushButtonOpenPtObjStatusAdm\
            .clicked.connect(self.open_objective_status_admission)
        self.pushButtonOpenPtDiagnosisAdm\
            .clicked.connect(self.open_diagnosis_admission)
        self.pushButtonOpenPtObjStatusDischarge\
            .clicked.connect(self.open_objective_status_discharge)
        self.pushButtonOpenPtNeuralStatusDischarge\
            .clicked.connect(self.open_neurology_status_discharge)
        self.pushButtonOpenPtDiagnosisDischarge\
            .clicked.connect(self.open_diagnosis_discharge)
        self.pushButtonOpenPtStatisticData\
            .clicked.connect(self.open_discharge_details)
        self.pushButtonOpenPtAppointments\
            .clicked.connect(self.open_medical_appointments)
        self.pushButtonOpen_mdrk\
            .clicked.connect(self.open_mdrk)
        self.pushButtonOpen_icf\
            .clicked.connect(self.open_icf)
        self.pushButtonOpen_dynamic\
            .clicked.connect(self.open_dynamic)
        self.pushButton_lecalo\
            .clicked.connect(self.put_a_ticks)
        self.pushButton_clean_ticks\
            .clicked.connect(self.clean_ticks)
        self.pushButtonOpenFolder\
            .clicked.connect(self.open_folder)
        self.pushButtonOpenPtLaboratoryData\
            .clicked.connect(self.open_lab_data)
        self.pushButtonOpenPtInstrumentalData\
            .clicked.connect(self.open_instr_data)
        self.pushButtonOpenPtConsultationData\
            .clicked.connect(self.open_consult)
        self.pushButtonOpenPtDischargeRecommend\
            .clicked.connect(self.open_recommends)
        self.pushButtonCreateDocument\
            .clicked.connect(self.create_docs)
        self.pushButtonSaveExit\
            .clicked.connect(self.save_and_close_card)
        self.pushButtonNotSaveExit\
            .clicked.connect(self.close_card)
        self.pushButton_create_diaries\
            .clicked.connect(self.create_diaries)
        self.pushButtonAddEvent\
            .clicked.connect(self.add_new_event)
        self.pushButton_2\
            .clicked.connect(self.print_keys_from_d)
        self.pushButtonOpenLogs\
            .clicked.connect(self.open_logs)
        self.pushButtonSave\
            .clicked.connect(self.save_history)
        self.pushButton_save_diary\
            .clicked.connect(self.save_diary)
        self.pushButton_close_diary\
            .clicked.connect(self.close_diary)

        self.checkBox_doc_complex\
            .stateChanged.connect(self.complex_doc_change)
        self.checkBox_not_save\
            .stateChanged.connect(self.activate_button)

    def update_descriptions(self):
        # обновляем "Лого_ИБ" и "patient_info"
        update_patient_info(self.d)
        # меняем подпись истории болезни данными из словаря
        self.ptFullNameCard.setText(self.d['Лого_ИБ'])
        self.label_unic_number.setText(self.d['unic_number'])
        self.label_type_hospitalisation.setText(self.d['тип_стационара'])

    def create_diaries_table(self):
        self.tableWidget_diaries.verticalHeader().hide()
        self.tableWidget_diaries.setColumnWidth(0, 300)  # ширина колонок

    def create_main_window(self):
        return self.windows['Frameless']()

    def create_window(self, main_win, folder_name, win_name, timeline):
        match folder_name:
            case 'common':
                if timeline is not None:
                    w = self.windows[folder_name][win_name](
                        user_info=self.user_info,
                        windows=self.windows,
                        main_win=main_win,
                        dictionary=self.d,
                        case_type='omr',
                        timeline=timeline)
                else:
                    w = self.windows[folder_name][win_name](
                        user_info=self.user_info,
                        windows=self.windows,
                        main_win=main_win,
                        dictionary=self.d,
                        case_type='omr')
            case 'omr':
                if timeline is not None:
                    w = self.windows[folder_name][win_name](
                        user_info=self.user_info,
                        windows=self.windows,
                        main_win=main_win,
                        dictionary=self.d,
                        timeline=timeline)
                else:
                    w = self.windows[folder_name][win_name](
                        user_info=self.user_info,
                        windows=self.windows,
                        main_win=main_win,
                        dictionary=self.d)
        return w

    def open_window(self, folder_name, win_name, timeline=None):
        win = self.create_main_window()
        win.setWidget(self.create_window(win, folder_name, win_name, timeline))
        win.show()
        self.main_win.close()

    def show_dairy(self):
        # определяем индекс дневника
        button = self.sender()
        index = self.tableWidget_diaries.indexAt(button.pos()).row()

        self.label_diary_index.setText(str(index + 1))

        self.plainTextEdit_diary.setEnabled(True)
        self.pushButton_save_diary.setEnabled(True)
        self.pushButton_close_diary.setEnabled(True)

        # если список дневников строка (после чтения json)
        if isinstance(self.d['дневники_табл'], str):
            # делаем из строки - список кортежей обратно
            self.d['дневники_табл'] = ast.literal_eval(self.d['дневники_табл'])
        # если это список ВАШ
        if self.d['дневники_табл'][index][1] == 'Динамика ВАШ':
            self.plainTextEdit_diary.setPlainText(self.d['ВАШ_список'])
        else:
            # заполняем текст дневника
            self.plainTextEdit_diary.setPlainText(
                self.d[f'дневник_текст_{index + 1}'])

    def save_diary(self):
        index = int(self.label_diary_index.text())

        if self.d['наличие_боли']:
            # если обновлен список ВАШ
            if index == len(self.d['дневники_табл']):
                self.d['ВАШ_список'] = self.plainTextEdit_diary.toPlainText()
            else:  # если дневниковая запись
                self.d[f'дневник_текст_{index}'] =\
                    self.plainTextEdit_diary.toPlainText()

            diaries_text = ''
            for j in range(len(self.d['дневники_табл']) - 1):  # !важные "-1"
                diaries_text += self.d[f'дневник_текст_{j + 1}']
            diaries_text += self.d['ВАШ_список']
        else:
            self.d[f'дневник_текст_{index}'] =\
                self.plainTextEdit_diary.toPlainText()
            diaries_text = ''
            for j in range(len(self.d['дневники_табл'])):
                diaries_text += self.d[f'дневник_текст_{j + 1}']
        self.d['дневник_текст_все'] = diaries_text[2:]

        self.close_diary()

        msg = f'"{self.d["дневники_табл"][index - 1][0]} - '\
              f'{self.d["дневники_табл"][index - 1][1]}" - '\
              f'успешно пересохранен'
        self.label_status.setText(msg)

    def close_diary(self):
        self.plainTextEdit_diary.setPlainText('')
        self.label_diary_index.setText('')
        self.plainTextEdit_diary.setEnabled(False)
        self.pushButton_save_diary.setEnabled(False)
        self.pushButton_close_diary.setEnabled(False)

    def activate_button(self):
        if self.checkBox_not_save.isChecked():
            self.pushButtonNotSaveExit.setEnabled(True)
        else:
            self.pushButtonNotSaveExit.setEnabled(False)

    def close_card(self):
        win = self.create_main_window()
        win.setWidget(
            self.windows['omr']['main_menu'](
                user_info=self.user_info,
                windows=self.windows,
                main_win=win))
        win.show()
        self.main_win.close()

    def save_and_close_card(self):
        self.save_history()
        self.close_card()

    def open_passport_data_window(self):
        self.open_window(folder_name='common',
                         win_name='passport')

    def open_objective_status_admission(self):
        self.open_window(folder_name='common',
                         win_name='obj_status_adm')

    def open_objective_status_discharge(self):
        if 'Соматический_статус' in self.d:
            self.open_window(folder_name='common',
                             win_name='obj_status_dis')
        else:
            status_message = f'Сначала введите данные соматического '\
                             f'статуса при поступлении.\n'\
                             f'Данные для выписки будут доступны после '\
                             f'выполнения этого действия.'
            self.label_status.setText(status_message)

    def open_neurology_status_admission(self):
        self.open_window(folder_name='common',
                         win_name='neur_status',
                         timeline='adm')

    def open_neurology_status_discharge(self):
        if 'Неврологический_статус' in self.d:
            self.open_window(folder_name='common',
                             win_name='neur_status',
                             timeline='dis')
        else:
            status_message = f'Сначала введите данные неврологического '\
                             f'статуса при поступлении.\n'\
                             f'Данные для выписки будут доступны после '\
                             f'выполнения этого действия.'
            self.label_status.setText(status_message)

    def open_diagnosis_admission(self):
        self.open_window(folder_name='common',
                         win_name='diagnosis',
                         timeline='adm')

    def open_diagnosis_discharge(self):
        if 'Основной_диагноз' in self.d:
            self.open_window(folder_name='common',
                             win_name='diagnosis',
                             timeline='dis')
        else:
            status_message = f'Сначала введите данные клинического '\
                             f'диагноза при поступлении.\n'\
                             f'Данные для выписки будут доступны после '\
                             f'выполнения этого действия.'
            self.label_status.setText(status_message)

    def open_discharge_details(self):
        self.open_window(folder_name='common',
                         win_name='dis_details')

    def open_medical_appointments(self):
        self.open_window(folder_name='omr',
                         win_name='appointments')

    def open_mdrk(self):
        self.open_window(folder_name='omr',
                         win_name='mdrk')

    def open_icf(self):
        self.open_window(folder_name='common',
                         win_name='icf',
                         timeline='frm')  # speciality

    def open_dynamic(self):
        self.open_window(folder_name='omr',
                         win_name='dynamic')

    def open_lab_data(self):
        self.open_window(folder_name='common',
                         win_name='lab_data')

    def open_instr_data(self):
        # self.open_window(folder_name='common',
        #                  win_name='instr_data')
        status_message = f'Раздел "Данные инструментальных '\
                         f'исследований" находится в разработке. '
        self.label_status.setText(status_message)

    def open_consult(self):
        # self.open_window(folder_name='common',
        #                  win_name='consult')
        status_message = f'Раздел "Консультации" '\
                         f'находится в разработке. '
        self.label_status.setText(status_message)

    def open_recommends(self):
        # self.open_window(folder_name='omr',
        #                  win_name='recommends')
        status_message = f'Раздел "Рекомендации для выписки" '\
                         f'находится в разработке. '
        self.label_status.setText(status_message)

    # функции для "галочек"
    def put_a_ticks(self):
        '''
        выставление "стандартных" галочек для создания документов для истории
        болезни (стат.талон для выписки; дополнение к стат.талону; дневники,
        шкалы, МКФ - одним файлом; выписной эпикриз)
        '''
        if self.checkBox_doc_statistic_talon.isEnabled():
            self.checkBox_doc_statistic_talon.setChecked(True)
        if self.checkBox_doc_statistic_talon_other.isEnabled():
            self.checkBox_doc_statistic_talon_other.setChecked(True)
        if self.checkBox_doc_complex.isEnabled():
            self.checkBox_doc_complex.setChecked(True)
        if self.checkBox_doc_discharge_summary.isEnabled():
            self.checkBox_doc_discharge_summary.setChecked(True)

    def clean_ticks(self):
        '''снятие всех галочек для создания документов'''
        self.checkBox_doc_initial_inspection.setChecked(False)
        self.checkBox_doc_appointments.setChecked(False)
        self.checkBox_doc_statistic_talon_face.setChecked(False)
        self.checkBox_doc_statistic_talon.setChecked(False)
        self.checkBox_doc_statistic_talon_other.setChecked(False)
        self.checkBox_doc_med_commission_1.setChecked(False)
        self.checkBox_doc_med_commission_2.setChecked(False)
        self.checkBox_doc_med_commission_dis.setChecked(False)
        self.checkBox_doc_med_commission_drugs.setChecked(False)
        self.checkBox_doc_diaries.setChecked(False)
        self.checkBox_doc_scale.setChecked(False)
        self.checkBox_doc_final_diary.setChecked(False)
        self.checkBox_doc_ICF.setChecked(False)
        self.checkBox_doc_complex.setChecked(False)
        self.checkBox_doc_discharge_summary.setChecked(False)
        self.checkBox_doc_additional_recommendations.setChecked(False)
        self.checkBox_doc_directions.setChecked(False)
        self.checkBox_doc_consents.setChecked(False)
        self.checkBox_doc_reference.setChecked(False)
        self.checkBox_doc_frontpage.setChecked(False)
        self.checkBox_doc_back_frontpage.setChecked(False)
        self.checkBox_doc_pass.setChecked(False)
        self.checkBox_doc_consultation.setChecked(False)
        self.checkBox_doc_full_history.setChecked(False)
        self.checkBox_doc_refusal.setChecked(False)

    def complex_doc_change(self):
        if self.checkBox_doc_complex.isChecked():
            self.checkBox_doc_diaries.setChecked(True)
            self.checkBox_doc_scale.setChecked(True)
            self.checkBox_doc_final_diary.setChecked(True)
            self.checkBox_doc_ICF.setChecked(True)
        else:
            self.checkBox_doc_diaries.setChecked(False)
            self.checkBox_doc_scale.setChecked(False)
            self.checkBox_doc_final_diary.setChecked(False)
            self.checkBox_doc_ICF.setChecked(False)

    def check_possible(self):
        '''
        self.check_list[0] - 'ФИО_пациента'
        self.check_list[1] - 'Соматический_статус'
        self.check_list[2] - 'Неврологический_статус'
        self.check_list[3] - 'Основной_диагноз'
        self.check_list[4] - 'лечение_таблетки'
        self.check_list[5] - 's_domen_1'
        self.check_list[6] - 'лабораторные_данные'
        self.check_list[7] - 'инструментальные_данные'
        self.check_list[8] - 'консультации_данные'
        self.check_list[9] - 'Соматический_статус_выписка'
        self.check_list[10] - 'Неврологический_статус_вып'
        self.check_list[11] - 'Основной_диагноз_вып'
        self.check_list[12] - 's_domen_dis_1'
        self.check_list[13] - 'вид_выбытия'
        self.check_list[14] - 'рекомендации_выписка'

        '''
        if all((self.check_list[1],
                self.check_list[2],
                self.check_list[3])):
            self.checkBox_doc_initial_inspection.setEnabled(True)
        else:
            self.checkBox_doc_initial_inspection.setEnabled(False)
        # лист назначений
        if self.check_list[4]:
            self.checkBox_doc_appointments.setEnabled(True)
        else:
            self.checkBox_doc_appointments.setEnabled(False)
        # стат.талон 1 стр.
        # if self.check_list[0]:
        #     self.checkBox_doc_statistic_talon_face.setEnabled(True)
        # else:
        #     self.checkBox_doc_statistic_talon_face.setEnabled(False)
        # стат.талон 2 стр. и справка по месте требования
        if (self.check_list[13]):
            self.checkBox_doc_statistic_talon.setEnabled(True)
            self.checkBox_doc_reference.setEnabled(True)
        else:
            self.checkBox_doc_statistic_talon.setEnabled(False)
            self.checkBox_doc_reference.setEnabled(False)
        # дополниение к стат.талону и шкалы
        if all((self.check_list[2],
                self.check_list[3],
                self.check_list[10],
                self.check_list[11])):
            self.checkBox_doc_statistic_talon_other.setEnabled(True)
            self.checkBox_doc_scale.setEnabled(True)
        else:
            self.checkBox_doc_statistic_talon_other.setEnabled(False)
            self.checkBox_doc_scale.setEnabled(False)
        # ВК по ЛН # 1
        if all((self.check_list[1],
                self.check_list[2],
                self.check_list[3],
                self.d['нужда_в_ЛН'])):
            self.checkBox_doc_med_commission_1.setEnabled(True)
        else:
            self.checkBox_doc_med_commission_1.setEnabled(False)
        # ВК по ЛН # 2
        if all((self.check_list[1],
                self.check_list[10],
                self.check_list[11],
                self.d['нужда_в_ЛН'])):
            self.checkBox_doc_med_commission_2.setEnabled(True)
            self.checkBox_doc_med_commission_dis.setEnabled(True)
        else:
            self.checkBox_doc_med_commission_2.setEnabled(False)
            self.checkBox_doc_med_commission_dis.setEnabled(False)
        # ВК по лекарствам
        # if
        #     self.checkBox_doc_med_commission_drugs.setEnabled(True)
        # else:
        #     self.checkBox_doc_med_commission_drugs.setEnabled(False)
        # Дневники и комплексный документ
        if 'дневники_табл' in self.d:
            self.checkBox_doc_diaries.setEnabled(True)
            self.checkBox_doc_complex.setEnabled(True)
        else:
            self.checkBox_doc_diaries.setEnabled(False)
            self.checkBox_doc_complex.setEnabled(False)
        # Итоговый дневник
        if all((self.check_list[9],
                self.check_list[10],
                self.check_list[11],
                self.check_list[12])):
            self.checkBox_doc_final_diary.setEnabled(True)
        else:
            self.checkBox_doc_final_diary.setEnabled(False)
        # МКФ
        if all((self.check_list[5],
                self.check_list[12])):
            self.checkBox_doc_ICF.setEnabled(True)
        else:
            self.checkBox_doc_ICF.setEnabled(False)
        # выписной эпикриз
        if all((self.check_list[4],
                self.check_list[10],
                self.check_list[11],
                self.check_list[13])):
            self.checkBox_doc_discharge_summary.setEnabled(True)
        else:
            self.checkBox_doc_discharge_summary.setEnabled(False)

        #     self.checkBox_doc_additional_recommendations.setEnabled(True)

        #     self.checkBox_doc_additional_recommendations.setEnabled(False)

        #     self.checkBox_doc_directions.setEnabled(True)

        #     self.checkBox_doc_directions.setEnabled(False)
        # согласия и пропуск
        if self.check_list[0]:
            self.checkBox_doc_consents.setEnabled(True)
            self.checkBox_doc_pass.setEnabled(True)
            # лицевая сторона обложки
            # if (d['паспорт'], d['полис_ОМС']) != '':
            #     self.checkBox_doc_frontpage.setEnabled(True)
            # else:
            #     self.checkBox_doc_frontpage.setEnabled(False)
        # оборотная сторона обложки
        if all((self.check_list[13],
                self.check_list[11])):
            self.checkBox_doc_back_frontpage.setEnabled(True)
        else:
            self.checkBox_doc_back_frontpage.setEnabled(False)

        #     self.checkBox_doc_consultation.setEnabled(True)

        #     self.checkBox_doc_consultation.setEnabled(False)

        #     self.checkBox_doc_full_history.setEnabled(True)

        #     self.checkBox_doc_full_history.setEnabled(False)

        # отказ от госпитализации
        if self.check_list[11]:
            self.checkBox_doc_refusal.setEnabled(True)
        else:
            self.checkBox_doc_refusal.setEnabled(False)

    #
    def open_folder(self):
        if 'созданные_документы' not in self.d:
            self.textBrowser.setText('Не создано ни одного документа!')
        else:
            self.textBrowser.setText(
                list_created_docs(self.d['созданные_документы']))
            try:
                open_folder_with_files(self.d)
            except FileNotFoundError:
                status_message = f'Созданные документы не обнаружены. '\
                                 f'Скорее всего они были созданы '\
                                 f'на другом компьютере и хранятся локально.'
                self.label_status.setText(status_message)

    def create_a_list_of_templates(self):
        templates = []
        if self.checkBox_doc_initial_inspection.isChecked():
            templates.append('Первичный осмотр')
        if self.checkBox_doc_appointments.isChecked():
            templates.append('Лист назначений')
        if self.checkBox_doc_statistic_talon_face.isChecked():
            templates.append('Стат.талон - 1 стр') #
        if self.checkBox_doc_statistic_talon.isChecked():
            templates.append('Стат.талон - 2 стр')
            templates.append('Стат.талон - 2 стр (530н)')
        if self.checkBox_doc_statistic_talon_other.isChecked():
            templates.append('Стат.талон - дополнение')
        if self.checkBox_doc_med_commission_1.isChecked():
            templates.append('ВК_продление_ЛН')
        if self.checkBox_doc_med_commission_2.isChecked():
            templates.append('ВК_продление_ЛН_2')
        if self.checkBox_doc_med_commission_dis.isChecked():
            templates.append('ВК_продление_ЛН_выписка')
        if self.checkBox_doc_med_commission_drugs.isChecked():
            templates.append('ВК_лекарства') #
        if self.checkBox_doc_discharge_summary.isChecked():
            templates.append('Выписной эпикриз')
        if self.checkBox_doc_additional_recommendations.isChecked():
            templates.append('Доп.рекомендации') #
        if self.checkBox_doc_directions.isChecked():
            templates.append('Направления') #
        if self.checkBox_doc_consents.isChecked():
            templates.append('Согласия')
        if self.checkBox_doc_frontpage.isChecked():
            templates.append('Обложка ИБ') #
        if self.checkBox_doc_back_frontpage.isChecked():
            templates.append('Оборот обложки ИБ')
        if self.checkBox_doc_pass.isChecked():
            templates.append('Пропуск_для_посещения')
        if self.checkBox_doc_consultation.isChecked():
            templates.append('Доп.консультация') #
        if self.checkBox_doc_full_history.isChecked():
            templates.append('Вся история болезни') #
        if self.checkBox_doc_reference.isChecked():
            templates.append('Справка')
        if self.checkBox_doc_refusal.isChecked():
            templates.append('Отказ_от_госпитализации')

        if self.checkBox_doc_complex.isChecked():
            templates.append('Шкалы, дневники, МКФ')
        else:
            if self.checkBox_doc_diaries.isChecked():
                templates.append('Дневники') #
            if self.checkBox_doc_final_diary.isChecked():
                templates.append('Итоговый осмотр') #
            if self.checkBox_doc_scale.isChecked():
                templates.append('Шкалы')
            if self.checkBox_doc_ICF.isChecked():
                templates.append('МКФ')

        if templates == []:
            return ['test']
        else:
            return templates

    def create_docs(self):
        templates = self.create_a_list_of_templates()

        flags = ('ВК_продление_ЛН',
                 'ВК_продление_ЛН_2',
                 'ВК_продление_ЛН_выписка')
        for template in flags:
            if template in templates:
                refresh_worklist_data(self.d)

        creating_documents(self.d, templates)
        self.textBrowser.setText(
            list_created_docs(self.d['созданные_документы']))

    @upload_history_to_yandex_cloud_bucket('omr')
    def save_history(self):
        # записываем словарь в json-файл и обновляем БД
        write_all_data_to_db_omr(self.d)
        # выводим сообщение об успехе сохранения
        text = '\tИстория болезни успешно сохранена на сервере!'
        self.label_status.setText(text)

    def check_data_blocks(self):
        '''
        проверяет наличие блоков данных в словаре(d)
        при успешной проверке меняет цвет соответсвующей
        кнопки в карте пациента
        '''
        # формируем словарь с проверочными ключами и
        # присваиваем им соответвующие кнопки
        buttons_dict = {
            'ФИО_пациента': self.pushButtonOpenPtPassportData,
            'Соматический_статус': self.pushButtonOpenPtObjStatusAdm,
            'Неврологический_статус': self.pushButtonOpenPtNeuralStatusAdm,
            'Основной_диагноз': self.pushButtonOpenPtDiagnosisAdm,
            'icf_all': self.pushButtonOpen_icf,
            'лечение_таблетки': self.pushButtonOpenPtAppointments,
            'цели_реабилитации': self.pushButtonOpen_mdrk,
            'лабораторные_данные': self.pushButtonOpenPtLaboratoryData,
            'инструментальные_данные': self.pushButtonOpenPtInstrumentalData,
            'консультации_данные': self.pushButtonOpenPtConsultationData,
            'Соматический_статус_выписка': self.pushButtonOpenPtObjStatusDischarge,  # noqa: E501
            'Неврологический_статус_вып': self.pushButtonOpenPtNeuralStatusDischarge,  # noqa: E501
            'Основной_диагноз_вып': self.pushButtonOpenPtDiagnosisDischarge,
            'динамика_вып': self.pushButtonOpen_dynamic,
            'вид_выбытия': self.pushButtonOpenPtStatisticData,
            'рекомендации_выписка': self.pushButtonOpenPtDischargeRecommend
        }

        # Собираем чек лист для "галочек" и валидности создания документов
        self.check_list = []
        # проверяем наличие блоков данных по соответствующих ключам в словаре d
        for key in buttons_dict:
            if key in self.d:
                # меняем стиль соответствующей кнопки
                if self.d[key] != '':
                    buttons_dict[key].setStyleSheet(style_True)
                    self.check_list.append(True)
                else:
                    self.check_list.append(False)
            else:
                self.check_list.append(False)

        self.create_check_line()
        self.check_diaries_create_possible()
        self.check_data_label()

    def create_check_line(self):
        check_line = ''
        for check in self.check_list:
            if check:
                check_line += '1'
            else:
                check_line += '0'
        self.d['check_line'] = check_line

    def check_data_label(self):
        if self.d['нужда_в_ЛН']:
            self.label_LN.setText('= ЛН =')
            self.label_LN.setStyleSheet(label_style_ln)
        else:
            self.label_LN.setText('')
        if 'ВИЧ_чек' in self.d and self.d['ВИЧ_чек']:
            self.label_b20.setText('ВИЧ +')
            self.label_b20.setStyleSheet(label_style_b20)

        if 'ВГС_чек' in self.d and self.d['ВГС_чек']:
            self.label_hvc.setText('Гепатит С')
            self.label_hvc.setStyleSheet(label_style_b20)

        if 'СД_чек' in self.d and self.d['СД_чек']:
            self.label_diabet.setText('Сах.диабет')
            self.label_diabet.setStyleSheet(label_style_diabet)

        # обозначаем в истории, если пациент выписан
        if self.d['status_act']:
            text = f"Активный случай"
            self.label_dis_check.setText(text)
            self.label_dis_check.setStyleSheet(label_style_act)
        else:
            text = f"Пациент выписан {self.d['дата_выписки']}.\n"\
                   f"История находится в архиве."
            self.label_dis_check.setText(text)
            self.label_dis_check.setStyleSheet(label_style_dis)

    def check_diaries_create_possible(self):
        check_list = ('ФИО_пациента',
                      'Соматический_статус',
                      'Неврологический_статус',
                      'Основной_диагноз',
                      'лечение_таблетки',
                      'icf_all',
                      'Соматический_статус_выписка',
                      'Неврологический_статус_вып',
                      'Основной_диагноз_вып',
                      'динамика_вып',
                      'цели_реабилитации')

        success_checking = True
        for key in check_list:
            if key not in self.d:
                success_checking = False

        if success_checking:
            self.pushButton_create_diaries.setEnabled(True)

    def create_diaries(self):
        if self.radioButton_everyday.isChecked():
            creating_diaries(self.d, 'everyday')
        elif self.radioButton_3_times_in_week.isChecked():
            creating_diaries(self.d, '3timesWeek')
        elif self.radioButton_twice_in_day.isChecked():
            creating_diaries(self.d, 'twice_everyday')
        else:
            status_message = f'Создание дневников невозможно, '\
                             f'не выбран ни один из режимов написания.'
            self.label_status.setText(status_message)
        self.update_diaries_table()

        self.check_possible()

    def update_diaries_table(self):
        # проверяем, что данные есть
        if 'дневники_табл' in self.d:
            # меняем формат если это строка
            if isinstance(self.d['дневники_табл'], str):
                self.d['дневники_табл'] = ast.literal_eval(
                    self.d['дневники_табл'])
            # устанавливаем количество строк в таблице равное
            # количеству найденных случаев
            self.tableWidget_diaries.setRowCount(
                rows := len(self.d['дневники_табл']))
            # формируем "Item"s для каждой клетки таблицы
            for i in range(rows):
                button_name = f"{self.d['дневники_табл'][i][0]}"\
                              f" - {self.d['дневники_табл'][i][1]}"
                button = QPushButton(button_name)
                button.setStyleSheet(button_other)
                button.clicked.connect(self.show_dairy)
                self.tableWidget_diaries.setCellWidget(i, 0, button)

    def check_created_docs(self):
        if 'созданные_документы' in self.d:
            if isinstance(self.d['созданные_документы'], str):
                self.d['созданные_документы'] = ast.literal_eval(
                    self.d['созданные_документы'])
            self.textBrowser.setText(
                list_created_docs(self.d['созданные_документы']))
        else:
            self.textBrowser.setText('Пока не создано ни одного документа :(')

    def add_new_event(self):
        pass

    def print_keys_from_d(self):
        n = 0
        print('Ключи актуального словаря')
        for i in self.d:
            n += 1
            print(f'{n}) {i}')
        print(f'    Всего: {n}')

    def set_styles(self):
        pass

    def open_logs(self):
        pass
