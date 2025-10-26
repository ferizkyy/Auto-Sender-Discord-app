import requests
import time
import random
from PyQt5 import QtCore

class Worker(QtCore.QObject):
    log_signal = QtCore.pyqtSignal(str, int, int)
    flog_signal = QtCore.pyqtSignal(str, int, int)
    cooldown = QtCore.pyqtSignal(int)
    finished = QtCore.pyqtSignal()

    def __init__(self, auth, proxy, delays_list, content, link):
        super().__init__()
        self.auth = auth
        self.proxy = proxy
        self.delays_list = delays_list
        self.content = content
        self.link = link
        self.running = True

    def run(self):
        headers = {
            "authorization": self.auth,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        proxies = {"http": self.proxy, "https": self.proxy}
        payload = {"content": self.content}

        count = 0
        fcount = 0

        while self.running:
            randomizer = random.choice(self.delays_list)
            try:
                req = requests.post(
                    self.link,
                    json=payload,
                    headers=headers,
                    proxies=proxies,
                    timeout=10
                )
                if req.status_code == 200:
                    count += 1
                    self.log_signal.emit("Message sent", count, randomizer)
                else:
                    fcount += 1
                    self.flog_signal.emit(f"Failed — Code {req.status_code}", fcount, randomizer)
            except Exception as e:
                fcount += 1
                self.flog_signal.emit(f"Error: {e}", fcount, randomizer)
            self.cooldown.emit(randomizer)
            time.sleep(randomizer)
        self.finished.emit()

    def stop(self):
        self.finished.emit()
        self.running = False
            