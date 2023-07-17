# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bta_Obj_status.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)
import res_main_rc
import res_main_rc
import res_main_rc

class Ui_StPrObjectivus(object):
    def setupUi(self, StPrObjectivus):
        if not StPrObjectivus.objectName():
            StPrObjectivus.setObjectName(u"StPrObjectivus")
        StPrObjectivus.resize(1130, 789)
        StPrObjectivus.setMinimumSize(QSize(0, 0))
        StPrObjectivus.setMaximumSize(QSize(10000, 10000))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(11)
        font.setBold(False)
        StPrObjectivus.setFont(font)
        StPrObjectivus.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(190, 190, 190, 255));\n"
"font-family: Roboto;")
        self.centralwidget = QWidget(StPrObjectivus)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pt_info_block = QFrame(self.centralwidget)
        self.pt_info_block.setObjectName(u"pt_info_block")
        self.pt_info_block.setStyleSheet(u"background-color: transparent;")
        self.pt_info_block.setFrameShape(QFrame.NoFrame)
        self.pt_info_block.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.pt_info_block)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_Pt_info = QLabel(self.pt_info_block)
        self.label_Pt_info.setObjectName(u"label_Pt_info")
        self.label_Pt_info.setFont(font)
        self.label_Pt_info.setStyleSheet(u"background-color: rgba(50, 98, 115, 100);\n"
"color: 13242B;\n"
"font-size: 11pt;\n"
"border: 1px solid rgba(50, 98, 115, 255);")

        self.horizontalLayout_3.addWidget(self.label_Pt_info)

        self.labelTimeline = QLabel(self.pt_info_block)
        self.labelTimeline.setObjectName(u"labelTimeline")
        self.labelTimeline.setMaximumSize(QSize(80, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setItalic(False)
        self.labelTimeline.setFont(font1)
        self.labelTimeline.setStyleSheet(u"color: White;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: rgba(92, 158, 173, 200)\n"
"")
        self.labelTimeline.setPixmap(QPixmap(u":/icon/icons/stethoscope_FILL0_wght400_GRAD0_opsz48.svg"))
        self.labelTimeline.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelTimeline)


        self.verticalLayout_4.addWidget(self.pt_info_block)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(11)
        self.tabWidget.setFont(font2)
        self.tabWidget.setStyleSheet(u"QTabWidget:pane {\n"
"border: 1px solid rgba(50, 98, 115, 255);\n"
"background-color: transparent;\n"
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
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setIconSize(QSize(28, 28))
        self.jaloby_anamnesis_page = QWidget()
        self.jaloby_anamnesis_page.setObjectName(u"jaloby_anamnesis_page")
        self.anamnesis_block = QFrame(self.jaloby_anamnesis_page)
        self.anamnesis_block.setObjectName(u"anamnesis_block")
        self.anamnesis_block.setGeometry(QRect(0, 0, 931, 671))
        self.gridLayout = QGridLayout(self.anamnesis_block)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.anamnesis_morbi = QFrame(self.anamnesis_block)
        self.anamnesis_morbi.setObjectName(u"anamnesis_morbi")
        self.anamnesis_morbi.setStyleSheet(u"font-size: 15pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.verticalLayout_5 = QVBoxLayout(self.anamnesis_morbi)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.label_6 = QLabel(self.anamnesis_morbi)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 25))
        self.label_6.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_6)

        self.plainTextEditPtAnamMorbi = QPlainTextEdit(self.anamnesis_morbi)
        self.plainTextEditPtAnamMorbi.setObjectName(u"plainTextEditPtAnamMorbi")
        palette = QPalette()
        brush = QBrush(QColor(19, 36, 43, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(238, 238, 238, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(237, 237, 237, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(110, 110, 110, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(147, 147, 147, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(19, 36, 43, 128))
        brush6.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush7 = QBrush(QColor(220, 220, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.plainTextEditPtAnamMorbi.setPalette(palette)
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.plainTextEditPtAnamMorbi.setFont(font3)
        self.plainTextEditPtAnamMorbi.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;")

        self.verticalLayout_5.addWidget(self.plainTextEditPtAnamMorbi)


        self.gridLayout.addWidget(self.anamnesis_morbi, 1, 0, 1, 2)

        self.allergo_block = QFrame(self.anamnesis_block)
        self.allergo_block.setObjectName(u"allergo_block")
        self.allergo_block.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_4 = QGridLayout(self.allergo_block)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(1)
        self.label_9 = QLabel(self.allergo_block)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.comboBoxPtAllergStatus = QComboBox(self.allergo_block)
        self.comboBoxPtAllergStatus.addItem("")
        self.comboBoxPtAllergStatus.addItem("")
        self.comboBoxPtAllergStatus.setObjectName(u"comboBoxPtAllergStatus")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtAllergStatus.setPalette(palette1)
        self.comboBoxPtAllergStatus.setFont(font3)
        self.comboBoxPtAllergStatus.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_4.addWidget(self.comboBoxPtAllergStatus, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.plainTextEditPtAnamAllerg = QPlainTextEdit(self.allergo_block)
        self.plainTextEditPtAnamAllerg.setObjectName(u"plainTextEditPtAnamAllerg")
        self.plainTextEditPtAnamAllerg.setMinimumSize(QSize(0, 60))
        self.plainTextEditPtAnamAllerg.setMaximumSize(QSize(16777215, 100))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.plainTextEditPtAnamAllerg.setPalette(palette2)
        self.plainTextEditPtAnamAllerg.setFont(font3)
        self.plainTextEditPtAnamAllerg.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_4.addWidget(self.plainTextEditPtAnamAllerg, 2, 0, 1, 3)


        self.gridLayout.addWidget(self.allergo_block, 3, 0, 1, 2)

        self.jaloby_2 = QFrame(self.anamnesis_block)
        self.jaloby_2.setObjectName(u"jaloby_2")
        self.horizontalLayout_2 = QHBoxLayout(self.jaloby_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.jaloby = QFrame(self.jaloby_2)
        self.jaloby.setObjectName(u"jaloby")
        self.jaloby.setStyleSheet(u"font-size: 15pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.verticalLayout_3 = QVBoxLayout(self.jaloby)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.label_5 = QLabel(self.jaloby)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 25))
        self.label_5.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.plainTextEditPtComplaints = QPlainTextEdit(self.jaloby)
        self.plainTextEditPtComplaints.setObjectName(u"plainTextEditPtComplaints")
        self.plainTextEditPtComplaints.setMinimumSize(QSize(0, 80))
        self.plainTextEditPtComplaints.setMaximumSize(QSize(16777215, 80))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.plainTextEditPtComplaints.setPalette(palette3)
        self.plainTextEditPtComplaints.setFont(font3)
        self.plainTextEditPtComplaints.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.verticalLayout_3.addWidget(self.plainTextEditPtComplaints)


        self.horizontalLayout_2.addWidget(self.jaloby)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.gridLayout.addWidget(self.jaloby_2, 0, 0, 1, 4)

        self.drugs_block = QFrame(self.anamnesis_block)
        self.drugs_block.setObjectName(u"drugs_block")
        self.drugs_block.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_5 = QGridLayout(self.drugs_block)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(5)
        self.gridLayout_5.setVerticalSpacing(1)
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.comboBoxPtDrugs = QComboBox(self.drugs_block)
        self.comboBoxPtDrugs.addItem("")
        self.comboBoxPtDrugs.addItem("")
        self.comboBoxPtDrugs.addItem("")
        self.comboBoxPtDrugs.setObjectName(u"comboBoxPtDrugs")
        self.comboBoxPtDrugs.setMaximumSize(QSize(16777215, 16777215))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtDrugs.setPalette(palette4)
        self.comboBoxPtDrugs.setFont(font3)
        self.comboBoxPtDrugs.setLayoutDirection(Qt.LeftToRight)
        self.comboBoxPtDrugs.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_5.addWidget(self.comboBoxPtDrugs, 1, 1, 1, 2)

        self.plainTextEditPtDrugs = QPlainTextEdit(self.drugs_block)
        self.plainTextEditPtDrugs.setObjectName(u"plainTextEditPtDrugs")
        self.plainTextEditPtDrugs.setMinimumSize(QSize(0, 60))
        self.plainTextEditPtDrugs.setMaximumSize(QSize(16777215, 100))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.plainTextEditPtDrugs.setPalette(palette5)
        self.plainTextEditPtDrugs.setFont(font3)
        self.plainTextEditPtDrugs.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_5.addWidget(self.plainTextEditPtDrugs, 2, 0, 1, 4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.label_8 = QLabel(self.drugs_block)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 25))
        self.label_8.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 4)


        self.gridLayout.addWidget(self.drugs_block, 2, 0, 1, 2)

        self.metric_data = QFrame(self.anamnesis_block)
        self.metric_data.setObjectName(u"metric_data")
        self.metric_data.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_11 = QGridLayout(self.metric_data)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(5)
        self.gridLayout_11.setVerticalSpacing(1)
        self.gridLayout_11.setContentsMargins(5, 5, 5, 5)
        self.labelPtTemperatureCelcium = QLabel(self.metric_data)
        self.labelPtTemperatureCelcium.setObjectName(u"labelPtTemperatureCelcium")
        palette6 = QPalette()
        brush8 = QBrush(QColor(50, 98, 115, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        brush9 = QBrush(QColor(0, 0, 0, 0))
        brush9.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette6.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush9)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush11 = QBrush(QColor(255, 255, 220, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
        brush12 = QBrush(QColor(50, 98, 115, 128))
        brush12.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette6.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette6.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtTemperatureCelcium.setPalette(palette6)
        self.labelPtTemperatureCelcium.setFont(font3)
        self.labelPtTemperatureCelcium.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_11.addWidget(self.labelPtTemperatureCelcium, 3, 4, 1, 1)

        self.label_7 = QLabel(self.metric_data)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 25))
        self.label_7.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_7, 0, 0, 1, 6)

        self.labelooo = QLabel(self.metric_data)
        self.labelooo.setObjectName(u"labelooo")
        self.labelooo.setMinimumSize(QSize(5, 0))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette7.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette7.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette7.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette7.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette7.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette7.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette7.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette7.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette7.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette7.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette7.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette7.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette7.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette7.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelooo.setPalette(palette7)
        self.labelooo.setFont(font3)
        self.labelooo.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_11.addWidget(self.labelooo, 5, 2, 3, 1)

        self.lineEditPtBreathingSpeed = QLineEdit(self.metric_data)
        self.lineEditPtBreathingSpeed.setObjectName(u"lineEditPtBreathingSpeed")
        self.lineEditPtBreathingSpeed.setFont(font3)
        self.lineEditPtBreathingSpeed.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_11.addWidget(self.lineEditPtBreathingSpeed, 1, 5, 1, 1)

        self.labelPtBloodPreasure = QLabel(self.metric_data)
        self.labelPtBloodPreasure.setObjectName(u"labelPtBloodPreasure")
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette8.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette8.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette8.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette8.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette8.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette8.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette8.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette8.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette8.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette8.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette8.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette8.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette8.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette8.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette8.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette8.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette8.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette8.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette8.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtBloodPreasure.setPalette(palette8)
        self.labelPtBloodPreasure.setFont(font3)
        self.labelPtBloodPreasure.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_11.addWidget(self.labelPtBloodPreasure, 5, 0, 3, 1)

        self.lineEditPtBloodPreasureSist = QLineEdit(self.metric_data)
        self.lineEditPtBloodPreasureSist.setObjectName(u"lineEditPtBloodPreasureSist")
        self.lineEditPtBloodPreasureSist.setMaximumSize(QSize(50, 16777215))
        self.lineEditPtBloodPreasureSist.setFont(font3)
        self.lineEditPtBloodPreasureSist.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_11.addWidget(self.lineEditPtBloodPreasureSist, 5, 1, 3, 1)

        self.lineEditPtWeight = QLineEdit(self.metric_data)
        self.lineEditPtWeight.setObjectName(u"lineEditPtWeight")
        self.lineEditPtWeight.setMaximumSize(QSize(110, 16777215))
        self.lineEditPtWeight.setFont(font3)
        self.lineEditPtWeight.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_11.addWidget(self.lineEditPtWeight, 1, 1, 1, 3)

        self.labelPtSaturation = QLabel(self.metric_data)
        self.labelPtSaturation.setObjectName(u"labelPtSaturation")
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette9.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette9.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette9.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette9.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette9.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette9.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette9.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette9.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette9.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette9.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette9.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette9.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette9.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette9.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette9.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette9.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette9.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtSaturation.setPalette(palette9)
        self.labelPtSaturation.setFont(font3)
        self.labelPtSaturation.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_11.addWidget(self.labelPtSaturation, 2, 4, 1, 1)

        self.lineEditSaturation = QLineEdit(self.metric_data)
        self.lineEditSaturation.setObjectName(u"lineEditSaturation")
        self.lineEditSaturation.setFont(font3)
        self.lineEditSaturation.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_11.addWidget(self.lineEditSaturation, 2, 5, 1, 1)

        self.lineEditPtGrowth = QLineEdit(self.metric_data)
        self.lineEditPtGrowth.setObjectName(u"lineEditPtGrowth")
        self.lineEditPtGrowth.setMaximumSize(QSize(110, 16777215))
        self.lineEditPtGrowth.setFont(font3)
        self.lineEditPtGrowth.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_11.addWidget(self.lineEditPtGrowth, 2, 1, 1, 3)

        self.labelPtWeight = QLabel(self.metric_data)
        self.labelPtWeight.setObjectName(u"labelPtWeight")
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette10.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette10.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette10.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette10.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette10.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette10.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette10.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette10.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette10.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette10.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette10.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette10.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette10.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette10.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette10.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette10.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette10.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette10.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette10.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette10.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette10.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette10.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtWeight.setPalette(palette10)
        self.labelPtWeight.setFont(font3)
        self.labelPtWeight.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_11.addWidget(self.labelPtWeight, 1, 0, 1, 1)

        self.lineEditPtTemperature = QLineEdit(self.metric_data)
        self.lineEditPtTemperature.setObjectName(u"lineEditPtTemperature")
        self.lineEditPtTemperature.setFont(font3)
        self.lineEditPtTemperature.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_11.addWidget(self.lineEditPtTemperature, 3, 5, 1, 1)

        self.labelPtGrowth = QLabel(self.metric_data)
        self.labelPtGrowth.setObjectName(u"labelPtGrowth")
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette11.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette11.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette11.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette11.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette11.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette11.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette11.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette11.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette11.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette11.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette11.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette11.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette11.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette11.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette11.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette11.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette11.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette11.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette11.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtGrowth.setPalette(palette11)
        self.labelPtGrowth.setFont(font3)
        self.labelPtGrowth.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_11.addWidget(self.labelPtGrowth, 2, 0, 1, 1)

        self.labelPtPulse = QLabel(self.metric_data)
        self.labelPtPulse.setObjectName(u"labelPtPulse")
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette12.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette12.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette12.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette12.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette12.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette12.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette12.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette12.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette12.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette12.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette12.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette12.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette12.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette12.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette12.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette12.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette12.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette12.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette12.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette12.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette12.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtPulse.setPalette(palette12)
        self.labelPtPulse.setFont(font3)
        self.labelPtPulse.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_11.addWidget(self.labelPtPulse, 5, 4, 3, 1)

        self.lineEditPtBloodPreasureDiast = QLineEdit(self.metric_data)
        self.lineEditPtBloodPreasureDiast.setObjectName(u"lineEditPtBloodPreasureDiast")
        self.lineEditPtBloodPreasureDiast.setMaximumSize(QSize(50, 16777215))
        self.lineEditPtBloodPreasureDiast.setFont(font3)
        self.lineEditPtBloodPreasureDiast.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_11.addWidget(self.lineEditPtBloodPreasureDiast, 5, 3, 3, 1)

        self.lineEditPtPulse = QLineEdit(self.metric_data)
        self.lineEditPtPulse.setObjectName(u"lineEditPtPulse")
        self.lineEditPtPulse.setFont(font3)
        self.lineEditPtPulse.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_11.addWidget(self.lineEditPtPulse, 5, 5, 3, 1)

        self.labelPtBreathingSpeed = QLabel(self.metric_data)
        self.labelPtBreathingSpeed.setObjectName(u"labelPtBreathingSpeed")
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette13.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette13.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette13.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette13.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette13.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette13.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette13.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette13.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette13.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette13.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette13.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette13.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette13.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette13.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette13.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette13.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette13.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette13.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette13.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette13.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette13.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette13.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette13.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette13.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette13.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette13.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette13.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtBreathingSpeed.setPalette(palette13)
        self.labelPtBreathingSpeed.setFont(font3)
        self.labelPtBreathingSpeed.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_11.addWidget(self.labelPtBreathingSpeed, 1, 4, 1, 1)

        self.label_imt = QLabel(self.metric_data)
        self.label_imt.setObjectName(u"label_imt")
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette14.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette14.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette14.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette14.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette14.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette14.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette14.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette14.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette14.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette14.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette14.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette14.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette14.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette14.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette14.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette14.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette14.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette14.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette14.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette14.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette14.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette14.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette14.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.label_imt.setPalette(palette14)
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(10)
        font4.setBold(True)
        self.label_imt.setFont(font4)
        self.label_imt.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_11.addWidget(self.label_imt, 8, 0, 1, 6)

        self.label_2 = QLabel(self.metric_data)
        self.label_2.setObjectName(u"label_2")
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette15.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette15.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette15.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette15.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette15.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette15.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette15.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette15.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette15.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette15.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette15.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette15.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette15.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette15.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette15.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette15.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette15.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette15.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette15.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette15.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette15.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette15.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette15.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette15.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette15.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette15.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette15.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.label_2.setPalette(palette15)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_11.addWidget(self.label_2, 10, 0, 1, 6)

        self.pushButton_add_to_diag = QPushButton(self.metric_data)
        self.pushButton_add_to_diag.setObjectName(u"pushButton_add_to_diag")
        self.pushButton_add_to_diag.setEnabled(False)
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush13 = QBrush(QColor(50, 98, 115, 190))
        brush13.setStyle(Qt.SolidPattern)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette16.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush14 = QBrush(QColor(236, 236, 236, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette16.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        brush15 = QBrush(QColor(108, 108, 108, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette16.setBrush(QPalette.Active, QPalette.Dark, brush15)
        brush16 = QBrush(QColor(145, 145, 145, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette16.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette16.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette16.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette16.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette16.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette16.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
        brush17 = QBrush(QColor(255, 255, 255, 128))
        brush17.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette16.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette16.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette16.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette16.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette16.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette16.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette16.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        brush18 = QBrush(QColor(50, 98, 115, 150))
        brush18.setStyle(Qt.SolidPattern)
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        brush19 = QBrush(QColor(50, 98, 115, 40))
        brush19.setStyle(Qt.SolidPattern)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush19)
        palette16.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette16.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette16.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette16.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush19)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush19)
        palette16.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        brush20 = QBrush(QColor(217, 217, 217, 255))
        brush20.setStyle(Qt.SolidPattern)
        palette16.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush20)
        palette16.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette16.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
        brush21 = QBrush(QColor(50, 98, 115, 75))
        brush21.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush21)
#endif
        self.pushButton_add_to_diag.setPalette(palette16)
        self.pushButton_add_to_diag.setFont(font)
        self.pushButton_add_to_diag.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout_11.addWidget(self.pushButton_add_to_diag, 9, 2, 1, 3)


        self.gridLayout.addWidget(self.metric_data, 1, 2, 1, 2)

        self.epid_block = QFrame(self.anamnesis_block)
        self.epid_block.setObjectName(u"epid_block")
        self.epid_block.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_8 = QGridLayout(self.epid_block)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(5)
        self.gridLayout_8.setVerticalSpacing(1)
        self.gridLayout_8.setContentsMargins(5, 5, 5, 5)
        self.comboBoxPtAnamEpid = QComboBox(self.epid_block)
        self.comboBoxPtAnamEpid.addItem("")
        self.comboBoxPtAnamEpid.addItem("")
        self.comboBoxPtAnamEpid.setObjectName(u"comboBoxPtAnamEpid")
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette17.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette17.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette17.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette17.setBrush(QPalette.Active, QPalette.Text, brush)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette17.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette17.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette17.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette17.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette17.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette17.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette17.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette17.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtAnamEpid.setPalette(palette17)
        self.comboBoxPtAnamEpid.setFont(font3)
        self.comboBoxPtAnamEpid.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_8.addWidget(self.comboBoxPtAnamEpid, 1, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_7, 1, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_8, 1, 2, 1, 1)

        self.label_10 = QLabel(self.epid_block)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_10, 0, 0, 1, 3)

        self.plainTextEditPtAnamEpid = QPlainTextEdit(self.epid_block)
        self.plainTextEditPtAnamEpid.setObjectName(u"plainTextEditPtAnamEpid")
        self.plainTextEditPtAnamEpid.setMinimumSize(QSize(0, 60))
        self.plainTextEditPtAnamEpid.setMaximumSize(QSize(16777215, 60))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette18.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette18.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette18.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette18.setBrush(QPalette.Active, QPalette.Text, brush)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette18.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette18.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette18.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette18.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette18.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette18.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette18.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette18.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.plainTextEditPtAnamEpid.setPalette(palette18)
        self.plainTextEditPtAnamEpid.setFont(font3)
        self.plainTextEditPtAnamEpid.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_8.addWidget(self.plainTextEditPtAnamEpid, 2, 0, 1, 3)


        self.gridLayout.addWidget(self.epid_block, 4, 0, 1, 2)

        self.diseases_block = QFrame(self.anamnesis_block)
        self.diseases_block.setObjectName(u"diseases_block")
        self.diseases_block.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_9 = QGridLayout(self.diseases_block)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(5)
        self.gridLayout_9.setVerticalSpacing(1)
        self.gridLayout_9.setContentsMargins(5, 5, 5, 5)
        self.checkBox_Fat = QCheckBox(self.diseases_block)
        self.checkBox_Fat.setObjectName(u"checkBox_Fat")
        self.checkBox_Fat.setFont(font)
        self.checkBox_Fat.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"   color: #702632;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QCheckBox::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")

        self.gridLayout_9.addWidget(self.checkBox_Fat, 6, 0, 1, 1)

        self.checkBox_Atherosclerosis_legs = QCheckBox(self.diseases_block)
        self.checkBox_Atherosclerosis_legs.setObjectName(u"checkBox_Atherosclerosis_legs")
        self.checkBox_Atherosclerosis_legs.setFont(font)
        self.checkBox_Atherosclerosis_legs.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"   color: #702632;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QCheckBox::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")

        self.gridLayout_9.addWidget(self.checkBox_Atherosclerosis_legs, 4, 1, 1, 1)

        self.checkBox_Stroke = QCheckBox(self.diseases_block)
        self.checkBox_Stroke.setObjectName(u"checkBox_Stroke")
        self.checkBox_Stroke.setFont(font)
        self.checkBox_Stroke.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"   color: #702632;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QCheckBox::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")

        self.gridLayout_9.addWidget(self.checkBox_Stroke, 5, 0, 1, 1)

        self.label_11 = QLabel(self.diseases_block)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 25))
        self.label_11.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_11, 0, 0, 1, 2)

        self.checkBox_other = QCheckBox(self.diseases_block)
        self.checkBox_other.setObjectName(u"checkBox_other")
        self.checkBox_other.setFont(font)
        self.checkBox_other.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"   color: #702632;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QCheckBox::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")

        self.gridLayout_9.addWidget(self.checkBox_other, 9, 0, 1, 1)

        self.checkBox_Hyperthyreosis = QCheckBox(self.diseases_block)
        self.checkBox_Hyperthyreosis.setObjectName(u"checkBox_Hyperthyreosis")
        self.checkBox_Hyperthyreosis.setFont(font)
        self.checkBox_Hyperthyreosis.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"   color: #702632;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QCheckBox::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")

        self.gridLayout_9.addWidget(self.checkBox_Hyperthyreosis, 2, 1, 1, 1)

        self.checkBox_Hypothyreosis = QCheckBox(self.diseases_block)
        self.checkBox_Hypothyreosis.setObjectName(u"checkBox_Hypothyreosis")
        self.checkBox_Hypothyreosis.setFont(font)
        self.checkBox_Hypothyreosis.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"   color: #702632;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QCheckBox::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")

        self.gridLayout_9.addWidget(self.checkBox_Hypothyreosis, 1, 1, 1, 1)

        self.checkBox_IBS = QCheckBox(self.diseases_block)
        self.checkBox_IBS.setObjectName(u"checkBox_IBS")
        self.checkBox_IBS.setFont(font)
        self.checkBox_IBS.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"   color: #702632;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QCheckBox::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")

        self.gridLayout_9.addWidget(self.checkBox_IBS, 4, 0, 1, 1)

        self.checkBox_Gastro = QCheckBox(self.diseases_block)
        self.checkBox_Gastro.setObjectName(u"checkBox_Gastro")
        self.checkBox_Gastro.setFont(font)
        self.checkBox_Gastro.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"   color: #702632;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QCheckBox::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")

        self.gridLayout_9.addWidget(self.checkBox_Gastro, 8, 0, 1, 1)

        self.checkBox_B20 = QCheckBox(self.diseases_block)
        self.checkBox_B20.setObjectName(u"checkBox_B20")
        self.checkBox_B20.setFont(font)
        self.checkBox_B20.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"   color: #702632;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QCheckBox::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")

        self.gridLayout_9.addWidget(self.checkBox_B20, 8, 1, 1, 1)

        self.checkBox_HBsAg = QCheckBox(self.diseases_block)
        self.checkBox_HBsAg.setObjectName(u"checkBox_HBsAg")
        self.checkBox_HBsAg.setFont(font)
        self.checkBox_HBsAg.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"   color: #702632;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QCheckBox::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")

        self.gridLayout_9.addWidget(self.checkBox_HBsAg, 6, 1, 1, 1)

        self.checkBox_Atherosclerosis_BCA = QCheckBox(self.diseases_block)
        self.checkBox_Atherosclerosis_BCA.setObjectName(u"checkBox_Atherosclerosis_BCA")
        self.checkBox_Atherosclerosis_BCA.setFont(font)
        self.checkBox_Atherosclerosis_BCA.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"   color: #702632;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QCheckBox::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")

        self.gridLayout_9.addWidget(self.checkBox_Atherosclerosis_BCA, 3, 1, 1, 1)

        self.checkBox_Astma = QCheckBox(self.diseases_block)
        self.checkBox_Astma.setObjectName(u"checkBox_Astma")
        self.checkBox_Astma.setFont(font)
        self.checkBox_Astma.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"   color: #702632;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QCheckBox::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")

        self.gridLayout_9.addWidget(self.checkBox_Astma, 7, 0, 1, 1)

        self.checkBox_NRS = QCheckBox(self.diseases_block)
        self.checkBox_NRS.setObjectName(u"checkBox_NRS")
        self.checkBox_NRS.setFont(font)
        self.checkBox_NRS.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"   color: #702632;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QCheckBox::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")

        self.gridLayout_9.addWidget(self.checkBox_NRS, 3, 0, 1, 1)

        self.checkBox_GB = QCheckBox(self.diseases_block)
        self.checkBox_GB.setObjectName(u"checkBox_GB")
        self.checkBox_GB.setFont(font)
        self.checkBox_GB.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"   color: #702632;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QCheckBox::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")

        self.gridLayout_9.addWidget(self.checkBox_GB, 1, 0, 1, 1)

        self.plainTextEdit_other_chronic_diseases = QPlainTextEdit(self.diseases_block)
        self.plainTextEdit_other_chronic_diseases.setObjectName(u"plainTextEdit_other_chronic_diseases")
        self.plainTextEdit_other_chronic_diseases.setMaximumSize(QSize(16777215, 150))
        self.plainTextEdit_other_chronic_diseases.setFont(font3)
        self.plainTextEdit_other_chronic_diseases.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;")

        self.gridLayout_9.addWidget(self.plainTextEdit_other_chronic_diseases, 10, 0, 1, 2)

        self.checkBox_SD = QCheckBox(self.diseases_block)
        self.checkBox_SD.setObjectName(u"checkBox_SD")
        self.checkBox_SD.setFont(font)
        self.checkBox_SD.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"   color: #702632;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QCheckBox::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")

        self.gridLayout_9.addWidget(self.checkBox_SD, 2, 0, 1, 1)

        self.checkBox_HCV = QCheckBox(self.diseases_block)
        self.checkBox_HCV.setObjectName(u"checkBox_HCV")
        self.checkBox_HCV.setFont(font)
        self.checkBox_HCV.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"   color: #702632;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QCheckBox::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}")

        self.gridLayout_9.addWidget(self.checkBox_HCV, 7, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_3, 11, 0, 1, 1)


        self.gridLayout.addWidget(self.diseases_block, 2, 2, 3, 2)

        icon = QIcon()
        icon.addFile(u":/icon/icons/message_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.jaloby_anamnesis_page, icon, "")
        self.work_page = QWidget()
        self.work_page.setObjectName(u"work_page")
        self.work_block = QFrame(self.work_page)
        self.work_block.setObjectName(u"work_block")
        self.work_block.setGeometry(QRect(10, 10, 911, 311))
        self.work_block.setStyleSheet(u"font-size: 11pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_6 = QGridLayout(self.work_block)
        self.gridLayout_6.setSpacing(5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.comboBoxWorkList_prognosis = QComboBox(self.work_block)
        self.comboBoxWorkList_prognosis.addItem("")
        self.comboBoxWorkList_prognosis.addItem("")
        self.comboBoxWorkList_prognosis.addItem("")
        self.comboBoxWorkList_prognosis.addItem("")
        self.comboBoxWorkList_prognosis.addItem("")
        self.comboBoxWorkList_prognosis.setObjectName(u"comboBoxWorkList_prognosis")
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette19.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette19.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette19.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette19.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette19.setBrush(QPalette.Active, QPalette.Text, brush)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette19.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette19.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette19.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette19.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette19.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette19.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette19.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette19.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette19.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette19.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette19.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette19.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette19.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxWorkList_prognosis.setPalette(palette19)
        self.comboBoxWorkList_prognosis.setFont(font3)
        self.comboBoxWorkList_prognosis.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_6.addWidget(self.comboBoxWorkList_prognosis, 12, 2, 1, 3)

        self.labelPtWorkListS = QLabel(self.work_block)
        self.labelPtWorkListS.setObjectName(u"labelPtWorkListS")
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette20.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette20.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette20.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette20.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette20.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette20.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette20.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette20.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette20.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette20.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette20.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette20.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette20.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette20.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette20.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette20.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette20.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette20.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette20.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette20.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette20.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette20.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette20.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette20.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette20.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette20.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette20.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette20.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette20.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette20.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtWorkListS.setPalette(palette20)
        self.labelPtWorkListS.setFont(font3)
        self.labelPtWorkListS.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelPtWorkListS.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelPtWorkListS, 10, 1, 1, 1)

        self.dateEditPtWorkListDateOpening = QDateEdit(self.work_block)
        self.dateEditPtWorkListDateOpening.setObjectName(u"dateEditPtWorkListDateOpening")
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette21.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette21.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette21.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette21.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette21.setBrush(QPalette.Active, QPalette.Text, brush)
        palette21.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette21.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette21.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette21.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette21.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette21.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette21.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette21.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette21.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette21.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette21.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette21.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette21.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.dateEditPtWorkListDateOpening.setPalette(palette21)
        self.dateEditPtWorkListDateOpening.setFont(font3)
        self.dateEditPtWorkListDateOpening.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.dateEditPtWorkListDateOpening.setTimeSpec(Qt.LocalTime)

        self.gridLayout_6.addWidget(self.dateEditPtWorkListDateOpening, 11, 2, 1, 1)

        self.labelPtWorkListNumber_2 = QLabel(self.work_block)
        self.labelPtWorkListNumber_2.setObjectName(u"labelPtWorkListNumber_2")
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette22.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette22.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette22.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette22.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette22.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette22.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette22.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette22.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette22.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette22.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette22.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette22.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette22.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette22.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette22.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette22.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette22.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette22.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette22.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette22.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette22.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette22.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette22.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette22.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette22.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette22.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette22.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette22.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette22.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette22.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette22.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette22.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette22.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtWorkListNumber_2.setPalette(palette22)
        self.labelPtWorkListNumber_2.setFont(font3)
        self.labelPtWorkListNumber_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelPtWorkListNumber_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelPtWorkListNumber_2, 9, 1, 1, 1)

        self.lineEditPtWorkPlace = QLineEdit(self.work_block)
        self.lineEditPtWorkPlace.setObjectName(u"lineEditPtWorkPlace")
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette23.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette23.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette23.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette23.setBrush(QPalette.Active, QPalette.Text, brush)
        palette23.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette23.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette23.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette23.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette23.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette23.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette23.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette23.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette23.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette23.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette23.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette23.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette23.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.lineEditPtWorkPlace.setPalette(palette23)
        self.lineEditPtWorkPlace.setFont(font3)
        self.lineEditPtWorkPlace.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_6.addWidget(self.lineEditPtWorkPlace, 5, 2, 1, 3)

        self.labelPtSickListInfo = QLabel(self.work_block)
        self.labelPtSickListInfo.setObjectName(u"labelPtSickListInfo")
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette24.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette24.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette24.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette24.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette24.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette24.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette24.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette24.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette24.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette24.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette24.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette24.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette24.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette24.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette24.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette24.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette24.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette24.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette24.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette24.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette24.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette24.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette24.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette24.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette24.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette24.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette24.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette24.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette24.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette24.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette24.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette24.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette24.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtSickListInfo.setPalette(palette24)
        self.labelPtSickListInfo.setFont(font3)
        self.labelPtSickListInfo.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelPtSickListInfo.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelPtSickListInfo, 3, 1, 1, 1)

        self.labelPtWorkListDateOpening = QLabel(self.work_block)
        self.labelPtWorkListDateOpening.setObjectName(u"labelPtWorkListDateOpening")
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette25.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette25.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette25.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette25.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette25.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette25.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette25.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette25.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette25.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette25.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette25.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette25.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette25.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette25.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette25.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette25.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette25.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette25.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette25.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette25.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette25.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette25.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette25.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette25.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette25.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette25.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette25.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette25.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette25.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette25.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette25.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette25.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette25.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette25.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtWorkListDateOpening.setPalette(palette25)
        self.labelPtWorkListDateOpening.setFont(font3)
        self.labelPtWorkListDateOpening.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelPtWorkListDateOpening.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelPtWorkListDateOpening, 11, 1, 1, 1)

        self.lineEditPtWorkListNumber1_1 = QLineEdit(self.work_block)
        self.lineEditPtWorkListNumber1_1.setObjectName(u"lineEditPtWorkListNumber1_1")
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette26.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette26.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette26.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette26.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette26.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette26.setBrush(QPalette.Active, QPalette.Text, brush)
        palette26.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette26.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette26.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette26.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette26.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette26.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette26.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette26.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette26.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette26.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette26.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette26.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette26.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette26.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette26.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette26.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette26.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.lineEditPtWorkListNumber1_1.setPalette(palette26)
        self.lineEditPtWorkListNumber1_1.setFont(font3)
        self.lineEditPtWorkListNumber1_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_6.addWidget(self.lineEditPtWorkListNumber1_1, 8, 2, 1, 3)

        self.checkBoxPtNeedSickList = QCheckBox(self.work_block)
        self.checkBoxPtNeedSickList.setObjectName(u"checkBoxPtNeedSickList")
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette27.setBrush(QPalette.Active, QPalette.Button, brush20)
        palette27.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette27.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette27.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette27.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette27.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette27.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette27.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette27.setBrush(QPalette.Active, QPalette.Window, brush20)
        palette27.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette27.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette27.setBrush(QPalette.Inactive, QPalette.Button, brush20)
        palette27.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette27.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette27.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette27.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette27.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette27.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette27.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette27.setBrush(QPalette.Inactive, QPalette.Window, brush20)
        palette27.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette27.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette27.setBrush(QPalette.Disabled, QPalette.Button, brush20)
        palette27.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette27.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette27.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette27.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette27.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette27.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette27.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette27.setBrush(QPalette.Disabled, QPalette.Window, brush20)
        palette27.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush20)
        brush22 = QBrush(QColor(238, 238, 238, 128))
        brush22.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette27.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush22)
#endif
        self.checkBoxPtNeedSickList.setPalette(palette27)
        self.checkBoxPtNeedSickList.setFont(font)
        self.checkBoxPtNeedSickList.setLayoutDirection(Qt.LeftToRight)
        self.checkBoxPtNeedSickList.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"   color: #702632;\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"   color: #EEEEEE;\n"
"}\n"
" \n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QCheckBox::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #EEEEEE;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_6.addWidget(self.checkBoxPtNeedSickList, 2, 2, 1, 1)

        self.labelPtSocialStatus = QLabel(self.work_block)
        self.labelPtSocialStatus.setObjectName(u"labelPtSocialStatus")
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette28.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette28.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette28.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette28.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette28.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette28.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette28.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette28.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette28.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette28.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette28.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette28.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette28.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette28.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette28.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette28.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette28.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette28.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette28.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette28.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette28.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette28.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette28.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette28.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette28.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette28.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette28.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette28.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette28.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette28.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette28.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette28.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette28.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette28.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette28.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette28.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette28.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtSocialStatus.setPalette(palette28)
        self.labelPtSocialStatus.setFont(font3)
        self.labelPtSocialStatus.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelPtSocialStatus.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelPtSocialStatus, 1, 1, 1, 1)

        self.dateEditPtWorkListDate1_2 = QDateEdit(self.work_block)
        self.dateEditPtWorkListDate1_2.setObjectName(u"dateEditPtWorkListDate1_2")
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette29.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette29.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette29.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette29.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette29.setBrush(QPalette.Active, QPalette.Text, brush)
        palette29.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette29.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette29.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette29.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette29.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette29.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette29.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette29.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette29.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette29.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette29.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette29.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette29.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette29.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette29.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette29.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette29.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette29.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette29.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette29.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette29.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette29.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.dateEditPtWorkListDate1_2.setPalette(palette29)
        self.dateEditPtWorkListDate1_2.setFont(font3)
        self.dateEditPtWorkListDate1_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.dateEditPtWorkListDate1_2.setTimeSpec(Qt.LocalTime)

        self.gridLayout_6.addWidget(self.dateEditPtWorkListDate1_2, 10, 4, 1, 1)

        self.labelPtWorkListNumber = QLabel(self.work_block)
        self.labelPtWorkListNumber.setObjectName(u"labelPtWorkListNumber")
        palette30 = QPalette()
        palette30.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette30.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette30.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette30.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette30.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette30.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette30.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette30.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette30.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette30.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette30.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette30.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette30.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette30.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette30.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette30.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette30.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette30.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette30.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette30.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette30.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette30.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette30.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette30.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette30.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette30.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette30.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette30.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette30.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette30.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette30.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette30.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette30.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette30.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette30.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette30.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette30.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette30.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette30.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette30.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette30.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette30.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette30.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette30.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette30.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette30.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtWorkListNumber.setPalette(palette30)
        self.labelPtWorkListNumber.setFont(font3)
        self.labelPtWorkListNumber.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelPtWorkListNumber.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelPtWorkListNumber, 8, 1, 1, 1)

        self.labelPtWorkPosition = QLabel(self.work_block)
        self.labelPtWorkPosition.setObjectName(u"labelPtWorkPosition")
        palette31 = QPalette()
        palette31.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette31.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette31.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette31.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette31.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette31.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette31.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette31.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette31.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette31.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette31.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette31.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette31.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette31.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette31.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette31.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette31.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette31.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette31.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette31.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette31.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette31.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette31.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette31.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette31.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette31.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette31.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette31.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette31.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette31.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette31.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette31.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette31.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette31.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette31.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette31.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette31.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette31.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette31.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette31.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette31.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette31.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette31.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette31.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette31.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette31.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtWorkPosition.setPalette(palette31)
        self.labelPtWorkPosition.setFont(font3)
        self.labelPtWorkPosition.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelPtWorkPosition.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelPtWorkPosition, 6, 1, 1, 1)

        self.labelPtWorkListNumber_3 = QLabel(self.work_block)
        self.labelPtWorkListNumber_3.setObjectName(u"labelPtWorkListNumber_3")
        self.labelPtWorkListNumber_3.setMaximumSize(QSize(50, 16777215))
        palette32 = QPalette()
        palette32.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette32.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette32.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette32.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette32.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette32.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette32.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette32.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette32.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette32.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette32.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette32.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette32.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette32.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette32.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette32.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette32.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette32.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette32.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette32.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette32.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette32.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette32.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette32.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette32.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette32.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette32.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette32.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette32.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette32.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette32.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette32.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette32.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette32.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette32.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette32.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette32.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette32.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette32.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette32.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette32.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette32.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette32.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette32.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette32.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette32.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtWorkListNumber_3.setPalette(palette32)
        self.labelPtWorkListNumber_3.setFont(font3)
        self.labelPtWorkListNumber_3.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_6.addWidget(self.labelPtWorkListNumber_3, 10, 3, 1, 1)

        self.comboBoxWorkListInfo = QComboBox(self.work_block)
        self.comboBoxWorkListInfo.addItem("")
        self.comboBoxWorkListInfo.addItem("")
        self.comboBoxWorkListInfo.addItem("")
        self.comboBoxWorkListInfo.setObjectName(u"comboBoxWorkListInfo")
        palette33 = QPalette()
        palette33.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette33.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette33.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette33.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette33.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette33.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette33.setBrush(QPalette.Active, QPalette.Text, brush)
        palette33.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette33.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette33.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette33.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette33.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette33.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette33.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette33.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette33.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette33.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette33.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette33.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette33.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette33.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette33.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette33.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette33.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette33.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette33.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette33.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette33.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette33.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette33.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxWorkListInfo.setPalette(palette33)
        self.comboBoxWorkListInfo.setFont(font3)
        self.comboBoxWorkListInfo.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_6.addWidget(self.comboBoxWorkListInfo, 3, 2, 1, 3)

        self.dateEditPtWorkListDate1_1 = QDateEdit(self.work_block)
        self.dateEditPtWorkListDate1_1.setObjectName(u"dateEditPtWorkListDate1_1")
        palette34 = QPalette()
        palette34.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette34.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette34.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette34.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette34.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette34.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette34.setBrush(QPalette.Active, QPalette.Text, brush)
        palette34.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette34.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette34.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette34.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette34.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette34.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette34.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette34.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette34.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette34.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette34.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette34.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette34.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette34.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette34.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette34.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette34.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette34.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette34.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette34.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette34.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette34.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette34.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette34.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette34.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette34.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette34.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.dateEditPtWorkListDate1_1.setPalette(palette34)
        self.dateEditPtWorkListDate1_1.setFont(font3)
        self.dateEditPtWorkListDate1_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.dateEditPtWorkListDate1_1.setTimeSpec(Qt.LocalTime)

        self.gridLayout_6.addWidget(self.dateEditPtWorkListDate1_1, 10, 2, 1, 1)

        self.labelPtWorkPlace = QLabel(self.work_block)
        self.labelPtWorkPlace.setObjectName(u"labelPtWorkPlace")
        palette35 = QPalette()
        palette35.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette35.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette35.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette35.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette35.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette35.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette35.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette35.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette35.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette35.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette35.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette35.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette35.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette35.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette35.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette35.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette35.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette35.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette35.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette35.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette35.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette35.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette35.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette35.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette35.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette35.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette35.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette35.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette35.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette35.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette35.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette35.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette35.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette35.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette35.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette35.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette35.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette35.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette35.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette35.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette35.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette35.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette35.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette35.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette35.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette35.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtWorkPlace.setPalette(palette35)
        self.labelPtWorkPlace.setFont(font3)
        self.labelPtWorkPlace.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelPtWorkPlace.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelPtWorkPlace, 5, 1, 1, 1)

        self.lineEditPtWorkPosition = QLineEdit(self.work_block)
        self.lineEditPtWorkPosition.setObjectName(u"lineEditPtWorkPosition")
        palette36 = QPalette()
        palette36.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette36.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette36.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette36.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette36.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette36.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette36.setBrush(QPalette.Active, QPalette.Text, brush)
        palette36.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette36.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette36.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette36.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette36.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette36.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette36.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette36.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette36.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette36.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette36.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette36.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette36.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette36.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette36.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette36.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette36.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette36.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette36.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette36.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette36.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette36.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette36.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette36.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette36.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette36.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette36.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.lineEditPtWorkPosition.setPalette(palette36)
        self.lineEditPtWorkPosition.setFont(font3)
        self.lineEditPtWorkPosition.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_6.addWidget(self.lineEditPtWorkPosition, 6, 2, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 4, 2, 1, 1)

        self.lineEditPtWorkListNumber_issued = QLineEdit(self.work_block)
        self.lineEditPtWorkListNumber_issued.setObjectName(u"lineEditPtWorkListNumber_issued")
        palette37 = QPalette()
        palette37.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette37.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette37.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette37.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette37.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette37.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette37.setBrush(QPalette.Active, QPalette.Text, brush)
        palette37.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette37.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette37.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette37.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette37.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette37.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette37.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette37.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette37.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette37.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette37.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette37.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette37.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette37.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette37.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette37.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette37.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette37.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette37.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette37.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette37.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette37.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette37.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.lineEditPtWorkListNumber_issued.setPalette(palette37)
        self.lineEditPtWorkListNumber_issued.setFont(font3)
        self.lineEditPtWorkListNumber_issued.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_6.addWidget(self.lineEditPtWorkListNumber_issued, 9, 2, 1, 3)

        self.labelPtSickListInfo_2 = QLabel(self.work_block)
        self.labelPtSickListInfo_2.setObjectName(u"labelPtSickListInfo_2")
        palette38 = QPalette()
        palette38.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette38.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette38.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette38.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette38.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette38.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette38.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette38.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette38.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette38.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette38.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette38.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette38.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette38.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette38.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette38.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette38.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette38.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette38.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette38.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette38.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette38.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette38.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette38.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette38.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette38.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette38.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette38.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette38.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette38.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette38.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette38.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette38.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette38.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette38.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette38.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette38.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette38.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette38.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette38.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette38.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette38.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette38.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette38.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette38.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette38.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtSickListInfo_2.setPalette(palette38)
        self.labelPtSickListInfo_2.setFont(font3)
        self.labelPtSickListInfo_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")
        self.labelPtSickListInfo_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelPtSickListInfo_2, 12, 1, 1, 1)

        self.comboBoxPtSocialStatus = QComboBox(self.work_block)
        self.comboBoxPtSocialStatus.addItem("")
        self.comboBoxPtSocialStatus.addItem("")
        self.comboBoxPtSocialStatus.addItem("")
        self.comboBoxPtSocialStatus.addItem("")
        self.comboBoxPtSocialStatus.addItem("")
        self.comboBoxPtSocialStatus.addItem("")
        self.comboBoxPtSocialStatus.addItem("")
        self.comboBoxPtSocialStatus.addItem("")
        self.comboBoxPtSocialStatus.addItem("")
        self.comboBoxPtSocialStatus.addItem("")
        self.comboBoxPtSocialStatus.addItem("")
        self.comboBoxPtSocialStatus.setObjectName(u"comboBoxPtSocialStatus")
        palette39 = QPalette()
        palette39.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette39.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette39.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette39.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette39.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette39.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette39.setBrush(QPalette.Active, QPalette.Text, brush)
        palette39.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette39.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette39.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette39.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette39.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette39.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette39.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette39.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette39.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette39.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette39.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette39.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette39.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette39.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette39.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette39.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette39.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette39.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette39.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette39.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette39.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette39.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette39.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette39.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette39.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtSocialStatus.setPalette(palette39)
        self.comboBoxPtSocialStatus.setFont(font3)
        self.comboBoxPtSocialStatus.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtSocialStatus.setEditable(True)

        self.gridLayout_6.addWidget(self.comboBoxPtSocialStatus, 1, 2, 1, 3)

        self.label_13 = QLabel(self.work_block)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 25))
        self.label_13.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_13, 0, 1, 1, 4)

        self.checkBoxPtNeedSickList_2 = QCheckBox(self.work_block)
        self.checkBoxPtNeedSickList_2.setObjectName(u"checkBoxPtNeedSickList_2")
        self.checkBoxPtNeedSickList_2.setEnabled(False)
        palette40 = QPalette()
        palette40.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette40.setBrush(QPalette.Active, QPalette.Button, brush20)
        palette40.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette40.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette40.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette40.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette40.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette40.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette40.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette40.setBrush(QPalette.Active, QPalette.Window, brush20)
        palette40.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette40.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette40.setBrush(QPalette.Inactive, QPalette.Button, brush20)
        palette40.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette40.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette40.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette40.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette40.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette40.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette40.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette40.setBrush(QPalette.Inactive, QPalette.Window, brush20)
        palette40.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette40.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette40.setBrush(QPalette.Disabled, QPalette.Button, brush20)
        palette40.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette40.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette40.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette40.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette40.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette40.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette40.setBrush(QPalette.Disabled, QPalette.Base, brush20)
        palette40.setBrush(QPalette.Disabled, QPalette.Window, brush20)
        palette40.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush20)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette40.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush22)
#endif
        self.checkBoxPtNeedSickList_2.setPalette(palette40)
        self.checkBoxPtNeedSickList_2.setFont(font)
        self.checkBoxPtNeedSickList_2.setStyleSheet(u"QCheckBox {\n"
"	color: #326273;\n"
"	border: none;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"   color: #702632;\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"   color: #EEEEEE;\n"
"}\n"
" \n"
"\n"
"QCheckBox::indicator:checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: #702632;\n"
"}\n"
"QCheckBox::indicator:!checked {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #702632;\n"
"	color: #FFFFFF;\n"
"	background-color: none;\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: #EEEEEE;\n"
"	color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}")

        self.gridLayout_6.addWidget(self.checkBoxPtNeedSickList_2, 2, 3, 1, 2)

        self.labelPtWorkListDateOpening_2 = QLabel(self.work_block)
        self.labelPtWorkListDateOpening_2.setObjectName(u"labelPtWorkListDateOpening_2")
        palette41 = QPalette()
        palette41.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette41.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette41.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette41.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette41.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette41.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette41.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette41.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette41.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette41.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette41.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette41.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette41.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette41.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette41.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette41.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette41.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette41.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette41.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette41.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette41.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette41.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette41.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette41.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette41.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette41.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette41.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette41.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette41.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette41.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette41.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette41.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette41.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette41.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette41.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette41.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette41.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette41.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette41.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette41.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette41.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette41.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette41.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette41.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette41.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette41.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtWorkListDateOpening_2.setPalette(palette41)
        self.labelPtWorkListDateOpening_2.setFont(font3)
        self.labelPtWorkListDateOpening_2.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_6.addWidget(self.labelPtWorkListDateOpening_2, 11, 3, 1, 2)

        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/personal_injury_FILL1_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.work_page, icon1, "")
        self.obj_status = QWidget()
        self.obj_status.setObjectName(u"obj_status")
        self.verticalLayout = QVBoxLayout(self.obj_status)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)

        self.frame_templates = QFrame(self.obj_status)
        self.frame_templates.setObjectName(u"frame_templates")
        self.frame_templates.setStyleSheet(u"font-size: 15pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_7 = QGridLayout(self.frame_templates)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(5)
        self.gridLayout_7.setVerticalSpacing(1)
        self.gridLayout_7.setContentsMargins(5, 5, 5, 5)
        self.comboBoxGeneralStTemplate = QComboBox(self.frame_templates)
        self.comboBoxGeneralStTemplate.addItem("")
        self.comboBoxGeneralStTemplate.setObjectName(u"comboBoxGeneralStTemplate")
        self.comboBoxGeneralStTemplate.setMaximumSize(QSize(16777215, 16777215))
        palette42 = QPalette()
        palette42.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette42.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette42.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette42.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette42.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette42.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette42.setBrush(QPalette.Active, QPalette.Text, brush)
        palette42.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette42.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette42.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette42.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette42.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette42.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette42.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette42.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette42.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette42.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette42.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette42.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette42.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette42.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette42.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette42.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette42.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette42.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette42.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette42.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette42.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette42.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette42.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette42.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette42.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette42.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette42.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxGeneralStTemplate.setPalette(palette42)
        self.comboBoxGeneralStTemplate.setFont(font3)
        self.comboBoxGeneralStTemplate.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.comboBoxGeneralStTemplate, 2, 0, 1, 1)

        self.pushButtonAddNewTemplateGeneralSt = QPushButton(self.frame_templates)
        self.pushButtonAddNewTemplateGeneralSt.setObjectName(u"pushButtonAddNewTemplateGeneralSt")
        palette43 = QPalette()
        palette43.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette43.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette43.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette43.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette43.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette43.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette43.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette43.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette43.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette43.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette43.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette43.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette43.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette43.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette43.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette43.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette43.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette43.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette43.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette43.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette43.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette43.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette43.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette43.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette43.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette43.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette43.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette43.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette43.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette43.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette43.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette43.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette43.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette43.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette43.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette43.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette43.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette43.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette43.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette43.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette43.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette43.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette43.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette43.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette43.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette43.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        self.pushButtonAddNewTemplateGeneralSt.setPalette(palette43)
        self.pushButtonAddNewTemplateGeneralSt.setFont(font)
        self.pushButtonAddNewTemplateGeneralSt.setStyleSheet(u"QPushButton {\n"
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
"background-color: #EEEEEE;\n"
"border: 1px solid rgba(50, 98, 115, 255);\n"
"}\n"
"\n"
"")

        self.gridLayout_7.addWidget(self.pushButtonAddNewTemplateGeneralSt, 4, 1, 1, 1)

        self.label = QLabel(self.frame_templates)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 2)

        self.pushButton_push_temp = QPushButton(self.frame_templates)
        self.pushButton_push_temp.setObjectName(u"pushButton_push_temp")
        palette44 = QPalette()
        palette44.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette44.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette44.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette44.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette44.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette44.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette44.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette44.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette44.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette44.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette44.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette44.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette44.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette44.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette44.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette44.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette44.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette44.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette44.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette44.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette44.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette44.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette44.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette44.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette44.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette44.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette44.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette44.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette44.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette44.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette44.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette44.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette44.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette44.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette44.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette44.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette44.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette44.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette44.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette44.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette44.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette44.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette44.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette44.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette44.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette44.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        self.pushButton_push_temp.setPalette(palette44)
        self.pushButton_push_temp.setFont(font)
        self.pushButton_push_temp.setStyleSheet(u"QPushButton {\n"
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
"background-color: #EEEEEE;\n"
"border: 1px solid rgba(50, 98, 115, 255);\n"
"}\n"
"\n"
"")

        self.gridLayout_7.addWidget(self.pushButton_push_temp, 2, 1, 1, 1)

        self.lineEdit_new_template_name = QLineEdit(self.frame_templates)
        self.lineEdit_new_template_name.setObjectName(u"lineEdit_new_template_name")
        self.lineEdit_new_template_name.setMinimumSize(QSize(350, 0))
        self.lineEdit_new_template_name.setFont(font3)
        self.lineEdit_new_template_name.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_7.addWidget(self.lineEdit_new_template_name, 4, 0, 1, 1)

        self.label_3 = QLabel(self.frame_templates)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_templates)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color: transparent;\n"
"border: none;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_4, 3, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_templates)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.frame = QFrame(self.obj_status)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(1)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.labelPtHearthNoise = QLabel(self.frame)
        self.labelPtHearthNoise.setObjectName(u"labelPtHearthNoise")
        self.labelPtHearthNoise.setMaximumSize(QSize(150, 16777215))
        palette45 = QPalette()
        palette45.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette45.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette45.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette45.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette45.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette45.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette45.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette45.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette45.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette45.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette45.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette45.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette45.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette45.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette45.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette45.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette45.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette45.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette45.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette45.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette45.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette45.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette45.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette45.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette45.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette45.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette45.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette45.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette45.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette45.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette45.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette45.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette45.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette45.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette45.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette45.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette45.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette45.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette45.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette45.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette45.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette45.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette45.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette45.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette45.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette45.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtHearthNoise.setPalette(palette45)
        self.labelPtHearthNoise.setFont(font3)
        self.labelPtHearthNoise.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtHearthNoise, 13, 0, 1, 1)

        self.comboBoxPtSkinState_1 = QComboBox(self.frame)
        self.comboBoxPtSkinState_1.addItem("")
        self.comboBoxPtSkinState_1.addItem("")
        self.comboBoxPtSkinState_1.addItem("")
        self.comboBoxPtSkinState_1.addItem("")
        self.comboBoxPtSkinState_1.addItem("")
        self.comboBoxPtSkinState_1.addItem("")
        self.comboBoxPtSkinState_1.setObjectName(u"comboBoxPtSkinState_1")
        palette46 = QPalette()
        palette46.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette46.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette46.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette46.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette46.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette46.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette46.setBrush(QPalette.Active, QPalette.Text, brush)
        palette46.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette46.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette46.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette46.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette46.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette46.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette46.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette46.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette46.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette46.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette46.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette46.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette46.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette46.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette46.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette46.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette46.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette46.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette46.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette46.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette46.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette46.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette46.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette46.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette46.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette46.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette46.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette46.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette46.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtSkinState_1.setPalette(palette46)
        self.comboBoxPtSkinState_1.setFont(font3)
        self.comboBoxPtSkinState_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtSkinState_1.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtSkinState_1, 2, 1, 1, 1)

        self.labelPtGeneralState = QLabel(self.frame)
        self.labelPtGeneralState.setObjectName(u"labelPtGeneralState")
        self.labelPtGeneralState.setMaximumSize(QSize(150, 16777215))
        palette47 = QPalette()
        palette47.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette47.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette47.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette47.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette47.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette47.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette47.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette47.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette47.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette47.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette47.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette47.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette47.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette47.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette47.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette47.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette47.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette47.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette47.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette47.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette47.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette47.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette47.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette47.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette47.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette47.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette47.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette47.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette47.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette47.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette47.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette47.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette47.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette47.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette47.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette47.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette47.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette47.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette47.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette47.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette47.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette47.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette47.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette47.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette47.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette47.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtGeneralState.setPalette(palette47)
        self.labelPtGeneralState.setFont(font3)
        self.labelPtGeneralState.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtGeneralState, 1, 0, 1, 1)

        self.labelPtDyspnea = QLabel(self.frame)
        self.labelPtDyspnea.setObjectName(u"labelPtDyspnea")
        self.labelPtDyspnea.setMaximumSize(QSize(150, 16777215))
        palette48 = QPalette()
        palette48.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette48.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette48.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette48.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette48.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette48.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette48.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette48.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette48.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette48.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette48.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette48.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette48.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette48.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette48.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette48.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette48.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette48.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette48.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette48.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette48.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette48.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette48.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette48.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette48.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette48.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette48.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette48.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette48.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette48.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette48.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette48.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette48.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette48.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette48.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette48.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette48.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette48.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette48.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette48.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette48.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette48.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette48.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette48.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette48.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette48.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette48.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette48.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtDyspnea.setPalette(palette48)
        self.labelPtDyspnea.setFont(font3)
        self.labelPtDyspnea.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtDyspnea, 9, 0, 1, 1)

        self.labelPtWheezing = QLabel(self.frame)
        self.labelPtWheezing.setObjectName(u"labelPtWheezing")
        self.labelPtWheezing.setMaximumSize(QSize(150, 16777215))
        palette49 = QPalette()
        palette49.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette49.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette49.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette49.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette49.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette49.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette49.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette49.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette49.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette49.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette49.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette49.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette49.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette49.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette49.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette49.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette49.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette49.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette49.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette49.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette49.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette49.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette49.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette49.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette49.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette49.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette49.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette49.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette49.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette49.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette49.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette49.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette49.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette49.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette49.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette49.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette49.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette49.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette49.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette49.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette49.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette49.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette49.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette49.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette49.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette49.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtWheezing.setPalette(palette49)
        self.labelPtWheezing.setFont(font3)
        self.labelPtWheezing.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtWheezing, 7, 0, 1, 1)

        self.comboBoxPtStomach_1 = QComboBox(self.frame)
        self.comboBoxPtStomach_1.addItem("")
        self.comboBoxPtStomach_1.addItem("")
        self.comboBoxPtStomach_1.addItem("")
        self.comboBoxPtStomach_1.addItem("")
        self.comboBoxPtStomach_1.setObjectName(u"comboBoxPtStomach_1")
        palette50 = QPalette()
        palette50.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette50.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette50.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette50.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette50.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette50.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette50.setBrush(QPalette.Active, QPalette.Text, brush)
        palette50.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette50.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette50.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette50.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette50.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette50.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette50.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette50.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette50.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette50.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette50.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette50.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette50.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette50.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette50.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette50.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette50.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette50.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette50.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette50.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette50.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette50.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette50.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette50.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette50.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette50.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette50.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette50.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette50.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtStomach_1.setPalette(palette50)
        self.comboBoxPtStomach_1.setFont(font3)
        self.comboBoxPtStomach_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtStomach_1.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtStomach_1, 14, 1, 1, 1)

        self.comboBoxPtBreathing_3 = QComboBox(self.frame)
        self.comboBoxPtBreathing_3.addItem("")
        self.comboBoxPtBreathing_3.addItem("")
        self.comboBoxPtBreathing_3.addItem("")
        self.comboBoxPtBreathing_3.setObjectName(u"comboBoxPtBreathing_3")
        palette51 = QPalette()
        palette51.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette51.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette51.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette51.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette51.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette51.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette51.setBrush(QPalette.Active, QPalette.Text, brush)
        palette51.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette51.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette51.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette51.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette51.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette51.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette51.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette51.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette51.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette51.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette51.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette51.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette51.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette51.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette51.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette51.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette51.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette51.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette51.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette51.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette51.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette51.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette51.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette51.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette51.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette51.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette51.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette51.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette51.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtBreathing_3.setPalette(palette51)
        self.comboBoxPtBreathing_3.setFont(font3)
        self.comboBoxPtBreathing_3.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtBreathing_3.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtBreathing_3, 6, 1, 1, 2)

        self.comboBoxPtUrination_3 = QComboBox(self.frame)
        self.comboBoxPtUrination_3.addItem("")
        self.comboBoxPtUrination_3.addItem("")
        self.comboBoxPtUrination_3.addItem("")
        self.comboBoxPtUrination_3.addItem("")
        self.comboBoxPtUrination_3.setObjectName(u"comboBoxPtUrination_3")
        palette52 = QPalette()
        palette52.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette52.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette52.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette52.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette52.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette52.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette52.setBrush(QPalette.Active, QPalette.Text, brush)
        palette52.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette52.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette52.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette52.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette52.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette52.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette52.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette52.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette52.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette52.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette52.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette52.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette52.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette52.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette52.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette52.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette52.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette52.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette52.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette52.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette52.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette52.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette52.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette52.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette52.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette52.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette52.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette52.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette52.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtUrination_3.setPalette(palette52)
        self.comboBoxPtUrination_3.setFont(font3)
        self.comboBoxPtUrination_3.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtUrination_3.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtUrination_3, 19, 1, 1, 2)

        self.comboBoxPtBreathing_1 = QComboBox(self.frame)
        self.comboBoxPtBreathing_1.addItem("")
        self.comboBoxPtBreathing_1.addItem("")
        self.comboBoxPtBreathing_1.addItem("")
        self.comboBoxPtBreathing_1.setObjectName(u"comboBoxPtBreathing_1")
        palette53 = QPalette()
        palette53.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette53.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette53.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette53.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette53.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette53.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette53.setBrush(QPalette.Active, QPalette.Text, brush)
        palette53.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette53.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette53.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette53.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette53.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette53.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette53.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette53.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette53.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette53.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette53.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette53.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette53.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette53.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette53.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette53.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette53.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette53.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette53.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette53.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette53.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette53.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette53.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette53.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette53.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette53.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette53.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtBreathing_1.setPalette(palette53)
        self.comboBoxPtBreathing_1.setFont(font3)
        self.comboBoxPtBreathing_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtBreathing_1.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtBreathing_1, 5, 1, 1, 1)

        self.comboBoxPtGeneralState = QComboBox(self.frame)
        self.comboBoxPtGeneralState.addItem("")
        self.comboBoxPtGeneralState.addItem("")
        self.comboBoxPtGeneralState.addItem("")
        self.comboBoxPtGeneralState.addItem("")
        self.comboBoxPtGeneralState.addItem("")
        self.comboBoxPtGeneralState.addItem("")
        self.comboBoxPtGeneralState.setObjectName(u"comboBoxPtGeneralState")
        palette54 = QPalette()
        palette54.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette54.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette54.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette54.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette54.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette54.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette54.setBrush(QPalette.Active, QPalette.Text, brush)
        palette54.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette54.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette54.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette54.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette54.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette54.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette54.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette54.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette54.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette54.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette54.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette54.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette54.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette54.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette54.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette54.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette54.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette54.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette54.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette54.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette54.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette54.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette54.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette54.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette54.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette54.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette54.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette54.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette54.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtGeneralState.setPalette(palette54)
        self.comboBoxPtGeneralState.setFont(font3)
        self.comboBoxPtGeneralState.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.comboBoxPtGeneralState, 1, 1, 1, 2)

        self.comboBoxPtHearthTone_3 = QComboBox(self.frame)
        self.comboBoxPtHearthTone_3.addItem("")
        self.comboBoxPtHearthTone_3.addItem("")
        self.comboBoxPtHearthTone_3.addItem("")
        self.comboBoxPtHearthTone_3.addItem("")
        self.comboBoxPtHearthTone_3.setObjectName(u"comboBoxPtHearthTone_3")
        palette55 = QPalette()
        palette55.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette55.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette55.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette55.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette55.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette55.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette55.setBrush(QPalette.Active, QPalette.Text, brush)
        palette55.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette55.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette55.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette55.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette55.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette55.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette55.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette55.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette55.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette55.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette55.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette55.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette55.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette55.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette55.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette55.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette55.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette55.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette55.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette55.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette55.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette55.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette55.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette55.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette55.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette55.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette55.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette55.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette55.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtHearthTone_3.setPalette(palette55)
        self.comboBoxPtHearthTone_3.setFont(font3)
        self.comboBoxPtHearthTone_3.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtHearthTone_3.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtHearthTone_3, 12, 1, 1, 2)

        self.comboBoxPtDyspnea_2 = QComboBox(self.frame)
        self.comboBoxPtDyspnea_2.addItem("")
        self.comboBoxPtDyspnea_2.addItem("")
        self.comboBoxPtDyspnea_2.addItem("")
        self.comboBoxPtDyspnea_2.addItem("")
        self.comboBoxPtDyspnea_2.setObjectName(u"comboBoxPtDyspnea_2")
        palette56 = QPalette()
        palette56.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette56.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette56.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette56.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette56.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette56.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette56.setBrush(QPalette.Active, QPalette.Text, brush)
        palette56.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette56.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette56.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette56.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette56.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette56.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette56.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette56.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette56.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette56.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette56.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette56.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette56.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette56.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette56.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette56.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette56.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette56.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette56.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette56.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette56.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette56.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette56.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette56.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette56.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette56.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette56.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette56.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette56.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtDyspnea_2.setPalette(palette56)
        self.comboBoxPtDyspnea_2.setFont(font3)
        self.comboBoxPtDyspnea_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtDyspnea_2.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtDyspnea_2, 10, 1, 1, 1)

        self.labelPtHearthTones = QLabel(self.frame)
        self.labelPtHearthTones.setObjectName(u"labelPtHearthTones")
        self.labelPtHearthTones.setMaximumSize(QSize(150, 16777215))
        palette57 = QPalette()
        palette57.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette57.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette57.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette57.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette57.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette57.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette57.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette57.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette57.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette57.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette57.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette57.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette57.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette57.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette57.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette57.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette57.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette57.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette57.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette57.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette57.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette57.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette57.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette57.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette57.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette57.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette57.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette57.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette57.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette57.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette57.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette57.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette57.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette57.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette57.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette57.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette57.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette57.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette57.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette57.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette57.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette57.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette57.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette57.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette57.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette57.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette57.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette57.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtHearthTones.setPalette(palette57)
        self.labelPtHearthTones.setFont(font3)
        self.labelPtHearthTones.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtHearthTones, 11, 0, 1, 1)

        self.comboBoxPtDefecation_2 = QComboBox(self.frame)
        self.comboBoxPtDefecation_2.addItem("")
        self.comboBoxPtDefecation_2.addItem("")
        self.comboBoxPtDefecation_2.addItem("")
        self.comboBoxPtDefecation_2.addItem("")
        self.comboBoxPtDefecation_2.setObjectName(u"comboBoxPtDefecation_2")
        palette58 = QPalette()
        palette58.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette58.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette58.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette58.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette58.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette58.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette58.setBrush(QPalette.Active, QPalette.Text, brush)
        palette58.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette58.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette58.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette58.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette58.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette58.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette58.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette58.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette58.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette58.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette58.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette58.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette58.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette58.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette58.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette58.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette58.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette58.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette58.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette58.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette58.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette58.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette58.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette58.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette58.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette58.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette58.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette58.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette58.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtDefecation_2.setPalette(palette58)
        self.comboBoxPtDefecation_2.setFont(font3)
        self.comboBoxPtDefecation_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtDefecation_2.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtDefecation_2, 16, 2, 1, 1)

        self.labelPtLymphnode = QLabel(self.frame)
        self.labelPtLymphnode.setObjectName(u"labelPtLymphnode")
        self.labelPtLymphnode.setMaximumSize(QSize(150, 16777215))
        palette59 = QPalette()
        palette59.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette59.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette59.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette59.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette59.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette59.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette59.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette59.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette59.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette59.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette59.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette59.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette59.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette59.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette59.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette59.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette59.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette59.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette59.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette59.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette59.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette59.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette59.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette59.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette59.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette59.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette59.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette59.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette59.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette59.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette59.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette59.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette59.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette59.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette59.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette59.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette59.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette59.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette59.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette59.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette59.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette59.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette59.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette59.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette59.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette59.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette59.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette59.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtLymphnode.setPalette(palette59)
        self.labelPtLymphnode.setFont(font3)
        self.labelPtLymphnode.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtLymphnode, 3, 0, 1, 1)

        self.labelPtDefecation = QLabel(self.frame)
        self.labelPtDefecation.setObjectName(u"labelPtDefecation")
        self.labelPtDefecation.setMaximumSize(QSize(150, 16777215))
        palette60 = QPalette()
        palette60.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette60.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette60.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette60.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette60.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette60.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette60.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette60.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette60.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette60.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette60.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette60.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette60.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette60.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette60.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette60.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette60.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette60.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette60.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette60.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette60.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette60.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette60.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette60.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette60.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette60.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette60.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette60.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette60.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette60.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette60.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette60.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette60.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette60.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette60.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette60.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette60.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette60.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette60.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette60.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette60.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette60.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette60.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette60.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette60.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette60.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette60.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette60.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtDefecation.setPalette(palette60)
        self.labelPtDefecation.setFont(font3)
        self.labelPtDefecation.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtDefecation, 16, 0, 1, 1)

        self.comboBoxPtBreathing_2 = QComboBox(self.frame)
        self.comboBoxPtBreathing_2.addItem("")
        self.comboBoxPtBreathing_2.addItem("")
        self.comboBoxPtBreathing_2.addItem("")
        self.comboBoxPtBreathing_2.setObjectName(u"comboBoxPtBreathing_2")
        palette61 = QPalette()
        palette61.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette61.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette61.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette61.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette61.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette61.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette61.setBrush(QPalette.Active, QPalette.Text, brush)
        palette61.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette61.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette61.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette61.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette61.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette61.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette61.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette61.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette61.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette61.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette61.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette61.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette61.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette61.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette61.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette61.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette61.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette61.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette61.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette61.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette61.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette61.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette61.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette61.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette61.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette61.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette61.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette61.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette61.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtBreathing_2.setPalette(palette61)
        self.comboBoxPtBreathing_2.setFont(font3)
        self.comboBoxPtBreathing_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtBreathing_2.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtBreathing_2, 5, 2, 1, 1)

        self.comboBoxPtDyspnea_1 = QComboBox(self.frame)
        self.comboBoxPtDyspnea_1.addItem("")
        self.comboBoxPtDyspnea_1.addItem("")
        self.comboBoxPtDyspnea_1.addItem("")
        self.comboBoxPtDyspnea_1.addItem("")
        self.comboBoxPtDyspnea_1.setObjectName(u"comboBoxPtDyspnea_1")
        palette62 = QPalette()
        palette62.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette62.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette62.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette62.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette62.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette62.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette62.setBrush(QPalette.Active, QPalette.Text, brush)
        palette62.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette62.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette62.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette62.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette62.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette62.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette62.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette62.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette62.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette62.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette62.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette62.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette62.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette62.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette62.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette62.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette62.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette62.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette62.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette62.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette62.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette62.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette62.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette62.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette62.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette62.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette62.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette62.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette62.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtDyspnea_1.setPalette(palette62)
        self.comboBoxPtDyspnea_1.setFont(font3)
        self.comboBoxPtDyspnea_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtDyspnea_1.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtDyspnea_1, 9, 2, 1, 1)

        self.labelPtBreathing = QLabel(self.frame)
        self.labelPtBreathing.setObjectName(u"labelPtBreathing")
        self.labelPtBreathing.setMaximumSize(QSize(150, 16777215))
        palette63 = QPalette()
        palette63.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette63.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette63.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette63.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette63.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette63.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette63.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette63.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette63.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette63.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette63.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette63.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette63.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette63.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette63.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette63.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette63.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette63.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette63.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette63.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette63.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette63.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette63.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette63.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette63.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette63.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette63.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette63.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette63.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette63.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette63.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette63.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette63.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette63.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette63.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette63.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette63.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette63.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette63.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette63.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette63.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette63.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette63.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette63.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette63.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette63.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette63.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette63.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtBreathing.setPalette(palette63)
        self.labelPtBreathing.setFont(font3)
        self.labelPtBreathing.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtBreathing, 5, 0, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 3)

        self.comboBoxPtUrination_2 = QComboBox(self.frame)
        self.comboBoxPtUrination_2.addItem("")
        self.comboBoxPtUrination_2.addItem("")
        self.comboBoxPtUrination_2.addItem("")
        self.comboBoxPtUrination_2.setObjectName(u"comboBoxPtUrination_2")
        palette64 = QPalette()
        palette64.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette64.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette64.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette64.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette64.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette64.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette64.setBrush(QPalette.Active, QPalette.Text, brush)
        palette64.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette64.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette64.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette64.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette64.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette64.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette64.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette64.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette64.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette64.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette64.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette64.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette64.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette64.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette64.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette64.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette64.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette64.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette64.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette64.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette64.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette64.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette64.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette64.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette64.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette64.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette64.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette64.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette64.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtUrination_2.setPalette(palette64)
        self.comboBoxPtUrination_2.setFont(font3)
        self.comboBoxPtUrination_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtUrination_2.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtUrination_2, 18, 2, 1, 1)

        self.comboBoxPtDyspneaChoice = QComboBox(self.frame)
        self.comboBoxPtDyspneaChoice.addItem("")
        self.comboBoxPtDyspneaChoice.addItem("")
        self.comboBoxPtDyspneaChoice.setObjectName(u"comboBoxPtDyspneaChoice")
        palette65 = QPalette()
        palette65.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette65.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette65.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette65.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette65.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette65.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette65.setBrush(QPalette.Active, QPalette.Text, brush)
        palette65.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette65.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette65.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette65.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette65.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette65.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette65.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette65.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette65.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette65.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette65.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette65.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette65.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette65.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette65.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette65.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette65.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette65.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette65.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette65.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette65.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette65.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette65.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette65.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette65.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette65.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette65.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette65.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette65.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtDyspneaChoice.setPalette(palette65)
        self.comboBoxPtDyspneaChoice.setFont(font3)
        self.comboBoxPtDyspneaChoice.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.comboBoxPtDyspneaChoice, 9, 1, 1, 1)

        self.comboBoxPtDefecation_1 = QComboBox(self.frame)
        self.comboBoxPtDefecation_1.addItem("")
        self.comboBoxPtDefecation_1.addItem("")
        self.comboBoxPtDefecation_1.addItem("")
        self.comboBoxPtDefecation_1.setObjectName(u"comboBoxPtDefecation_1")
        palette66 = QPalette()
        palette66.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette66.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette66.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette66.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette66.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette66.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette66.setBrush(QPalette.Active, QPalette.Text, brush)
        palette66.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette66.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette66.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette66.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette66.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette66.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette66.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette66.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette66.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette66.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette66.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette66.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette66.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette66.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette66.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette66.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette66.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette66.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette66.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette66.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette66.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette66.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette66.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette66.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette66.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette66.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette66.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette66.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette66.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtDefecation_1.setPalette(palette66)
        self.comboBoxPtDefecation_1.setFont(font3)
        self.comboBoxPtDefecation_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtDefecation_1.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtDefecation_1, 16, 1, 1, 1)

        self.comboBoxPtDyspnea_3 = QComboBox(self.frame)
        self.comboBoxPtDyspnea_3.addItem("")
        self.comboBoxPtDyspnea_3.addItem("")
        self.comboBoxPtDyspnea_3.setObjectName(u"comboBoxPtDyspnea_3")
        palette67 = QPalette()
        palette67.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette67.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette67.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette67.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette67.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette67.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette67.setBrush(QPalette.Active, QPalette.Text, brush)
        palette67.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette67.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette67.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette67.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette67.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette67.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette67.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette67.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette67.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette67.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette67.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette67.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette67.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette67.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette67.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette67.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette67.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette67.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette67.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette67.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette67.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette67.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette67.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette67.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette67.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette67.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette67.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette67.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette67.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtDyspnea_3.setPalette(palette67)
        self.comboBoxPtDyspnea_3.setFont(font3)
        self.comboBoxPtDyspnea_3.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtDyspnea_3.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtDyspnea_3, 10, 2, 1, 1)

        self.comboBoxPtMucousMembr_1 = QComboBox(self.frame)
        self.comboBoxPtMucousMembr_1.addItem("")
        self.comboBoxPtMucousMembr_1.addItem("")
        self.comboBoxPtMucousMembr_1.addItem("")
        self.comboBoxPtMucousMembr_1.addItem("")
        self.comboBoxPtMucousMembr_1.addItem("")
        self.comboBoxPtMucousMembr_1.addItem("")
        self.comboBoxPtMucousMembr_1.setObjectName(u"comboBoxPtMucousMembr_1")
        palette68 = QPalette()
        palette68.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette68.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette68.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette68.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette68.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette68.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette68.setBrush(QPalette.Active, QPalette.Text, brush)
        palette68.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette68.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette68.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette68.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette68.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette68.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette68.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette68.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette68.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette68.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette68.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette68.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette68.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette68.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette68.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette68.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette68.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette68.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette68.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette68.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette68.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette68.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette68.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette68.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette68.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette68.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette68.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette68.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette68.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtMucousMembr_1.setPalette(palette68)
        self.comboBoxPtMucousMembr_1.setFont(font3)
        self.comboBoxPtMucousMembr_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtMucousMembr_1.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtMucousMembr_1, 4, 1, 1, 2)

        self.labelPtUrination = QLabel(self.frame)
        self.labelPtUrination.setObjectName(u"labelPtUrination")
        self.labelPtUrination.setMaximumSize(QSize(150, 16777215))
        palette69 = QPalette()
        palette69.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette69.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette69.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette69.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette69.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette69.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette69.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette69.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette69.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette69.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette69.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette69.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette69.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette69.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette69.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette69.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette69.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette69.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette69.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette69.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette69.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette69.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette69.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette69.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette69.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette69.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette69.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette69.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette69.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette69.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette69.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette69.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette69.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette69.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette69.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette69.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette69.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette69.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette69.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette69.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette69.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette69.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette69.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette69.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette69.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette69.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette69.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette69.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtUrination.setPalette(palette69)
        self.labelPtUrination.setFont(font3)
        self.labelPtUrination.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtUrination, 18, 0, 1, 1)

        self.comboBoxPtUrination_1 = QComboBox(self.frame)
        self.comboBoxPtUrination_1.addItem("")
        self.comboBoxPtUrination_1.addItem("")
        self.comboBoxPtUrination_1.addItem("")
        self.comboBoxPtUrination_1.addItem("")
        self.comboBoxPtUrination_1.addItem("")
        self.comboBoxPtUrination_1.addItem("")
        self.comboBoxPtUrination_1.addItem("")
        self.comboBoxPtUrination_1.setObjectName(u"comboBoxPtUrination_1")
        palette70 = QPalette()
        palette70.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette70.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette70.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette70.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette70.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette70.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette70.setBrush(QPalette.Active, QPalette.Text, brush)
        palette70.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette70.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette70.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette70.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette70.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette70.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette70.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette70.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette70.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette70.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette70.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette70.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette70.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette70.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette70.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette70.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette70.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette70.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette70.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette70.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette70.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette70.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette70.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette70.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette70.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette70.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette70.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette70.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette70.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtUrination_1.setPalette(palette70)
        self.comboBoxPtUrination_1.setFont(font3)
        self.comboBoxPtUrination_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtUrination_1.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtUrination_1, 18, 1, 1, 1)

        self.comboBoxPtDefecation_3 = QComboBox(self.frame)
        self.comboBoxPtDefecation_3.addItem("")
        self.comboBoxPtDefecation_3.addItem("")
        self.comboBoxPtDefecation_3.addItem("")
        self.comboBoxPtDefecation_3.addItem("")
        self.comboBoxPtDefecation_3.addItem("")
        self.comboBoxPtDefecation_3.addItem("")
        self.comboBoxPtDefecation_3.setObjectName(u"comboBoxPtDefecation_3")
        palette71 = QPalette()
        palette71.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette71.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette71.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette71.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette71.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette71.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette71.setBrush(QPalette.Active, QPalette.Text, brush)
        palette71.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette71.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette71.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette71.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette71.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette71.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette71.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette71.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette71.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette71.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette71.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette71.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette71.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette71.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette71.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette71.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette71.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette71.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette71.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette71.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette71.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette71.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette71.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette71.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette71.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette71.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette71.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette71.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette71.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtDefecation_3.setPalette(palette71)
        self.comboBoxPtDefecation_3.setFont(font3)
        self.comboBoxPtDefecation_3.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtDefecation_3.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtDefecation_3, 17, 1, 1, 2)

        self.labelPtSkinState = QLabel(self.frame)
        self.labelPtSkinState.setObjectName(u"labelPtSkinState")
        self.labelPtSkinState.setMaximumSize(QSize(150, 16777215))
        palette72 = QPalette()
        palette72.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette72.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette72.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette72.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette72.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette72.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette72.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette72.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette72.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette72.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette72.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette72.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette72.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette72.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette72.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette72.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette72.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette72.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette72.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette72.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette72.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette72.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette72.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette72.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette72.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette72.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette72.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette72.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette72.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette72.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette72.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette72.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette72.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette72.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette72.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette72.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette72.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette72.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette72.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette72.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette72.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette72.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette72.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette72.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette72.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette72.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette72.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette72.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtSkinState.setPalette(palette72)
        self.labelPtSkinState.setFont(font3)
        self.labelPtSkinState.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtSkinState, 2, 0, 1, 1)

        self.comboBoxPtHearthTone_2 = QComboBox(self.frame)
        self.comboBoxPtHearthTone_2.addItem("")
        self.comboBoxPtHearthTone_2.addItem("")
        self.comboBoxPtHearthTone_2.setObjectName(u"comboBoxPtHearthTone_2")
        palette73 = QPalette()
        palette73.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette73.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette73.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette73.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette73.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette73.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette73.setBrush(QPalette.Active, QPalette.Text, brush)
        palette73.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette73.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette73.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette73.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette73.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette73.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette73.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette73.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette73.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette73.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette73.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette73.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette73.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette73.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette73.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette73.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette73.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette73.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette73.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette73.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette73.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette73.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette73.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette73.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette73.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette73.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette73.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette73.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette73.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtHearthTone_2.setPalette(palette73)
        self.comboBoxPtHearthTone_2.setFont(font3)
        self.comboBoxPtHearthTone_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtHearthTone_2.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtHearthTone_2, 11, 2, 1, 1)

        self.comboBoxPtHearthNoiseChoice = QComboBox(self.frame)
        self.comboBoxPtHearthNoiseChoice.addItem("")
        self.comboBoxPtHearthNoiseChoice.addItem("")
        self.comboBoxPtHearthNoiseChoice.setObjectName(u"comboBoxPtHearthNoiseChoice")
        palette74 = QPalette()
        palette74.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette74.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette74.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette74.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette74.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette74.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette74.setBrush(QPalette.Active, QPalette.Text, brush)
        palette74.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette74.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette74.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette74.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette74.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette74.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette74.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette74.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette74.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette74.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette74.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette74.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette74.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette74.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette74.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette74.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette74.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette74.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette74.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette74.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette74.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette74.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette74.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette74.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette74.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette74.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette74.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette74.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette74.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtHearthNoiseChoice.setPalette(palette74)
        self.comboBoxPtHearthNoiseChoice.setFont(font3)
        self.comboBoxPtHearthNoiseChoice.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.comboBoxPtHearthNoiseChoice, 13, 1, 1, 1)

        self.comboBoxPtWheezing_1 = QComboBox(self.frame)
        self.comboBoxPtWheezing_1.addItem("")
        self.comboBoxPtWheezing_1.addItem("")
        self.comboBoxPtWheezing_1.addItem("")
        self.comboBoxPtWheezing_1.setObjectName(u"comboBoxPtWheezing_1")
        palette75 = QPalette()
        palette75.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette75.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette75.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette75.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette75.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette75.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette75.setBrush(QPalette.Active, QPalette.Text, brush)
        palette75.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette75.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette75.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette75.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette75.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette75.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette75.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette75.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette75.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette75.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette75.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette75.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette75.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette75.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette75.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette75.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette75.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette75.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette75.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette75.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette75.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette75.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette75.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette75.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette75.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette75.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette75.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette75.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette75.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtWheezing_1.setPalette(palette75)
        self.comboBoxPtWheezing_1.setFont(font3)
        self.comboBoxPtWheezing_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtWheezing_1.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtWheezing_1, 7, 2, 1, 1)

        self.labelPtStObjOther = QLabel(self.frame)
        self.labelPtStObjOther.setObjectName(u"labelPtStObjOther")
        self.labelPtStObjOther.setMaximumSize(QSize(150, 16777215))
        palette76 = QPalette()
        palette76.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette76.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette76.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette76.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette76.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette76.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette76.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette76.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette76.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette76.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette76.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette76.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette76.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette76.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette76.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette76.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette76.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette76.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette76.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette76.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette76.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette76.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette76.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette76.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette76.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette76.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette76.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette76.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette76.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette76.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette76.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette76.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette76.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette76.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette76.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette76.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette76.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette76.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette76.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette76.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette76.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette76.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette76.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette76.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette76.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette76.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette76.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette76.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtStObjOther.setPalette(palette76)
        self.labelPtStObjOther.setFont(font3)
        self.labelPtStObjOther.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtStObjOther, 20, 0, 1, 1)

        self.comboBoxPtWheezing_3 = QComboBox(self.frame)
        self.comboBoxPtWheezing_3.addItem("")
        self.comboBoxPtWheezing_3.addItem("")
        self.comboBoxPtWheezing_3.addItem("")
        self.comboBoxPtWheezing_3.addItem("")
        self.comboBoxPtWheezing_3.setObjectName(u"comboBoxPtWheezing_3")
        palette77 = QPalette()
        palette77.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette77.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette77.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette77.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette77.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette77.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette77.setBrush(QPalette.Active, QPalette.Text, brush)
        palette77.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette77.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette77.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette77.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette77.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette77.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette77.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette77.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette77.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette77.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette77.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette77.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette77.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette77.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette77.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette77.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette77.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette77.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette77.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette77.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette77.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette77.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette77.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette77.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette77.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette77.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette77.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette77.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette77.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtWheezing_3.setPalette(palette77)
        self.comboBoxPtWheezing_3.setFont(font3)
        self.comboBoxPtWheezing_3.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtWheezing_3.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtWheezing_3, 8, 2, 1, 1)

        self.comboBoxPtHearthTone_1 = QComboBox(self.frame)
        self.comboBoxPtHearthTone_1.addItem("")
        self.comboBoxPtHearthTone_1.addItem("")
        self.comboBoxPtHearthTone_1.addItem("")
        self.comboBoxPtHearthTone_1.setObjectName(u"comboBoxPtHearthTone_1")
        palette78 = QPalette()
        palette78.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette78.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette78.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette78.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette78.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette78.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette78.setBrush(QPalette.Active, QPalette.Text, brush)
        palette78.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette78.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette78.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette78.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette78.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette78.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette78.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette78.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette78.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette78.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette78.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette78.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette78.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette78.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette78.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette78.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette78.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette78.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette78.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette78.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette78.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette78.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette78.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette78.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette78.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette78.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette78.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette78.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette78.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtHearthTone_1.setPalette(palette78)
        self.comboBoxPtHearthTone_1.setFont(font3)
        self.comboBoxPtHearthTone_1.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtHearthTone_1.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtHearthTone_1, 11, 1, 1, 1)

        self.comboBoxPtWheezingChoice = QComboBox(self.frame)
        self.comboBoxPtWheezingChoice.addItem("")
        self.comboBoxPtWheezingChoice.addItem("")
        self.comboBoxPtWheezingChoice.setObjectName(u"comboBoxPtWheezingChoice")
        palette79 = QPalette()
        palette79.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette79.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette79.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette79.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette79.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette79.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette79.setBrush(QPalette.Active, QPalette.Text, brush)
        palette79.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette79.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette79.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette79.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette79.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette79.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette79.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette79.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette79.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette79.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette79.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette79.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette79.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette79.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette79.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette79.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette79.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette79.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette79.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette79.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette79.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette79.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette79.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette79.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette79.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette79.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette79.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette79.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette79.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtWheezingChoice.setPalette(palette79)
        self.comboBoxPtWheezingChoice.setFont(font3)
        self.comboBoxPtWheezingChoice.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.comboBoxPtWheezingChoice, 7, 1, 1, 1)

        self.comboBoxPtStomach_3 = QComboBox(self.frame)
        self.comboBoxPtStomach_3.addItem("")
        self.comboBoxPtStomach_3.addItem("")
        self.comboBoxPtStomach_3.setObjectName(u"comboBoxPtStomach_3")
        palette80 = QPalette()
        palette80.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette80.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette80.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette80.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette80.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette80.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette80.setBrush(QPalette.Active, QPalette.Text, brush)
        palette80.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette80.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette80.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette80.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette80.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette80.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette80.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette80.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette80.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette80.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette80.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette80.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette80.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette80.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette80.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette80.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette80.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette80.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette80.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette80.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette80.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette80.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette80.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette80.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette80.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette80.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette80.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette80.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette80.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtStomach_3.setPalette(palette80)
        self.comboBoxPtStomach_3.setFont(font3)
        self.comboBoxPtStomach_3.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtStomach_3.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtStomach_3, 15, 1, 1, 2)

        self.comboBoxPtSkinState_2 = QComboBox(self.frame)
        self.comboBoxPtSkinState_2.addItem("")
        self.comboBoxPtSkinState_2.addItem("")
        self.comboBoxPtSkinState_2.setObjectName(u"comboBoxPtSkinState_2")
        palette81 = QPalette()
        palette81.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette81.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette81.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette81.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette81.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette81.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette81.setBrush(QPalette.Active, QPalette.Text, brush)
        palette81.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette81.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette81.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette81.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette81.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette81.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette81.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette81.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette81.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette81.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette81.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette81.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette81.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette81.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette81.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette81.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette81.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette81.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette81.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette81.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette81.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette81.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette81.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette81.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette81.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette81.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette81.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette81.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette81.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtSkinState_2.setPalette(palette81)
        self.comboBoxPtSkinState_2.setFont(font3)
        self.comboBoxPtSkinState_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtSkinState_2.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtSkinState_2, 2, 2, 1, 1)

        self.labelPtMucousMembr = QLabel(self.frame)
        self.labelPtMucousMembr.setObjectName(u"labelPtMucousMembr")
        self.labelPtMucousMembr.setMaximumSize(QSize(150, 16777215))
        palette82 = QPalette()
        palette82.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette82.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette82.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette82.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette82.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette82.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette82.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette82.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette82.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette82.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette82.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette82.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette82.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette82.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette82.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette82.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette82.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette82.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette82.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette82.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette82.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette82.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette82.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette82.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette82.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette82.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette82.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette82.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette82.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette82.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette82.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette82.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette82.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette82.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette82.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette82.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette82.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette82.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette82.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette82.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette82.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette82.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette82.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette82.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette82.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette82.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette82.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette82.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtMucousMembr.setPalette(palette82)
        self.labelPtMucousMembr.setFont(font3)
        self.labelPtMucousMembr.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtMucousMembr, 4, 0, 1, 1)

        self.comboBoxPtWheezing_2 = QComboBox(self.frame)
        self.comboBoxPtWheezing_2.addItem("")
        self.comboBoxPtWheezing_2.addItem("")
        self.comboBoxPtWheezing_2.addItem("")
        self.comboBoxPtWheezing_2.addItem("")
        self.comboBoxPtWheezing_2.setObjectName(u"comboBoxPtWheezing_2")
        palette83 = QPalette()
        palette83.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette83.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette83.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette83.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette83.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette83.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette83.setBrush(QPalette.Active, QPalette.Text, brush)
        palette83.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette83.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette83.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette83.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette83.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette83.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette83.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette83.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette83.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette83.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette83.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette83.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette83.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette83.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette83.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette83.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette83.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette83.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette83.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette83.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette83.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette83.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette83.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette83.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette83.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette83.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette83.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette83.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette83.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtWheezing_2.setPalette(palette83)
        self.comboBoxPtWheezing_2.setFont(font3)
        self.comboBoxPtWheezing_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtWheezing_2.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtWheezing_2, 8, 1, 1, 1)

        self.labelPtStomach = QLabel(self.frame)
        self.labelPtStomach.setObjectName(u"labelPtStomach")
        self.labelPtStomach.setMaximumSize(QSize(150, 16777215))
        palette84 = QPalette()
        palette84.setBrush(QPalette.Active, QPalette.WindowText, brush8)
        palette84.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette84.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette84.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette84.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette84.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette84.setBrush(QPalette.Active, QPalette.Text, brush8)
        palette84.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette84.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        palette84.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette84.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette84.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette84.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette84.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette84.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette84.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette84.setBrush(QPalette.Inactive, QPalette.WindowText, brush8)
        palette84.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette84.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette84.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette84.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette84.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette84.setBrush(QPalette.Inactive, QPalette.Text, brush8)
        palette84.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette84.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette84.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette84.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette84.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette84.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette84.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette84.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette84.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette84.setBrush(QPalette.Disabled, QPalette.WindowText, brush8)
        palette84.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette84.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette84.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette84.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette84.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette84.setBrush(QPalette.Disabled, QPalette.Text, brush8)
        palette84.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette84.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        palette84.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette84.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette84.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette84.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette84.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette84.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette84.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.labelPtStomach.setPalette(palette84)
        self.labelPtStomach.setFont(font3)
        self.labelPtStomach.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"border: none;")

        self.gridLayout_2.addWidget(self.labelPtStomach, 14, 0, 1, 1)

        self.comboBoxPtStomach_2 = QComboBox(self.frame)
        self.comboBoxPtStomach_2.addItem("")
        self.comboBoxPtStomach_2.addItem("")
        self.comboBoxPtStomach_2.addItem("")
        self.comboBoxPtStomach_2.setObjectName(u"comboBoxPtStomach_2")
        palette85 = QPalette()
        palette85.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette85.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette85.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette85.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette85.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette85.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette85.setBrush(QPalette.Active, QPalette.Text, brush)
        palette85.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette85.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette85.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette85.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette85.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette85.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette85.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette85.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette85.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette85.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette85.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette85.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette85.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette85.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette85.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette85.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette85.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette85.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette85.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette85.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette85.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette85.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette85.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette85.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette85.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette85.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette85.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette85.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette85.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtStomach_2.setPalette(palette85)
        self.comboBoxPtStomach_2.setFont(font3)
        self.comboBoxPtStomach_2.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtStomach_2.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtStomach_2, 14, 2, 1, 1)

        self.comboBoxPtHearthNoise = QComboBox(self.frame)
        self.comboBoxPtHearthNoise.addItem("")
        self.comboBoxPtHearthNoise.addItem("")
        self.comboBoxPtHearthNoise.addItem("")
        self.comboBoxPtHearthNoise.setObjectName(u"comboBoxPtHearthNoise")
        palette86 = QPalette()
        palette86.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette86.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette86.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette86.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette86.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette86.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette86.setBrush(QPalette.Active, QPalette.Text, brush)
        palette86.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette86.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette86.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette86.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette86.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette86.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette86.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette86.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette86.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette86.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette86.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette86.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette86.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette86.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette86.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette86.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette86.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette86.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette86.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette86.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette86.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette86.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette86.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette86.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette86.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette86.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette86.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette86.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette86.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtHearthNoise.setPalette(palette86)
        self.comboBoxPtHearthNoise.setFont(font3)
        self.comboBoxPtHearthNoise.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtHearthNoise.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtHearthNoise, 13, 2, 1, 1)

        self.comboBoxPtLymphnode = QComboBox(self.frame)
        self.comboBoxPtLymphnode.addItem("")
        self.comboBoxPtLymphnode.addItem("")
        self.comboBoxPtLymphnode.setObjectName(u"comboBoxPtLymphnode")
        palette87 = QPalette()
        palette87.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette87.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette87.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette87.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette87.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette87.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette87.setBrush(QPalette.Active, QPalette.Text, brush)
        palette87.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette87.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette87.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette87.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette87.setBrush(QPalette.Active, QPalette.PlaceholderText, brush6)
#endif
        palette87.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette87.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette87.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette87.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette87.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette87.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette87.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette87.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette87.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette87.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette87.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette87.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush6)
#endif
        palette87.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette87.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette87.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette87.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette87.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette87.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette87.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette87.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette87.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette87.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette87.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette87.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.comboBoxPtLymphnode.setPalette(palette87)
        self.comboBoxPtLymphnode.setFont(font3)
        self.comboBoxPtLymphnode.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")
        self.comboBoxPtLymphnode.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBoxPtLymphnode, 3, 1, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 21, 1, 1, 1)

        self.plainTextEditPtStObjOther = QPlainTextEdit(self.frame)
        self.plainTextEditPtStObjOther.setObjectName(u"plainTextEditPtStObjOther")
        self.plainTextEditPtStObjOther.setMinimumSize(QSize(0, 60))
        self.plainTextEditPtStObjOther.setMaximumSize(QSize(16777215, 60))
        self.plainTextEditPtStObjOther.setFont(font3)
        self.plainTextEditPtStObjOther.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.plainTextEditPtStObjOther, 20, 1, 1, 2)


        self.verticalLayout.addWidget(self.frame)

        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/stethoscope_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.obj_status, icon2, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.groupBox_wom = QGroupBox(self.centralwidget)
        self.groupBox_wom.setObjectName(u"groupBox_wom")
        self.groupBox_wom.setStyleSheet(u"font-size: 9pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);\n"
"")
        self.groupBox_wom.setAlignment(Qt.AlignCenter)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_wom)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 20, 5, 5)
        self.pushButtonHelp = QPushButton(self.groupBox_wom)
        self.pushButtonHelp.setObjectName(u"pushButtonHelp")
        self.pushButtonHelp.setEnabled(False)
        palette88 = QPalette()
        palette88.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette88.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette88.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette88.setBrush(QPalette.Active, QPalette.Midlight, brush14)
        palette88.setBrush(QPalette.Active, QPalette.Dark, brush15)
        palette88.setBrush(QPalette.Active, QPalette.Mid, brush16)
        palette88.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette88.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette88.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette88.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette88.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette88.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette88.setBrush(QPalette.Active, QPalette.AlternateBase, brush14)
        palette88.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette88.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette88.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette88.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette88.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette88.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette88.setBrush(QPalette.Inactive, QPalette.Midlight, brush14)
        palette88.setBrush(QPalette.Inactive, QPalette.Dark, brush15)
        palette88.setBrush(QPalette.Inactive, QPalette.Mid, brush16)
        palette88.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette88.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette88.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette88.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette88.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette88.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette88.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush14)
        palette88.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette88.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette88.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette88.setBrush(QPalette.Disabled, QPalette.WindowText, brush18)
        palette88.setBrush(QPalette.Disabled, QPalette.Button, brush19)
        palette88.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette88.setBrush(QPalette.Disabled, QPalette.Midlight, brush14)
        palette88.setBrush(QPalette.Disabled, QPalette.Dark, brush15)
        palette88.setBrush(QPalette.Disabled, QPalette.Mid, brush16)
        palette88.setBrush(QPalette.Disabled, QPalette.Text, brush18)
        palette88.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette88.setBrush(QPalette.Disabled, QPalette.ButtonText, brush18)
        palette88.setBrush(QPalette.Disabled, QPalette.Base, brush19)
        palette88.setBrush(QPalette.Disabled, QPalette.Window, brush19)
        palette88.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette88.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush20)
        palette88.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette88.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette88.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush21)
#endif
        self.pushButtonHelp.setPalette(palette88)
        self.pushButtonHelp.setFont(font)
        self.pushButtonHelp.setStyleSheet(u"QPushButton {\n"
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
        icon3.addFile(u":/icon/icons/info_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonHelp.setIcon(icon3)

        self.verticalLayout_6.addWidget(self.pushButtonHelp)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.pushButtonNotSaveExit = QPushButton(self.groupBox_wom)
        self.pushButtonNotSaveExit.setObjectName(u"pushButtonNotSaveExit")
        palette89 = QPalette()
        palette89.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette89.setBrush(QPalette.Active, QPalette.Button, brush13)
        palette89.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette89.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette89.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette89.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette89.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette89.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette89.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette89.setBrush(QPalette.Active, QPalette.Base, brush13)
        palette89.setBrush(QPalette.Active, QPalette.Window, brush13)
        palette89.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette89.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette89.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette89.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette89.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette89.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette89.setBrush(QPalette.Inactive, QPalette.Button, brush13)
        palette89.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette89.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette89.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette89.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette89.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette89.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette89.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette89.setBrush(QPalette.Inactive, QPalette.Base, brush13)
        palette89.setBrush(QPalette.Inactive, QPalette.Window, brush13)
        palette89.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette89.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette89.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette89.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette89.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette89.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette89.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette89.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette89.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette89.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette89.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette89.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette89.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette89.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette89.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette89.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette89.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette89.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette89.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette89.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette89.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        self.pushButtonNotSaveExit.setPalette(palette89)
        self.pushButtonNotSaveExit.setFont(font)
        self.pushButtonNotSaveExit.setStyleSheet(u"QPushButton {\n"
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
"background-color: #EEEEEE;\n"
"border: 1px solid rgba(50, 98, 115, 255);\n"
"}\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/block_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonNotSaveExit.setIcon(icon4)
        self.pushButtonNotSaveExit.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.pushButtonNotSaveExit)

        self.pushButtonSaveExit = QPushButton(self.groupBox_wom)
        self.pushButtonSaveExit.setObjectName(u"pushButtonSaveExit")
        palette90 = QPalette()
        palette90.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush23 = QBrush(QColor(92, 158, 173, 255))
        brush23.setStyle(Qt.SolidPattern)
        palette90.setBrush(QPalette.Active, QPalette.Button, brush23)
        palette90.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette90.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette90.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette90.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette90.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette90.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette90.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette90.setBrush(QPalette.Active, QPalette.Base, brush23)
        palette90.setBrush(QPalette.Active, QPalette.Window, brush23)
        palette90.setBrush(QPalette.Active, QPalette.Shadow, brush10)
        palette90.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        palette90.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette90.setBrush(QPalette.Active, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette90.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette90.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette90.setBrush(QPalette.Inactive, QPalette.Button, brush23)
        palette90.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette90.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette90.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette90.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette90.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette90.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette90.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette90.setBrush(QPalette.Inactive, QPalette.Base, brush23)
        palette90.setBrush(QPalette.Inactive, QPalette.Window, brush23)
        palette90.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette90.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette90.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette90.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette90.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette90.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette90.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette90.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette90.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette90.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette90.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette90.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette90.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette90.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette90.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette90.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette90.setBrush(QPalette.Disabled, QPalette.Shadow, brush10)
        palette90.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush7)
        palette90.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette90.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette90.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        self.pushButtonSaveExit.setPalette(palette90)
        self.pushButtonSaveExit.setFont(font)
        self.pushButtonSaveExit.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(92, 158, 173, 255);\n"
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
"background-color: #EEEEEE;\n"
"border: 1px solid rgba(50, 98, 115, 255);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/save_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSaveExit.setIcon(icon5)
        self.pushButtonSaveExit.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.pushButtonSaveExit)


        self.horizontalLayout_4.addWidget(self.groupBox_wom)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        StPrObjectivus.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.plainTextEditPtComplaints, self.plainTextEditPtAnamMorbi)
        QWidget.setTabOrder(self.plainTextEditPtAnamMorbi, self.lineEditPtWeight)
        QWidget.setTabOrder(self.lineEditPtWeight, self.lineEditPtGrowth)
        QWidget.setTabOrder(self.lineEditPtGrowth, self.lineEditPtBloodPreasureSist)
        QWidget.setTabOrder(self.lineEditPtBloodPreasureSist, self.lineEditPtBloodPreasureDiast)
        QWidget.setTabOrder(self.lineEditPtBloodPreasureDiast, self.lineEditPtBreathingSpeed)
        QWidget.setTabOrder(self.lineEditPtBreathingSpeed, self.lineEditSaturation)
        QWidget.setTabOrder(self.lineEditSaturation, self.lineEditPtTemperature)
        QWidget.setTabOrder(self.lineEditPtTemperature, self.lineEditPtPulse)
        QWidget.setTabOrder(self.lineEditPtPulse, self.comboBoxPtDrugs)
        QWidget.setTabOrder(self.comboBoxPtDrugs, self.comboBoxPtAllergStatus)
        QWidget.setTabOrder(self.comboBoxPtAllergStatus, self.comboBoxPtAnamEpid)
        QWidget.setTabOrder(self.comboBoxPtAnamEpid, self.checkBox_GB)
        QWidget.setTabOrder(self.checkBox_GB, self.checkBox_Hypothyreosis)
        QWidget.setTabOrder(self.checkBox_Hypothyreosis, self.comboBoxPtHearthTone_3)
        QWidget.setTabOrder(self.comboBoxPtHearthTone_3, self.checkBox_Hyperthyreosis)
        QWidget.setTabOrder(self.checkBox_Hyperthyreosis, self.checkBox_SD)
        QWidget.setTabOrder(self.checkBox_SD, self.checkBox_NRS)
        QWidget.setTabOrder(self.checkBox_NRS, self.checkBox_Atherosclerosis_BCA)
        QWidget.setTabOrder(self.checkBox_Atherosclerosis_BCA, self.checkBox_IBS)
        QWidget.setTabOrder(self.checkBox_IBS, self.checkBox_Atherosclerosis_legs)
        QWidget.setTabOrder(self.checkBox_Atherosclerosis_legs, self.checkBox_Stroke)
        QWidget.setTabOrder(self.checkBox_Stroke, self.checkBox_Fat)
        QWidget.setTabOrder(self.checkBox_Fat, self.checkBox_HBsAg)
        QWidget.setTabOrder(self.checkBox_HBsAg, self.checkBox_Astma)
        QWidget.setTabOrder(self.checkBox_Astma, self.checkBox_HCV)
        QWidget.setTabOrder(self.checkBox_HCV, self.plainTextEditPtStObjOther)
        QWidget.setTabOrder(self.plainTextEditPtStObjOther, self.checkBox_B20)
        QWidget.setTabOrder(self.checkBox_B20, self.checkBox_Gastro)
        QWidget.setTabOrder(self.checkBox_Gastro, self.checkBox_other)
        QWidget.setTabOrder(self.checkBox_other, self.plainTextEdit_other_chronic_diseases)
        QWidget.setTabOrder(self.plainTextEdit_other_chronic_diseases, self.comboBoxPtGeneralState)
        QWidget.setTabOrder(self.comboBoxPtGeneralState, self.comboBoxPtSkinState_1)
        QWidget.setTabOrder(self.comboBoxPtSkinState_1, self.comboBoxPtMucousMembr_1)
        QWidget.setTabOrder(self.comboBoxPtMucousMembr_1, self.comboBoxPtSkinState_2)
        QWidget.setTabOrder(self.comboBoxPtSkinState_2, self.comboBoxPtBreathing_2)
        QWidget.setTabOrder(self.comboBoxPtBreathing_2, self.comboBoxPtBreathing_1)
        QWidget.setTabOrder(self.comboBoxPtBreathing_1, self.comboBoxPtLymphnode)
        QWidget.setTabOrder(self.comboBoxPtLymphnode, self.comboBoxPtWheezing_1)
        QWidget.setTabOrder(self.comboBoxPtWheezing_1, self.comboBoxPtBreathing_3)
        QWidget.setTabOrder(self.comboBoxPtBreathing_3, self.comboBoxPtWheezingChoice)
        QWidget.setTabOrder(self.comboBoxPtWheezingChoice, self.comboBoxPtWheezing_2)
        QWidget.setTabOrder(self.comboBoxPtWheezing_2, self.comboBoxPtWheezing_3)
        QWidget.setTabOrder(self.comboBoxPtWheezing_3, self.plainTextEditPtDrugs)
        QWidget.setTabOrder(self.plainTextEditPtDrugs, self.comboBoxPtStomach_3)
        QWidget.setTabOrder(self.comboBoxPtStomach_3, self.comboBoxPtDyspnea_3)
        QWidget.setTabOrder(self.comboBoxPtDyspnea_3, self.comboBoxPtUrination_3)
        QWidget.setTabOrder(self.comboBoxPtUrination_3, self.comboBoxPtHearthTone_1)
        QWidget.setTabOrder(self.comboBoxPtHearthTone_1, self.comboBoxPtStomach_1)
        QWidget.setTabOrder(self.comboBoxPtStomach_1, self.comboBoxPtUrination_2)
        QWidget.setTabOrder(self.comboBoxPtUrination_2, self.comboBoxPtHearthNoiseChoice)
        QWidget.setTabOrder(self.comboBoxPtHearthNoiseChoice, self.comboBoxPtStomach_2)
        QWidget.setTabOrder(self.comboBoxPtStomach_2, self.comboBoxPtUrination_1)
        QWidget.setTabOrder(self.comboBoxPtUrination_1, self.comboBoxPtHearthTone_2)
        QWidget.setTabOrder(self.comboBoxPtHearthTone_2, self.comboBoxPtDefecation_2)
        QWidget.setTabOrder(self.comboBoxPtDefecation_2, self.comboBoxPtHearthNoise)
        QWidget.setTabOrder(self.comboBoxPtHearthNoise, self.comboBoxPtDefecation_1)
        QWidget.setTabOrder(self.comboBoxPtDefecation_1, self.comboBoxPtDyspnea_2)
        QWidget.setTabOrder(self.comboBoxPtDyspnea_2, self.comboBoxPtDefecation_3)
        QWidget.setTabOrder(self.comboBoxPtDefecation_3, self.dateEditPtWorkListDate1_1)
        QWidget.setTabOrder(self.dateEditPtWorkListDate1_1, self.comboBoxWorkListInfo)
        QWidget.setTabOrder(self.comboBoxWorkListInfo, self.lineEditPtWorkPosition)
        QWidget.setTabOrder(self.lineEditPtWorkPosition, self.lineEditPtWorkPlace)
        QWidget.setTabOrder(self.lineEditPtWorkPlace, self.comboBoxPtSocialStatus)
        QWidget.setTabOrder(self.comboBoxPtSocialStatus, self.lineEditPtWorkListNumber1_1)
        QWidget.setTabOrder(self.lineEditPtWorkListNumber1_1, self.dateEditPtWorkListDateOpening)
        QWidget.setTabOrder(self.dateEditPtWorkListDateOpening, self.plainTextEditPtAnamAllerg)
        QWidget.setTabOrder(self.plainTextEditPtAnamAllerg, self.comboBoxPtDyspneaChoice)
        QWidget.setTabOrder(self.comboBoxPtDyspneaChoice, self.plainTextEditPtAnamEpid)
        QWidget.setTabOrder(self.plainTextEditPtAnamEpid, self.comboBoxPtDyspnea_1)

        self.retranslateUi(StPrObjectivus)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(StPrObjectivus)
    # setupUi

    def retranslateUi(self, StPrObjectivus):
        StPrObjectivus.setWindowTitle(QCoreApplication.translate("StPrObjectivus", u"WoM - \u0416\u0430\u043b\u043e\u0431\u044b, \u0430\u043d\u0430\u043c\u043d\u0435\u0437 \u0438 \u043e\u0431\u044a\u0435\u043a\u0442\u0438\u0432\u043d\u044b\u0439 \u0441\u0442\u0430\u0442\u0443\u0441", None))
        self.label_Pt_info.setText(QCoreApplication.translate("StPrObjectivus", u"PatientInfo\n"
"fff", None))
        self.labelTimeline.setText("")
        self.label_6.setText(QCoreApplication.translate("StPrObjectivus", u"\u0410\u043d\u0430\u043c\u043d\u0435\u0437 \u0437\u0430\u0431\u043e\u043b\u0435\u0432\u0430\u043d\u0438\u044f", None))
        self.plainTextEditPtAnamMorbi.setPlaceholderText(QCoreApplication.translate("StPrObjectivus", u"\u041d\u0430\u043f\u0438\u0448\u0438\u0442\u0435 \u0430\u043d\u0430\u043c\u043d\u0435\u0437", None))
        self.label_9.setText(QCoreApplication.translate("StPrObjectivus", u"\u0410\u043b\u043b\u0435\u0440\u0433\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0430\u043d\u0430\u043c\u043d\u0435\u0437", None))
        self.comboBoxPtAllergStatus.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u041e\u0442\u0440\u0438\u0446\u0430\u0435\u0442", None))
        self.comboBoxPtAllergStatus.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0415\u0421\u0422\u042c", None))

        self.plainTextEditPtAnamAllerg.setPlaceholderText(QCoreApplication.translate("StPrObjectivus", u"\u041f\u0440\u0438 \u043d\u0430\u043b\u0438\u0447\u0438\u0438 \u0430\u043b\u043b\u0435\u0440\u0433\u0438\u0438: \u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043b\u0435\u043a.\u043f\u0440\u0435\u043f\u0430\u0440\u0430\u0442 \u0438 \u0442\u0438\u043f \u0430\u043b\u043b\u0435\u0440\u0433\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u0440\u0435\u0430\u043a\u0446\u0438\u0438 \u043d\u0430 \u043d\u0435\u0433\u043e", None))
        self.label_5.setText(QCoreApplication.translate("StPrObjectivus", u"\u0416\u0430\u043b\u043e\u0431\u044b \u043d\u0430:", None))
        self.plainTextEditPtComplaints.setPlaceholderText(QCoreApplication.translate("StPrObjectivus", u"\u041d\u0430\u043f\u0438\u0448\u0438\u0442\u0435 \u0436\u0430\u043b\u043e\u0431\u044b \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.comboBoxPtDrugs.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u041d\u0435 \u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u0442", None))
        self.comboBoxPtDrugs.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0421\u0438\u0442\u0443\u0430\u0446\u0438\u043e\u043d\u043d\u043e", None))
        self.comboBoxPtDrugs.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u041f\u043e\u0441\u0442\u043e\u044f\u043d\u043d\u043e", None))

        self.plainTextEditPtDrugs.setPlaceholderText(QCoreApplication.translate("StPrObjectivus", u"\u043f\u0435\u0440\u0435\u0447\u0438\u0441\u043b\u0438\u0442\u0435 \u043f\u0440\u0435\u043f\u0430\u0440\u0430\u0442\u044b \u0441 \u0434\u043e\u0437\u043e\u0439, \u0440\u0435\u0436\u0438\u043c\u043e\u043c \u0438 \u043f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c\u044e \u043f\u0440\u0438\u0435\u043c\u0430", None))
        self.label_8.setText(QCoreApplication.translate("StPrObjectivus", u"\u041f\u0440\u0438\u043d\u0438\u043c\u0430\u0435\u043c\u044b\u0435 \u043c\u0435\u0434\u0438\u043a\u0430\u043c\u0435\u043d\u0442\u044b", None))
        self.labelPtTemperatureCelcium.setText(QCoreApplication.translate("StPrObjectivus", u"<html><head/><body><p>t \u0442\u0435\u043b\u0430, <span style=\" vertical-align:super;\">o</span>\u0421</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("StPrObjectivus", u"\u0410\u043d\u0442\u0440\u043e\u043f\u043e\u043c\u0435\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.labelooo.setText(QCoreApplication.translate("StPrObjectivus", u"/", None))
        self.labelPtBloodPreasure.setText(QCoreApplication.translate("StPrObjectivus", u"\u0410\u0414, \u043c\u043c.\u0440\u0442.\u0441\u0442.", None))
        self.labelPtSaturation.setText(QCoreApplication.translate("StPrObjectivus", u"\u0421\u0430\u0442\u0443\u0440\u0430\u0446\u0438\u044f, %", None))
        self.labelPtWeight.setText(QCoreApplication.translate("StPrObjectivus", u"\u0412\u0435\u0441, \u043a\u0433", None))
        self.labelPtGrowth.setText(QCoreApplication.translate("StPrObjectivus", u"\u0420\u043e\u0441\u0442, \u0441\u043c", None))
        self.labelPtPulse.setText(QCoreApplication.translate("StPrObjectivus", u"\u0427\u0421\u0421, \u0432 1 \u043c\u0438\u043d", None))
        self.labelPtBreathingSpeed.setText(QCoreApplication.translate("StPrObjectivus", u"\u0427\u0414\u0414, \u0432 1 \u043c\u0438\u043d", None))
        self.label_imt.setText("")
        self.label_2.setText("")
        self.pushButton_add_to_diag.setText(QCoreApplication.translate("StPrObjectivus", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432 \u0434\u0438\u0430\u0433\u043d\u043e\u0437", None))
        self.comboBoxPtAnamEpid.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u0421\u043f\u043e\u043a\u043e\u0439\u043d\u044b\u0439", None))
        self.comboBoxPtAnamEpid.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u043e\u0442\u044f\u0433\u043e\u0449\u0435\u043d", None))

        self.label_10.setText(QCoreApplication.translate("StPrObjectivus", u"\u042d\u043f\u0438\u0434\u0435\u043c\u0438\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0430\u043d\u0430\u043c\u043d\u0435\u0437", None))
        self.plainTextEditPtAnamEpid.setPlaceholderText(QCoreApplication.translate("StPrObjectivus", u"\u041f\u0440\u0438 \u043e\u0442\u044f\u0433\u043e\u0449\u0435\u043d\u043d\u043e\u043c \u044d\u043f\u0438\u0434.\u0430\u043d\u0430\u043c\u043d\u0435\u0437\u0435 - \u0440\u0430\u0441\u043f\u0438\u0448\u0438\u0442\u0435 \u043f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435, \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u044b \u0438 \u0442.\u0434.", None))
        self.checkBox_Fat.setText(QCoreApplication.translate("StPrObjectivus", u"\u041e\u0436\u0438\u0440\u0435\u043d\u0438\u0435", None))
        self.checkBox_Atherosclerosis_legs.setText(QCoreApplication.translate("StPrObjectivus", u"\u0410\u0442\u0435\u0440\u043e\u0441\u043a\u043b\u0435\u0440\u043e\u0437 \u0430\u0430 \u043d/\u043a", None))
        self.checkBox_Stroke.setText(QCoreApplication.translate("StPrObjectivus", u"\u041f\u041e\u041d\u041c\u041a", None))
        self.label_11.setText(QCoreApplication.translate("StPrObjectivus", u"\u0425\u0440\u043e\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0437\u0430\u0431\u043e\u043b\u0435\u0432\u0430\u043d\u0438\u044f", None))
        self.checkBox_other.setText(QCoreApplication.translate("StPrObjectivus", u"\u0414\u0440\u0443\u0433\u043e\u0435", None))
        self.checkBox_Hyperthyreosis.setText(QCoreApplication.translate("StPrObjectivus", u"\u0413\u0438\u043f\u0435\u0440\u0442\u0438\u0440\u0435\u043e\u0437", None))
        self.checkBox_Hypothyreosis.setText(QCoreApplication.translate("StPrObjectivus", u"\u0413\u0438\u043f\u043e\u0442\u0438\u0440\u0435\u043e\u0437", None))
        self.checkBox_IBS.setText(QCoreApplication.translate("StPrObjectivus", u"\u0418\u0411\u0421 / \u0421\u041d / \u041f\u0418\u041a\u0421 / \u0410\u041a\u0428 / \u0427\u041a\u0412", None))
        self.checkBox_Gastro.setText(QCoreApplication.translate("StPrObjectivus", u"\u0413\u0430\u0441\u0442\u0440\u0438\u0442 / \u042f\u0411\u0416 / \u042f\u0411\u0414\u041f\u041a", None))
        self.checkBox_B20.setText(QCoreApplication.translate("StPrObjectivus", u"\u0412\u0418\u0427-\u0438\u043d\u0444\u0435\u043a\u0446\u0438\u044f", None))
        self.checkBox_HBsAg.setText(QCoreApplication.translate("StPrObjectivus", u"\u0412\u0438\u0440\u0443\u0441\u043d\u044b\u0439 \u0433\u0435\u043f\u0430\u0442\u0438\u0442 \u0412", None))
        self.checkBox_Atherosclerosis_BCA.setText(QCoreApplication.translate("StPrObjectivus", u"\u0410\u0442\u0435\u0440\u043e\u0441\u043a\u043b\u0435\u0440\u043e\u0437 \u0411\u0426\u0410", None))
        self.checkBox_Astma.setText(QCoreApplication.translate("StPrObjectivus", u"\u0411\u0440\u043e\u043d\u0445\u0438\u0430\u043b\u044c\u043d\u0430\u044f \u0430\u0441\u0442\u043c\u0430", None))
        self.checkBox_NRS.setText(QCoreApplication.translate("StPrObjectivus", u"\u041d\u0430\u0440\u0443\u0448\u0435\u043d\u0438\u044f \u0440\u0438\u0442\u043c\u0430 \u0441\u0435\u0440\u0434\u0446\u0430", None))
        self.checkBox_GB.setText(QCoreApplication.translate("StPrObjectivus", u"\u0413\u0438\u043f\u0435\u0440\u0442\u043e\u043d\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0431\u043e\u043b\u0435\u0437\u043d\u044c", None))
        self.plainTextEdit_other_chronic_diseases.setPlaceholderText(QCoreApplication.translate("StPrObjectivus", u"\u043a\u0440\u0430\u0442\u043a\u043e \u0440\u0430\u0441\u043f\u0438\u0448\u0438\u0442\u0435 \u0434\u0440\u0443\u0433\u0438\u0435 \u0445\u0440\u043e\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0437\u0430\u0431\u043e\u043b\u0435\u0432\u0430\u043d\u0438\u044f", None))
        self.checkBox_SD.setText(QCoreApplication.translate("StPrObjectivus", u"\u0421\u0430\u0445\u0430\u0440\u043d\u044b\u0439 \u0434\u0438\u0430\u0431\u0435\u0442", None))
        self.checkBox_HCV.setText(QCoreApplication.translate("StPrObjectivus", u"\u0412\u0438\u0440\u0443\u0441\u043d\u044b\u0439 \u0433\u0435\u043f\u0430\u0442\u0438\u0442 \u0421", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.jaloby_anamnesis_page), QCoreApplication.translate("StPrObjectivus", u"\u0416\u0430\u043b\u043e\u0431\u044b, \u0430\u043d\u0430\u043c\u043d\u0435\u0437", None))
        self.comboBoxWorkList_prognosis.setItemText(0, "")
        self.comboBoxWorkList_prognosis.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0411\u043b\u0430\u0433\u043e\u043f\u0440\u0438\u044f\u0442\u043d\u044b\u0439", None))
        self.comboBoxWorkList_prognosis.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u0431\u043b\u0430\u0433\u043e\u043f\u0440\u0438\u044f\u0442\u043d\u044b\u0439", None))
        self.comboBoxWorkList_prognosis.setItemText(3, QCoreApplication.translate("StPrObjectivus", u"\u0421\u043e\u043c\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439", None))
        self.comboBoxWorkList_prognosis.setItemText(4, QCoreApplication.translate("StPrObjectivus", u"\u041d\u0435\u0431\u043b\u0430\u0433\u043e\u043f\u0440\u0438\u044f\u0442\u043d\u044b\u0439", None))

        self.labelPtWorkListS.setText(QCoreApplication.translate("StPrObjectivus", u"<html><head/><body><p align=\"right\">c</p></body></html>", None))
        self.dateEditPtWorkListDateOpening.setDisplayFormat(QCoreApplication.translate("StPrObjectivus", u"dd.MM.yyyy", None))
        self.labelPtWorkListNumber_2.setText(QCoreApplication.translate("StPrObjectivus", u"\u041a\u0435\u043c \u0432\u044b\u0434\u0430\u043d:", None))
        self.labelPtSickListInfo.setText(QCoreApplication.translate("StPrObjectivus", u"\u041b\u041d:", None))
        self.labelPtWorkListDateOpening.setText(QCoreApplication.translate("StPrObjectivus", u"\u041d\u0430 \u043b\u0438\u0441\u0442\u0435 \u043d\u0435\u0442\u0440\u0443\u0434\u043e\u0441\u043f\u043e\u0441\u043e\u0431\u043d\u043e\u0441\u0442\u0438 \u0441:", None))
        self.checkBoxPtNeedSickList.setText(QCoreApplication.translate("StPrObjectivus", u"\u041d\u0443\u0436\u0434\u0430\u0435\u0442\u0441\u044f \u0432 \u041b\u041d", None))
        self.labelPtSocialStatus.setText(QCoreApplication.translate("StPrObjectivus", u"\u0421\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u0442\u0430\u0442\u0443\u0441:", None))
        self.dateEditPtWorkListDate1_2.setDisplayFormat(QCoreApplication.translate("StPrObjectivus", u"dd.MM.yyyy", None))
        self.labelPtWorkListNumber.setText(QCoreApplication.translate("StPrObjectivus", u"\u041d\u043e\u043c\u0435\u0440 \u041b\u041d:", None))
        self.labelPtWorkPosition.setText(QCoreApplication.translate("StPrObjectivus", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c:", None))
        self.labelPtWorkListNumber_3.setText(QCoreApplication.translate("StPrObjectivus", u"<html><head/><body><p align=\"center\">\u043f\u043e</p></body></html>", None))
        self.comboBoxWorkListInfo.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u043d\u0435 \u0442\u0440\u0435\u0431\u0443\u0435\u0442\u0441\u044f", None))
        self.comboBoxWorkListInfo.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u043d\u0430\u0445\u043e\u0434\u0438\u0442\u0441\u044f \u043d\u0430 \u041b\u041d", None))
        self.comboBoxWorkListInfo.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u043d\u0443\u0436\u0434\u0430\u0435\u0442\u0441\u044f \u0432 \u043f\u0435\u0440\u0432\u0438\u0447\u043d\u043e\u043c \u041b\u041d", None))

        self.dateEditPtWorkListDate1_1.setDisplayFormat(QCoreApplication.translate("StPrObjectivus", u"dd.MM.yyyy", None))
        self.labelPtWorkPlace.setText(QCoreApplication.translate("StPrObjectivus", u"\u041c\u0435\u0441\u0442\u043e \u0440\u0430\u0431\u043e\u0442\u044b:", None))
        self.labelPtSickListInfo_2.setText(QCoreApplication.translate("StPrObjectivus", u"\u0422\u0440\u0443\u0434\u043e\u0432\u043e\u0439 \u043f\u0440\u043e\u0433\u043d\u043e\u0437:", None))
        self.comboBoxPtSocialStatus.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u0411\u0435\u0437\u0440\u0430\u0431\u043e\u0442\u043d\u044b\u0439", None))
        self.comboBoxPtSocialStatus.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u041f\u0435\u043d\u0441\u0438\u043e\u043d\u0435\u0440", None))
        self.comboBoxPtSocialStatus.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u0420\u0430\u0431\u043e\u0442\u0430\u0435\u0442, \u0443\u0441\u0442\u0440\u043e\u0435\u043d \u043e\u0444\u0438\u0446\u0438\u0430\u043b\u044c\u043d\u043e", None))
        self.comboBoxPtSocialStatus.setItemText(3, QCoreApplication.translate("StPrObjectivus", u"\u041d\u0430\u0445\u043e\u0434\u0438\u0442\u0441\u044f \u043d\u0430 \u0443\u0447\u0435\u0442\u0435 \u0432 \u0426\u0417\u041d", None))
        self.comboBoxPtSocialStatus.setItemText(4, QCoreApplication.translate("StPrObjectivus", u"\u0418\u041f", None))
        self.comboBoxPtSocialStatus.setItemText(5, QCoreApplication.translate("StPrObjectivus", u"\u0418\u043d\u0432\u0430\u043b\u0438\u0434 I \u0433\u0440\u0443\u043f\u043f\u044b", None))
        self.comboBoxPtSocialStatus.setItemText(6, QCoreApplication.translate("StPrObjectivus", u"\u0418\u043d\u0432\u0430\u043b\u0438\u0434 II \u0433\u0440\u0443\u043f\u043f\u044b", None))
        self.comboBoxPtSocialStatus.setItemText(7, QCoreApplication.translate("StPrObjectivus", u"\u0418\u043d\u0432\u0430\u043b\u0438\u0434 III \u0433\u0440\u0443\u043f\u043f\u044b", None))
        self.comboBoxPtSocialStatus.setItemText(8, QCoreApplication.translate("StPrObjectivus", u"\u0423\u0447\u0430\u0449\u0438\u0439\u0441\u044f \u0448\u043a\u043e\u043b\u044b", None))
        self.comboBoxPtSocialStatus.setItemText(9, QCoreApplication.translate("StPrObjectivus", u"\u0421\u0442\u0443\u0434\u0435\u043d\u0442", None))
        self.comboBoxPtSocialStatus.setItemText(10, QCoreApplication.translate("StPrObjectivus", u"\u0421\u0442\u0443\u0434\u0435\u043d\u0442 \u0412\u0423\u0417", None))

        self.label_13.setText(QCoreApplication.translate("StPrObjectivus", u"\u0421\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0439 \u0430\u043d\u0430\u043c\u043d\u0435\u0437 \u0438 \u044d\u043a\u0441\u043f\u0435\u0440\u0442\u0438\u0437\u0430 \u043d\u0435\u0442\u0440\u0443\u0434\u043e\u0441\u043f\u043e\u0441\u043e\u0431\u043d\u043e\u0441\u0442\u0438", None))
        self.checkBoxPtNeedSickList_2.setText(QCoreApplication.translate("StPrObjectivus", u"\u041f\u0435\u0440\u0432\u0438\u0447\u043d\u044b\u0439", None))
        self.labelPtWorkListDateOpening_2.setText(QCoreApplication.translate("StPrObjectivus", u"(\u043f\u0435\u0440\u0432\u0438\u0447\u043d\u044b\u0439 \u041b\u041d)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.work_page), QCoreApplication.translate("StPrObjectivus", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043f\u043e \u043d\u0435\u0441\u0442\u0440\u0443\u0434\u043e\u0441\u043f\u043e\u0441\u043e\u0431\u043d\u043e\u0441\u0442\u0438", None))
        self.comboBoxGeneralStTemplate.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u041d\u043e\u0440\u043c\u0430", None))

        self.pushButtonAddNewTemplateGeneralSt.setText(QCoreApplication.translate("StPrObjectivus", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u0448\u0430\u0431\u043b\u043e\u043d", None))
        self.label.setText(QCoreApplication.translate("StPrObjectivus", u"\u0428\u0430\u0431\u043b\u043e\u043d\u044b \u0441\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u0441\u0442\u0430\u0442\u0443\u0441\u0430", None))
        self.pushButton_push_temp.setText(QCoreApplication.translate("StPrObjectivus", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.lineEdit_new_template_name.setText("")
        self.lineEdit_new_template_name.setPlaceholderText(QCoreApplication.translate("StPrObjectivus", u"\u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043d\u043e\u0432\u043e\u0433\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430", None))
        self.label_3.setText(QCoreApplication.translate("StPrObjectivus", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0448\u0430\u0431\u043b\u043e\u043d \u0434\u043b\u044f \u0432\u0441\u0442\u0430\u0432\u043a\u0438", None))
        self.label_4.setText(QCoreApplication.translate("StPrObjectivus", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430", None))
        self.labelPtHearthNoise.setText(QCoreApplication.translate("StPrObjectivus", u"\u0428\u0443\u043c\u044b \u0441\u0435\u0440\u0434\u0446\u0430:", None))
        self.comboBoxPtSkinState_1.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u0444\u0438\u0437\u0438\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u0438\u0435", None))
        self.comboBoxPtSkinState_1.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0433\u0438\u043f\u0435\u0440\u0435\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u044b", None))
        self.comboBoxPtSkinState_1.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u0431\u043b\u0435\u0434\u043d\u043e\u0432\u0430\u0442\u044b\u0435", None))
        self.comboBoxPtSkinState_1.setItemText(3, QCoreApplication.translate("StPrObjectivus", u"\u0431\u043b\u0435\u0434\u043d\u044b\u0435", None))
        self.comboBoxPtSkinState_1.setItemText(4, QCoreApplication.translate("StPrObjectivus", u"\u043c\u0440\u0430\u043c\u043e\u0440\u043d\u044b\u0435", None))
        self.comboBoxPtSkinState_1.setItemText(5, QCoreApplication.translate("StPrObjectivus", u"\u0438\u043a\u0442\u0435\u0440\u0438\u0447\u043d\u044b\u0435", None))

        self.labelPtGeneralState.setText(QCoreApplication.translate("StPrObjectivus", u"\u041e\u0431\u0449\u0435\u0435 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435:", None))
        self.labelPtDyspnea.setText(QCoreApplication.translate("StPrObjectivus", u"\u041e\u0434\u044b\u0448\u043a\u0430:", None))
        self.labelPtWheezing.setText(QCoreApplication.translate("StPrObjectivus", u"\u0425\u0440\u0438\u043f\u044b:", None))
        self.comboBoxPtStomach_1.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u043d\u0435\u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d", None))
        self.comboBoxPtStomach_1.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u043d\u044b\u0439, \u0431\u043e\u043b\u044c\u0448\u0435 \u0432 \u044d\u043f\u0438\u0433\u0430\u0441\u0442\u0440\u0438\u0438", None))
        self.comboBoxPtStomach_1.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u043d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u043d\u044b\u0439, \u0431\u043e\u043b\u044c\u0448\u0435 \u0432 \u043f\u043e\u0434\u0432\u0437\u0434\u043e\u0448\u043d\u043e\u0439 \u043e\u0431\u043b\u0430\u0441\u0442\u0438", None))
        self.comboBoxPtStomach_1.setItemText(3, QCoreApplication.translate("StPrObjectivus", u"\u0434\u043e\u0441\u043a\u043e\u043e\u0431\u0440\u0430\u0437\u043d\u044b\u0439", None))

        self.comboBoxPtBreathing_3.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u043f\u0440\u043e\u0432\u043e\u0434\u0438\u0442\u0441\u044f \u0432\u043e \u0432\u0441\u0435 \u043e\u0442\u0434\u0435\u043b\u044b", None))
        self.comboBoxPtBreathing_3.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u043e\u0441\u043b\u0430\u0431\u043b\u0435\u043d\u043e \u0432 \u043d\u0438\u0436\u043d\u0438\u0445 \u043e\u0442\u0434\u0435\u043b\u0430\u0445", None))
        self.comboBoxPtBreathing_3.setItemText(2, "")

        self.comboBoxPtUrination_3.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"-----", None))
        self.comboBoxPtUrination_3.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"5-6 \u0440\u0430\u0437 \u0432 \u0441\u0443\u0442\u043a\u0438", None))
        self.comboBoxPtUrination_3.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"8-10 \u0440\u0430\u0437 \u0432 \u0441\u0443\u0442\u043a\u0438", None))
        self.comboBoxPtUrination_3.setItemText(3, QCoreApplication.translate("StPrObjectivus", u"\u043d\u0438\u043a\u0442\u0443\u0440\u0438\u044f", None))

        self.comboBoxPtBreathing_1.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u0441\u0432\u043e\u0431\u043e\u0434\u043d\u043e\u0435, \u0447\u0435\u0440\u0435\u0437 \u043d\u043e\u0441", None))
        self.comboBoxPtBreathing_1.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0447\u0435\u0440\u0435\u0437 \u0440\u043e\u0442", None))
        self.comboBoxPtBreathing_1.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u0447\u0435\u0440\u0435\u0437 \u0422\u0421\u0422", None))

        self.comboBoxPtGeneralState.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u0443\u0434\u043e\u0432\u043b\u0435\u0442\u0432\u043e\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435", None))
        self.comboBoxPtGeneralState.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0431\u043b\u0438\u0436\u0435 \u043a \u0443\u0434\u043e\u0432\u043b\u0435\u0442\u0432\u043e\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u043c\u0443", None))
        self.comboBoxPtGeneralState.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u0441\u0440\u0435\u0434\u043d\u0435\u0439 \u0441\u0442\u0435\u043f\u0435\u043d\u0438 \u0442\u044f\u0436\u0435\u0441\u0442\u0438", None))
        self.comboBoxPtGeneralState.setItemText(3, QCoreApplication.translate("StPrObjectivus", u"\u0442\u044f\u0436\u0435\u043b\u043e\u0435", None))
        self.comboBoxPtGeneralState.setItemText(4, QCoreApplication.translate("StPrObjectivus", u"\u043a\u0440\u0430\u0439\u043d\u0435\u0439 \u0441\u0442\u0435\u043f\u0435\u043d\u0438 \u0442\u044f\u0436\u0435\u0441\u0442\u0438", None))
        self.comboBoxPtGeneralState.setItemText(5, QCoreApplication.translate("StPrObjectivus", u"\u0442\u0435\u0440\u043c\u0438\u043d\u0430\u043b\u044c\u043d\u043e\u0435", None))

        self.comboBoxPtHearthTone_3.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"-----", None))
        self.comboBoxPtHearthTone_3.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0430\u043a\u0446\u0435\u043d\u0442 \u0432\u0442\u043e\u0440\u043e\u0433\u043e \u0442\u043e\u043d\u0430 \u043d\u0430\u0434 \u0430\u043e\u0440\u0442\u043e\u0439", None))
        self.comboBoxPtHearthTone_3.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u0430\u043a\u0446\u0435\u043d\u0442 \u0432\u0442\u043e\u0440\u043e\u0433\u043e \u0442\u043e\u043d\u0430 \u043d\u0430\u0434 \u043b\u0435\u0433\u043e\u0447\u043d\u043e\u0439 \u0430\u0440\u0442\u0435\u0440\u0438\u0435\u0439", None))
        self.comboBoxPtHearthTone_3.setItemText(3, QCoreApplication.translate("StPrObjectivus", u"\u0440\u0438\u0442\u043c \u0433\u0430\u043b\u043e\u043f\u0430", None))

        self.comboBoxPtDyspnea_2.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"-----", None))
        self.comboBoxPtDyspnea_2.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u043b\u0435\u0433\u043a\u0430\u044f", None))
        self.comboBoxPtDyspnea_2.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u0443\u043c\u0435\u0440\u0435\u043d\u043d\u0430\u044f", None))
        self.comboBoxPtDyspnea_2.setItemText(3, QCoreApplication.translate("StPrObjectivus", u"\u0432\u044b\u0440\u0430\u0436\u0435\u043d\u043d\u0430\u044f", None))

        self.labelPtHearthTones.setText(QCoreApplication.translate("StPrObjectivus", u"\u0422\u043e\u043d\u044b \u0441\u0435\u0440\u0434\u0446\u0430:", None))
        self.comboBoxPtDefecation_2.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u0440\u0435\u0433\u0443\u043b\u044f\u0440\u043d\u044b\u0439", None))
        self.comboBoxPtDefecation_2.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0441\u043a\u043b\u043e\u043d\u043d\u043e\u0441\u0442\u044c \u043a \u0437\u0430\u043f\u043e\u0440\u0430\u043c", None))
        self.comboBoxPtDefecation_2.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u0437\u0430\u043f\u043e\u0440\u044b", None))
        self.comboBoxPtDefecation_2.setItemText(3, QCoreApplication.translate("StPrObjectivus", u"\u0443\u0447\u0430\u0449\u0435\u043d\u043d\u044b\u0439", None))

        self.labelPtLymphnode.setText(QCoreApplication.translate("StPrObjectivus", u"\u041b\u0438\u043c\u0444\u043e\u0443\u0437\u043b\u044b:", None))
        self.labelPtDefecation.setText(QCoreApplication.translate("StPrObjectivus", u"\u0421\u0442\u0443\u043b:", None))
        self.comboBoxPtBreathing_2.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u0432\u0435\u0437\u0438\u043a\u0443\u043b\u044f\u0440\u043d\u043e\u0435", None))
        self.comboBoxPtBreathing_2.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0436\u0435\u0441\u0442\u043a\u043e\u0435", None))
        self.comboBoxPtBreathing_2.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u0431\u0440\u043e\u043d\u0445\u0438\u0430\u043b\u044c\u043d\u043e\u0435", None))

        self.comboBoxPtDyspnea_1.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"-----", None))
        self.comboBoxPtDyspnea_1.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0438\u043d\u0441\u043f\u0438\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f", None))
        self.comboBoxPtDyspnea_1.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u044d\u043a\u0441\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f", None))
        self.comboBoxPtDyspnea_1.setItemText(3, QCoreApplication.translate("StPrObjectivus", u"\u0441\u043c\u0435\u0448\u0430\u043d\u043d\u0430\u044f", None))

        self.labelPtBreathing.setText(QCoreApplication.translate("StPrObjectivus", u"\u0414\u044b\u0445\u0430\u043d\u0438\u0435:", None))
        self.label_12.setText(QCoreApplication.translate("StPrObjectivus", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u0441\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u0441\u0442\u0430\u0442\u0443\u0441\u0430", None))
        self.comboBoxPtUrination_2.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u0434\u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u043e\u0435", None))
        self.comboBoxPtUrination_2.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0434\u0438\u0443\u0440\u0435\u0437 \u0441\u043d\u0438\u0436\u0435\u043d", None))
        self.comboBoxPtUrination_2.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u043f\u043e\u043b\u0438\u0443\u0440\u0438\u044f", None))

        self.comboBoxPtDyspneaChoice.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u043d\u0435\u0442", None))
        self.comboBoxPtDyspneaChoice.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0415\u0421\u0422\u042c", None))

        self.comboBoxPtDefecation_1.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u043e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u043d\u044b\u0439", None))
        self.comboBoxPtDefecation_1.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u043a\u0430\u0448\u0438\u0446\u0435\u043e\u0431\u0440\u0430\u0437\u043d\u044b\u0439", None))
        self.comboBoxPtDefecation_1.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u0436\u0438\u0434\u043a\u0438\u0439", None))

        self.comboBoxPtDyspnea_3.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"-----", None))
        self.comboBoxPtDyspnea_3.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0443\u0441\u0438\u043b\u0438\u0432\u0430\u0435\u0442\u0441\u044f \u043f\u0440\u0438 \u0434\u0432\u0438\u0436\u0435\u043d\u0438\u0438", None))

        self.comboBoxPtMucousMembr_1.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u0444\u0438\u0437\u0438\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u043e\u043a\u0440\u0430\u0441\u043a\u0438", None))
        self.comboBoxPtMucousMembr_1.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0433\u0438\u043f\u0435\u0440\u0435\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u044b", None))
        self.comboBoxPtMucousMembr_1.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u0431\u043b\u0435\u0434\u043d\u043e\u0432\u0430\u0442\u044b\u0435", None))
        self.comboBoxPtMucousMembr_1.setItemText(3, QCoreApplication.translate("StPrObjectivus", u"\u0431\u043b\u0435\u0434\u043d\u044b\u0435", None))
        self.comboBoxPtMucousMembr_1.setItemText(4, QCoreApplication.translate("StPrObjectivus", u"\u043c\u0440\u0430\u043c\u043e\u0440\u043d\u044b\u0435", None))
        self.comboBoxPtMucousMembr_1.setItemText(5, QCoreApplication.translate("StPrObjectivus", u"\u0438\u043a\u0442\u0435\u0440\u0438\u0447\u043d\u044b\u0435", None))

        self.labelPtUrination.setText(QCoreApplication.translate("StPrObjectivus", u"\u041c\u043e\u0447\u0435\u0438\u0441\u043f\u0443\u0441\u043a\u0430\u043d\u0438\u0435:", None))
        self.comboBoxPtUrination_1.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u043a\u043e\u043d\u0442\u0440\u043e\u043b\u0438\u0440\u0443\u0435\u0442", None))
        self.comboBoxPtUrination_1.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0438\u043c\u043f\u0435\u0440\u0430\u0442\u0438\u0432\u043d\u044b\u0435 \u043f\u043e\u0437\u044b\u0432\u044b", None))
        self.comboBoxPtUrination_1.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u043f\u0435\u0440\u0438\u043e\u0434\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043d\u0435\u0443\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435", None))
        self.comboBoxPtUrination_1.setItemText(3, QCoreApplication.translate("StPrObjectivus", u"\u043d\u0435\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u0435", None))
        self.comboBoxPtUrination_1.setItemText(4, QCoreApplication.translate("StPrObjectivus", u"\u043f\u0435\u0440\u0438\u043e\u0434\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043a\u0430\u0442\u0435\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.comboBoxPtUrination_1.setItemText(5, QCoreApplication.translate("StPrObjectivus", u"\u0447\u0435\u0440\u0435\u0437 \u0446\u0438\u0441\u0442\u043e\u0441\u0442\u043e\u043c\u0443", None))
        self.comboBoxPtUrination_1.setItemText(6, QCoreApplication.translate("StPrObjectivus", u"\u043f\u043e \u043a\u0430\u0442\u0435\u0442\u0435\u0440\u0443", None))

        self.comboBoxPtDefecation_3.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u0435\u0436\u0435\u0434\u043d\u0435\u0432\u043d\u044b\u0439", None))
        self.comboBoxPtDefecation_3.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"1 \u0440\u0430\u0437 \u0432 2 \u0434\u043d\u044f", None))
        self.comboBoxPtDefecation_3.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"1 \u0440\u0430\u0437 \u0432 3-4 \u0434\u043d\u044f", None))
        self.comboBoxPtDefecation_3.setItemText(3, QCoreApplication.translate("StPrObjectivus", u"\u0434\u043e 1 \u0440\u0430\u0437\u0430 \u0432 \u043d\u0435\u0434\u0435\u043b\u044e", None))
        self.comboBoxPtDefecation_3.setItemText(4, QCoreApplication.translate("StPrObjectivus", u"2-3 \u0440\u0430\u0437\u0430 \u0432 \u0434\u0435\u043d\u044c", None))
        self.comboBoxPtDefecation_3.setItemText(5, QCoreApplication.translate("StPrObjectivus", u"\u0434\u043e 6 \u0440\u0430\u0437 \u0432 \u0434\u0435\u043d\u044c", None))

        self.labelPtSkinState.setText(QCoreApplication.translate("StPrObjectivus", u"\u041a\u043e\u0436\u043d\u044b\u0435 \u043f\u043e\u043a\u0440\u043e\u0432\u044b:", None))
        self.comboBoxPtHearthTone_2.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u0440\u0438\u0442\u043c\u0438\u0447\u043d\u044b\u0435", None))
        self.comboBoxPtHearthTone_2.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0430\u0440\u0438\u0442\u043c\u0438\u0447\u043d\u044b\u0435", None))

        self.comboBoxPtHearthNoiseChoice.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u043d\u0435\u0442", None))
        self.comboBoxPtHearthNoiseChoice.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0415\u0421\u0422\u042c", None))

        self.comboBoxPtWheezing_1.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"-----", None))
        self.comboBoxPtWheezing_1.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0435\u0434\u0438\u043d\u0438\u0447\u043d\u044b\u0435", None))
        self.comboBoxPtWheezing_1.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0435", None))

        self.labelPtStObjOther.setText(QCoreApplication.translate("StPrObjectivus", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435:", None))
        self.comboBoxPtWheezing_3.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"-----", None))
        self.comboBoxPtWheezing_3.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0432 \u043d\u0438\u0436\u043d\u0438\u0445 \u043e\u0442\u0434\u0435\u043b\u0430\u0445", None))
        self.comboBoxPtWheezing_3.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u0432 \u043e\u0431\u043b\u0430\u0441\u0442\u0438 \u0432\u0435\u0440\u0445\u0443\u0448\u0435\u043a", None))
        self.comboBoxPtWheezing_3.setItemText(3, QCoreApplication.translate("StPrObjectivus", u"\u043d\u0430\u0434 \u0432\u0441\u0435\u0439 \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u044c\u044e \u043b\u0435\u0433\u043a\u0438\u0445", None))

        self.comboBoxPtHearthTone_1.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u044f\u0441\u043d\u044b\u0435", None))
        self.comboBoxPtHearthTone_1.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u043f\u0440\u0438\u0433\u043b\u0443\u0448\u0435\u043d\u044b", None))
        self.comboBoxPtHearthTone_1.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u0433\u043b\u0443\u0445\u0438\u0435", None))

        self.comboBoxPtWheezingChoice.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u043d\u0435\u0442", None))
        self.comboBoxPtWheezingChoice.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0415\u0421\u0422\u042c", None))

        self.comboBoxPtStomach_3.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u0443\u0447\u0430\u0441\u0442\u0432\u0443\u0435\u0442 \u0432 \u0430\u043a\u0442\u0435 \u0434\u044b\u0445\u0430\u043d\u0438\u044f", None))
        self.comboBoxPtStomach_3.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0432\u0437\u0434\u0443\u0442", None))

        self.comboBoxPtSkinState_2.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u0432\u044b\u0441\u044b\u043f\u0430\u043d\u0438\u0439 \u043d\u0435\u0442", None))
        self.comboBoxPtSkinState_2.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u043f\u0441\u043e\u0440\u0438\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0432\u044b\u0441\u044b\u043f\u0430\u043d\u0438\u044f \u043d\u0430 \u043b\u043e\u043a\u0442\u044f\u0445 ", None))

        self.labelPtMucousMembr.setText(QCoreApplication.translate("StPrObjectivus", u"\u0421\u043b\u0438\u0437\u0438\u0441\u0442\u044b\u0435:", None))
        self.comboBoxPtWheezing_2.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"-----", None))
        self.comboBoxPtWheezing_2.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0441\u0443\u0445\u0438\u0435", None))
        self.comboBoxPtWheezing_2.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u0432\u043b\u0430\u0436\u043d\u044b\u0435", None))
        self.comboBoxPtWheezing_2.setItemText(3, "")

        self.labelPtStomach.setText(QCoreApplication.translate("StPrObjectivus", u"\u0416\u0438\u0432\u043e\u0442:", None))
        self.comboBoxPtStomach_2.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u0431\u0435\u0437\u0431\u043e\u043b\u0435\u0437\u043d\u0435\u043d\u043d\u044b\u0439", None))
        self.comboBoxPtStomach_2.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0431\u043e\u043b\u0435\u0437\u043d\u0435\u043d\u043d\u044b\u0439 \u0432 \u044d\u043f\u0438\u0433\u0430\u0441\u0442\u0440\u0438\u0438", None))
        self.comboBoxPtStomach_2.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u0431\u043e\u043b\u0435\u0437\u043d\u0435\u043d\u043d\u044b\u0439 \u043f\u0440\u0438 \u0433\u043b\u0443\u0431\u043e\u043a\u043e\u0439 \u043f\u0430\u043b\u044c\u043f\u0430\u0446\u0438\u0438", None))

        self.comboBoxPtHearthNoise.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"-----", None))
        self.comboBoxPtHearthNoise.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0421\u0438\u0441\u0442\u043e\u043b\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0448\u0443\u043c \u043d\u0430\u0434 \u0430\u043e\u0440\u0442\u043e\u0439", None))
        self.comboBoxPtHearthNoise.setItemText(2, QCoreApplication.translate("StPrObjectivus", u"\u0414\u0438\u0430\u0441\u0442\u043e\u043b\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0448\u0443\u043c \u0432 \u043e\u0431\u043b\u0430\u0441\u0442\u0438 \u043c\u0438\u0442\u0440\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u043a\u043b\u0430\u043f\u0430\u043d\u0430", None))

        self.comboBoxPtLymphnode.setItemText(0, QCoreApplication.translate("StPrObjectivus", u"\u043d\u0435 \u0443\u0432\u0435\u043b\u0438\u0447\u0435\u043d\u044b", None))
        self.comboBoxPtLymphnode.setItemText(1, QCoreApplication.translate("StPrObjectivus", u"\u0443\u0432\u0435\u043b\u0438\u0447\u0435\u043d \u043f\u043e\u0434\u043c\u044b\u0448\u0435\u0447\u043d\u044b\u0439 \u043b\u0438\u043c\u0444\u043e\u0443\u0437\u0435\u043b \u0441\u043f\u0440\u0430\u0432\u0430", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.obj_status), QCoreApplication.translate("StPrObjectivus", u"\u0421\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0441\u0442\u0430\u0442\u0443\u0441", None))
        self.groupBox_wom.setTitle(QCoreApplication.translate("StPrObjectivus", u"World of Medicine", None))
        self.pushButtonHelp.setText(QCoreApplication.translate("StPrObjectivus", u"Help", None))
        self.pushButtonNotSaveExit.setText(QCoreApplication.translate("StPrObjectivus", u"\u041d\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.pushButtonSaveExit.setText(QCoreApplication.translate("StPrObjectivus", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c\n"
"\u0438 \u0432\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432\n"
"\u043a\u0430\u0440\u0442\u0443 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
    # retranslateUi

