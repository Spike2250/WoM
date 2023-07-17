import sys  # sys нужен для передачи argv в QApplication
from PySide6 import QtWidgets
from wom.GUI.windows.win_aggregator import windows


def show():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    w = windows['bta']['main_window'](windows)
    w.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
