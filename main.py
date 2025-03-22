import json
import sys

from PySide6.QtCore import QTimer, QEvent
from PySide6.QtNetwork import QNetworkCookie
from PySide6.QtWebEngineCore import QWebEngineProfile
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_main import Ui_MainWindow
import threading


class YouTubeMusic(QMainWindow):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(YouTubeMusic, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        super(YouTubeMusic, self).__init__()
        self.cookies_list = []
        self.filename = 'cookies.json'
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.profile = QWebEngineProfile().defaultProfile()
        self.cookie_store = self.profile.cookieStore()
        self.cookie_store.cookieAdded.connect(self.save_cookies)
        self.load_cookies()

    def closeEvent(self, event: QEvent) -> None:
        with open(self.filename, 'w') as file:
            json.dump([{
                'name': cookie.name().toStdString(),
                'value': cookie.value().toStdString(),
                'domain': cookie.domain(),
                'path': cookie.path(),
                'isSecure': cookie.isSecure(),
                'isHttpOnly': cookie.isHttpOnly()
            } for cookie in self.cookies_list], file, indent=4)
        print("Cookies saved.", len(self.cookies_list))
        event.accept()

    def save_cookies(self, cookie: QNetworkCookie) -> None:
        for ind, cookie_ in enumerate(self.cookies_list):
            if cookie_.name() == cookie.name():
                self.cookies_list[ind] = cookie
                break
        else:
            self.cookies_list.append(cookie)

    def load_cookies(self) -> None:
        try:
            with open(self.filename, 'r') as file:
                cookies = json.load(file)
                for cookie_data in cookies:
                    cookie = QNetworkCookie(
                        bytes(cookie_data['name'], 'utf-8'),
                        bytes(cookie_data['value'], 'utf-8')
                    )
                    cookie.setDomain(cookie_data['domain'])
                    cookie.setPath(cookie_data['path'])
                    cookie.setSecure(cookie_data['isSecure'])
                    cookie.setHttpOnly(cookie_data['isHttpOnly'])
                    self.cookies_list.append(cookie)
                    self.cookie_store.setCookie(cookie)
        except json.decoder.JSONDecodeError:
            print("Cookie file is empty. Starting with an empty cookie store.")
        except FileNotFoundError:
            print("Cookie file not found. Starting with an empty cookie store.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YouTubeMusic()
    window.show()

    sys.exit(app.exec())
