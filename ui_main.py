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
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtNetwork import QNetworkCookie
from PySide6.QtWebEngineCore import QWebEngineProfile, QWebEngineCookieStore
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QSizePolicy,
                               QWidget)


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
        self.cookies_list = []
        self.cookie_store = self.profile.cookieStore()
        self.cookie_store.cookieAdded.connect(self.on_cookie_added)
        self.webEngineView = QWebEngineView(self.centralwidget)
        self.webEngineView.setObjectName(u"webEngineView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy)
        self.webEngineView.setUrl(QUrl(u"https://music.youtube.com/"))
        self.load_cookies("cookies.json")
        self.gridLayout.addWidget(self.webEngineView, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def on_cookie_added(self, cookie):
        print("Cookie added:", cookie)
        self.save_cookies("cookies.json", cookie)  # Сохраняем куки каждый раз, когда добавляется новый

    def save_cookies(self, filename, cookie):
        # Создаем список для сохранения куков
        self.cookies_list.append(cookie)
        # Сохраняем куки в файл
        with open(filename, 'w') as file:
            json.dump([{
                'name': cookie.name().toStdString(),
                'value': cookie.value().toStdString(),
                'domain': cookie.domain(),
                'path': cookie.path(),
                'isSecure': cookie.isSecure(),
                'isHttpOnly': cookie.isHttpOnly()
            } for cookie in self.cookies_list], file, indent=4)

    def load_cookies(self, filename):
        try:
            with open(filename, 'r') as file:
                cookies_list = json.load(file)
                for cookie_data in cookies_list:
                    cookie = QNetworkCookie(
                        bytes(cookie_data['name'], 'utf-8'),
                        bytes(cookie_data['value'], 'utf-8')
                    )
                    cookie.setDomain(cookie_data['domain'])
                    cookie.setPath(cookie_data['path'])
                    cookie.setSecure(cookie_data['isSecure'])
                    cookie.setHttpOnly(cookie_data['isHttpOnly'])
                    self.cookie_store.setCookie(cookie)
        except FileNotFoundError:
            print("Cookie file not found. Starting with an empty cookie store.")
        except json.decoder.JSONDecodeError:
            print("Cookie file is empty. Starting with an empty cookie store.")


    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"YouTube Music", None))
        MainWindow.setWindowIcon(QIcon("icon.png"))
    # retranslateUi
