# -*- coding: utf-8 -*-
from ui.deadline_option_widget import Ui_Form

from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class SettingWidget(QWidget):
   def __init__(self):

      QWidget.__init__(self)

      self.ui = Ui_Form()
      self.ui.setupUi(self)


