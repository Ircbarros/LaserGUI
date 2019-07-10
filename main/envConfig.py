# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import sys
import rosgraph


class envConfig(QDialog):
    def __init__(self, parent=None):
        # super(envConfig, self).__init__(parent)
        QDialog.__init__(self)

        layout = QVBoxLayout(self)
        self.setWindowTitle('Enviroment Configuration')
        self.resize(430, 150)

        self.myIP = QtWidgets.QLineEdit(self)
        self.masterIP = QtWidgets.QLineEdit(self)
        self.masterURI = QtWidgets.QLineEdit(self)
        self.hostname = QtWidgets.QLineEdit(self)
        self.namespace = QtWidgets.QLineEdit(self)
        self.perspective = QtWidgets.QLineEdit(self)
        self.rosSource = QtWidgets.QLineEdit(self)
        self.rosEtcDirectory = QtWidgets.QLineEdit(self)
        self.rosRoot = QtWidgets.QLineEdit(self)

        ok = QtWidgets.QPushButton("OK")
        default = QtWidgets.QPushButton("Default")
        cancel = QtWidgets.QPushButton("Cancel")

        self.myIP.setPlaceholderText("ROS_MY_IP (ex.:192.168.43.87)")
        self.masterIP.setPlaceholderText("ROS_MASTER_IP (ex.: 192.168.43.87)")
        self.masterURI.setPlaceholderText("ROS_MASTER_URI (ex.: http://local" +
                                          "host:11311)")
        self.hostname.setPlaceholderText("ROS_HOSTNAME (ex.:192.168.43.87)")
        self.namespace.setPlaceholderText("ROS_NAMESPACE (ex.: robot_0)")
        self.perspective.setPlaceholderText("ROS_SAVED_PERSPECTIVE (ex.:/" +
                                            "config/my_dashboard.perspective)")
        self.rosSource.setPlaceholderText("ROS_SOURCE (ex.:/opt/ros/" +
                                          "<distro>/setup.bash)")
        self.rosEtcDirectory.setPlaceholderText("ROS_ETC_DIR (ex.:/opt/" +
                                                "ros/indigo/etc/ros)")
        self.rosRoot.setPlaceholderText("ROS_ROOT (ex.:/opt/ros/indigo/share/ros)")

        layout.addWidget(self.myIP)
        layout.addWidget(self.masterIP)
        layout.addWidget(self.masterURI)
        layout.addWidget(self.hostname)
        layout.addWidget(self.namespace)
        layout.addWidget(self.perspective)
        layout.addWidget(self.rosSource)
        layout.addWidget(self.rosEtcDirectory)
        layout.addWidget(self.rosRoot)

        layout.addWidget(ok)
        layout.addWidget(default)
        layout.addWidget(cancel)
        self.show()
        self.exec_()

        self.setLayout(layout)

        self.setWindowTitle("Environment Options")

        ok.clicked.connect(self.okOption)
        default.clicked.connect(self.defaultOption)
        default.reject.connect(self.reject)


    @pyqtSlot()
    def okOption(self):
        myIP = self.myIP.text()
        masterIP = self.masterIP.text()
        masterURI = self.masterURI.text()
        hostnameText = self.hostname.text()
        namespace = self.namespace.text()
        perspective = self.perspective.text()
        source = self.rosSource.text()
        etcDirectory = self.rosEtcDirectory.text()
        root = self.rosRoot.text()
        print(myIP)
        print(masterIP)
        print(masterURI)
        print(namespace)
        QMessageBox.question(self, "OK!", "The changes was saved" +
                             textboxValue, QMessageBox.Ok, QMessageBox.Ok)


    def defaultOption(self):
        callerid = data_connection_header['callerid']
        master = rosgraph.Master('listener') 
        ip = master.lookupNode(callerid)
        defaultHostname = ''
        defaultIP = ''
        defaultMasterIP = '1.1.1.1'
        defaultMasterURI = str('http;//$'+defaultMasterIP+':11311')
        self.masterURI.text(defaultMasterURI)

        print(myIP)
        print(masterIP)
        print(masterURI)
        print(namespace)


def main():
    app = QtWidgets.QApplication(sys.argv)
    config = envConfig()
    config.show()
    app.exec_()

if __name__ == "__main__":
    main()
