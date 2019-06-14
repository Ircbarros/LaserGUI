from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog, QVBoxLayout, QFileDialog
import sys
import urllib.request


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
        self.url.setText("")
        self.saveLocation.setText("")

        self.progress.setValue(0)
        self.progress.setAlignment(QtCore.Qt.AlignCenter)

        layout.addWidget(self.url)
        layout.addWidget(self.saveLocation)
        layout.addWidget(search)
        layout.addWidget(self.progress)
        layout.addWidget(download)

        self.setLayout(layout)

        self.setWindowTitle("Carregar Arquivo")

        download.clicked.connect(self.downloadFile)
        search.clicked.connect(self.searchFile)

    def searchFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        saveFile = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()",
                                               options=options)
        self.saveLocation.setText(str(saveFile))

    def downloadFile(self):
        url = self.url.text()
        directoryLocation = self.saveLocation.text()

        try:
            urllib.request.urlretrieve(url, directoryLocation, self.report)
        except Exception:
            QMessageBox.warning(self, "Erro!", "Falha no Download!")
            return

        QMessageBox.information(self, "Informação:", "Download Concluído!")
        self.progress.setValue(0)
        self.url.setText("")
        self.saveLocation("")

    def report(self, blocknr, blocksize, size):
        readed = blocknr*blocksize
        percent = (readed*100)/size
        self.progress.setValue(int(percent))


app = QtWidgets.QApplication(sys.argv)
dl = Downloader()
dl.show()
app.exec_()
