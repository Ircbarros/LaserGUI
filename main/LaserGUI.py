# Is interesting use Catkin tools
# -*- coding: utf-8 -*-

import webbrowser
import sys
import os
import Logo_Vectors_rc
import subprocess
from subprocess import call, Popen, PIPE, check_output
import signal
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from laserSettings import *


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
        Error = QtWidgets.QMessageBox()
        Error.setText('Desculpe, opção em desenvolvimento.')
        Error.setIcon(QtWidgets.QMessageBox.Information)
        Error.setWindowTitle('Atenção!')
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


class Ui_MainWindow(QtWidgets.QMainWindow):

    # Abre a página da UFPB
    def UFPBClick(self):
        # Only 1 click at every 5 seconds
        self.UFPBButton.setDown(True)
        QTimer.singleShot(5000, lambda: self.UFPBButton.setDown(False))
        webbrowser.open('http://ppgi.ci.ufpb.br/')

    def MonitoringTool(self):
        self.MonitorButton.setDown(True)
        QTimer.singleShot(5000, lambda: self.MonitorButton.setDown(False))
        MonitorCommand = 'rosrun rqt_robot_monitor rqt_robot_monitor'
        # Using Popen instead of Call because the first one don't block the process
        monitorRqtProcess = subprocess.Popen(MonitorCommand, stdout=PIPE,
                                             stdin=PIPE, shell=True)
        MonitorProcStdout = monitorRqtProcess.communicate()[0].strip()
        print (MonitorProcStdout)

    def RqtTool(self):
        self.RqtButton.setDown(True)
        QTimer.singleShot(5000, lambda: self.RqtButton.setDown(False))
        RqtCommand = 'rqt'
        # Using Popen instead of Call because the first one don't block the process
        RqtProcess = subprocess.Popen(RqtCommand, stdout=PIPE,
                                      stdin=PIPE, shell=True)
        RqtToolProcStdout = RqtProcess.communicate()[0].strip()
        print (RqtToolProcStdout)

    def RqtBagTool(self):
        self.RqtBagButton.setDown(True)
        QTimer.singleShot(5000, lambda: self.RqtBagButton.setDown(False))
        BagCommand = 'rqt_bag'
        # Using Popen instead of Call because the first one don't block the process
        BagProcess = subprocess.Popen(BagCommand, stdout=PIPE,
                                      stdin=PIPE, shell=True)
        BagProcStdout = BagProcess.communicate()[0].strip()
        print (BagProcStdout)

    def rqtConsoleTool(self):
        self.rqtConsoleButton.setDown(True)
        QTimer.singleShot(5000, lambda: self.rqtConsoleButton.setDown(False))
        rqtConsoleCommand = 'rqt_console'
        # Using Popen instead of Call because the first one don't block the process
        rqtConsoleProcess = subprocess.Popen(rqtConsoleCommand, stdout=PIPE,
                                             stdin=PIPE, shell=True)
        rqtConsoleProcStdout = rqtConsoleProcess.communicate()[0].strip()
        print (rqtConsoleProcStdout)

    def rqtLoggerTool(self):
        self.rqtLoggerButton.setDown(True)
        QTimer.singleShot(5000, lambda: self.rqtLoggerButton.setDown(False))
        rqtLoggerCommand = 'rosrun rqt_logger_level rqt_logger_level'
        # Using Popen instead of Call because the first one don't block the process
        rqtLoggerProcess = subprocess.Popen(rqtLoggerCommand, stdout=PIPE,
                                            stdin=PIPE, shell=True)
        rqtLoggerProcStdout = rqtLoggerProcess.communicate()[0].strip()
        print (rqtLoggerProcStdout)

    def mainState(self):
        if (self.PlayButton.isChecked() is True):
            print('Play selecionado')

        elif (self.StopButton.isChecked() is True):
            print('Stop selecionado')
            self.RqtBagButton.setDown(True)
            killRosNode = 'rosnode kill -a'
            killRosMaster = 'killall -9 rosmaster'
            killRosCore = 'killall -9 roscore'
            QTimer.singleShot(5000, lambda: self.RqtBagButton.setDown(False))
            # Using Popen instead of Call because the first one don't block the process
            coreKillProcess = subprocess.Popen(killRosCore, stdout=PIPE,
                                               stdin=PIPE, shell=True)
            nodeKillProcess = subprocess.Popen(killRosNode, stdout=PIPE,
                                               stdin=PIPE, shell=True)
            masterKillProcess = subprocess.Popen(killRosMaster, stdout=PIPE,
                                                 stdin=PIPE, shell=True)
            stopCoreProcStdout = coreKillProcess.communicate()[0].strip()
            stopNodeProcStdout = nodeKillProcess.communicate()[0].strip()
            stopMasterProcStdout = masterKillProcess.communicate()[0].strip()
            print (stopCoreProcStdout, stopNodeProcStdout,
                   stopMasterProcStdout)

        elif (self.PauseButton.isChecked() is True):
            print('Pause selecionado')

        elif (self.JoystickButton.isChecked() is True):
            print('Joy selecionado')
            joySelection = 'roslaunch turtlebot_teleop keyboard_teleop.launch'
            joyProcess = subprocess.Popen(joySelection, stdout=PIPE,
                                          stdin=PIPE, shell=True)
            joyProcStdout = joyProcess.communicate()[0].strip()
            print (joyProcStdout)

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
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/Config.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ConfigButton.setIcon(icon3)
        self.ConfigButton.setIconSize(QtCore.QSize(30, 30))
        self.ConfigButton.setObjectName("ConfigButton")
        self.ConfigButton.setToolTip('Configure Enviroment Variables')
        self.ConfigButton.clicked.connect(laserSettings)
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
        self.MailButton.setToolTip('Contact the LASER Laboratory')
        self.MailButton.clicked.connect(InProgress)
        #  Box de Simulação
        # self.Simulation = QtWidgets.QGraphicsView(self.Base)
        # self.Simulation.setGeometry(QtCore.QRect(121, 120, 940, 340))
        # self.Simulation.setObjectName("Simulation")
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
        self.MonitorButton.move(1107, 280)
        self.MonitorButton.setStyleSheet("color: white;\n"
                                         "background: rgba(41, 63, 71, 0.75);")
        self.MonitorButton.setObjectName("MonitorButton")
        self.MonitorButton.setToolTip('Open the Robot Monitoring Tool ' +
                                      '(Make sure diagnostic_aggregator is runing!)')
        self.MonitorButton.clicked.connect(self.MonitoringTool)
        #  Botão para Abertura do Logged Diagnostics
        self.RqtBagButton = QtWidgets.QPushButton(self.Base)
        self.RqtBagButton.setText("Create an RQT Bag File")
        self.RqtBagButton.move(1102, 305)
        self.RqtBagButton.setStyleSheet("color: white;\n"
                                        "background: rgba(41, 63, 71, 0.75);")
        self.RqtBagButton.setObjectName("RqtBagButton")
        self.RqtBagButton.setToolTip('Open the Rosbag Tool ' +
                                     '(Make sure roscore and rosmaster is runing!)')
        self.RqtBagButton.clicked.connect(self.RqtBagTool)
        #  Botão para Abertura do RQT Dashboard
        self.RqtButton = QtWidgets.QPushButton(self.Base)
        self.RqtButton.setText("Create an RQT Dashboard")
        self.RqtButton.move(1094, 330)
        self.RqtButton.setStyleSheet("color: white;\n"
                                     "background: rgba(41, 63, 71, 0.75);")
        self.RqtButton.setObjectName("RuntimeButton")
        self.RqtButton.setToolTip('Open the RQT Dashboard or a Saved Perspective ' +
                                  '(Make sure roscore and rosmaster is runing!)')
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
        # Início dos Frames e Labels Graph, Tolls e Debug
        self.graphSettingsFrame = QtWidgets.QFrame(self.Base)
        self.graphSettingsFrame.setGeometry(QtCore.QRect(1063, 122, 218, 30))
        self.graphSettingsFrame.setStyleSheet("background: rgba(29, 222, 216, 0.1);")
        self.graphSettingsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graphSettingsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graphSettingsFrame.setObjectName("graphSettingsFrame")
        self.graphSettingsLabel = QtWidgets.QLabel(self.graphSettingsFrame)
        self.graphSettingsLabel.setGeometry(QtCore.QRect(53, 9, 115, 20))
        self.graphSettingsLabel.setStyleSheet("background: transparent;\n"
                                              "font: 10pt \"Khmer OS System\";\n"
                                              "color: white;")
        self.graphSettingsLabel.setObjectName("graphSettingsLabel")
        self.toolsFrame = QtWidgets.QFrame(self.Base)
        self.toolsFrame.setGeometry(QtCore.QRect(1063, 240, 218, 30))
        self.toolsFrame.setStyleSheet("background: rgba(29, 222, 216, 0.1);")
        self.toolsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.toolsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toolsFrame.setObjectName("toolsFrame")
        self.toolsLabel = QtWidgets.QLabel(self.toolsFrame)
        self.toolsLabel.setGeometry(QtCore.QRect(88, 10, 40, 16))
        self.toolsLabel.setStyleSheet("background: transparent;\n"
                                      "font: 9pt \"Khmer OS System\";\n"
                                      "color: white;")
        self.toolsLabel.setObjectName("toolsLabel")
        self.debugFrame = QtWidgets.QFrame(self.Base)
        self.debugFrame.setGeometry(QtCore.QRect(1063, 360, 218, 30))
        self.debugFrame.setStyleSheet("background: rgba(29, 222, 216, 0.1);")
        self.debugFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.debugFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.debugFrame.setObjectName("debugFrame")
        self.debugLabel = QtWidgets.QLabel(self.debugFrame)
        self.debugLabel.setGeometry(QtCore.QRect(65, 9, 90, 16))
        self.debugLabel.setStyleSheet("background: transparent;\n"
                                      "font: 9pt \"Khmer OS System\";\n"
                                      "color: white;")
        self.debugLabel.setObjectName("debugLabel")
        #  Botão para Abertura do RQT Console
        self.rqtConsoleButton = QtWidgets.QPushButton(self.Base)
        self.rqtConsoleButton.setText("Open RQT Console")
        self.rqtConsoleButton.move(1115, 400)
        self.rqtConsoleButton.setStyleSheet("color: white;\n"
                                            "background: rgba(41, 63, 71, 0.75);")
        self.rqtConsoleButton.setObjectName("rqtConsoleButton")
        self.rqtConsoleButton.setToolTip('Filter messages by node, text and more.')
        self.rqtConsoleButton.clicked.connect(self.rqtConsoleTool)
        #  Botão para Abertura do RQT LOGGER LEVEL
        self.rqtLoggerButton = QtWidgets.QPushButton(self.Base)
        self.rqtLoggerButton.setText("Open RQT Logger Level")
        self.rqtLoggerButton.move(1100, 427)
        self.rqtLoggerButton.setStyleSheet("color: white;\n"
                                           "background: rgba(41, 63, 71, 0.75);")
        self.rqtLoggerButton.setObjectName("rqtLoggerButton")
        self.rqtLoggerButton.setToolTip('See messages marked as DEBUG')
        self.rqtLoggerButton.clicked.connect(self.rqtLoggerTool)

        # Final dos Frames e Graph, Tools e Debug
        # Início do Frame e Label do MAIN CONTROL
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
        self.RobotFour = QtWidgets.QRadioButton(self.RobotSelection)
        self.RobotFour.setGeometry(QtCore.QRect(156, 27, 31, 21))
        self.RobotFour.setStyleSheet("background: transparent;\n"
                                     "color: rgb(206, 255, 188);")
        self.RobotFour.setObjectName("RobotFour")
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
        self.toolsFrame.raise_()
        self.MenuLine.raise_()
        self.LogoFrame.raise_()
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
        self.rqtConsoleButton.raise_()
        self.rqtLoggerButton.raise_()
        self.SuperiorLine.raise_()
        self.InferiorLine.raise_()
        self.LateraLine.raise_()
        self.Terminal.raise_()
        self.graphSettingsFrame.raise_()
        self.toolsFrame.raise_()
        self.debugFrame.raise_()
        self.MainControl.raise_()
        self.Controller.raise_()
        self.RobotSelection.raise_()
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
        self.graphSettingsLabel.setText(_translate("MainWindow",
                                                   "GRAPH SETTINGS"))
        self.toolsLabel.setText(_translate("MainWindow", "TOOLS"))
        self.debugLabel.setText(_translate("MainWindow", "DEBUG & TEST"))
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
        self.RobotFour.setText(_translate("MainWindow", "4"))
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
