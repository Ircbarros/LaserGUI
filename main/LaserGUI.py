# Is interesting use Catkin tools
# -*- coding: utf-8 -*-

import webbrowser
import sys
import os
import Logo_Vectors_rc
import subprocess
import signal
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *


class EmbTerminal(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(EmbTerminal, self).__init__(parent)
        self.process = QtCore.QProcess(self)
        self.terminal = QtWidgets.QWidget(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.terminal)
        # Works also with urxvt:
        self.process.start('urxvt', ['-embed', str(int(self.winId()))])
        self.setGeometry(90, 460, 1160, 125)


class InProgress(QtWidgets.QWidget):
    def __init__(self, parent=None):
        Error = QMessageBox()
        Error.setText("Desculpe, opção em desenvolvimento.")
        Error.setIcon(QMessageBox.Information)
        Error.setWindowTitle("Atenção!")
        Error.show()
        Error.exec_()


class Homebox(QtWidgets.QWidget):
    def __init__(self, parent=None):
        HomeInfo = QMessageBox()
        HomeInfo.setText("Você já está na aba HOME")
        HomeInfo.setIcon(QMessageBox.Information)
        HomeInfo.setWindowTitle("Atenção!")
        HomeInfo.show()
        HomeInfo.exec_()


class rvizScreen(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(rvizScreen, self).__init__(parent)
        self.process = QtCore.QProcess(self)
        self.rvizScreen = QtWidgets.QWidget(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.rvizScreen)
        self.process.start('rviz', ['-embed', str(int(self.winId()))])
        # Works also with urxvt:
        # self.process.start('rviz', ['-embed', str(int(self.winId()))])
        # self.setGeometry(121, 120, 940, 340)

class Ui_MainWindow(QtWidgets.QWidget):

    # Abre a página da UFPB
    def UFPBClick(self):
        self.UFPBButton.setDown(True)
        QTimer.singleShot(5000, lambda: self.UFPBButton.setDown(False))
        webbrowser.open('http://ppgi.ci.ufpb.br/')

    def RqtTool(self):
        self.RqtButton.setDown(True)
        QTimer.singleShot(5000, lambda: self.RqtButton.setDown(False))
        subprocess.call('rqt', shell=False)

    def RqtBagTool(self):
        self.RqtBagButton.setDown(True)
        QTimer.singleShot(5000, lambda: self.RqtBagButton.setDown(False))
        subprocess.call('rqt_bag', shell=False)

    def mainState(self):
        if (self.PlayButton.isChecked() is True):
            print('Play selecionado')
            subprocess.call('roscore', shell=True)
            subprocess.call('roslaunch turtlebot_bringup minimal.launch',
                            shell=True)            
            rvizScreen()
        elif (self.StopButton.isChecked() is True):
            print('Stop selecionado')
            # os.kill(signal.CTRL_C_EVENT)
            # process.send_signal(signal.SIGINT)
            subprocess.call('rosnode kill -a', shell=False)
            subprocess.call('killall -9 rosmaster', shell=False)
        elif (self.PauseButton.isChecked() is True):
            print('Pause selecionado')
        elif (self.JoystickButton.isChecked() is True):
            print('Joy selecionado')
            subprocess.call('roslaunch turtlebot_teleop keyboard_teleop.launch',
                            shell=True)
    def controlState(self):
        if (self.FuzzyButton.isChecked() is True):
            print('Fuzzy selecionado')
        elif (self.FelipeButton.isChecked() is True):
            print('Felipe selecionado')
        elif (self.OtherButton.isChecked() is True):
            print('Augusto selecionado')
        elif (self.PWMButton.isChecked() is True):
            print('PWM selecionado')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 600))
        MainWindow.setBaseSize(QtCore.QSize(1280, 600))
        self.Base = QtWidgets.QWidget(MainWindow)
        self.Base.setStyleSheet("background: #2A2E37;")
        self.Base.setObjectName("Base")
        self.LogoFrame = QtWidgets.QFrame(self.Base)
        self.LogoFrame.setGeometry(QtCore.QRect(0, 0, 120, 120))
        self.LogoFrame.setStyleSheet("background: rgba(25, 27, 33, 0.2);\n"
                                     "image: url(:/newPrefix/LogoLaser.png);")
        self.LogoFrame.setObjectName("LogoFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.LogoFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.MenuFrame = QtWidgets.QFrame(self.Base)
        self.MenuFrame.setGeometry(QtCore.QRect(0, 0, 120, 600))
        self.MenuFrame.setStyleSheet("background: #313640;\n"
                                     "")
        self.MenuFrame.setObjectName("MenuFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.MenuFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.MenuLine = QtWidgets.QFrame(self.Base)
        self.MenuLine.setGeometry(QtCore.QRect(120, 0, 2, 600))
        self.MenuLine.setStyleSheet("background: rgba(41, 63, 71, 0.75);")
        self.MenuLine.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MenuLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.MenuLine.setObjectName("MenuLine")
        # Botão Home (Principal)
        self.HomeButton = QtWidgets.QCommandLinkButton(self.Base)
        self.HomeButton.setGeometry(QtCore.QRect(5, 200, 110, 70))
        self.HomeButton.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                      "color: white;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HomeButton.setIcon(icon)
        self.HomeButton.setIconSize(QtCore.QSize(45, 45))
        self.HomeButton.setObjectName("HomeButton")
        self.HomeButton.clicked.connect(Homebox)
        # Botão para Data dos Sistemas Multi-Robôs
        self.DataButton = QtWidgets.QCommandLinkButton(self.Base)
        self.DataButton.setGeometry(QtCore.QRect(5, 300, 110, 70))
        self.DataButton.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                      "color: white;\n"
                                      "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/Data.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DataButton.setIcon(icon1)
        self.DataButton.setIconSize(QtCore.QSize(45, 45))
        self.DataButton.setObjectName("DataButton")
        self.DataButton.clicked.connect(InProgress)
        #  Botão para Configuração de Wifi/Network
        self.WiFiButton = QtWidgets.QCommandLinkButton(self.Base)
        self.WiFiButton.setGeometry(QtCore.QRect(5, 400, 110, 70))
        self.WiFiButton.setStyleSheet("background: rgba(29, 222, 216, 0.1);\n"
                                      "color: white;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/Conection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.WiFiButton.setIcon(icon2)
        self.WiFiButton.setIconSize(QtCore.QSize(45, 45))
        self.WiFiButton.setObjectName("WiFiButton")
        self.WiFiButton.clicked.connect(InProgress)
        #  Botão para Configurações
        self.ConfigButton = QtWidgets.QCommandLinkButton(self.Base)
        self.ConfigButton.setGeometry(QtCore.QRect(1070, 40, 100, 50))
        self.ConfigButton.setStyleSheet("color: white;\n"
                                        "background: rgba(41, 63, 71, 0.75);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/Config.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ConfigButton.setIcon(icon3)
        self.ConfigButton.setIconSize(QtCore.QSize(30, 30))
        self.ConfigButton.setObjectName("ConfigButton")
        self.ConfigButton.clicked.connect(InProgress)
        #  Botão para Contato via E-mail
        self.MailButton = QtWidgets.QCommandLinkButton(self.Base)
        self.MailButton.setGeometry(QtCore.QRect(1180, 40, 81, 50))
        self.MailButton.setStyleSheet("color: white;\n"
                                      "background: rgba(41, 63, 71, 0.75);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/Contact.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MailButton.setIcon(icon4)
        self.MailButton.setIconSize(QtCore.QSize(30, 30))
        self.MailButton.setObjectName("MailButton")
        self.MailButton.clicked.connect(InProgress)
        #  Box de Simulação
        ## self.Simulation = QtWidgets.QGraphicsView(self.Base)
        ## self.Simulation.setGeometry(QtCore.QRect(121, 120, 940, 340))
        ## self.Simulation.setObjectName("Simulation")
        self.Simulation = QtWidgets.QTabWidget(self.Base)
        self.Simulation.setGeometry(QtCore.QRect(121, 120, 940, 340))
        self.Simulation.setTabPosition(QtWidgets.QTabWidget.South)
        self.Simulation.setObjectName("Simulation")
        # Botão do Logo UFPB com Link para Site
        self.UFPBButton = QtWidgets.QCommandLinkButton(self.Base)
        self.UFPBButton.setGeometry(QtCore.QRect(10, 540, 100, 50))
        self.UFPBButton.setStyleSheet("color: white;\n"
                                      "font: 7pt \"Sans Serif\";\n"
                                      "background: rgba(41, 63, 71, 0.75);")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/Ufpb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.UFPBButton.setIcon(icon5)
        self.UFPBButton.setIconSize(QtCore.QSize(30, 30))
        self.UFPBButton.setObjectName("UFPBButton")
        # Evento de Click
        self.UFPBButton.clicked.connect(self.UFPBClick)
        #  Botão para Abertura do Monitoring
        self.MonitorButton = QtWidgets.QPushButton(self.Base)
        self.MonitorButton.setText("Open Monitoring Tool")
        self.MonitorButton.move(1110, 280)
        self.MonitorButton.setStyleSheet("color: white;\n"
                                         "background: rgba(41, 63, 71, 0.75);")
        self.MonitorButton.setObjectName("MonitorButton")
        self.MonitorButton.clicked.connect(self.UFPBClick)
        #  Botão para Abertura do Logged Diagnostics
        self.RqtBagButton = QtWidgets.QPushButton(self.Base)
        self.RqtBagButton.setText("Create an RQT Bag File")
        self.RqtBagButton.move(1105, 305)
        self.RqtBagButton.setStyleSheet("color: white;\n"
                                        "background: rgba(41, 63, 71, 0.75);")
        self.RqtBagButton.setObjectName("RqtBagButton")
        self.RqtBagButton.clicked.connect(self.RqtBagTool)
        #  Botão para Abertura do RQT Dashboard
        self.RqtButton = QtWidgets.QPushButton(self.Base)
        self.RqtButton.setText("Create an RQT Dashboard")
        self.RqtButton.move(1095, 330)
        self.RqtButton.setStyleSheet("color: white;\n"
                                     "background: rgba(41, 63, 71, 0.75);")
        self.RqtButton.setObjectName("RuntimeButton")
        self.RqtButton.clicked.connect(self.RqtTool)
        # Início de Interface da GUI
        self.SuperiorLine = QtWidgets.QFrame(self.Base)
        self.SuperiorLine.setGeometry(QtCore.QRect(121, 120, 1280, 2))
        self.SuperiorLine.setStyleSheet("background: #1DDED8;")
        self.SuperiorLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SuperiorLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.SuperiorLine.setObjectName("SuperiorLine")
        self.InferiorLine = QtWidgets.QFrame(self.Base)
        self.InferiorLine.setGeometry(QtCore.QRect(121, 460, 1280, 2))
        self.InferiorLine.setStyleSheet("background: #1DDED8;")
        self.InferiorLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.InferiorLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.InferiorLine.setObjectName("InferiorLine")
        self.LateraLine = QtWidgets.QFrame(self.Base)
        self.LateraLine.setGeometry(QtCore.QRect(1061, 0, 2, 462))
        self.LateraLine.setStyleSheet("background: #1DDED8;")
        self.LateraLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.LateraLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LateraLine.setObjectName("LateraLine")
        self.Terminal = QtWidgets.QTabWidget(self.Base)
        self.Terminal.setGeometry(QtCore.QRect(121, 462, 1160, 141))
        self.Terminal.setTabPosition(QtWidgets.QTabWidget.South)
        self.Terminal.setObjectName("Terminal")
        self.TerminalFrame = QtWidgets.QWidget()
        self.TerminalFrame.setObjectName("TerminalFrame")
        # Inicia o terminal no app
        self.Terminal.addTab(EmbTerminal(), "urvxt")
        # Final da chamada do terminal
        self.InformationFrame = QtWidgets.QFrame(self.Base)
        self.InformationFrame.setGeometry(QtCore.QRect(1063, 122, 218, 30))
        self.InformationFrame.setStyleSheet("background: rgba(29, 222, 216, 0.1);")
        self.InformationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.InformationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.InformationFrame.setObjectName("InformationFrame")
        self.InformationLabel = QtWidgets.QLabel(self.InformationFrame)
        self.InformationLabel.setGeometry(QtCore.QRect(60, 9, 101, 16))
        self.InformationLabel.setStyleSheet("background: transparent;\n"
                                            "font: 10pt \"Khmer OS System\";\n"
                                            "color: white;")
        self.InformationLabel.setObjectName("InformationLabel")
        self.LogsFrame = QtWidgets.QFrame(self.Base)
        self.LogsFrame.setGeometry(QtCore.QRect(1063, 240, 218, 30))
        self.LogsFrame.setStyleSheet("background: rgba(29, 222, 216, 0.1);")
        self.LogsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LogsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LogsFrame.setObjectName("LogsFrame")
        self.LogsLabel = QtWidgets.QLabel(self.LogsFrame)
        self.LogsLabel.setGeometry(QtCore.QRect(100, 10, 31, 16))
        self.LogsLabel.setStyleSheet("background: transparent;\n"
                                     "font: 9pt \"Khmer OS System\";\n"
                                     "color: white;")
        self.LogsLabel.setObjectName("LogsLabel")
        self.OrientationFrame = QtWidgets.QFrame(self.Base)
        self.OrientationFrame.setGeometry(QtCore.QRect(1063, 360, 218, 30))
        self.OrientationFrame.setStyleSheet("background: rgba(29, 222, 216, 0.1);")
        self.OrientationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.OrientationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.OrientationFrame.setObjectName("OrientationFrame")
        self.OrientationLabel = QtWidgets.QLabel(self.OrientationFrame)
        self.OrientationLabel.setGeometry(QtCore.QRect(70, 9, 81, 16))
        self.OrientationLabel.setStyleSheet("background: transparent;\n"
                                            "font: 9pt \"Khmer OS System\";\n"
                                            "color: white;")
        self.OrientationLabel.setObjectName("OrientationLabel")
        self.Battery = QtWidgets.QFrame(self.Base)
        self.Battery.setGeometry(QtCore.QRect(1110, 170, 41, 31))
        self.Battery.setStyleSheet("image: url(:/newPrefix/BatteryHigh.png);")
        self.Battery.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Battery.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Battery.setObjectName("Battery")
        self.BatteryValue = QtWidgets.QLCDNumber(self.Base)
        self.BatteryValue.setGeometry(QtCore.QRect(1110, 200, 41, 23))
        self.BatteryValue.setObjectName("BatteryValue")
        self.Wifi = QtWidgets.QFrame(self.Base)
        self.Wifi.setGeometry(QtCore.QRect(1200, 170, 41, 31))
        self.Wifi.setStyleSheet("image: url(:/newPrefix/InternetSignalHigh.png);")
        self.Wifi.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Wifi.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Wifi.setObjectName("Wifi")
        self.WifiValue = QtWidgets.QLCDNumber(self.Base)
        self.WifiValue.setGeometry(QtCore.QRect(1200, 200, 41, 23))
        self.WifiValue.setObjectName("WifiValue")
        self.MainControl = QtWidgets.QFrame(self.Base)
        self.MainControl.setGeometry(QtCore.QRect(210, 10, 218, 91))
        self.MainControl.setStyleSheet("background: rgba(29, 222, 216, 0.1);")
        self.MainControl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainControl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainControl.setObjectName("MainControl")
        self.MainControlLabel = QtWidgets.QLabel(self.MainControl)
        self.MainControlLabel.setGeometry(QtCore.QRect(60, 5, 91, 16))
        self.MainControlLabel.setStyleSheet("background: transparent;\n"
                                            "color: white;")
        self.MainControlLabel.setObjectName("MainControlLabel")
        self.MainControlLine = QtWidgets.QFrame(self.MainControl)
        self.MainControlLine.setGeometry(QtCore.QRect(50, 20, 110, 1))
        self.MainControlLine.setStyleSheet("background: #1DDED8;")
        self.MainControlLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.MainControlLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.MainControlLine.setObjectName("MainControlLine")
        # Inicio do Radio Buttons Principais
        # Botão para Iniciar Simulação
        self.PlayButton = QtWidgets.QRadioButton(self.MainControl)
        self.PlayButton.setGeometry(QtCore.QRect(20, 30, 71, 21))
        self.PlayButton.setStyleSheet("background: transparent;\n"
                                      "color: rgb(154, 255, 152);")
        self.PlayButton.setObjectName("PlayButton")
        self.PlayButton.setChecked(False)
        self.PlayButton.toggled.connect(self.mainState)
        # Botão para Joystick (Teclado)
        self.JoystickButton = QtWidgets.QRadioButton(self.MainControl)
        self.JoystickButton.setGeometry(QtCore.QRect(120, 30, 71, 21))
        self.JoystickButton.setStyleSheet("background: transparent;\n"
                                          "color: rgb(206, 255, 188);")
        self.JoystickButton.setObjectName("JoystickButton")
        self.JoystickButton.setChecked(False)
        self.JoystickButton.toggled.connect(self.mainState)
        # Botão para Pausar Simulação
        self.PauseButton = QtWidgets.QRadioButton(self.MainControl)
        self.PauseButton.setGeometry(QtCore.QRect(20, 60, 71, 21))
        self.PauseButton.setStyleSheet("background: transparent;\n"
                                       "color: rgb(248, 255, 162);")
        self.PauseButton.setObjectName("PauseButton")
        self.PauseButton.setChecked(False)
        self.PauseButton.toggled.connect(self.mainState)
        # Botão para Parar Simulação
        self.StopButton = QtWidgets.QRadioButton(self.MainControl)
        self.StopButton.setGeometry(QtCore.QRect(118, 60, 71, 21))
        self.StopButton.setStyleSheet("background: transparent;\n"
                                      "color: red;")
        self.StopButton.setObjectName("StopButton")
        self.StopButton.setChecked(False)
        self.StopButton.toggled.connect(self.mainState)
        # Design do Box de Controladores
        self.Controller = QtWidgets.QFrame(self.Base)
        self.Controller.setGeometry(QtCore.QRect(470, 10, 218, 91))
        self.Controller.setStyleSheet("background: rgba(29, 222, 216, 0.1);")
        self.Controller.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Controller.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Controller.setObjectName("Controller")
        self.ControllerLabel = QtWidgets.QLabel(self.Controller)
        self.ControllerLabel.setGeometry(QtCore.QRect(60, 5, 91, 16))
        self.ControllerLabel.setStyleSheet("background: transparent;\n"
                                           "color: white;")
        self.ControllerLabel.setObjectName("ControllerLabel")
        self.ControllerLine = QtWidgets.QFrame(self.Controller)
        self.ControllerLine.setGeometry(QtCore.QRect(50, 20, 110, 1))
        self.ControllerLine.setStyleSheet("background: #1DDED8;")
        self.ControllerLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.ControllerLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ControllerLine.setObjectName("ControllerLine")
        # Botões para Acionamento de Controladores
        # Fuzzy
        self.FuzzyButton = QtWidgets.QRadioButton(self.Controller)
        self.FuzzyButton.setGeometry(QtCore.QRect(20, 30, 91, 21))
        self.FuzzyButton.setStyleSheet("background: transparent;\n"
                                       "color: rgb(206, 255, 188);\n"
                                       "\n"
                                       "")
        self.FuzzyButton.setObjectName("FuzzyButton")
        self.FuzzyButton.setChecked(False)
        self.FuzzyButton.toggled.connect(self.controlState)
        # Botão para Acionamento do Controle de Felipe
        self.FelipeButton = QtWidgets.QRadioButton(self.Controller)
        self.FelipeButton.setGeometry(QtCore.QRect(20, 60, 91, 21))
        self.FelipeButton.setStyleSheet("background: transparent;\n"
                                        "color: rgb(206, 255, 188);\n"
                                        "")
        self.FelipeButton.setObjectName("FelipeButton")
        self.FelipeButton.setChecked(False)
        self.FelipeButton.toggled.connect(self.controlState)
        # Botão para Acionamento do Controle de Augusto
        self.OtherButton = QtWidgets.QRadioButton(self.Controller)
        self.OtherButton.setGeometry(QtCore.QRect(110, 30, 81, 21))
        self.OtherButton.setStyleSheet("background: transparent;\n"
                                       "color: rgb(206, 255, 188);")
        self.OtherButton.setObjectName("OtherButton")
        self.OtherButton.setChecked(False)
        self.OtherButton.toggled.connect(self.controlState)
        # PWM
        self.PWMButton = QtWidgets.QRadioButton(self.Controller)
        self.PWMButton.setGeometry(QtCore.QRect(111, 60, 81, 21))
        self.PWMButton.setStyleSheet("background: transparent;\n"
                                     "color: rgb(206, 255, 188);")
        self.PWMButton.setObjectName("PWMButton")
        self.PWMButton.setChecked(False)
        self.PWMButton.toggled.connect(self.controlState)
        # Inicío de Radio Buttons para Seleção dos Robôs
        self.RobotSelection = QtWidgets.QFrame(self.Base)
        self.RobotSelection.setGeometry(QtCore.QRect(730, 10, 218, 51))
        self.RobotSelection.setStyleSheet("background: rgba(29, 222, 216, 0.1);")
        self.RobotSelection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RobotSelection.setFrameShadow(QtWidgets.QFrame.Raised)
        self.RobotSelection.setObjectName("RobotSelection")
        self.RobotSelectionLabel = QtWidgets.QLabel(self.RobotSelection)
        self.RobotSelectionLabel.setGeometry(QtCore.QRect(48, 5, 121, 16))
        self.RobotSelectionLabel.setStyleSheet("background: transparent;\n"
                                               "color: white;")
        self.RobotSelectionLabel.setObjectName("RobotSelectionLabel")
        self.RobotSelectionLine = QtWidgets.QFrame(self.RobotSelection)
        self.RobotSelectionLine.setGeometry(QtCore.QRect(50, 20, 110, 1))
        self.RobotSelectionLine.setStyleSheet("background: #1DDED8;")
        self.RobotSelectionLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.RobotSelectionLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.RobotSelectionLine.setObjectName("RobotSelectionLine")
        self.RobotOne = QtWidgets.QRadioButton(self.RobotSelection)
        self.RobotOne.setGeometry(QtCore.QRect(14, 27, 31, 21))
        self.RobotOne.setStyleSheet("background: transparent;\n"
                                    "color: rgb(206, 255, 188);")
        self.RobotOne.setObjectName("RobotOne")
        self.RobotTwo = QtWidgets.QRadioButton(self.RobotSelection)
        self.RobotTwo.setGeometry(QtCore.QRect(60, 27, 31, 21))
        self.RobotTwo.setStyleSheet("background: transparent;\n"
                                    "color: rgb(206, 255, 188);")
        self.RobotTwo.setObjectName("RobotTwo")
        self.RobotThree = QtWidgets.QRadioButton(self.RobotSelection)
        self.RobotThree.setGeometry(QtCore.QRect(110, 27, 31, 21))
        self.RobotThree.setStyleSheet("background: transparent;\n"
                                      "color: rgb(206, 255, 188);")
        self.RobotThree.setObjectName("RobotThree")
        self.RobotThree_2 = QtWidgets.QRadioButton(self.RobotSelection)
        self.RobotThree_2.setGeometry(QtCore.QRect(156, 27, 31, 21))
        self.RobotThree_2.setStyleSheet("background: transparent;\n"
                                        "color: rgb(206, 255, 188);")
        self.RobotThree_2.setObjectName("RobotThree_2")
        self.XValue = QtWidgets.QLCDNumber(self.Base)
        self.XValue.setGeometry(QtCore.QRect(1090, 400, 31, 23))
        self.XValue.setObjectName("XValue")
        self.XLabel = QtWidgets.QLabel(self.Base)
        self.XLabel.setGeometry(QtCore.QRect(1070, 405, 21, 16))
        self.XLabel.setStyleSheet("background: transparent;\n"
                                  "font: 11pt \"Sans Serif\";\n"
                                  "color: red;")
        self.XLabel.setObjectName("XLabel")
        self.YValue = QtWidgets.QLCDNumber(self.Base)
        self.YValue.setGeometry(QtCore.QRect(1170, 400, 31, 23))
        self.YValue.setObjectName("YValue")
        self.YLabel = QtWidgets.QLabel(self.Base)
        self.YLabel.setGeometry(QtCore.QRect(1150, 405, 21, 16))
        self.YLabel.setStyleSheet("background: transparent;\n"
                                  "font: 11pt \"Sans Serif\";\n"
                                  "color: yellow;")
        self.YLabel.setObjectName("YLabel")
        self.ZValue = QtWidgets.QLCDNumber(self.Base)
        self.ZValue.setGeometry(QtCore.QRect(1240, 400, 31, 23))
        self.ZValue.setObjectName("ZValue")
        self.ZLabel = QtWidgets.QLabel(self.Base)
        self.ZLabel.setGeometry(QtCore.QRect(1220, 405, 21, 16))
        self.ZLabel.setStyleSheet("background: transparent;\n"
                                  "font: 11pt \"Sans Serif\";\n"
                                  "color: green;")
        self.ZLabel.setObjectName("ZLabel")
        self.PitchValue = QtWidgets.QLCDNumber(self.Base)
        self.PitchValue.setGeometry(QtCore.QRect(1125, 430, 31, 23))
        self.PitchValue.setObjectName("PitchValue")
        self.PitchLabel = QtWidgets.QLabel(self.Base)
        self.PitchLabel.setGeometry(QtCore.QRect(1080, 435, 51, 16))
        self.PitchLabel.setStyleSheet("background: transparent;\n"
                                      "font: 11pt \"Sans Serif\";\n"
                                      "color: rgb(206, 255, 188);")
        self.PitchLabel.setObjectName("PitchLabel")
        self.YallValue = QtWidgets.QLabel(self.Base)
        self.YallValue.setGeometry(QtCore.QRect(1185, 435, 41, 16))
        self.YallValue.setStyleSheet("background: transparent;\n"
                                     "font: 11pt \"Sans Serif\";\n"
                                     "color: rgb(206, 255, 188);")
        self.YallValue.setObjectName("YallValue")
        self.YalNumber = QtWidgets.QLCDNumber(self.Base)
        self.YalNumber.setGeometry(QtCore.QRect(1230, 430, 31, 23))
        self.YalNumber.setObjectName("YalNumber")
        self.TeamSelection = QtWidgets.QFrame(self.Base)
        self.TeamSelection.setGeometry(QtCore.QRect(730, 60, 218, 41))
        self.TeamSelection.setStyleSheet("background: rgba(29, 222, 216, 0.1);")
        self.TeamSelection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TeamSelection.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TeamSelection.setObjectName("TeamSelection")
        self.TeamSelectionName = QtWidgets.QLabel(self.TeamSelection)
        self.TeamSelectionName.setGeometry(QtCore.QRect(80, 2, 41, 16))
        self.TeamSelectionName.setStyleSheet("background: transparent;\n"
                                             "color: white;")
        self.TeamSelectionName.setObjectName("TeamSelectionName")
        self.TeamSelectionLine = QtWidgets.QFrame(self.TeamSelection)
        self.TeamSelectionLine.setGeometry(QtCore.QRect(80, 18, 35, 1))
        self.TeamSelectionLine.setStyleSheet("background: #1DDED8;")
        self.TeamSelectionLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.TeamSelectionLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.TeamSelectionLine.setObjectName("TeamSelectionLine")
        self.TeamOne = QtWidgets.QRadioButton(self.TeamSelection)
        self.TeamOne.setGeometry(QtCore.QRect(50, 22, 31, 21))
        self.TeamOne.setStyleSheet("background: transparent;\n"
                                   "color: rgb(206, 255, 188);")
        self.TeamOne.setObjectName("TeamOne")
        self.TeamTwo = QtWidgets.QRadioButton(self.TeamSelection)
        self.TeamTwo.setGeometry(QtCore.QRect(100, 22, 31, 21))
        self.TeamTwo.setStyleSheet("background: transparent;\n"
                                   "color: rgb(206, 255, 188);")
        self.TeamTwo.setObjectName("TeamTwo")
        self.MenuFrame.raise_()
        self.LogoFrame.raise_()
        self.MenuLine.raise_()
        self.HomeButton.raise_()
        self.DataButton.raise_()
        self.WiFiButton.raise_()
        self.ConfigButton.raise_()
        self.MailButton.raise_()
        self.Simulation.raise_()
        self.UFPBButton.raise_()
        self.MonitorButton.raise_()
        self.RqtBagButton.raise_()
        self.RqtButton.raise_()
        self.SuperiorLine.raise_()
        self.InferiorLine.raise_()
        self.LateraLine.raise_()
        self.Terminal.raise_()
        self.InformationFrame.raise_()
        self.LogsFrame.raise_()
        self.OrientationFrame.raise_()
        self.Battery.raise_()
        self.BatteryValue.raise_()
        self.Wifi.raise_()
        self.WifiValue.raise_()
        self.MainControl.raise_()
        self.Controller.raise_()
        self.RobotSelection.raise_()
        self.XValue.raise_()
        self.XLabel.raise_()
        self.YValue.raise_()
        self.YLabel.raise_()
        self.ZValue.raise_()
        self.ZLabel.raise_()
        self.PitchValue.raise_()
        self.PitchLabel.raise_()
        self.YallValue.raise_()
        self.YalNumber.raise_()
        self.TeamSelection.raise_()
        MainWindow.setCentralWidget(self.Base)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LaserGUI"))
        self.HomeButton.setText(_translate("MainWindow", "Home"))
        self.DataButton.setText(_translate("MainWindow", "Data"))
        self.WiFiButton.setText(_translate("MainWindow", "Ad-hoc"))
        self.ConfigButton.setText(_translate("MainWindow", "Config"))
        self.MailButton.setText(_translate("MainWindow", "Mail"))
        self.UFPBButton.setText(_translate("MainWindow", "PPGI UFPB"))
        self.InformationLabel.setText(_translate("MainWindow", "INFORMATIONS"))
        self.LogsLabel.setText(_translate("MainWindow", "APPs"))
        self.OrientationLabel.setText(_translate("MainWindow", "ORIENTATION"))
        self.MainControlLabel.setText(_translate("MainWindow", "MAIN CONTROL"))
        self.PlayButton.setText(_translate("MainWindow", "Play"))
        self.JoystickButton.setText(_translate("MainWindow", "Joystick"))
        self.PauseButton.setText(_translate("MainWindow", "Pause"))
        self.StopButton.setText(_translate("MainWindow", "Stop"))
        self.ControllerLabel.setText(_translate("MainWindow", "CONTROLLER"))
        self.FuzzyButton.setText(_translate("MainWindow", "Fuzzy"))
        self.FelipeButton.setText(_translate("MainWindow", "PBD"))
        self.OtherButton.setText(_translate("MainWindow", "PDNMPC"))
        self.PWMButton.setText(_translate("MainWindow", "PWM"))
        self.RobotSelectionLabel.setText(_translate("MainWindow",
                                                    "ROBOT SELECTION"))
        self.RobotOne.setText(_translate("MainWindow", "1"))
        self.RobotTwo.setText(_translate("MainWindow", "2"))
        self.RobotThree.setText(_translate("MainWindow", "3"))
        self.RobotThree_2.setText(_translate("MainWindow", "4"))
        self.XLabel.setText(_translate("MainWindow", "X:"))
        self.YLabel.setText(_translate("MainWindow", "Y:"))
        self.ZLabel.setText(_translate("MainWindow", "Z:"))
        self.PitchLabel.setText(_translate("MainWindow", "Pitch:"))
        self.YallValue.setText(_translate("MainWindow", "Yall:"))
        self.TeamSelectionName.setText(_translate("MainWindow", "TEAM:"))
        self.TeamOne.setText(_translate("MainWindow", "1"))
        self.TeamTwo.setText(_translate("MainWindow", "2"))


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
