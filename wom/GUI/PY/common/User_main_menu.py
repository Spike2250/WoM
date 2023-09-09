# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'User_main_menu.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from wom.GUI.widgets.my_pushButton import PushButton
import res_main_rc
import res_main_rc

class Ui_main_menu(object):
    def setupUi(self, main_menu):
        if not main_menu.objectName():
            main_menu.setObjectName(u"main_menu")
        main_menu.resize(1243, 807)
        main_menu.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(190, 190, 190, 255));\n"
"font-family: Roboto;")
        self.verticalLayout_4 = QVBoxLayout(main_menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(main_menu)
        self.main_frame.setObjectName(u"main_frame")
        self.gridLayout = QGridLayout(self.main_frame)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_save = PushButton(self.main_frame)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setEnabled(False)
        self.pushButton_save.setMinimumSize(QSize(150, 0))
        self.pushButton_save.setMaximumSize(QSize(16777215, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(50, 98, 115, 190))
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
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        brush7 = QBrush(QColor(133, 174, 227, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush9 = QBrush(QColor(255, 255, 255, 128))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        brush10 = QBrush(QColor(50, 98, 115, 150))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        brush11 = QBrush(QColor(50, 98, 115, 40))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        brush12 = QBrush(QColor(12, 94, 200, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush13 = QBrush(QColor(50, 98, 115, 75))
        brush13.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.pushButton_save.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_save.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.pushButton_save)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 2, 1, 1)

        self.logo_frame = QFrame(self.main_frame)
        self.logo_frame.setObjectName(u"logo_frame")
        self.logo_frame.setMaximumSize(QSize(16777215, 100))
        self.logo_frame.setStyleSheet(u"background-color: transparent;")
        self.gridLayout_3 = QGridLayout(self.logo_frame)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labelLogo = QLabel(self.logo_frame)
        self.labelLogo.setObjectName(u"labelLogo")
        palette1 = QPalette()
        brush14 = QBrush(QColor(112, 38, 50, 190))
        brush14.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush14)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush14)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush14)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush15 = QBrush(QColor(112, 38, 50, 95))
        brush15.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush15)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush14)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush14)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush14)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush15)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.labelLogo.setPalette(palette1)
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(9)
        font1.setBold(False)
        self.labelLogo.setFont(font1)
        self.labelLogo.setStyleSheet(u"background-color: none;\n"
"color: rgba(112, 38, 50, 190);")

        self.gridLayout_3.addWidget(self.labelLogo, 0, 0, 2, 1)


        self.gridLayout.addWidget(self.logo_frame, 0, 1, 1, 2)

        self.overview_frame = QFrame(self.main_frame)
        self.overview_frame.setObjectName(u"overview_frame")
        self.overview_frame.setStyleSheet(u"font-size: 9pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);\n"
"")
        self.verticalLayout = QVBoxLayout(self.overview_frame)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.label_overview = QLabel(self.overview_frame)
        self.label_overview.setObjectName(u"label_overview")
        self.label_overview.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_overview.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_overview)

        self.tableWidget_overview = QTableWidget(self.overview_frame)
        self.tableWidget_overview.setObjectName(u"tableWidget_overview")
        self.tableWidget_overview.setMinimumSize(QSize(600, 0))
        self.tableWidget_overview.setMaximumSize(QSize(600, 16777215))
        self.tableWidget_overview.setStyleSheet(u"QTableWidget {\n"
"   selection-background-color: rgba(50, 98, 115, 120);\n"
"   background-color: rgba(50, 98, 115, 40);\n"
"   color: #FFFFFF;\n"
"   font-weight: Normal;\n"
"   border-color: rgba(50, 98, 115, 255);\n"
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
        self.tableWidget_overview.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout.addWidget(self.tableWidget_overview)


        self.gridLayout.addWidget(self.overview_frame, 1, 2, 1, 1)

        self.logs_frame = QFrame(self.main_frame)
        self.logs_frame.setObjectName(u"logs_frame")
        self.logs_frame.setMaximumSize(QSize(16777215, 70))
        self.logs_frame.setStyleSheet(u"font-size: 9pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.logs_frame.setFrameShape(QFrame.HLine)
        self.horizontalLayout_6 = QHBoxLayout(self.logs_frame)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.label_status = QLabel(self.logs_frame)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setMinimumSize(QSize(0, 50))
        self.label_status.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_status.setFont(font2)
        self.label_status.setStyleSheet(u"background-color: rgba(50, 98, 115, 100);\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"")
        self.label_status.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_status)


        self.gridLayout.addWidget(self.logs_frame, 3, 1, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(28, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.frame_user_data = QFrame(self.main_frame)
        self.frame_user_data.setObjectName(u"frame_user_data")
        self.frame_user_data.setStyleSheet(u"background-color: transparent;")
        self.verticalLayout_2 = QVBoxLayout(self.frame_user_data)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.user_frame = QFrame(self.frame_user_data)
        self.user_frame.setObjectName(u"user_frame")
        self.user_frame.setMaximumSize(QSize(16777215, 120))
        self.user_frame.setStyleSheet(u"font-size: 9pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_2 = QGridLayout(self.user_frame)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_user = PushButton(self.user_frame)
        self.pushButton_user.setObjectName(u"pushButton_user")
        self.pushButton_user.setEnabled(True)
        self.pushButton_user.setMinimumSize(QSize(30, 30))
        self.pushButton_user.setMaximumSize(QSize(30, 30))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.pushButton_user.setPalette(palette2)
        self.pushButton_user.setFont(font)
        self.pushButton_user.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_user.setStyleSheet(u"QPushButton {\n"
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
        icon = QIcon()
        icon.addFile(u":/icon/icons/account_box_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_user.setIcon(icon)
        self.pushButton_user.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_user)

        self.pushButton_settings = PushButton(self.user_frame)
        self.pushButton_settings.setObjectName(u"pushButton_settings")
        self.pushButton_settings.setEnabled(True)
        self.pushButton_settings.setMinimumSize(QSize(30, 30))
        self.pushButton_settings.setMaximumSize(QSize(30, 30))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.pushButton_settings.setPalette(palette3)
        self.pushButton_settings.setFont(font)
        self.pushButton_settings.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_settings.setStyleSheet(u"QPushButton {\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/miscellaneous_services_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_settings.setIcon(icon1)
        self.pushButton_settings.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_settings)

        self.pushButton_analyse = PushButton(self.user_frame)
        self.pushButton_analyse.setObjectName(u"pushButton_analyse")
        self.pushButton_analyse.setEnabled(False)
        self.pushButton_analyse.setMinimumSize(QSize(30, 30))
        self.pushButton_analyse.setMaximumSize(QSize(30, 30))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.pushButton_analyse.setPalette(palette4)
        self.pushButton_analyse.setFont(font)
        self.pushButton_analyse.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_analyse.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/analytics_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_analyse.setIcon(icon2)
        self.pushButton_analyse.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_analyse)

        self.pushButton_achievements = PushButton(self.user_frame)
        self.pushButton_achievements.setObjectName(u"pushButton_achievements")
        self.pushButton_achievements.setEnabled(False)
        self.pushButton_achievements.setMinimumSize(QSize(30, 30))
        self.pushButton_achievements.setMaximumSize(QSize(30, 30))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette5.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.pushButton_achievements.setPalette(palette5)
        self.pushButton_achievements.setFont(font)
        self.pushButton_achievements.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_achievements.setStyleSheet(u"QPushButton {\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/conditions_FILL1_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_achievements.setIcon(icon3)
        self.pushButton_achievements.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_achievements)

        self.pushButton_statistic = PushButton(self.user_frame)
        self.pushButton_statistic.setObjectName(u"pushButton_statistic")
        self.pushButton_statistic.setEnabled(False)
        self.pushButton_statistic.setMinimumSize(QSize(30, 30))
        self.pushButton_statistic.setMaximumSize(QSize(30, 30))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush)
        palette6.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.pushButton_statistic.setPalette(palette6)
        self.pushButton_statistic.setFont(font)
        self.pushButton_statistic.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_statistic.setStyleSheet(u"QPushButton {\n"
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
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/auto_stories_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_statistic.setIcon(icon4)
        self.pushButton_statistic.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_statistic)

        self.pushButton_social = PushButton(self.user_frame)
        self.pushButton_social.setObjectName(u"pushButton_social")
        self.pushButton_social.setEnabled(False)
        self.pushButton_social.setMinimumSize(QSize(30, 30))
        self.pushButton_social.setMaximumSize(QSize(30, 30))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush)
        palette7.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette7.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette7.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette7.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette7.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.pushButton_social.setPalette(palette7)
        self.pushButton_social.setFont(font)
        self.pushButton_social.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_social.setStyleSheet(u"QPushButton {\n"
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
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/record_voice_over_FILL1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_social.setIcon(icon5)
        self.pushButton_social.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_social)

        self.pushButton_tickets = PushButton(self.user_frame)
        self.pushButton_tickets.setObjectName(u"pushButton_tickets")
        self.pushButton_tickets.setEnabled(True)
        self.pushButton_tickets.setMinimumSize(QSize(30, 30))
        self.pushButton_tickets.setMaximumSize(QSize(30, 30))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette8.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush)
        palette8.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette8.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette8.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette8.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette8.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette8.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.pushButton_tickets.setPalette(palette8)
        self.pushButton_tickets.setFont(font)
        self.pushButton_tickets.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_tickets.setStyleSheet(u"QPushButton {\n"
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
        icon6 = QIcon()
        icon6.addFile(u":/icon/icons/sticky_note_2_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_tickets.setIcon(icon6)
        self.pushButton_tickets.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_tickets)

        self.pushButton_logout = PushButton(self.user_frame)
        self.pushButton_logout.setObjectName(u"pushButton_logout")
        self.pushButton_logout.setEnabled(True)
        self.pushButton_logout.setMinimumSize(QSize(30, 30))
        self.pushButton_logout.setMaximumSize(QSize(30, 30))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette9.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush)
        palette9.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette9.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette9.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette9.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette9.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette9.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.pushButton_logout.setPalette(palette9)
        self.pushButton_logout.setFont(font)
        self.pushButton_logout.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_logout.setStyleSheet(u"QPushButton {\n"
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
        icon7 = QIcon()
        icon7.addFile(u":/icon/icons/west_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_logout.setIcon(icon7)
        self.pushButton_logout.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton_logout)


        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 2, 1, 3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label_user_img = QLabel(self.user_frame)
        self.label_user_img.setObjectName(u"label_user_img")
        self.label_user_img.setMinimumSize(QSize(85, 85))
        self.label_user_img.setMaximumSize(QSize(85, 85))
        self.label_user_img.setLayoutDirection(Qt.LeftToRight)
        self.label_user_img.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_user_img.setPixmap(QPixmap(u":/icon/icons/face_FILL1_wght400_GRAD0_opsz48.svg"))
        self.label_user_img.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label_user_img)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 5, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 4, 5, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 3, 5, 1, 1)

        self.label_7 = QLabel(self.user_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(110, 16777215))
        self.label_7.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_7, 2, 1, 1, 1)

        self.label_6 = QLabel(self.user_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(110, 16777215))
        self.label_6.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_6, 1, 1, 1, 1)

        self.label_4 = QLabel(self.user_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(110, 16777215))
        self.label_4.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_user_name = QLabel(self.user_frame)
        self.label_user_name.setObjectName(u"label_user_name")
        self.label_user_name.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_user_name, 0, 2, 1, 4)

        self.label_user_status = QLabel(self.user_frame)
        self.label_user_status.setObjectName(u"label_user_status")
        self.label_user_status.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_user_status, 2, 2, 1, 1)

        self.label_user_id = QLabel(self.user_frame)
        self.label_user_id.setObjectName(u"label_user_id")
        self.label_user_id.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_user_id, 1, 2, 1, 1)

        self.label_user_act_before = QLabel(self.user_frame)
        self.label_user_act_before.setObjectName(u"label_user_act_before")
        self.label_user_act_before.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_user_act_before, 2, 3, 1, 2)

        self.label_user_login = QLabel(self.user_frame)
        self.label_user_login.setObjectName(u"label_user_login")
        self.label_user_login.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label_user_login, 1, 3, 1, 2)


        self.verticalLayout_2.addWidget(self.user_frame)

        self.workplace_frame = QFrame(self.frame_user_data)
        self.workplace_frame.setObjectName(u"workplace_frame")
        self.workplace_frame.setStyleSheet(u"font-size: 9pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_4 = QGridLayout(self.workplace_frame)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.tableWidget = QTableWidget(self.workplace_frame)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(600, 0))
        self.tableWidget.setMaximumSize(QSize(600, 16777215))
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"   selection-background-color: rgba(50, 98, 115, 120);\n"
"   background-color: rgba(50, 98, 115, 40);\n"
"   color: #FFFFFF;\n"
"   font-weight: Normal;\n"
"   border-color: rgba(50, 98, 115, 255);\n"
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
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.gridLayout_4.addWidget(self.tableWidget, 2, 0, 1, 6)

        self.label_5 = QLabel(self.workplace_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 6)

        self.label_workplace = QLabel(self.workplace_frame)
        self.label_workplace.setObjectName(u"label_workplace")
        self.label_workplace.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_workplace.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_workplace, 1, 2, 1, 4)

        self.pushButton_add_workplace = PushButton(self.workplace_frame)
        self.pushButton_add_workplace.setObjectName(u"pushButton_add_workplace")
        self.pushButton_add_workplace.setEnabled(False)
        self.pushButton_add_workplace.setMinimumSize(QSize(0, 0))
        self.pushButton_add_workplace.setMaximumSize(QSize(16777215, 16777215))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette10.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette10.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette10.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush)
        palette10.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette10.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette10.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette10.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette10.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette10.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette10.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette10.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.pushButton_add_workplace.setPalette(palette10)
        self.pushButton_add_workplace.setFont(font)
        self.pushButton_add_workplace.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_add_workplace.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_4.addWidget(self.pushButton_add_workplace, 1, 0, 1, 2)


        self.verticalLayout_2.addWidget(self.workplace_frame)


        self.gridLayout.addWidget(self.frame_user_data, 1, 1, 2, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)


        self.verticalLayout_4.addWidget(self.main_frame)


        self.retranslateUi(main_menu)

        QMetaObject.connectSlotsByName(main_menu)
    # setupUi

    def retranslateUi(self, main_menu):
        main_menu.setWindowTitle(QCoreApplication.translate("main_menu", u"Form", None))
        self.pushButton_save.setText(QCoreApplication.translate("main_menu", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.labelLogo.setText(QCoreApplication.translate("main_menu", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">World of Medicine</span></p></body></html>", None))
        self.label_overview.setText(QCoreApplication.translate("main_menu", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440", None))
        self.label_status.setText(QCoreApplication.translate("main_menu", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.pushButton_user.setText("")
        self.pushButton_settings.setText("")
        self.pushButton_analyse.setText("")
        self.pushButton_achievements.setText("")
        self.pushButton_statistic.setText("")
        self.pushButton_social.setText("")
        self.pushButton_tickets.setText("")
        self.pushButton_logout.setText("")
        self.label_user_img.setText("")
        self.label_7.setText(QCoreApplication.translate("main_menu", u"\u0421\u0442\u0430\u0442\u0443\u0441:", None))
        self.label_6.setText(QCoreApplication.translate("main_menu", u"UserID:", None))
        self.label_4.setText(QCoreApplication.translate("main_menu", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c:", None))
        self.label_user_name.setText(QCoreApplication.translate("main_menu", u"#\u0438\u043c\u044f#", None))
        self.label_user_status.setText(QCoreApplication.translate("main_menu", u"#status#", None))
        self.label_user_id.setText(QCoreApplication.translate("main_menu", u"#ID#", None))
        self.label_user_act_before.setText(QCoreApplication.translate("main_menu", u"#act_before#", None))
        self.label_user_login.setText(QCoreApplication.translate("main_menu", u"#login#", None))
        self.label_5.setText(QCoreApplication.translate("main_menu", u"\u0420\u0430\u0431\u043e\u0447\u0438\u0435 \u043c\u0435\u0441\u0442\u0430", None))
        self.label_workplace.setText(QCoreApplication.translate("main_menu", u"#workplaces#", None))
        self.pushButton_add_workplace.setText(QCoreApplication.translate("main_menu", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043d\u043e\u0432\u043e\u0435", None))
    # retranslateUi

