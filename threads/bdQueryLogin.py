import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from threading import Thread


from utils import broadcast
from services import connection_db


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    broadcast = broadcast.Broadcast()

    def run(self):
        self.application = connection_db.Oracle_db()

        self.app = Thread(target=self.application.login)
        self.app.start()

        while (self.app.is_alive()):

            time.sleep(1)
            self.progress.emit(1)

        self.progress.emit(1)
        self.finished.emit()


class Login(QMainWindow):

    broadcast = broadcast.Broadcast()

    def acabou(self):
        self.endApp()

    def runUpdate(self):
        data = self.broadcast.labelinfo()
        text = '<html><head/><body><p align="center"><span style=" font-size:12pt; font-weight:600; color:#ffffff;">'+str(data)+'</span></p></body></html>'
        self.loadLabel.setText(text)

    def run(self, beginApp, endApp, loadLabel):
        # Step 2: Create a QThread object
        self.thread = QThread()

        self.beginApp = beginApp
        self.endApp = endApp
        self.loadLabel = loadLabel

        # Step 3: Create a worker object
        self.worker = Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.runUpdate)

        # Step 6: Start the thread
        self.beginApp()
        self.thread.start()

        self.thread.finished.connect(self.acabou)
