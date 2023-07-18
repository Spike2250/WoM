from PySide6 import QtWidgets, QtCore
from datetime import timedelta, datetime
from wom.GUI.PY import bta_AddNewPatient
from wom.app_logic.service_func import (datedif, convert_date as c_date,
                                        create_mkb_nmu_dict, add_mkb10_nmu)
from wom.app_logic.db_func.db_bta import (read_d_from_db_bta,
                                          read_db_active_cases_bta,
                                          read_db_archive_cases_bta,
                                          write_all_data_to_db_bta,
                                          write_fullness_table_bta)
from wom.app_logic.create_docs import (creating_documents,
                                       open_folder_with_files)
from wom.app_logic.parsing import parse_promed
from wom.app_logic.postprocessing import update_after_passport_data


class Ui_AddNewPatient(QtWidgets.QMainWindow,
                       bta_AddNewPatient.Ui_PatientPassportData):
    def __init__(self, windows):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.windows = windows

        self.set_connections()
        self.add_values_to_popup_lists()
        self.tricks()
        self.show_uin_label()

    def set_connections(self):
        # коннекты кнопок
        self.pushButtonCreateHistory.clicked.connect(self.create_history)
        self.pushButtonPrintConsent.clicked.connect(self.create_consent)
        self.pushButton_add_from_promed.clicked.connect(self.parse_promed_data)
        self.pushButtonBackToMenu.clicked.connect(self.back_to_main_menu)
        self.pushButton_today.clicked.connect(self.set_adm_date_today)
        self.pushButton_yesterday.clicked.connect(self.set_adm_date_yesterday)
        #
        self.checkBoxPtNeedSickList.stateChanged.connect(self.activate_first_ln_box)

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
        self.comboBox_mkb.clear()
        self.comboBox_mkb.addItems(list(self.mkb10))
        self.comboBox_nmu.clear()
        self.comboBox_nmu.addItems(list(self.nmu))

    def tricks(self):
        # автозаполнение
        self.dateEdit_adm_date.dateChanged.connect(
            self.change_DischargeDate_plan)
        self.dateEdit_adm_date.dateChanged.connect(
            self.change_dis_info)
        self.comboBox_mkb.currentTextChanged.connect(
            self.change_nmu)
        self.comboBox_mkb.currentTextChanged.connect(
            self.change_mkb_desc)
        self.comboBox_nmu.currentTextChanged.connect(
            self.change_nmu_desc)
        self.dateEdit_dis_date_plan.dateChanged.connect(
            self.change_dis_info)

    def set_adm_date_today(self):
        today = datetime.now().strftime('%d.%m.%Y')
        self.dateEdit_adm_date.setDate(
            QtCore.QDate.fromString(today, "dd.MM.yyyy"))

    def set_adm_date_yesterday(self):
        yesterday = (datetime.now() - timedelta(1)).strftime('%d.%m.%Y')
        self.dateEdit_adm_date.setDate(
            QtCore.QDate.fromString(yesterday, "dd.MM.yyyy"))

    def change_dis_info(self):
        adm_date = self.dateEdit_adm_date.dateTime().toString('dd.MM.yyyy')
        dis_date = self.dateEdit_dis_date_plan.dateTime().toString('dd.MM.yyyy')
        typeHosp = self.comboBox_hospit_type.currentText()

        if typeHosp in {'Круглосуточный стационар', 'БТ - круглосуточный'}:
            bed_days = datedif(adm_date, dis_date) - 1
        else:
            bed_days = datedif(adm_date, dis_date)
        dis_date = c_date(dis_date)

        text = f'   {dis_date.strftime("%A")} \t({bed_days} к/д)'
        self.label_discharge_info.setText(text)

    def show_uin_label(self):
        # написание UIN
        uin = f"Клиническому случаю будет присвоен UIN: {d['unic_number']}"
        self.label_unic_number.setText(uin)

    def change_nmu(self):
        '''
        '''
        mkb10_code = self.comboBox_mkb.currentText()

        if mkb10_code in {'I69.0', 'I69.1',
                          'I69.2', 'I69.3',
                          'I69.4', 'I69.8',
                          'I69.9'}:
            self.comboBox_nmu.setCurrentText('B05.023.001')
        elif mkb10_code in {'M51.1', 'M51.0',
                            'M50.1', 'M50.0'}:
            self.comboBox_nmu.setCurrentText('B05.024.002')
        elif mkb10_code in {'U09.9'}:
            self.comboBox_nmu.setCurrentText('B05.070.001.011')
        elif mkb10_code in {'T91.3', 'T91.1'}:
            self.comboBox_nmu.setCurrentText('B05.024.001')
        elif mkb10_code in {'T90.5'}:
            self.comboBox_nmu.setCurrentText('B05.024.003')
        elif mkb10_code in {'G81.1', 'G82.1',
                            'G82.4'}:
            self.comboBox_nmu.setCurrentText('A25.24.001.002')
        elif mkb10_code in {'G61.0', 'G20'}:
            self.comboBox_nmu.setCurrentText('B05.023.002.002')
        elif mkb10_code in {'M24.5'}:
            self.comboBox_nmu.setCurrentText('B05.050.005')

    def change_DischargeDate_plan(self):
        '''
        '''
        hospit_type = self.comboBox_hospit_type.currentText()
        day_adm = c_date(
            self.dateEdit_adm_date.dateTime().toString('dd.MM.yyyy'))

        if hospit_type == 'БТ - круглосуточный':
            discharge_date_plan = day_adm + timedelta(1)
        else:
            discharge_date_plan = day_adm
        self.dateEdit_dis_date_plan.setDate(QtCore.QDate.fromString(
            discharge_date_plan.strftime('%d.%m.%Y'), "dd.MM.yyyy"))

    def change_mkb_desc(self):
        cbox_text = self.comboBox_mkb.currentText()
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
        cbox_text = self.comboBox_nmu.currentText()
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

    def create_consent(self):
        '''
        функция создает и открывает файл (.docx)
            с различными согласиями пациента
            с возможностью их редактирования
            и вывода на печать

        '''
        self.write_to_dictionary()
        creating_documents(d, ['Согласия'])
        open_folder_with_files(d)

    def open_patient_card(self):
        pass
        # Создаём объект класса Ui_PatientCard
        # self.window_card = Ui_PatientCard()
        # self.window_card.show()  # Показываем окно

    def write_to_dictionary(self):
        d['status_act'] = True  # Статус пациента (False - выписан, True - нет)
        # создаем чек-лайн для БД наполненности
        d['check_line'] = '1000000'

        # записываем остальные данные
        # lineEdit's
        d['фамилия'] = self.surname.text()
        d['имя'] = self.name.text()
        d['отчество'] = self.dadname.text()
        d['адрес'] = self.adress.text()
        d['телефон'] = self.phone.text()
        d['электронная_почта'] = self.email.text()
        d['паспорт'] = self.passport.text()
        d['полис_ОМС'] = self.polis_oms.text()
        d['СНИЛС'] = self.snils.text()
        d['номер_истории'] = self.history_number.text()
        d['палата'] = self.room_number.text()
        # comboBox's
        d['препарат_БТА'] = self.comboBox_bta_preparat.currentText()
        d['тип_стационара'] = self.comboBox_hospit_type.currentText()
        d['МКБ'] = self.comboBox_mkb.currentText()
        d['услуга'] = self.comboBox_nmu.currentText()
        d['ЛПУ_кто_направил'] = self.comboBox_referring_health_facility.currentText()
        d['пол'] = self.comboBox_gender.currentText()
        d['ФИО_врача'] = self.comboBox_therapist.currentText()
        d['зав_отделением'] = self.comboBox_department_head.currentText()
        # dateEdit's
        d['дата_поступления'] = self.dateEdit_adm_date.dateTime().toString('dd.MM.yyyy')
        d['дата_выписки_план'] = self.dateEdit_dis_date_plan.dateTime().toString('dd.MM.yyyy')
        d['дата_рождения'] = self.dateEdit_birthday.dateTime().toString('dd.MM.yyyy')
        # timeEdit's
        d['время_поступления'] = self.timeEdit_adm_time.dateTime().toString('hh:mm')
        # checkBox's
        d['нужда_в_ЛН'] = self.checkBoxPtNeedSickList.isChecked()
        d['нужда_в_ЛН_первич'] = self.checkBoxPtNeedSickList_2.isChecked()
        d['не_может_подписаться'] = self.checkBox_signature_cant.isChecked()

        # профиль коек
        # НЕЛЬЗЯ ПОТОМ ИЗМЕНИТЬ
        d['профиль_коек'] = 'неврологические для взрослых'

        # название отделения
        if d['тип_стационара'] == 'БТ - круглосуточный':
            d['название_отделения'] = '4102. Неврологическое отделение (Панфилова, 20)'
        elif d['тип_стационара'] == 'БТ - дневной':
            d['название_отделения'] = '4202. Неврологический дневной стационар'

        # добавление надписей, при невозможнссти пациента поставить подпись
        if d['не_может_подписаться']:
            d['нмпп'] = 'не может подписаться'
            d['нмпп_дата_поступления'] = d['дата_поступления']
            d['нмпп_дата_выписки'] = d['дата_выписки_план']
            d['нмпп_ФИО_врача'] = d['ФИО_врача']
            d['нмпп_зав_отделением'] = d['зав_отделением']

        add_mkb10_nmu(d)

        update_after_passport_data(d)

    def check_unique_person(self):
        active_data = read_db_active_cases_bta()
        archive_data = read_db_archive_cases_bta()

        try_d = {
            'фамилия': self.surname.text(),
            'имя': self.name.text(),
            'отчество': self.dadname.text(),
        }

        fullname = f"{try_d['фамилия']} {try_d['имя']} {try_d['отчество']}"
        birthday = self.dateEdit_birthday.dateTime().toString('dd.MM.yyyy')

        for x in active_data:
            if x[3] == fullname:
                # получаем uin
                uin = x[8]
                # записываем словарь из БД в словарь
                archive_d = read_d_from_db_bta(uin)
                if birthday == archive_d['дата_рождения']:
                    text = f'В активных случаях уже есть '\
                           f'идентичный пациент! '\
                           f'Добавление истории болезни отменено!'
                    return text

        for x in archive_data:
            if x[3] == fullname:
                # получаем uin
                uin = x[7]
                # записываем словарь из БД в словарь
                archive_d = read_d_from_db_bta(uin)
                if birthday == archive_d['дата_рождения']:
                    return uin  # Для использования истории как новой основы

        return True

    def create_history(self):
        global d
        uin = self.check_unique_person()
        # если пациент уникальный
        if uin is True:
            # записываем новые данные в словарь
            self.write_to_dictionary()
            # загружаем в бакет YandexCloud
            self.save_history()
            # открываем карту пациента
            self.open_patient_card()
            self.hide()
        # если вернули uin
        # elif len(uin) == 36:
        #     # скачиваем архивную историю
        #     self.d_arch = read_d_from_db(uin)
        #     # записываем новые данные в словарь
        #     self.write_to_dictionary()
        #     self.window_arch = Ui_load_arch_data(self.d_arch)
        #     self.window_arch.show()
        #     self.hide()
        # если такая история уже есть в активных
        else:

            # очищаем все поля
            # lineEdit's
            self.surname.setText('')
            self.name.setText('')
            self.dadname.setText('')
            self.adress.setText('')
            self.phone.setText('')
            self.email.setText('')
            self.passport.setText('')
            self.polis_oms.setText('')
            self.snils.setText('')
            self.history_number.setText('')
            self.room_number.setText('')
            # comboBox's
            self.comboBox_bta_preparat.setCurrentText('')
            self.comboBox_hospit_type.setCurrentText('')
            self.comboBox_mkb.setCurrentText('')
            self.comboBox_nmu.setCurrentText('')
            self.comboBox_referring_health_facility.setCurrentText('')
            self.comboBox_gender.setCurrentText('')
            self.comboBox_therapist.setCurrentText('')
            self.comboBox_department_head.setCurrentText('')
            # dateEdit's
            self.dateEdit_adm_date.setDate(
                QtCore.QDate.fromString("01.01.2000", "dd.MM.yyyy"))
            self.dateEdit_dis_date_plan.setDate(
                QtCore.QDate.fromString("01.01.2000", "dd.MM.yyyy"))
            self.dateEdit_birthday.setDate(
                QtCore.QDate.fromString("01.01.2000", "dd.MM.yyyy"))
            # timeEdit's
            self.timeEdit_adm_time.setTime(
                QtCore.QTime.fromString("00:00", "hh:mm"))
            # checkBox's
            self.checkBoxPtNeedSickList.setChecked(False)
            self.checkBoxPtNeedSickList_2.setChecked(False)
            self.checkBox_signature_cant.setChecked(False)

            # выводим сообщение об отмене добавления истории
            # style = "QPlainTextEdit {font-family: Roboto;font-size: 15px;background-color:#AF830B;}"
            # self.plainTextEdit_descriptions.setStyleSheet(style)
            self.plainTextEdit_descriptions.setPlainText(f"{uin}\n")

    def save_history(self):
        # записываем словарь в json-файл и обновляем БД
        write_all_data_to_db_bta(d)
        write_fullness_table_bta(d)

    def back_to_main_menu(self):
        self.window_menu = Ui_MainMenu()
        self.window_menu.show()  # Показываем окно
        self.hide()

    def parse_promed_data(self):
        if (x := self.plainTextEdit_promed_data.toPlainText()) != '':
            try:
                promed_data = parse_promed(x)
                self.surname.setText(promed_data['surname'])
                self.name.setText(promed_data['name'])
                self.dadname.setText(promed_data['dadname'])
                self.dateEdit_birthday.setDate(
                    QtCore.QDate.fromString(promed_data['birthday'], "dd.MM.yyyy"))
                self.adress.setText(promed_data['adress'])
                self.phone.setText(promed_data['phone_number'])
                self.passport.setText(promed_data['passport'])
                self.polis_oms.setText(promed_data['oms_polis'])
                self.snils.setText(promed_data['snils'])
                self.comboBox_gender.setCurrentText(promed_data['sex'])
                msg = f"Парсинг прошел успешно! :)"
                self.plainTextEdit_descriptions_promed.setPlainText(msg)
            except IndexError:
                msg = f"Вводимая строка НЕ соответствует\n"\
                      f"формату ЕИСЗ ПК (Промед) и\n"\
                      f"непригодна для парсинга"
                self.plainTextEdit_descriptions_promed.setPlainText(msg)
                self.plainTextEdit_promed_data.setPlainText('')
            except UnboundLocalError:
                msg = f"Вводимая строка НЕ соответствует\n"\
                      f"формату ЕИСЗ ПК (Промед) и\n"\
                      f"непригодна для парсинга"
                self.plainTextEdit_descriptions_promed.setPlainText(msg)
                self.plainTextEdit_promed_data.setPlainText('')
        else:
            msg = f"Строка пуста!\nПарсинг не возможен!"
            self.plainTextEdit_descriptions_promed.setPlainText(msg)