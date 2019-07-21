import subprocess
import time
import sys
import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication


class Mcve(QMainWindow):

    def __init__(self):
        super(Mcve, self).__init__()
        
        menu = self.menuBar()
        rvizMenu = menu.addMenu('RViz')
        attach_action = QAction('Attach', self, checkable=True)
        attach_action.setStatusTip('Attach the RViz Screen')
        attach_action.setChecked(False)
        attach_action.triggered.connect(self.attach)

        rvizMenu.addAction(attach_action)

        self.dock = PyQt5.QtWidgets.QDockWidget("Attach window", self)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)

        subprocess.Popen('rviz')
        time.sleep(0.5)
        lookForID = "wmctrl -l | grep -i RViz | awk '{print $1}'"
        self.rvizID = subprocess.check_output(lookForID, shell=True)
        print(self.rvizID)
        if self.rvizID == 0:
            raise Exception("Process not found")

    def detach(self):
        try:
            self._window.setParent(None)
            # win32gui.SetWindowLong(self.hwnd, win32con.GWL_EXSTYLE, self._style)
            self._window.show()
            self.dock.setWidget(None)
            self._widget = None
            self._window = None
        except Exception as e:
            import traceback
            traceback.print_exc()

    def attach(self):
        # self._style = win32gui.GetWindowLong(self.hwnd, win32con.GWL_EXSTYLE)
        self._window = Qt.QWindow.fromWinId(self.rvizID)
        self._widget = self.createWindowContainer(self._window)
        self.dock.setWidget(self._widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    rviz = Mcve()
    rviz.show()
    sys.exit(app.exec_())