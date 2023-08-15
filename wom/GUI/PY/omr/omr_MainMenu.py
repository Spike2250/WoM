# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'omr_MainMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import res_main_rc

class Ui_omr_main_menu(object):
    def setupUi(self, omr_main_menu):
        if not omr_main_menu.objectName():
            omr_main_menu.setObjectName(u"omr_main_menu")
        omr_main_menu.resize(1230, 769)
        omr_main_menu.setMinimumSize(QSize(1230, 700))
        omr_main_menu.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(190, 190, 190, 255));\n"
"font-family: Roboto;")
        self.verticalLayout_7 = QVBoxLayout(omr_main_menu)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.main_frame = QFrame(omr_main_menu)
        self.main_frame.setObjectName(u"main_frame")
        self.verticalLayout_6 = QVBoxLayout(self.main_frame)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.top_panel = QFrame(self.main_frame)
        self.top_panel.setObjectName(u"top_panel")
        self.top_panel.setMaximumSize(QSize(16777215, 150))
        self.gridLayout_3 = QGridLayout(self.top_panel)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 5, 4, 1)

        self.labelLogo = QLabel(self.top_panel)
        self.labelLogo.setObjectName(u"labelLogo")
        self.labelLogo.setMaximumSize(QSize(250, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(50, 98, 115, 190))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(226, 212, 193, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(60, 145, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(36, 119, 227, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(6, 47, 100, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(8, 62, 133, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(133, 174, 227, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        brush9 = QBrush(QColor(255, 255, 220, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
        brush10 = QBrush(QColor(50, 98, 115, 95))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush11 = QBrush(QColor(12, 94, 200, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.labelLogo.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(9)
        font.setBold(False)
        self.labelLogo.setFont(font)
        self.labelLogo.setStyleSheet(u"background-color: none;\n"
"color: rgba(50, 98, 115, 190);")

        self.gridLayout_3.addWidget(self.labelLogo, 0, 6, 2, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 1, 3, 1)

        self.add_new_patient = QPushButton(self.top_panel)
        self.add_new_patient.setObjectName(u"add_new_patient")
        self.add_new_patient.setMinimumSize(QSize(0, 45))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
        brush12 = QBrush(QColor(255, 255, 255, 128))
        brush12.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        brush13 = QBrush(QColor(238, 238, 238, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush13)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.add_new_patient.setPalette(palette1)
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.add_new_patient.setFont(font1)
        self.add_new_patient.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 14pt;\n"
"color: White;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"background-color: #EEEEEE;\n"
"border: 1px solid rgba(50, 98, 115, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icons/person_add_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_new_patient.setIcon(icon)
        self.add_new_patient.setIconSize(QSize(32, 32))

        self.gridLayout_3.addWidget(self.add_new_patient, 1, 2, 2, 1)

        self.autorised_user = QLabel(self.top_panel)
        self.autorised_user.setObjectName(u"autorised_user")
        self.autorised_user.setStyleSheet(u"color: rgba(50, 98, 115, 255);\n"
"background-color: transparent")

        self.gridLayout_3.addWidget(self.autorised_user, 0, 0, 1, 3)

        self.user_profile = QPushButton(self.top_panel)
        self.user_profile.setObjectName(u"user_profile")
        self.user_profile.setEnabled(False)
        self.user_profile.setMinimumSize(QSize(0, 30))
        self.user_profile.setMaximumSize(QSize(200, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(14)
        self.user_profile.setFont(font2)
        self.user_profile.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 14pt;\n"
"color: White;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/manage_accounts_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.user_profile.setIcon(icon1)
        self.user_profile.setIconSize(QSize(32, 32))

        self.gridLayout_3.addWidget(self.user_profile, 1, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.top_panel)

        self.central_panel = QHBoxLayout()
        self.central_panel.setObjectName(u"central_panel")
        self.left_panel = QFrame(self.main_frame)
        self.left_panel.setObjectName(u"left_panel")
        self.left_panel.setMaximumSize(QSize(220, 16777215))
        self.left_panel.setStyleSheet(u"background-color: rgba(50, 98, 115, 40);\n"
"font-size: 11pt;")
        self.verticalLayout = QVBoxLayout(self.left_panel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.help_page = QPushButton(self.left_panel)
        self.help_page.setObjectName(u"help_page")
        self.help_page.setEnabled(False)
        self.help_page.setFont(font2)
        self.help_page.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 14pt;\n"
"color: White;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/info_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.help_page.setIcon(icon2)
        self.help_page.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.help_page)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.schedule = QPushButton(self.left_panel)
        self.schedule.setObjectName(u"schedule")
        self.schedule.setEnabled(False)
        self.schedule.setFont(font2)
        self.schedule.setLayoutDirection(Qt.RightToLeft)
        self.schedule.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 14pt;\n"
"color: White;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/calendar_month_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.schedule.setIcon(icon3)
        self.schedule.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.schedule)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.almanac = QPushButton(self.left_panel)
        self.almanac.setObjectName(u"almanac")
        self.almanac.setMinimumSize(QSize(0, 31))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        brush14 = QBrush(QColor(50, 98, 115, 150))
        brush14.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        brush15 = QBrush(QColor(50, 98, 115, 40))
        brush15.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
        brush16 = QBrush(QColor(50, 98, 115, 75))
        brush16.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush16)
#endif
        self.almanac.setPalette(palette2)
        self.almanac.setFont(font1)
        self.almanac.setLayoutDirection(Qt.RightToLeft)
        self.almanac.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 14pt;\n"
"color: White;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/auto_stories_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.almanac.setIcon(icon4)
        self.almanac.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.almanac)

        self.norm_docs = QPushButton(self.left_panel)
        self.norm_docs.setObjectName(u"norm_docs")
        self.norm_docs.setEnabled(False)
        self.norm_docs.setFont(font2)
        self.norm_docs.setLayoutDirection(Qt.RightToLeft)
        self.norm_docs.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 14pt;\n"
"color: White;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/book_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.norm_docs.setIcon(icon5)
        self.norm_docs.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.norm_docs)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.partners = QPushButton(self.left_panel)
        self.partners.setObjectName(u"partners")
        self.partners.setEnabled(False)
        self.partners.setFont(font2)
        self.partners.setLayoutDirection(Qt.RightToLeft)
        self.partners.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 14pt;\n"
"color: White;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icons/sticky_note_2_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.partners.setIcon(icon6)
        self.partners.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.partners)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.return_back = QPushButton(self.left_panel)
        self.return_back.setObjectName(u"return_back")
        self.return_back.setEnabled(True)
        self.return_back.setMinimumSize(QSize(0, 30))
        self.return_back.setMaximumSize(QSize(200, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(11)
        self.return_back.setFont(font3)
        self.return_back.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(112, 38, 50, 190);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(112, 38, 50, 255);\n"
"border: 2px solid rgba(145, 47, 64, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(145, 47, 64, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"background-color: #EEEEEE;\n"
"border: 1px solid rgba(112, 38, 50, 255);\n"
"}\n"
"\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icons/west_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.return_back.setIcon(icon7)
        self.return_back.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.return_back)

        self.label_111 = QLabel(self.left_panel)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setMinimumSize(QSize(200, 200))
        self.label_111.setMaximumSize(QSize(200, 200))
        self.label_111.setStyleSheet(u"color: rgba(50, 98, 115, 255)")
        self.label_111.setScaledContents(True)
        self.label_111.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_111)


        self.central_panel.addWidget(self.left_panel)

        self.tabWidget = QTabWidget(self.main_frame)
        self.tabWidget.setObjectName(u"tabWidget")
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(13)
        font4.setBold(True)
        self.tabWidget.setFont(font4)
        self.tabWidget.setStyleSheet(u"QTabWidget:pane {\n"
"border: 1px solid rgba(50, 98, 115, 255);\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 12pt;\n"
"color: White;\n"
"border: 1px solid rgba(50, 98, 115, 255);\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 1px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(50, 98, 115, 255);\n"
"}")
        self.tabWidget.setIconSize(QSize(28, 28))
        self.actual = QWidget()
        self.actual.setObjectName(u"actual")
        self.verticalLayout_8 = QVBoxLayout(self.actual)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_actual = QFrame(self.actual)
        self.frame_actual.setObjectName(u"frame_actual")
        self.verticalLayout_2 = QVBoxLayout(self.frame_actual)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.refreshing_active_list = QFrame(self.frame_actual)
        self.refreshing_active_list.setObjectName(u"refreshing_active_list")
        self.refreshing_active_list.setStyleSheet(u"background-color: rgba(50, 98, 115, 40);\n"
"font-size: 11pt;")
        self.gridLayout = QGridLayout(self.refreshing_active_list)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_sort = QGroupBox(self.refreshing_active_list)
        self.groupBox_sort.setObjectName(u"groupBox_sort")
        self.groupBox_sort.setMinimumSize(QSize(0, 50))
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setItalic(False)
        self.groupBox_sort.setFont(font5)
        self.groupBox_sort.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);")
        self.gridLayout_5 = QGridLayout(self.groupBox_sort)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(1)
        self.gridLayout_5.setContentsMargins(-1, 1, -1, 1)
        self.radioButton_room = QRadioButton(self.groupBox_sort)
        self.radioButton_room.setObjectName(u"radioButton_room")
        self.radioButton_room.setFont(font5)
        self.radioButton_room.setStyleSheet(u"QRadioButton {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"QRadioButton:checked {\n"
"   color: #702632;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")

        self.gridLayout_5.addWidget(self.radioButton_room, 0, 2, 1, 1)

        self.radioButton_date = QRadioButton(self.groupBox_sort)
        self.radioButton_date.setObjectName(u"radioButton_date")
        self.radioButton_date.setFont(font5)
        self.radioButton_date.setStyleSheet(u"QRadioButton {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"QRadioButton:checked {\n"
"   color: #702632;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")
        self.radioButton_date.setChecked(True)

        self.gridLayout_5.addWidget(self.radioButton_date, 0, 0, 1, 1)

        self.radioButton_doc = QRadioButton(self.groupBox_sort)
        self.radioButton_doc.setObjectName(u"radioButton_doc")
        self.radioButton_doc.setFont(font5)
        self.radioButton_doc.setLayoutDirection(Qt.LeftToRight)
        self.radioButton_doc.setStyleSheet(u"QRadioButton {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"QRadioButton:checked {\n"
"   color: #702632;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")
        self.radioButton_doc.setChecked(False)

        self.gridLayout_5.addWidget(self.radioButton_doc, 0, 1, 1, 1)

        self.radioButton_name = QRadioButton(self.groupBox_sort)
        self.radioButton_name.setObjectName(u"radioButton_name")
        self.radioButton_name.setFont(font5)
        self.radioButton_name.setStyleSheet(u"QRadioButton {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"QRadioButton:checked {\n"
"   color: #702632;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")

        self.gridLayout_5.addWidget(self.radioButton_name, 0, 3, 1, 1)


        self.gridLayout.addWidget(self.groupBox_sort, 0, 0, 1, 1)

        self.find_patient = QPushButton(self.refreshing_active_list)
        self.find_patient.setObjectName(u"find_patient")
        self.find_patient.setMaximumSize(QSize(150, 16777215))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.find_patient.setPalette(palette3)
        self.find_patient.setFont(font5)
        self.find_patient.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icon/icons/search_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.find_patient.setIcon(icon8)
        self.find_patient.setIconSize(QSize(26, 26))

        self.gridLayout.addWidget(self.find_patient, 1, 1, 1, 2)

        self.lineEdit_find_active = QLineEdit(self.refreshing_active_list)
        self.lineEdit_find_active.setObjectName(u"lineEdit_find_active")
        font6 = QFont()
        font6.setFamilies([u"Roboto"])
        font6.setPointSize(11)
        font6.setBold(True)
        font6.setItalic(False)
        self.lineEdit_find_active.setFont(font6)
        self.lineEdit_find_active.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"")

        self.gridLayout.addWidget(self.lineEdit_find_active, 1, 0, 1, 1)

        self.refresh_pt_list = QPushButton(self.refreshing_active_list)
        self.refresh_pt_list.setObjectName(u"refresh_pt_list")
        self.refresh_pt_list.setMinimumSize(QSize(0, 50))
        self.refresh_pt_list.setMaximumSize(QSize(150, 16777215))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.refresh_pt_list.setPalette(palette4)
        self.refresh_pt_list.setFont(font5)
        self.refresh_pt_list.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icon/icons/autorenew_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refresh_pt_list.setIcon(icon9)
        self.refresh_pt_list.setIconSize(QSize(26, 26))

        self.gridLayout.addWidget(self.refresh_pt_list, 0, 1, 1, 2)

        self.tableWidget_db = QTableWidget(self.refreshing_active_list)
        if (self.tableWidget_db.columnCount() < 11):
            self.tableWidget_db.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_db.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_db.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_db.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_db.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_db.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_db.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_db.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_db.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_db.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_db.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_db.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tableWidget_db.setObjectName(u"tableWidget_db")
        self.tableWidget_db.setFont(font5)
        self.tableWidget_db.setStyleSheet(u"QTableWidget {\n"
"   selection-background-color: rgba(50, 98, 115, 120);\n"
"   background-color: rgba(50, 98, 115, 40);\n"
"   color: #FFFFFF;\n"
"   font-weight: Normal;\n"
"   border-color: #000000;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"   background-color: rgba(50, 98, 115, 220);\n"
"   color: #FFFFFF;\n"
"   font-family: Roboto;\n"
"   font-size: 15px;\n"
"   font-weight: Normal;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"   selection-background-color: rgba(50, 98, 115, 120);\n"
"   background-color: rgba(50, 98, 115, 40);\n"
"   color: #13242B;\n"
"   font-size: 15px;\n"
"   font-weight: Normal;\n"
"   border-style: none;\n"
"   border-bottom: #13242B;\n"
"}\n"
"\n"
"QScrollBar {\n"
"background-color: rgba(50, 98, 115, 70);\n"
"}\n"
"")
        self.tableWidget_db.horizontalHeader().setDefaultSectionSize(100)

        self.gridLayout.addWidget(self.tableWidget_db, 5, 0, 1, 4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_print_patient_list = QPushButton(self.refreshing_active_list)
        self.pushButton_print_patient_list.setObjectName(u"pushButton_print_patient_list")
        self.pushButton_print_patient_list.setMaximumSize(QSize(16777215, 16777215))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush17 = QBrush(QColor(50, 98, 115, 130))
        brush17.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette5.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette5.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette5.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette5.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.pushButton_print_patient_list.setPalette(palette5)
        self.pushButton_print_patient_list.setFont(font5)
        self.pushButton_print_patient_list.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_print_patient_list.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 130);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/icon/icons/print_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_print_patient_list.setIcon(icon10)
        self.pushButton_print_patient_list.setIconSize(QSize(20, 20))

        self.verticalLayout_5.addWidget(self.pushButton_print_patient_list)

        self.pushButton_print_patient_list_2 = QPushButton(self.refreshing_active_list)
        self.pushButton_print_patient_list_2.setObjectName(u"pushButton_print_patient_list_2")
        self.pushButton_print_patient_list_2.setMaximumSize(QSize(250, 16777215))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush17)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette6.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush17)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush17)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush17)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush17)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush17)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush17)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush17)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.pushButton_print_patient_list_2.setPalette(palette6)
        self.pushButton_print_patient_list_2.setFont(font5)
        self.pushButton_print_patient_list_2.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_print_patient_list_2.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 130);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}")
        self.pushButton_print_patient_list_2.setIcon(icon10)
        self.pushButton_print_patient_list_2.setIconSize(QSize(20, 20))

        self.verticalLayout_5.addWidget(self.pushButton_print_patient_list_2)

        self.pushButton_print_lists = QPushButton(self.refreshing_active_list)
        self.pushButton_print_lists.setObjectName(u"pushButton_print_lists")
        self.pushButton_print_lists.setFont(font5)
        self.pushButton_print_lists.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 130);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}")
        self.pushButton_print_lists.setIcon(icon10)
        self.pushButton_print_lists.setIconSize(QSize(20, 20))

        self.verticalLayout_5.addWidget(self.pushButton_print_lists)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 3, 2, 1)

        self.label_act_pt = QLabel(self.refreshing_active_list)
        self.label_act_pt.setObjectName(u"label_act_pt")
        self.label_act_pt.setMinimumSize(QSize(250, 0))
        self.label_act_pt.setScaledContents(False)
        self.label_act_pt.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_act_pt, 4, 0, 1, 4)

        self.checkBox_alone_doc = QCheckBox(self.refreshing_active_list)
        self.checkBox_alone_doc.setObjectName(u"checkBox_alone_doc")
        self.checkBox_alone_doc.setEnabled(False)
        self.checkBox_alone_doc.setFont(font5)
        self.checkBox_alone_doc.setStyleSheet(u"background-color: transparent")

        self.gridLayout.addWidget(self.checkBox_alone_doc, 2, 1, 1, 3)


        self.verticalLayout_2.addWidget(self.refreshing_active_list)


        self.verticalLayout_8.addWidget(self.frame_actual)

        icon11 = QIcon()
        icon11.addFile(u":/icon/icons/view_list_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.actual, icon11, "")
        self.archive = QWidget()
        self.archive.setObjectName(u"archive")
        self.verticalLayout_9 = QVBoxLayout(self.archive)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_archive = QFrame(self.archive)
        self.frame_archive.setObjectName(u"frame_archive")
        self.verticalLayout_4 = QVBoxLayout(self.frame_archive)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.archive_list = QFrame(self.frame_archive)
        self.archive_list.setObjectName(u"archive_list")
        self.archive_list.setStyleSheet(u"background-color: rgba(50, 98, 115, 40);\n"
"font-size: 11pt;")
        self.gridLayout_2 = QGridLayout(self.archive_list)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setContentsMargins(7, 7, 7, 7)
        self.pushButtonOpenArchive = QPushButton(self.archive_list)
        self.pushButtonOpenArchive.setObjectName(u"pushButtonOpenArchive")
        self.pushButtonOpenArchive.setMaximumSize(QSize(150, 16777215))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette7.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
        palette7.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        palette7.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette7.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.pushButtonOpenArchive.setPalette(palette7)
        self.pushButtonOpenArchive.setFont(font5)
        self.pushButtonOpenArchive.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}")
        self.pushButtonOpenArchive.setIcon(icon8)
        self.pushButtonOpenArchive.setIconSize(QSize(26, 26))

        self.gridLayout_2.addWidget(self.pushButtonOpenArchive, 4, 2, 2, 1)

        self.lineEdit = QLineEdit(self.archive_list)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font6)
        self.lineEdit.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit, 4, 0, 2, 2)

        self.label_archive_pt = QLabel(self.archive_list)
        self.label_archive_pt.setObjectName(u"label_archive_pt")
        self.label_archive_pt.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_archive_pt, 6, 0, 1, 3)

        self.pushButton_report_manager = QPushButton(self.archive_list)
        self.pushButton_report_manager.setObjectName(u"pushButton_report_manager")
        self.pushButton_report_manager.setEnabled(False)
        self.pushButton_report_manager.setFont(font5)
        self.pushButton_report_manager.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")

        self.gridLayout_2.addWidget(self.pushButton_report_manager, 0, 3, 2, 1)

        self.groupBox_sort_archive = QGroupBox(self.archive_list)
        self.groupBox_sort_archive.setObjectName(u"groupBox_sort_archive")
        self.groupBox_sort_archive.setMinimumSize(QSize(0, 50))
        self.groupBox_sort_archive.setFont(font5)
        self.groupBox_sort_archive.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);")
        self.gridLayout_6 = QGridLayout(self.groupBox_sort_archive)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(1)
        self.gridLayout_6.setContentsMargins(-1, 1, -1, 1)
        self.radioButton_discharge = QRadioButton(self.groupBox_sort_archive)
        self.radioButton_discharge.setObjectName(u"radioButton_discharge")
        self.radioButton_discharge.setFont(font5)
        self.radioButton_discharge.setStyleSheet(u"QRadioButton {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"QRadioButton:checked {\n"
"   color: #702632;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")
        self.radioButton_discharge.setChecked(True)

        self.gridLayout_6.addWidget(self.radioButton_discharge, 0, 1, 1, 1)

        self.radioButton_admission = QRadioButton(self.groupBox_sort_archive)
        self.radioButton_admission.setObjectName(u"radioButton_admission")
        self.radioButton_admission.setFont(font5)
        self.radioButton_admission.setStyleSheet(u"QRadioButton {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"QRadioButton:checked {\n"
"   color: #702632;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")
        self.radioButton_admission.setChecked(False)

        self.gridLayout_6.addWidget(self.radioButton_admission, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_sort_archive, 0, 1, 2, 2)

        self.dates = QHBoxLayout()
        self.dates.setObjectName(u"dates")
        self.label_3 = QLabel(self.archive_list)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.RightToLeft)
        self.label_3.setStyleSheet(u"background-color: none;\n"
"color: #13242B;\n"
"")

        self.dates.addWidget(self.label_3)

        self.dateEdit_find_1 = QDateEdit(self.archive_list)
        self.dateEdit_find_1.setObjectName(u"dateEdit_find_1")
        self.dateEdit_find_1.setFont(font6)
        self.dateEdit_find_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"")

        self.dates.addWidget(self.dateEdit_find_1)

        self.label_4 = QLabel(self.archive_list)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLayoutDirection(Qt.RightToLeft)
        self.label_4.setStyleSheet(u"background-color: none;\n"
"color: #13242B;\n"
"")

        self.dates.addWidget(self.label_4)

        self.dateEdit_find_2 = QDateEdit(self.archive_list)
        self.dateEdit_find_2.setObjectName(u"dateEdit_find_2")
        self.dateEdit_find_2.setFont(font6)
        self.dateEdit_find_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"")

        self.dates.addWidget(self.dateEdit_find_2)


        self.gridLayout_2.addLayout(self.dates, 0, 0, 1, 1)

        self.change_dates = QFrame(self.archive_list)
        self.change_dates.setObjectName(u"change_dates")
        self.verticalLayout_3 = QVBoxLayout(self.change_dates)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_month = QPushButton(self.change_dates)
        self.pushButton_month.setObjectName(u"pushButton_month")
        self.pushButton_month.setMinimumSize(QSize(150, 20))
        self.pushButton_month.setFont(font5)
        self.pushButton_month.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_month)

        self.pushButton_previous_month = QPushButton(self.change_dates)
        self.pushButton_previous_month.setObjectName(u"pushButton_previous_month")
        self.pushButton_previous_month.setMinimumSize(QSize(150, 20))
        self.pushButton_previous_month.setFont(font5)
        self.pushButton_previous_month.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_previous_month)

        self.pushButton_year = QPushButton(self.change_dates)
        self.pushButton_year.setObjectName(u"pushButton_year")
        self.pushButton_year.setMinimumSize(QSize(150, 20))
        self.pushButton_year.setFont(font5)
        self.pushButton_year.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 11pt;\n"
"color: White;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_year)


        self.gridLayout_2.addWidget(self.change_dates, 1, 0, 3, 1)


        self.verticalLayout_4.addWidget(self.archive_list)

        self.tableWidget_archive_bd = QTableWidget(self.frame_archive)
        if (self.tableWidget_archive_bd.columnCount() < 9):
            self.tableWidget_archive_bd.setColumnCount(9)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_archive_bd.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_archive_bd.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_archive_bd.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_archive_bd.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_archive_bd.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_archive_bd.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_archive_bd.setHorizontalHeaderItem(6, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_archive_bd.setHorizontalHeaderItem(7, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_archive_bd.setHorizontalHeaderItem(8, __qtablewidgetitem19)
        self.tableWidget_archive_bd.setObjectName(u"tableWidget_archive_bd")
        font7 = QFont()
        font7.setFamilies([u"Roboto"])
        font7.setBold(False)
        font7.setItalic(False)
        self.tableWidget_archive_bd.setFont(font7)
        self.tableWidget_archive_bd.setStyleSheet(u"QTableWidget {\n"
"   selection-background-color: rgba(50, 98, 115, 120);\n"
"   background-color: rgba(50, 98, 115, 40);\n"
"   color: #FFFFFF;\n"
"   font-weight: Normal;\n"
"   border-color: #000000;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"   background-color: rgba(50, 98, 115, 220);\n"
"   color: #FFFFFF;\n"
"   font-family: Roboto;\n"
"   font-size: 15px;\n"
"   font-weight: Normal;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"   selection-background-color: rgba(50, 98, 115, 120);\n"
"   background-color: rgba(50, 98, 115, 40);\n"
"   color: #13242B;\n"
"   font-size: 15px;\n"
"   font-weight: Normal;\n"
"   border-style: none;\n"
"   border-bottom: #13242B;\n"
"}\n"
"\n"
"QScrollBar {\n"
"background-color: rgba(50, 98, 115, 70);\n"
"}\n"
"")
        self.tableWidget_archive_bd.horizontalHeader().setDefaultSectionSize(100)

        self.verticalLayout_4.addWidget(self.tableWidget_archive_bd)


        self.verticalLayout_9.addWidget(self.frame_archive)

        icon12 = QIcon()
        icon12.addFile(u":/icon/icons/person_search_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.archive, icon12, "")

        self.central_panel.addWidget(self.tabWidget)


        self.verticalLayout_6.addLayout(self.central_panel)


        self.verticalLayout_7.addWidget(self.main_frame)


        self.retranslateUi(omr_main_menu)

        self.partners.setDefault(False)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(omr_main_menu)
    # setupUi

    def retranslateUi(self, omr_main_menu):
        omr_main_menu.setWindowTitle(QCoreApplication.translate("omr_main_menu", u"Form", None))
        self.labelLogo.setText(QCoreApplication.translate("omr_main_menu", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">World of Medicine</span><span style=\" font-size:10pt;\"><br/></span>\u043e\u0442\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u043c\u0435\u0434\u0438\u0446\u0438\u043d\u0441\u043a\u043e\u0439 \u0440\u0435\u0430\u0431\u0438\u043b\u0438\u0442\u0430\u0446\u0438\u0438<br/>\u0432\u0440\u0430\u0447-\u0424\u0420\u041c (v.1.2 alfa)</p></body></html>", None))
        self.add_new_patient.setText(QCoreApplication.translate("omr_main_menu", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0441\u043b\u0443\u0447\u0430\u0439 \u0433\u043e\u0441\u043f\u0438\u0442\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.autorised_user.setText("")
        self.user_profile.setText(QCoreApplication.translate("omr_main_menu", u"\u041b\u0438\u0447\u043d\u044b\u0439 \u043a\u0430\u0431\u0438\u043d\u0435\u0442", None))
        self.help_page.setText(QCoreApplication.translate("omr_main_menu", u"HELP", None))
        self.schedule.setText(QCoreApplication.translate("omr_main_menu", u"\u041f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435\n"
"\u0433\u043e\u0441\u043f\u0438\u0442\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0439", None))
        self.almanac.setText(QCoreApplication.translate("omr_main_menu", u"\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a", None))
        self.norm_docs.setText(QCoreApplication.translate("omr_main_menu", u"\u041d\u043e\u0440\u043c\u0430\u0442\u0438\u0432\u043d\u044b\u0435\n"
"\u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b", None))
        self.partners.setText(QCoreApplication.translate("omr_main_menu", u"\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044b \u043e\u0442\n"
"\u043f\u0430\u0440\u0442\u043d\u0435\u0440\u043e\u0432", None))
        self.return_back.setText(QCoreApplication.translate("omr_main_menu", u"\u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432 \u043c\u0435\u043d\u044e", None))
        self.label_111.setText(QCoreApplication.translate("omr_main_menu", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u0417\u0434\u0435\u0441\u044c<br/>\u043c\u043e\u0433\u043b\u0430 \u0431\u044b\u0442\u044c<br/>\u0412\u0430\u0448\u0430 \u0440\u0435\u043a\u043b\u0430\u043c\u0430<br/></span><span style=\" font-size:6pt;\">\u0428\u0443\u0442\u043a\u0430!<br/>\u041d\u0430\u0445\u0435\u0440 \u043d\u0438\u043a\u0430\u043a\u043e\u0439 \u0440\u0435\u043a\u043b\u0430\u043c\u044b!</span></p></body></html>", None))
        self.groupBox_sort.setTitle(QCoreApplication.translate("omr_main_menu", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.radioButton_room.setText(QCoreApplication.translate("omr_main_menu", u"\u043f\u043e \u043f\u0430\u043b\u0430\u0442\u0430\u043c", None))
        self.radioButton_date.setText(QCoreApplication.translate("omr_main_menu", u"\u043f\u043e \u0434\u0430\u0442\u0435 \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f", None))
        self.radioButton_doc.setText(QCoreApplication.translate("omr_main_menu", u"\u043f\u043e \u0432\u0440\u0430\u0447\u0430\u043c", None))
        self.radioButton_name.setText(QCoreApplication.translate("omr_main_menu", u"\u043f\u043e \u0430\u043b\u0444\u0430\u0432\u0438\u0442\u0443", None))
        self.find_patient.setText(QCoreApplication.translate("omr_main_menu", u"\u043d\u0430\u0439\u0442\u0438", None))
        self.lineEdit_find_active.setPlaceholderText(QCoreApplication.translate("omr_main_menu", u"\u043f\u043e\u0438\u0441\u043a\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None))
        self.refresh_pt_list.setText(QCoreApplication.translate("omr_main_menu", u"\u043e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        ___qtablewidgetitem = self.tableWidget_db.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("omr_main_menu", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435", None));
        ___qtablewidgetitem1 = self.tableWidget_db.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("omr_main_menu", u"\u0422\u0438\u043f", None));
        ___qtablewidgetitem2 = self.tableWidget_db.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("omr_main_menu", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0442.", None));
        ___qtablewidgetitem3 = self.tableWidget_db.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("omr_main_menu", u"\u041f\u0430\u043b\u0430\u0442\u0430", None));
        ___qtablewidgetitem4 = self.tableWidget_db.horizontalHeaderItem(5)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("omr_main_menu", u"\u0424\u0418\u041e \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None));
        ___qtablewidgetitem5 = self.tableWidget_db.horizontalHeaderItem(6)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("omr_main_menu", u"\u041c\u041a\u041110", None));
        ___qtablewidgetitem6 = self.tableWidget_db.horizontalHeaderItem(7)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("omr_main_menu", u"\u0412\u0440\u0430\u0447", None));
        ___qtablewidgetitem7 = self.tableWidget_db.horizontalHeaderItem(8)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("omr_main_menu", u"\u041b\u041d", None));
        ___qtablewidgetitem8 = self.tableWidget_db.horizontalHeaderItem(9)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("omr_main_menu", u"\u0421\u0442\u043e\u043b", None));
        ___qtablewidgetitem9 = self.tableWidget_db.horizontalHeaderItem(10)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("omr_main_menu", u"UIN", None));
        self.pushButton_print_patient_list.setText(QCoreApplication.translate("omr_main_menu", u"\u041f\u0435\u0447\u0430\u0442\u044c \u0441\u043f\u0438\u0441\u043a\u0430 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u043e\u0432", None))
        self.pushButton_print_patient_list_2.setText(QCoreApplication.translate("omr_main_menu", u"\u041f\u0435\u0447\u0430\u0442\u044c \u0441\u043f\u0438\u0441\u043a\u0430 \u0434\u043b\u044f \u0432\u044b\u043f\u0438\u0441\u043a\u0438", None))
        self.pushButton_print_lists.setText(QCoreApplication.translate("omr_main_menu", u"\u041f\u0435\u0447\u0430\u0442\u044c \u0438\u043d\u0434\u0438\u0432\u0438\u0434\u0443\u0430\u043b\u044c\u043d\u044b\u0445\n"
"\u0441\u043f\u0438\u0441\u043a\u043e\u0432 \u0434\u043b\u044f \u0432\u0440\u0430\u0447\u0435\u0439", None))
        self.label_act_pt.setText("")
        self.checkBox_alone_doc.setText(QCoreApplication.translate("omr_main_menu", u"\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u043c\u043e\u0438 \u0438\u0441\u0442\u043e\u0440\u0438\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.actual), QCoreApplication.translate("omr_main_menu", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0442\u0435\u043a\u0443\u0449\u0438\u0445 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u043e\u0432", None))
        self.pushButtonOpenArchive.setText(QCoreApplication.translate("omr_main_menu", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("omr_main_menu", u"\u043f\u043e\u0438\u0441\u043a\u043e\u0432\u0430\u044f \u0441\u0442\u0440\u043e\u043a\u0430", None))
        self.label_archive_pt.setText("")
        self.pushButton_report_manager.setText(QCoreApplication.translate("omr_main_menu", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440\n"
"\u043f\u0435\u0447\u0430\u0442\u0438 \u043e\u0442\u0447\u0435\u0442\u043e\u0432", None))
        self.groupBox_sort_archive.setTitle(QCoreApplication.translate("omr_main_menu", u"\u043f\u043e\u0438\u0441\u043a", None))
        self.radioButton_discharge.setText(QCoreApplication.translate("omr_main_menu", u"\u043f\u043e \u0434\u0430\u0442\u0435 \u0432\u044b\u043f\u0438\u0441\u043a\u0438", None))
        self.radioButton_admission.setText(QCoreApplication.translate("omr_main_menu", u"\u043f\u043e \u0434\u0430\u0442\u0435 \u043f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("omr_main_menu", u"<html><head/><body><p align=\"right\">\u043e\u0442</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("omr_main_menu", u"<html><head/><body><p align=\"right\">\u0434\u043e</p></body></html>", None))
        self.pushButton_month.setText(QCoreApplication.translate("omr_main_menu", u"\u0442\u0435\u043a\u0443\u0449\u0438\u0439 \u043c\u0435\u0441\u044f\u0446", None))
        self.pushButton_previous_month.setText(QCoreApplication.translate("omr_main_menu", u"\u043f\u0440\u0435\u0434\u044b\u0434\u0443\u0449\u0438\u0439 \u043c\u0435\u0441\u044f\u0446", None))
        self.pushButton_year.setText(QCoreApplication.translate("omr_main_menu", u"\u0442\u0435\u043a\u0443\u0449\u0438\u0439 \u0433\u043e\u0434", None))
        ___qtablewidgetitem10 = self.tableWidget_archive_bd.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("omr_main_menu", u"\u0422\u0438\u043f", None));
        ___qtablewidgetitem11 = self.tableWidget_archive_bd.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("omr_main_menu", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u0442.", None));
        ___qtablewidgetitem12 = self.tableWidget_archive_bd.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("omr_main_menu", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u043f.", None));
        ___qtablewidgetitem13 = self.tableWidget_archive_bd.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("omr_main_menu", u"\u0424\u0418\u041e \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None));
        ___qtablewidgetitem14 = self.tableWidget_archive_bd.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("omr_main_menu", u"\u041c\u041a\u041110", None));
        ___qtablewidgetitem15 = self.tableWidget_archive_bd.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("omr_main_menu", u"\u0412\u0440\u0430\u0447", None));
        ___qtablewidgetitem16 = self.tableWidget_archive_bd.horizontalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("omr_main_menu", u"\u041b\u041d", None));
        ___qtablewidgetitem17 = self.tableWidget_archive_bd.horizontalHeaderItem(8)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("omr_main_menu", u"UIN", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.archive), QCoreApplication.translate("omr_main_menu", u"\u0410\u0440\u0445\u0438\u0432 \u0438\u0441\u0442\u043e\u0440\u0438\u0439 \u0431\u043e\u043b\u0435\u0437\u043d\u0438", None))
    # retranslateUi

