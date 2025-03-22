# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
import json
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QCloseEvent)
from PySide6.QtNetwork import QNetworkCookie
from PySide6.QtWebEngineCore import QWebEngineProfile, QWebEngineCookieStore
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QSizePolicy,
                               QWidget, QMessageBox)


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1349, 821)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.profile = QWebEngineProfile().defaultProfile()
        self.cookie_store = self.profile.cookieStore()
        self.webEngineView = QWebEngineView(self.profile)
        self.setCentralWidget(self.webEngineView)
        self.webEngineView.setObjectName(u"webEngineView")
        self.profile.HttpCacheType(QWebEngineProfile.HttpCacheType.DiskHttpCache)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy)
        self.webEngineView.setUrl(QUrl(u"https://music.youtube.com/"))
        self.gridLayout.addWidget(self.webEngineView, 0, 0, 0, 0)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"YouTube Music", None))
        MainWindow.setWindowIcon(QIcon("icon.png"))
    # retranslateUi
