import sys  # sys нужен для передачи argv в QApplication
from PySide6 import QtWidgets
from wom.GUI.windows.win_aggregator import windows


def show():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    w = windows['bta']['main_menu'](windows)
    w.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


# StyleSheet = """
# /* Панель заголовка */
#                 TitleBar {
#                     background-color: rgb(54, 157, 180);
#                 }
# /* Минимизировать кнопку `Максимальное выключение` Общий фон по умолчанию */
#                 #buttonMinimum,#buttonMaximum,#buttonClose, #buttonMy {
#                     border: none;
#                     background-color: rgb(54, 157, 180);
#                 }
# /* Зависание */
#                 #buttonMinimum:hover,#buttonMaximum:hover {
#                     background-color: rgb(48, 141, 162);
#                 }
#                 #buttonClose:hover {
#                     color: white;
#                     background-color: rgb(232, 17, 35);
#                 }
#                 #buttonMy:hover {
#                     color: white;
#                     background-color: green;   /* rgb(232, 17, 35) */
#                 }
# /* Мышь удерживать */
#                 #buttonMinimum:pressed,#buttonMaximum:pressed {
#                     background-color: rgb(44, 125, 144);
#                 }
#                 #buttonClose:pressed {
#                     color: white;
#                     background-color: rgb(161, 73, 92);
#                 }
#                 """


# def show():
#     app = QtWidgets.QApplication(sys.argv)
#     app.setStyleSheet(StyleSheet)
#     w = windows['Frameless']()
#     w.setWindowTitle('Тестовая строка заголовка')
#     # w.setWindowIcon(QIcon('Qt.ico'))
#     w.setWidget(windows['test'](w))  # Добавить свое окно
#     w.show()
#     sys.exit(app.exec_())
