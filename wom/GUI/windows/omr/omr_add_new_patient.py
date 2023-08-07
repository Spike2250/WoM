from PySide6 import QtWidgets, QtCore
from datetime import timedelta, datetime
from wom.GUI.PY.omr import omr_AddNewPatient
from wom.app_logic.service_func import (datedif, convert_date as c_date,
                                        create_mkb_nmu_dict, add_mkb10_nmu)
from wom.app_logic.db_func.db_omr import (DATABASE,
                                          read_d_from_db,
                                          read_db_active_cases,
                                          read_db_archive_cases,
                                          write_all_data_to_db,
                                          write_fullness_table,
                                          write_scale_table)
from wom.app_logic.db_func.bucket_func import (download_db_from_bucket,
                                               upload_db_to_bucket,
                                               upload_to_bucket,
                                               BUCKET_MAIN)
from wom.app_logic.create_docs import (creating_documents,
                                       open_folder_with_files)
from wom.app_logic.parsing import parse_promed
from wom.app_logic.writing.postprocessing.passport import update_after_passport_data  # noqa: E501


# Окно создания новой истории болезни
class Ui_AddNewPatient(QtWidgets.QWidget,
                       omr_AddNewPatient.Ui_PatientPassportData):
    def __init__(self, windows, main_win, dictionary):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.windows = windows
        self.main_win = main_win
        self.d = dictionary

        main_win.setWindowTitle('Тестовая строка заголовка')
        objectTitleBar = main_win.titleBar
        objectTitleBar.signalButtonMy.connect(self.onButtonMy)

        self.set_connections()
        self.add_values_to_popup_lists()
        self.tricks()
        self.show_uin_label()
        self.set_styles()

    def onButtonMy(self):
        # self.textEdit.append("Нажата `Своя Кнопка`!")
        pass

    def open_window(self, name):
        win = self.windows['Frameless']()
        win.setWidget(self.windows['omr'][name](
            windows=self.windows, main_win=win, dictionary=self.d))
        win.show()
        self.main_win.close()

    def back_to_main_menu(self):
        win = self.windows['Frameless']()
        win.setWidget(self.windows['omr']['main_menu'](
            windows=self.windows, main_win=win))
        win.show()
        self.main_win.close()

    def set_connections(self):
        #
        # self.plainTextEdit_descriptions.setEditable(False)
        # коннекты кнопок
        self.pushButtonCreateHistory.clicked.connect(self.create_history)
        self.pushButtonPrintConsent.clicked.connect(self.create_consent)
        self.pushButtonAddRelative.clicked.connect(self.add_patient_relative)
        self.pushButton_add_from_promed.clicked.connect(self.parse_promed_data)
        self.pushButtonBackToMenu.clicked.connect(self.back_to_main_menu)
        self.pushButton_today.clicked.connect(self.set_adm_date_today)
        #
        self.checkBoxPtNeedSickList\
            .stateChanged.connect(self.activate_first_ln_box)

    def activate_first_ln_box(self):
        if self.checkBoxPtNeedSickList.isChecked():
            self.checkBoxPtNeedSickList_2.setEnabled(True)
        else:
            self.checkBoxPtNeedSickList_2.setChecked(False)
            self.checkBoxPtNeedSickList_2.setEnabled(False)

    def add_values_to_popup_lists(self):
        # загружаем словари МКБ10 и НМУ
        self.mkb10, self.nmu = create_mkb_nmu_dict()
        # добавление значений в выплывающие списки
        self.comboBoxPtMKB10_main.clear()
        self.comboBoxPtMKB10_main.addItems(list(self.mkb10))
        self.comboBoxPtNMU_code.clear()
        self.comboBoxPtNMU_code.addItems(list(self.nmu))

    def tricks(self):
        # автозаполнение
        self.dateEditPtAdmissionDay.dateChanged.connect(
            self.change_DischargeDate_plan)
        self.dateEditPtAdmissionDay.dateChanged.connect(
            self.change_dis_info)
        self.comboBoxPtMKB10_main.currentTextChanged.connect(
            self.change_nmu)
        self.comboBoxPtRoomNumber.currentTextChanged.connect(
            self.change_doctor)
        self.comboBoxPtMKB10_main.currentTextChanged.connect(
            self.change_mkb_desc)
        self.comboBoxPtMKB10_main.currentTextChanged.connect(
            self.change_need_psylogo)
        self.comboBoxPtNMU_code.currentTextChanged.connect(
            self.change_nmu_desc)
        self.comboBoxTherapist.currentTextChanged.connect(
            self.change_button_color)
        self.dateEditDischargeDate_plan.dateChanged.connect(
            self.change_dis_info)

    def set_adm_date_today(self):
        today = datetime.now().strftime('%d.%m.%Y')
        self.dateEditPtAdmissionDay.setDate(
            QtCore.QDate.fromString(today, "dd.MM.yyyy"))

    def change_dis_info(self):
        adm_date = self.dateEditPtAdmissionDay\
            .dateTime().toString('dd.MM.yyyy')
        dis_date = self.dateEditDischargeDate_plan\
            .dateTime().toString('dd.MM.yyyy')
        typeHosp = self.comboBoxPtHoptitalisationType.currentText()

        if typeHosp in {'Круглосуточный стационар', 'БТ - круглосуточный'}:
            bed_days = datedif(adm_date, dis_date) - 1
        else:
            bed_days = datedif(adm_date, dis_date)
        dis_date = c_date(dis_date)

        text = f'   {dis_date.strftime("%A")} \t({bed_days} к/д)'
        self.label_discharge_info.setText(text)

    def show_uin_label(self):
        # написание UIN
        uin = f"Клиническому случаю будет присвоен "\
              f"UIN: {self.d['unic_number']}"
        self.label_unic_number.setText(uin)

    def change_nmu(self):
        '''
        '''
        mkb10_code = self.comboBoxPtMKB10_main.currentText()

        if mkb10_code in {'I69.0', 'I69.1',
                          'I69.2', 'I69.3',
                          'I69.4', 'I69.8',
                          'I69.9'}:
            self.comboBoxPtNMU_code.setCurrentText('B05.023.001')
        elif mkb10_code in {'M51.1', 'M51.0',
                            'M50.1', 'M50.0'}:
            self.comboBoxPtNMU_code.setCurrentText('B05.024.002')
        elif mkb10_code in {'U09.9'}:
            self.comboBoxPtNMU_code.setCurrentText('B05.070.001.011')
        elif mkb10_code in {'T91.3', 'T91.1'}:
            self.comboBoxPtNMU_code.setCurrentText('B05.024.001')
        elif mkb10_code in {'T90.5'}:
            self.comboBoxPtNMU_code.setCurrentText('B05.024.003')
        elif mkb10_code in {'G81.1', 'G82.1',
                            'G82.4'}:
            self.comboBoxPtNMU_code.setCurrentText('A25.24.001.002')
        elif mkb10_code in {'G61.0', 'G20'}:
            self.comboBoxPtNMU_code.setCurrentText('B05.023.002.002')
        elif mkb10_code in {'M24.5'}:
            self.comboBoxPtNMU_code.setCurrentText('B05.050.005')

    def change_doctor(self):
        '''
        '''
        room_number = self.comboBoxPtRoomNumber.currentText()

        if room_number in {'201', '202',
                           '205', '213',
                           '305'}:
            self.comboBoxTherapist.setCurrentText('Тыричев С.В.')
        elif room_number in {'209', '210',
                             '211', '212',
                             '301', '303',
                             '308A', '313'}:
            self.comboBoxTherapist.setCurrentText('Шадрин А.А.')
        elif room_number in {'208', '307',
                             '309', '310',
                             '311', '315'}:
            self.comboBoxTherapist.setCurrentText('Тимофеев А.П.')
        elif room_number in {'204', '206',
                             '302', '304',
                             '306', '308',
                             '312'}:
            self.comboBoxTherapist.setCurrentText('Шилов И.С.')

    def change_DischargeDate_plan(self):
        '''
        '''
        day_adm = c_date(
            self.dateEditPtAdmissionDay.dateTime().toString('dd.MM.yyyy'))
        week_day_adm = int(day_adm.strftime("%w"))
        # если пациент поступил в понедельник
        if week_day_adm in {1}:
            discharge_date_plan = day_adm + timedelta(14)
        # если пациент поступил во вторник
        elif week_day_adm in {2}:
            discharge_date_plan = day_adm + timedelta(13)
        # если пациент поступил в среду или пятницу
        elif week_day_adm in {3, 5}:
            discharge_date_plan = day_adm + timedelta(14)
        # если пациент поступил в четверг или субботу
        elif week_day_adm in {4, 6}:
            discharge_date_plan = day_adm + timedelta(13)
        # если пациент поступил в воскресение
        elif week_day_adm in {0}:
            discharge_date_plan = day_adm + timedelta(12)
        discharge_date_plan = discharge_date_plan.strftime("%d.%m.%Y")

        self.dateEditDischargeDate_plan.setDate(
            QtCore.QDate.fromString(discharge_date_plan, "dd.MM.yyyy"))

    def change_mkb_desc(self):
        cbox_text = self.comboBoxPtMKB10_main.currentText()
        if (cur_text := self.plainTextEdit_descriptions.toPlainText()) != '':
            cur_nmu = cur_text.split('\n')[1]
            self.plainTextEdit_descriptions.toPlainText()
            try:
                text = f'МКБ-10: {cbox_text} - '\
                       f'{self.mkb10[f"{cbox_text}"]}'\
                       f'\n{cur_nmu}'
                self.plainTextEdit_descriptions.setPlainText(text)
            except KeyError:
                text = f'МКБ-10: не определен'\
                       f'\n{cur_nmu}'
                self.plainTextEdit_descriptions.setPlainText(text)
        else:
            try:
                text = f'МКБ-10: {cbox_text} - {self.mkb10[f"{cbox_text}"]}\n'
                self.plainTextEdit_descriptions.setPlainText(text)
            except KeyError:
                text = f'МКБ-10: не определен\n'
                self.plainTextEdit_descriptions.setPlainText(text)

    def change_nmu_desc(self):
        cbox_text = self.comboBoxPtNMU_code.currentText()
        if (cur_text := self.plainTextEdit_descriptions.toPlainText()) != '':
            cur_mkb10 = cur_text.split('\n')[0]
            self.plainTextEdit_descriptions.toPlainText()
            try:
                text = f'{cur_mkb10}\n'\
                       f'НМУ: {cbox_text} - '\
                       f'{self.nmu[f"{cbox_text}"]}'
                self.plainTextEdit_descriptions.setPlainText(text)
            except KeyError:
                text = f'{cur_mkb10}\n'\
                       f'НМУ: не определен'
                self.plainTextEdit_descriptions.setPlainText(text)
        else:
            try:
                text = f'\nНМУ: {cbox_text} - {self.nmu[f"{cbox_text}"]}'
                self.plainTextEdit_descriptions.setPlainText(text)
            except KeyError:
                text = f'\nНМУ: не определен'
                self.plainTextEdit_descriptions.setPlainText(text)

    def change_button_color(self):
        doc = self.comboBoxTherapist.currentText()
        # if doc == 'Шилов И.С.':
        #     self.pushButtonCreateHistory.setStyleSheet(button_shilov)
        # elif doc == 'Шадрин А.А.':
        #     self.pushButtonCreateHistory.setStyleSheet(button_shadrin)
        # elif doc == 'Тыричев С.В.':
        #     self.pushButtonCreateHistory.setStyleSheet(button_tyrichev)
        # elif doc == 'Тимофеев А.П.':
        #     self.pushButtonCreateHistory.setStyleSheet(button_timofeev)
        # else:
        #     self.pushButtonCreateHistory.setStyleSheet(style_True)

    def change_need_psylogo(self):
        mkb10_code = self.comboBoxPtMKB10_main.currentText()
        if mkb10_code in {'I69.0', 'I69.1',
                          'I69.2', 'I69.3',
                          'I69.4', 'I69.8',
                          'I69.9', 'T90.5',
                          'G61.0', 'G20',
                          'G81.1', 'G82.1',
                          'G82.4'}:
            self.checkBox_need_psylogo.setChecked(True)

    def create_consent(self):
        '''
        функция создает и открывает файл (.docx)
            с различными согласиями пациента
            с возможностью их редактирования
            и вывода на печать

        '''
        self.write_to_dictionary()
        creating_documents(self.d, ['Согласия'])
        open_folder_with_files(self.d)

    def add_patient_relative(self):
        '''

        '''
        self.write_to_dictionary()
        self.open_window('add_relative')

    def open_patient_card(self):
        self.w = self.windows['omr']['patient_card'](
            windows=self.windows, main_win=self.main_win, dictionary=self.d)
        self.w.show()

    def write_to_dictionary(self):
        self.d['status_act'] = True
        # создаем чек-лайн для БД наполненности
        self.d['check_line'] = '100000000000000'
        # записываем остальные данные
        self.d['фамилия'] = self.lineEditPtSurName.text()
        self.d['имя'] = self.lineEditPtName.text()
        self.d['отчество'] = self.lineEditPtDadName.text()
        self.d['дата_рождения'] = \
            self.dateEditPtBirthDay.dateTime().toString('dd.MM.yyyy')
        self.d['адрес'] = self.lineEditPtAdress.text()
        self.d['дата_поступления'] = \
            self.dateEditPtAdmissionDay.dateTime().toString('dd.MM.yyyy')
        self.d['время_поступления'] = \
            self.timeEditPtAdmissionTime.dateTime().toString('hh:mm')
        self.d['тип_стационара'] = \
            self.comboBoxPtHoptitalisationType.currentText()
        self.d['нужда_в_ЛН'] = self.checkBoxPtNeedSickList.isChecked()
        self.d['нужда_в_ЛН_первич'] = self.checkBoxPtNeedSickList_2.isChecked()
        self.d['ФИО_врача'] = self.comboBoxTherapist.currentText()
        self.d['телефон'] = self.lineEditPtPhone.text()
        self.d['электронная_почта'] = self.lineEditPtEmail.text()
        self.d['паспорт'] = self.lineEditPtPassportNumber.text()
        self.d['полис_ОМС'] = self.lineEditPtOmsNumber.text()
        self.d['СНИЛС'] = self.lineEditPtSNILS.text()
        self.d['МКБ'] = self.comboBoxPtMKB10_main.currentText()
        self.d['услуга'] = self.comboBoxPtNMU_code.currentText()
        self.d['палата'] = self.comboBoxPtRoomNumber.currentText()
        self.d['пол'] = self.comboBoxGender.currentText()
        if self.checkBoxPtLeftHanded.isChecked():
            self.d['Правша'] = False
        else:
            self.d['Правша'] = True
        self.d['дата_выписки_план'] = \
            self.dateEditDischargeDate_plan.dateTime().toString('dd.MM.yyyy')
        self.d['номер_истории'] = self.lineEdit_history_number.text()
        self.d['зав_отделением'] = self.comboBox_department_head.currentText()
        self.d['ЛПУ_кто_направил'] = \
            self.comboBox_referring_health_facility.currentText()
        self.d['профиль_коек'] = self.comboBox_bedprofile.currentText()
        self.d['нужда_логопед_психолог'] = \
            self.checkBox_need_psylogo.isChecked()
        add_mkb10_nmu(self.d)

        update_after_passport_data(self.d)

    def check_unique_person(self):
        active_data = read_db_active_cases()
        archive_data = read_db_archive_cases()

        try_d = {
            'фамилия': self.lineEditPtSurName.text(),
            'имя': self.lineEditPtName.text(),
            'отчество': self.lineEditPtDadName.text(),
        }

        fullname = f"{try_d['фамилия']} {try_d['имя']} {try_d['отчество']}"
        birthday = self.dateEditPtBirthDay.dateTime().toString('dd.MM.yyyy')

        for case in active_data:
            if case["full_name"] == fullname:
                # получаем uin
                uin = case["case_id"]
                # скачиваем json из бакета (YandexCloud)
                # download_from_bucket(BUCKET_MAIN, f'{uin}.json')
                # записываем словарь из БД в словарь
                archive_d = read_d_from_db(uin)
                if birthday == archive_d['дата_рождения']:
                    text = f'В активных случаях уже есть '\
                           f'идентичный пациент! '\
                           f'Добавление истории болезни отменено!'
                    return text

        uins = []
        for case in archive_data:
            if case["full_name"] == fullname:
                # получаем uin
                uins.append(case["case_id"])
        for uin in uins:
            # скачиваем json из бакета (YandexCloud)
            # download_from_bucket(BUCKET_MAIN, f'{uin}.json')
            # записываем словарь из БД в словарь
            archive_d = read_d_from_db(uin)
            if birthday != archive_d['дата_рождения']:
                uins.pop(uin)
        if uins != []:
            return uins

        return True

    def check_not_empty(self):
        main_data_list = [
            self.lineEditPtSurName.text(),
            self.lineEditPtName.text(),
            self.lineEditPtDadName.text(),
            self.dateEditPtBirthDay.dateTime().toString('dd.MM.yyyy'),
            self.dateEditPtAdmissionDay.dateTime().toString('dd.MM.yyyy'),
            self.timeEditPtAdmissionTime.dateTime().toString('hh:mm'),
            self.comboBoxPtRoomNumber.currentText(),
        ]
        check_list_empty = []

        for i in main_data_list:
            if i in ('', '01.01.2000', '00:00'):
                check_list_empty.append(False)
            else:
                check_list_empty.append(True)

        return check_list_empty

    def create_history(self):
        uin = self.check_unique_person()
        # если пациент уникальный
        if uin is True:
            # проверяем что данные заполнены
            if all((self.check_not_empty())):
                # записываем новые данные в словарь
                self.write_to_dictionary()
                # загружаем в бакет YandexCloud
                self.save_history()
                # открываем карту пациента
                self.open_window('patient_card')
            else:
                text = f'      Данные заполнены не полном объеме!\n'\
                       f'Создание истории болезни отменено!\n'\
                       f'Поля фамилия, имя, отчество, дата рождения, '\
                       f'дата поступления, время поступления и '\
                       f'номер палаты не должны быть пустыми!'
                self.plainTextEdit_descriptions_promed.setPlainText(text)
        # если вернули список uin
        elif isinstance(uin, list):
            histories = []
            for i in uin:
                # считываем архивные истории
                histories.append(read_d_from_db(i))
            # записываем новые данные в словарь
            self.write_to_dictionary()
            self.open_window('load_arch')
        # если такая история уже есть в активных
        elif isinstance(uin, str):
            # очищаем все поля
            self.plainTextEdit_promed_data.setPlainText('')
            self.lineEditPtSurName.setText('')
            self.lineEditPtName.setText('')
            self.lineEditPtDadName.setText('')
            self.lineEditPtAdress.setText('')
            self.dateEditPtBirthDay.setDate(
                QtCore.QDate.fromString("01.01.2000", "dd.MM.yyyy"))
            self.dateEditPtAdmissionDay.setDate(
                QtCore.QDate.fromString("01.01.2000", "dd.MM.yyyy"))
            self.timeEditPtAdmissionTime.setTime(
                QtCore.QTime.fromString("00:00", "hh:mm"))
            self.dateEditDischargeDate_plan.setDate(
                QtCore.QDate.fromString("01.01.2000", "dd.MM.yyyy"))
            self.comboBoxPtHoptitalisationType.setCurrentText('')
            self.checkBoxPtNeedSickList.setChecked(False)
            self.comboBoxTherapist.setCurrentText('')
            self.lineEditPtPhone.setText('')
            self.lineEditPtEmail.setText('')
            self.lineEditPtPassportNumber.setText('')
            self.lineEditPtOmsNumber.setText('')
            self.lineEditPtSNILS.setText('')
            self.comboBoxPtMKB10_main.setCurrentText('')
            self.comboBoxPtNMU_code.setCurrentText('')
            self.comboBoxPtRoomNumber.setCurrentText('')
            self.comboBoxGender.setCurrentText('')
            self.checkBoxPtLeftHanded.setChecked(False)
            self.lineEdit_history_number.text()
            self.comboBox_department_head.setCurrentText('')
            self.comboBox_referring_health_facility.setCurrentText('')

            # выводим сообщение об отмене добавления истории
            style = "QPlainTextEdit {\
                        font-family: Roboto;\
                        font-size: 15px;background-color:#AF830B;\
                    }"
            self.plainTextEdit_descriptions.setStyleSheet(style)
            self.plainTextEdit_descriptions.setPlainText(f"{uin}\n")

    @staticmethod
    def _upload_history_to_yandex_cloud_bucket(func):
        def wrapper(d):
            # скачиваем актуальную БД из бакета
            # (для минимизации возможного расхождения с уже скачаной)
            download_db_from_bucket(BUCKET_MAIN, DATABASE)
            func(d)
            # загружаем в бакет
            upload_db_to_bucket(BUCKET_MAIN, DATABASE)
            upload_to_bucket(BUCKET_MAIN, f"{d['unic_number']}.json")
        return wrapper

    @_upload_history_to_yandex_cloud_bucket
    def save_history(self):
        write_all_data_to_db(self.d)
        write_fullness_table(self.d)
        write_scale_table(self.d)

    def parse_promed_data(self):
        if (promed := self.plainTextEdit_promed_data.toPlainText()) != '':
            try:
                promed_data = parse_promed(promed)

                self.lineEditPtSurName.setText(promed_data['surname'])
                self.lineEditPtName.setText(promed_data['name'])
                self.lineEditPtDadName.setText(promed_data['dadname'])
                self.dateEditPtBirthDay.setDate(QtCore.QDate.fromString(
                    promed_data['birthday'], "dd.MM.yyyy"))
                self.lineEditPtAdress.setText(promed_data['adress'])
                self.lineEditPtPhone.setText(promed_data['phone_number'])
                self.lineEditPtPassportNumber.setText(promed_data['passport'])
                self.lineEditPtOmsNumber.setText(promed_data['oms_polis'])
                self.lineEditPtSNILS.setText(promed_data['snils'])
                self.comboBoxGender.setCurrentText(promed_data['sex'])
                msg = f"Парсинг прошел успешно! :)"
                self.plainTextEdit_promed_data.setPlainText('')
                self.plainTextEdit_descriptions_promed.setPlainText(msg)
            except IndexError:
                msg = f"Вводимая строка НЕ соответствует\n"\
                      f"формату ЕИСЗ ПК (Промед) и\n"\
                      f"непригодна для парсинга"
                self.plainTextEdit_promed_data.setPlainText('')
                self.plainTextEdit_descriptions_promed.setPlainText(msg)
            except UnboundLocalError:
                msg = f"Вводимая строка НЕ соответствует\n"\
                      f"формату ЕИСЗ ПК (Промед) и\n"\
                      f"непригодна для парсинга"
                self.plainTextEdit_promed_data.setPlainText('')
                self.plainTextEdit_descriptions_promed.setPlainText(msg)
        else:
            msg = f"Строка пуста!\nПарсинг не возможен!"
            self.plainTextEdit_descriptions_promed.setPlainText(msg)

    def set_styles(self):
        self.plainTextEdit_descriptions.setEnabled(False)
        # self.pushButtonCreateHistory.setStyleSheet(style_True)
        # self.plainTextEdit_descriptions.setStyleSheet(plainTextEdit_desc)