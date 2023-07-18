
import uuid  # генератор случайных UIN
from datetime import timedelta, datetime
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import (QTableWidgetItem as QTW_Item,
                               QAbstractItemView,
                               QPushButton,
                               QProgressBar)

from wom.GUI.PY import bta_MainMenu
from wom.app_logic.service_func import (convert_date as c_date,
                                        calc_percent_fullness)
from wom.app_logic.db_func.db_bta import (read_d_from_db_bta,
                                          read_db_active_cases_bta,
                                          read_db_archive_cases_bta,
                                          read_fullness_db_bta)
from wom.styles_qss import main_styles
# from wom.GUI.windows.win_aggregator import windows


class Ui_MainMenu(QtWidgets.QMainWindow,
                  bta_MainMenu.Ui_MainWindow):
    def __init__(self, windows):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.windows = windows

        self.set_connections()
        self.create_tables()
        self.show_active_cases()

    def set_connections(self):
        # коннекты кнопок
        self.add_new_patient.clicked.connect(
            self.create_new_case)
        self.refresh_pt_list.clicked.connect(
            self.show_active_cases)
        self.find_patient.clicked.connect(
            self.show_active_cases)
        self.pushButtonOpenArchive.clicked.connect(
            self.show_archive_cases)
        self.pushButton_month.clicked.connect(
            self.set_current_month_dates)
        self.pushButton_previous_month.clicked.connect(
            self.set_previous_month_dates)
        self.pushButton_year.clicked.connect(
            self.set_current_year_dates)
        self.pushButton_report_manager.clicked.connect(
            self.open_report_manager)
        # HotKeys
        self.refresh_pt_list.setShortcut('Return')
        self.pushButtonOpenArchive.setShortcut('Return')

    def create_tables(self):
        # делаем значения таблицы неизменяемыми
        self.tableWidget_db.setEditTriggers(
            QAbstractItemView.NoEditTriggers)
        self.tableWidget_archive_bd.setEditTriggers(
            QAbstractItemView.NoEditTriggers)
        # таблица активных случаев
        self.tableWidget_db.setColumnWidth(0, 100)  # ширина колонок
        self.tableWidget_db.setColumnWidth(1, 75)  # по номеру колонки
        self.tableWidget_db.setColumnWidth(2, 40)
        self.tableWidget_db.setColumnWidth(3, 85)
        self.tableWidget_db.setColumnWidth(4, 280)
        self.tableWidget_db.setColumnWidth(5, 85)
        self.tableWidget_db.setColumnWidth(6, 150)
        self.tableWidget_db.setColumnWidth(7, 55)
        self.tableWidget_db.setColumnWidth(8, 280)
        # таблица архивных случаев
        self.tableWidget_archive_bd.setColumnWidth(0, 75)  # ширина колонок
        self.tableWidget_archive_bd.setColumnWidth(1, 40)  # по номеру колонки
        self.tableWidget_archive_bd.setColumnWidth(2, 85)
        self.tableWidget_archive_bd.setColumnWidth(3, 85)
        self.tableWidget_archive_bd.setColumnWidth(4, 280)
        self.tableWidget_archive_bd.setColumnWidth(5, 55)
        self.tableWidget_archive_bd.setColumnWidth(6, 150)
        self.tableWidget_archive_bd.setColumnWidth(7, 45)
        self.tableWidget_archive_bd.setColumnWidth(8, 280)
        # устанавливаем стандартные даты поиска
        self.today = datetime.now().strftime('%d.%m.%Y')
        self.dateEdit_find_1.setDate(
            QtCore.QDate.fromString('01.01.2022', "dd.MM.yyyy"))
        self.dateEdit_find_2.setDate(
            QtCore.QDate.fromString(self.today, "dd.MM.yyyy"))
        # устанавливаем placeholdertext
        find_text = 'введите поисковой запрос'
        self.lineEdit.setPlaceholderText(find_text)
        self.lineEdit_find_active.setPlaceholderText(find_text)

    def set_current_month_dates(self):
        date = f'01.{self.today[-7:]}'
        self.dateEdit_find_1.setDate(
            QtCore.QDate.fromString(date, "dd.MM.yyyy"))
        self.dateEdit_find_2.setDate(
            QtCore.QDate.fromString(self.today, "dd.MM.yyyy"))

    def set_current_year_dates(self):
        date = f'01.01.{self.today[-4:]}'
        self.dateEdit_find_1.setDate(
            QtCore.QDate.fromString(date, "dd.MM.yyyy"))
        self.dateEdit_find_2.setDate(
            QtCore.QDate.fromString(self.today, "dd.MM.yyyy"))

    def set_previous_month_dates(self):
        date2 = (c_date(f'01.{self.today[-7:]}') - timedelta(1))
        date2 = date2.strftime('%d.%m.%Y')
        date1 = f'01.{date2[-7:]}'
        self.dateEdit_find_1.setDate(
            QtCore.QDate.fromString(date1, "dd.MM.yyyy"))
        self.dateEdit_find_2.setDate(
            QtCore.QDate.fromString(date2, "dd.MM.yyyy"))

    def create_new_case(self):
        # Очищаем глобальный словарь
        global d
        d = {}
        # создаем уникальный индентификатор случая
        d['unic_number'] = str(uuid.uuid4())  # УНИКАЛЬНЫЙ ID ДЛЯ БАЗЫ ДАННЫХ
        # открываем окно добавления нового пациента
        self.window_add_new = self.windows['bta']['add_new_patient'](self.windows)
        self.window_add_new.show()
        self.hide()

    def open_patient_card(self):
        # Очищаем глобальный словарь
        global d
        d = {}
        # Fucking magic!!!!! (.sender(), .indexAt())
        # Определяем из какой строки была кнопка вызвавшая функцию
        button = self.sender()
        i = self.tableWidget_db.indexAt(button.pos()).row()
        # получаем uin из таблицы
        uin = self.tableWidget_db.item(i, 8).text()
        # записываем словарь из БД в глобальный словарь
        d = read_d_from_db_bta(uin)
        # открываем окно истории болезни
        # self.window_card = Ui_PatientCard()
        # self.window_card.show()
        # self.hide()

    def open_patient_card_from_archive(self):
        # Очищаем глобальный словарь
        global d
        d = {}
        # Fucking magic!!!!! (.sender(), .indexAt())
        # Определяем из какой строки была кнопка вызвавшая функцию
        button = self.sender()
        i = self.tableWidget_archive_bd.indexAt(button.pos()).row()
        # получаем uin из таблицы
        uin = self.tableWidget_archive_bd.item(i, 8).text()
        # записываем словарь из БД в глобальный словарь
        d = read_d_from_db_bta(uin)
        # открываем окно истории болезни
        # self.window_card = Ui_PatientCard()
        # self.window_card.show()
        # self.hide()

    def show_active_cases(self):
        # определяем критерии поиска
        find = self.lineEdit_find_active.text().lower()
        # читаем БД и получаем список кортежей активных случаев
        data = read_db_active_cases_bta()
        # data = read_db_active_cases()
        # проверяем, что данные есть
        if data is not None:
            # сортируем все по алфавиту
            data = sorted(
                data,
                key=lambda x: x[3],
                reverse=False
            )
            # по чек-боксам сортируем дополнительно
            # по дате поступления
            if self.radioButton_date.isChecked():
                data = sorted(
                    data,
                    key=lambda x: c_date(x[1]),
                    reverse=False
                )
            # по врачу
            elif self.radioButton_doc.isChecked():
                data.sort(
                    key=lambda x: x[4],
                    reverse=False
                )
            # собираем новый список кортежей по критериям поиска
            new_data = []
            for i in data:
                if find in i[3].lower():
                    new_data.append(i)
            data = new_data
            # устанавливаем количество строк в таблице равное
            # количеству найденных случаев
            self.tableWidget_db.setRowCount(len(data))
            # формируем подпись о полученных данных
            self.label_act_pt.setText(f'Найдено {len(data)} активных случаев')
            # формируем "Item"s для каждой клетки таблицы
            for i in range(len(data)):
                # создаем кнопку
                button = QPushButton('Открыть')
                # создаем иконку
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/icon/icons/sticky_note_2_white_36dp.svg"),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)
                button.setIcon(icon)
                button.setStyleSheet(main_styles.button_del)
                # соединяем кнопку с функцией открытия истории болезни
                button.clicked.connect(self.open_patient_card)
                # определяем полноту истории
                fullness = read_fullness_db_bta(data[i][6])
                # fullness = read_fullness_db(data[i][8])
                percent = calc_percent_fullness(fullness, bta=True)
                progress = QProgressBar()
                progress.setValue(percent)
                progress.setTextVisible(False)
                progress.setStyleSheet(main_styles.progress)
                # заполняем ячейки
                # первая колонка - прогресс-бар
                self.tableWidget_db.setCellWidget(i, 0, progress)
                # вторая колонка - кнопка
                self.tableWidget_db.setCellWidget(i, 1, button)
                # третья колонка - тип госпитализации
                if data[i][0] == 'БТ - круглосуточный':
                    self.tableWidget_db.setItem(i, 2, QTW_Item('КС'))
                elif data[i][0] == 'БТ - дневной':
                    self.tableWidget_db.setItem(i, 2, QTW_Item('ДС'))
                else:
                    self.tableWidget_db.setItem(i, 2, QTW_Item('UN'))
                # с 4й по 8ю
                self.tableWidget_db.setItem(i, 3, QTW_Item(data[i][1]))
                self.tableWidget_db.setItem(i, 4, QTW_Item(data[i][2]))
                self.tableWidget_db.setItem(i, 5, QTW_Item(data[i][3]))
                self.tableWidget_db.setItem(i, 6, QTW_Item(data[i][4]))
                # девятая колонка - нужда в ЛН
                if data[i][5] == '1':
                    self.tableWidget_db.setItem(i, 7, QTW_Item('+'))
                else:
                    self.tableWidget_db.setItem(i, 7, QTW_Item(' '))
                # 10
                self.tableWidget_db.setItem(i, 8, QTW_Item(data[i][6]))
        else:
            self.label_act_pt.setText('Не найден ни один активный случай')

    def show_archive_cases(self):
        # определяем критерии поиска
        dates = (
            c_date(self.dateEdit_find_1.dateTime().toString('dd.MM.yyyy')),
            c_date(self.dateEdit_find_2.dateTime().toString('dd.MM.yyyy')))
        find = self.lineEdit.text().lower()
        # читаем БД и получаем список кортежей случаев
        data = read_db_archive_cases_bta()
        # сортируем список
        # проверяем, что данные есть
        if data is not None:
            # сортируем все по алфавиту
            data = sorted(
                data,
                key=lambda x: x[3],
                reverse=False)
            # и по дате выписки
            data = sorted(
                data,
                key=lambda x: c_date(x[2]),
                reverse=False)
            # корректируем список кортежей
            new_data = []
            # определяем критерий поиска по датам
            if self.radioButton_admission.isChecked():
                j = 1  # дата поступления
            elif self.radioButton_discharge.isChecked():
                j = 2  # дата выписки
            # собираем новый список кортежей по критериям поиска
            for i in data:
                if dates[0] <= c_date(i[j]) <= dates[1]:
                    if find in i[3].lower():
                        new_data.append(i)
            data = new_data

            # устанавливаем количество строк в таблице равное
            # количеству найденных случаев
            self.tableWidget_archive_bd.setRowCount(len(data))
            # формируем подпись о полученных данных
            self.label_archive_pt.setText(f'Найдено {len(data)} историй болезни')
            # формируем "Item"s для каждой клетки таблицы
            for i in range(len(data)):
                # создаем кнопку
                button = QPushButton('open')
                # создаем иконку
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/icon/icons/sticky_note_2_white_36dp.svg"),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)
                button.setIcon(icon)
                button.setStyleSheet(main_styles.button_del)
                # соединяем кнопку с функцией открытия истории болезни
                button.clicked.connect(self.open_patient_card_from_archive)
                # заполняем ячейки
                # первая колонка - кнопка
                self.tableWidget_archive_bd.setCellWidget(i, 0, button)
                # вторая колонка - тип госпитализации
                if data[i][0] == 'БТ - круглосуточный':
                    self.tableWidget_archive_bd.setItem(i, 1, QTW_Item('КС'))
                elif data[i][0] == 'БТ - дневной':
                    self.tableWidget_archive_bd.setItem(i, 1, QTW_Item('ДС'))
                else:
                    self.tableWidget_archive_bd.setItem(i, 1, QTW_Item('UN'))
                # с 3й по 7ю
                self.tableWidget_archive_bd.setItem(i, 2, QTW_Item(data[i][1]))
                self.tableWidget_archive_bd.setItem(i, 3, QTW_Item(data[i][2]))
                self.tableWidget_archive_bd.setItem(i, 4, QTW_Item(data[i][3]))
                self.tableWidget_archive_bd.setItem(i, 5, QTW_Item(data[i][4]))
                self.tableWidget_archive_bd.setItem(i, 6, QTW_Item(data[i][5]))
                # восьмая колонка - нужда в ЛН
                if data[i][6] == '1':
                    self.tableWidget_archive_bd.setItem(i, 7, QTW_Item('+'))
                else:
                    self.tableWidget_archive_bd.setItem(i, 7, QTW_Item(' '))
                # 9
                self.tableWidget_archive_bd.setItem(i, 8, QTW_Item(data[i][7]))
        else:
            self.label_act_pt.setText('Не найден ни один случай')

    def open_report_manager(self):
        pass
