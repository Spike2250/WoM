from PySide6 import QtWidgets
from PySide6.QtWidgets import (QAbstractItemView,
                               QTableWidgetItem as QTW_Item,
                               QLineEdit,
                               QPushButton)

from wom.GUI.PY.common import Icf
from wom.app_logic.handbooks.icf_dict import multy_domens
from wom.app_logic.handbooks.description_of_domains import domains_desc


class Ui_icf_psylogo(QtWidgets.QWidget, Icf.Ui_icf):
    def __init__(self, windows, main_win, dictionary, case_type, timeline):
        super().__init__()
        self.setupUi(self)
        self.windows = windows
        self.main_win = main_win
        self.d = dictionary
        self.case_type = case_type
        self.timeline = timeline

        self.func_for_initial()
        self.refresh_table_icf()
        self.set_connections()
        self.set_styles()

    def func_for_initial(self):
        '''
        '''
        self.create_table()
        self.set_items_in_finding_line()
        self.set_templates_list()
        self.set_patient_info()
        # вставка данных из словаря
        self.paste_data_from_d()

    def create_table(self):
        self.tableWidget.setEditTriggers(
            QAbstractItemView.NoEditTriggers)
        self.tableWidget.setColumnWidth(0, 510)
        self.tableWidget.setColumnWidth(1, 50)
        self.tableWidget.setColumnWidth(2, 40)
        self.tableWidget.setColumnWidth(3, 50)
        self.tableWidget.setColumnWidth(4, 40)
        self.tableWidget.setColumnWidth(5, 35)

        self.tableWidget.setRowCount(1)

    def set_items_in_finding_line(self):
        self.comboBox_find_domen.clear()
        self.comboBox_find_domen.addItems(sorted(multy_domens))

    def push_domen(self):
        if (text := self.comboBox_find_domen.currentText()) != '':
            if text[0] not in ('s', 'd', 'b', 'e'):
                part2, part1 = text.split(' - ')
                text = f'{part1} - {part2}'

            self.plainTextEdit_new_domen.setPlainText(text)
            self.comboBox_find_domen.setCurrentText('')
            self.lineEdit_new_domen_numbers.setEnabled(True)
            self.lineEdit_new_domen_numbers_dynamic.setEnabled(True)

    def clean_domen(self):
        self.plainTextEdit_new_domen.setPlainText('')
        self.lineEdit_new_domen_numbers.setText('')
        self.lineEdit_new_domen_numbers_dynamic.setText('')
        self.comboBox_find_domen.setCurrentText('')
        self.label_check_correct.setText('')
        self.label_check_correct_dynamic.setText('')
        self.lineEdit_new_domen_numbers.setEnabled(False)
        self.lineEdit_new_domen_numbers_dynamic.setEnabled(False)
        self.pushButton_add_domen.setEnabled(False)

    def checking_validate_domen(self):
        self.check_domen = False
        if (domen_text := self.plainTextEdit_new_domen.toPlainText()) != '':
            if len(domen_text.split(' - ')) == 2:
                if domen_text[0] == 's':
                    self.check_domen = True
                    self.textBrowser_description.setPlainText(
                        domains_desc['s'])
                elif domen_text[0] == 'b':
                    self.check_domen = True
                    self.textBrowser_description.setPlainText(
                        domains_desc['b'])
                elif domen_text[0] == 'd':
                    self.check_domen = True
                    self.textBrowser_description.setPlainText(
                        domains_desc['d'])
                elif domen_text[0] == 'e':
                    self.check_domen = True
                    self.textBrowser_description.setPlainText(
                        domains_desc['e'])
                else:
                    self.textBrowser_description.setPlainText(
                        domains_desc['not_recognized'])
            else:
                self.textBrowser_description.setPlainText(
                    domains_desc['not_valid_format'])
        else:
            self.textBrowser_description.setPlainText('')

    def change_valid_numbers_text(self):
        valid_text = 'Ok!'
        novalid_text = 'No!!'
        widget = self.sender()

        if (name := widget.objectName()) != '':
            domen = self.plainTextEdit_new_domen.toPlainText()
            numbers = widget.text()
            if self.checking_validate_numbers(domen, numbers):
                if name == 'lineEdit_new_domen_numbers':
                    self.label_check_correct.setText(valid_text)
                elif name == 'lineEdit_new_domen_numbers_dynamic':
                    self.label_check_correct_dynamic.setText(valid_text)
            else:
                if name == 'lineEdit_new_domen_numbers':
                    self.label_check_correct.setText(novalid_text)
                elif name == 'lineEdit_new_domen_numbers_dynamic':
                    self.label_check_correct_dynamic.setText(novalid_text)
        else:
            # мы в таблице
            pos = (self.tableWidget.indexAt(widget.pos()).row(),
                   self.tableWidget.indexAt(widget.pos()).column())
            domen = self.tableWidget.item(pos[0], 0).text()
            numbers = widget.text()
            if self.checking_validate_numbers(domen, numbers):
                self.tableWidget.setItem(
                    pos[0], pos[1] + 1, QTW_Item(valid_text))
            else:
                self.tableWidget.setItem(
                    pos[0], pos[1] + 1, QTW_Item(novalid_text))

            # добавляем описание определителей домена
            if domen[0] == 's':
                self.textBrowser_description.setPlainText(domains_desc['s'])
            elif domen[0] == 'b':
                self.textBrowser_description.setPlainText(domains_desc['b'])
            elif domen[0] == 'd':
                self.textBrowser_description.setPlainText(domains_desc['d'])
            elif domen[0] == 'e':
                self.textBrowser_description.setPlainText(domains_desc['e'])

    def checking_validate_numbers(self, domen, numbers):
        check_numbers = False

        if domen != '':
            try:
                if domen[0] == 's':
                    # контроль, что введены только цифры
                    for i in range(len(numbers)):
                        int(numbers[i])
                    #
                    if len(numbers) == 3:
                        if numbers[0] in ('0', '1', '2', '3',
                                          '4', '8', '9'):
                            check_numbers = True
                elif domen[0] == 'b':
                    if len(numbers) == 1:
                        if numbers[0] in ('0', '1', '2', '3',
                                          '4', '8', '9'):
                            check_numbers = True
                elif domen[0] == 'd':
                    if 2 <= (tx_n := len(numbers)) <= 4:
                        check_list = []
                        for i in range(tx_n):
                            if numbers[i] in ('0', '1', '2', '3',
                                              '4', '8', '9'):
                                check_list.append(True)
                            else:
                                check_list.append(False)
                        if all((check_list)):
                            check_numbers = True
                elif domen[0] == 'e':
                    if len(numbers) == 1:
                        if numbers[0] in ('0', '1', '2', '3',
                                          '4', '8', '9'):
                            check_numbers = True
                    elif len(numbers) == 2:
                        if numbers[0] == '+':
                            if numbers[1] in ('0', '1', '2', '3',
                                              '4', '8', '9'):
                                check_numbers = True
                else:
                    self.label_check_correct.setText('Домен н/к!')

                return check_numbers

            except ValueError:
                return False

    def set_templates_list(self):
        # список шаблонов
        if self.type_icf == 'psy':
            self.templates_icf = read_icf_psy_templates()
        elif self.type_icf == 'logo':
            self.templates_icf = read_icf_logo_templates()

        if self.templates_icf is not None:
            self.templates_list = list(self.templates_icf)
            self.comboBox_template.clear()
            if len(self.templates_list) <= 1:
                self.comboBox_template.addItem(self.templates_list[0])
            else:
                self.comboBox_template.addItems(self.templates_list)
        else:
            self.templates_icf = {}
            self.comboBox_template.clear()

    def add_new_template(self):
        new_template_name = self.lineEdit_new_template_name.text()
        # проверяем не пустое ли имя нового шаблона
        if new_template_name != '':
            self.templates_icf[new_template_name] = self.icf_l
            if self.type_icf == 'psy':
                psy_icf_template_json_recording(self.templates_icf)
            elif self.type_icf == 'logo':
                logo_icf_template_json_recording(self.templates_icf)
        else:
            # имя шаблона пустое
            pass

        self.lineEdit_new_template_name.setText('')
        self.set_templates_list()

    def push_active_template(self):
        '''
        '''
        template_name = self.comboBox_template.currentText()
        # вставляем полученные данные
        self.icf_l = []
        for i in self.templates_icf[template_name]:
            self.icf_l.append(i)
        self.refresh_table_icf()

    def set_connections(self):
        # коннекты кнопок
        self.pushButtonNotSaveExit.clicked.connect(self.exit_not_save)
        self.pushButtonSaveExit.clicked.connect(self.exit_and_save)
        self.pushButtonAddNewTemplate.clicked.connect(
            self.add_new_template)
        self.pushButton_push_temp.clicked.connect(
            self.push_active_template)
        self.pushButton_push_domen.clicked.connect(self.push_domen)
        self.pushButton_add_domen.clicked.connect(self.add_domen_to_list)
        self.pushButton_push_domen_2.clicked.connect(self.clean_domen)
        # коннекты зависимостей
        self.plainTextEdit_new_domen.textChanged.connect(
            self.checking_validate_domen)
        self.lineEdit_new_domen_numbers.textChanged.connect(
            self.change_valid_numbers_text)
        self.lineEdit_new_domen_numbers_dynamic.textChanged.connect(
            self.change_valid_numbers_text)
        self.lineEdit_new_domen_numbers.textChanged.connect(
            self.check_to_push)
        self.lineEdit_new_domen_numbers_dynamic.textChanged.connect(
            self.check_to_push)

    def check_to_push(self):
        if self.label_check_correct.text() == 'Ok!':
            if self.label_check_correct_dynamic.text() == 'Ok!':
                self.pushButton_add_domen.setEnabled(True)
            else:
                self.pushButton_add_domen.setEnabled(False)
        else:
            self.pushButton_add_domen.setEnabled(False)

    def set_patient_info(self):
        # Заполнение Patient Info
        if 'patient_info' in self.d:
            self.label_Pt_info.setText(self.d['patient_info'])
        else:
            self.label_Pt_info.setText('Ошибка! Нет "patient_info" в словаре!')

        if self.type_icf == 'psy':
            self.label_who_call.setText('Клинический психолог')
        elif self.type_icf == 'logo':
            self.label_who_call.setText('Логопед-афазиолог')

    def add_domen_to_list(self):

        domen = self.plainTextEdit_new_domen.toPlainText()
        numbers_adm = self.lineEdit_new_domen_numbers.text()
        numbers_dis = self.lineEdit_new_domen_numbers_dynamic.text()

        if all((self.check_domen,
                self.checking_validate_numbers(domen, numbers_adm),
                self.checking_validate_numbers(domen, numbers_dis))):
            d_temp = {
                'domen': domen,
                'numbers_adm': numbers_adm,
                'numbers_dis': numbers_dis,
            }
            self.icf_l.append(d_temp)

        self.refresh_table_icf()
        self.clean_domen()

    def refresh_table_icf(self):
        table = self.tableWidget
        # Заполнение всех ячеек данными, если они уже есть
        if self.icf_l is not []:
            if (icf_n := len(self.icf_l)) >= 1:
                table.setRowCount(0)
                table.setRowCount(icf_n)
                for i in range(icf_n):
                    # создаем строки ввода
                    lineEdit_num_adm = QLineEdit(self.icf_l[i]['numbers_adm'])
                    lineEdit_num_dis = QLineEdit(self.icf_l[i]['numbers_dis'])
                    lineEdit_num_adm.textChanged.connect(
                        self.change_valid_numbers_text)
                    lineEdit_num_dis.textChanged.connect(
                        self.change_valid_numbers_text)
                    lineEdit_num_adm.setStyleSheet(lineEdit_style)
                    lineEdit_num_dis.setStyleSheet(lineEdit_style)
                    # создаем кнопку
                    button_del = QPushButton('X')
                    button_del.clicked.connect(self.delete_domen)
                    button_del.setStyleSheet(bta_style_del_button)

                    # заполняем таблицу
                    table.setItem(i, 0, QTW_Item(self.icf_l[i]['domen']))
                    table.setCellWidget(i, 1, lineEdit_num_adm)
                    table.setCellWidget(i, 3, lineEdit_num_dis)
                    table.setCellWidget(i, 5, button_del)
            else:
                table.setRowCount(0)
                table.setRowCount(1)
                table.setItem(
                    0, 0, QTW_Item('Включенные домены отсутствуют'))

    def delete_domen(self):
        button = self.sender()
        i = self.tableWidget.indexAt(button.pos()).row()
        self.icf_l.pop(i)
        self.refresh_table_icf()

    def paste_data_from_d(self):
        '''
        '''
        # Вставка данных из словаря при их наличии
        if self.type_icf == 'psy':
            if 'icf_psy' in d:
                self.icf_l = d['icf_psy']
        elif self.type_icf == 'logo':
            if 'icf_logo' in d:
                self.icf_l = d['icf_logo']

    def all_write_to_dict(self):
        '''
        '''
        table = self.tableWidget
        if len(self.icf_l) > 0:
            # перебираем таблицу и перезаписываем данные
            new_icf_l = []
            for row in range(table.rowCount()):
                # проверяем валидность данных
                if all((table.item(row, 2) is None
                        or table.item(row, 2).text() != 'No!!',
                        table.item(row, 4) is None
                        or table.item(row, 4).text() != 'No!!')):
                    # формируем новый словарь
                    domen = {
                        'domen': table.item(row, 0).text(),
                        'numbers_adm': table.cellWidget(row, 1).text(),
                        'numbers_dis': table.cellWidget(row, 3).text(),
                    }
                    # добавляем словарь к новому списку
                    new_icf_l.append(domen)
                else:
                    raise ValueError

            d[f'icf_{self.type_icf}'] = new_icf_l
            update_after_icf_psylogo(d, self.type_icf)
        else:
            # условно рейзим ошибку для понимания что таблица пуста
            raise IndexError

    def exit_and_save(self):
        try:
            self.all_write_to_dict()
            write_all_data_to_db(d)
            self.hide()
            self.window_card = Ui_PatientCard_Psy()
            self.window_card.show()
        # проверка на валидность не прошла
        except ValueError:
            text = 'Сохранение отменено!\n'\
                   'Значения в таблице не валидны!\n'\
                   'Перепроверьте значения и попробуйте сохранить снова.'
            self.textBrowser_description.setPlainText(text)
        # таблица пуста
        except IndexError:
            # закрываем без сохранения
            self.exit_not_save()

    def exit_not_save(self):
        self.hide()
        self.window_card = Ui_PatientCard_Psy()
        self.window_card.show()

    def set_styles(self):
        pass
