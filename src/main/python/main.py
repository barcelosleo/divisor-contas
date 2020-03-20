from os import path

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow

import sys

from View.MainWindowView import MainWindowView
from Model.migrate import migrate

if __name__ == '__main__':
    if not path.exists('__local.db'):
        migrate()
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWindowView()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)