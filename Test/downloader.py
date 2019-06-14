from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog, QVBoxLayout, QMainWindow, QFileDialog
import Logo_Vectors_rc
import webbrowser
import sys
from urllib import request


class Downloader(QDialog):
    def __init__(self, parent=None):
        super(Downloader, self).__init__(parent)
        QDialog.__init__(self)

        layout = QVBoxLayout(self)

        self.url = QtWidgets.QLineEdit()
        self.saveLocation = QtWidgets.QLineEdit()
        self.progress = QtWidgets.QProgressBar()
        download = QtWidgets.QPushButton("Download")
        search = QtWidgets.QPushButton("Procurar Diretório")

        self.url.setPlaceholderText("URL ou Link")
        self.saveLocation.setPlaceholderText("Diretório")

        self.progress.setValue(0)
        self.progress.setAlignment(QtCore.Qt.AlignCenter)

        layout.addWidget(self.url)
        layout.addWidget(self.saveLocation)
        layout.addWidget(search)
        layout.addWidget(self.progress)
        layout.addWidget(download)

        self.setLayout(layout)
        self.setWindowTitle("Carregar Arquivo")
        self.setFocus()

        download.clicked.connect(self.downloadFile)
        search.clicked.connect(self.searchFile)

    def searchFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()",
                                               "","All Files (*)", options=options)
    
    def downloadFile(self):
        url = self.url.text()
        saveLocation = self.saveLocation.text()

        try:
            request.urlretrieve(url, saveLocation, self.report)
        except Exception:
            QMessageBox.warning(self, "Erro!", "Falha no Download!")
            return

        QMessageBox.information(self, "Informação:", "Download Concluído!")
        self.progress.setValue(0)
        self.url.setText("")
        self.saveLocation.setText("")

    def report(self, blocknum, blocksize, totalsize):
        readed = blocknum * blocksize
        if totalsize > 0:
            percent = readed * 100 / totalsize
            self.progress.setValue(int(percent))


app = QtWidgets.QApplication(sys.argv)
dl = Downloader()
dl.show()
app.exec_()