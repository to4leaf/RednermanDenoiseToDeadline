# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'body_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(787, 244)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(720, 200))
        Form.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(11)
        Form.setFont(font)
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.denoise_path_layout = QHBoxLayout()
        self.denoise_path_layout.setObjectName(u"denoise_path_layout")
        self.denoise_path_label = QLabel(Form)
        self.denoise_path_label.setObjectName(u"denoise_path_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.denoise_path_label.sizePolicy().hasHeightForWidth())
        self.denoise_path_label.setSizePolicy(sizePolicy1)
        self.denoise_path_label.setMaximumSize(QSize(90, 16777215))

        self.denoise_path_layout.addWidget(self.denoise_path_label)

        self.denoise_path_lineedit = QLineEdit(Form)
        self.denoise_path_lineedit.setObjectName(u"denoise_path_lineedit")

        self.denoise_path_layout.addWidget(self.denoise_path_lineedit)


        self.verticalLayout.addLayout(self.denoise_path_layout)

        self.options_layout = QHBoxLayout()
        self.options_layout.setObjectName(u"options_layout")
        self.name_prefix_label = QLabel(Form)
        self.name_prefix_label.setObjectName(u"name_prefix_label")
        sizePolicy1.setHeightForWidth(self.name_prefix_label.sizePolicy().hasHeightForWidth())
        self.name_prefix_label.setSizePolicy(sizePolicy1)
        self.name_prefix_label.setMaximumSize(QSize(90, 16777215))

        self.options_layout.addWidget(self.name_prefix_label)

        self.name_prefix_lineedit = QLineEdit(Form)
        self.name_prefix_lineedit.setObjectName(u"name_prefix_lineedit")

        self.options_layout.addWidget(self.name_prefix_lineedit)

        self.name_prefix_spacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.options_layout.addItem(self.name_prefix_spacer)

        self.strength_label = QLabel(Form)
        self.strength_label.setObjectName(u"strength_label")

        self.options_layout.addWidget(self.strength_label)

        self.strength_combobox = QComboBox(Form)
        self.strength_combobox.setObjectName(u"strength_combobox")
        self.strength_combobox.setMinimumSize(QSize(70, 0))
        self.strength_combobox.setMaximumSize(QSize(16777215, 16777215))
        self.strength_combobox.setEditable(True)

        self.options_layout.addWidget(self.strength_combobox)

        self.strength_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.options_layout.addItem(self.strength_spacer)


        self.verticalLayout.addLayout(self.options_layout)

        self.target_layout = QHBoxLayout()
        self.target_layout.setObjectName(u"target_layout")
        self.target_label = QLabel(Form)
        self.target_label.setObjectName(u"target_label")
        sizePolicy1.setHeightForWidth(self.target_label.sizePolicy().hasHeightForWidth())
        self.target_label.setSizePolicy(sizePolicy1)
        self.target_label.setMaximumSize(QSize(90, 16777215))

        self.target_layout.addWidget(self.target_label)

        self.primary_checkbox = QCheckBox(Form)
        self.primary_checkbox.setObjectName(u"primary_checkbox")

        self.target_layout.addWidget(self.primary_checkbox)

        self.ml_checkbox = QCheckBox(Form)
        self.ml_checkbox.setObjectName(u"ml_checkbox")

        self.target_layout.addWidget(self.ml_checkbox)

        self.lpe_checkbox = QCheckBox(Form)
        self.lpe_checkbox.setObjectName(u"lpe_checkbox")

        self.target_layout.addWidget(self.lpe_checkbox)

        self.target_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.target_layout.addItem(self.target_spacer)

        self.deadline_checkbox = QCheckBox(Form)
        self.deadline_checkbox.setObjectName(u"deadline_checkbox")

        self.target_layout.addWidget(self.deadline_checkbox)


        self.verticalLayout.addLayout(self.target_layout)

        self.frame_layout = QHBoxLayout()
        self.frame_layout.setObjectName(u"frame_layout")
        self.fixed_label = QLabel(Form)
        self.fixed_label.setObjectName(u"fixed_label")
        sizePolicy1.setHeightForWidth(self.fixed_label.sizePolicy().hasHeightForWidth())
        self.fixed_label.setSizePolicy(sizePolicy1)
        self.fixed_label.setMaximumSize(QSize(90, 16777215))

        self.frame_layout.addWidget(self.fixed_label)

        self.start_label = QLabel(Form)
        self.start_label.setObjectName(u"start_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.start_label.sizePolicy().hasHeightForWidth())
        self.start_label.setSizePolicy(sizePolicy2)
        self.start_label.setMaximumSize(QSize(16777215, 16777215))

        self.frame_layout.addWidget(self.start_label)

        self.start_lineedit = QLineEdit(Form)
        self.start_lineedit.setObjectName(u"start_lineedit")
        self.start_lineedit.setMaximumSize(QSize(60, 16777215))

        self.frame_layout.addWidget(self.start_lineedit)

        self.end_label = QLabel(Form)
        self.end_label.setObjectName(u"end_label")
        sizePolicy2.setHeightForWidth(self.end_label.sizePolicy().hasHeightForWidth())
        self.end_label.setSizePolicy(sizePolicy2)
        self.end_label.setMaximumSize(QSize(16777215, 16777215))

        self.frame_layout.addWidget(self.end_label)

        self.end_lineedit = QLineEdit(Form)
        self.end_lineedit.setObjectName(u"end_lineedit")
        self.end_lineedit.setMaximumSize(QSize(60, 16777215))

        self.frame_layout.addWidget(self.end_lineedit)

        self.frame_checkbox = QCheckBox(Form)
        self.frame_checkbox.setObjectName(u"frame_checkbox")

        self.frame_layout.addWidget(self.frame_checkbox)

        self.frame_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.frame_layout.addItem(self.frame_spacer)


        self.verticalLayout.addLayout(self.frame_layout)

        self.setting_layout = QVBoxLayout()
        self.setting_layout.setObjectName(u"setting_layout")

        self.verticalLayout.addLayout(self.setting_layout)

        self.button_layout = QHBoxLayout()
        self.button_layout.setObjectName(u"button_layout")
        self.local_button = QPushButton(Form)
        self.local_button.setObjectName(u"local_button")

        self.button_layout.addWidget(self.local_button)

        self.stop_button = QPushButton(Form)
        self.stop_button.setObjectName(u"stop_button")

        self.button_layout.addWidget(self.stop_button)

        self.fram_button = QPushButton(Form)
        self.fram_button.setObjectName(u"fram_button")

        self.button_layout.addWidget(self.fram_button)


        self.verticalLayout.addLayout(self.button_layout)

        self.local_progressbar = QProgressBar(Form)
        self.local_progressbar.setObjectName(u"local_progressbar")
        self.local_progressbar.setValue(24)

        self.verticalLayout.addWidget(self.local_progressbar)


        self.horizontalLayout_5.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"[WW] Renderman for Katana Denoiser", None))
        self.denoise_path_label.setText(QCoreApplication.translate("Form", u"Denoise Path", None))
        self.name_prefix_label.setText(QCoreApplication.translate("Form", u"Name Prefix", None))
        self.strength_label.setText(QCoreApplication.translate("Form", u"Strength", None))
        self.target_label.setText(QCoreApplication.translate("Form", u"Target", None))
        self.primary_checkbox.setText(QCoreApplication.translate("Form", u"Primary", None))
        self.ml_checkbox.setText(QCoreApplication.translate("Form", u"ML", None))
        self.lpe_checkbox.setText(QCoreApplication.translate("Form", u"LPE", None))
        self.deadline_checkbox.setText(QCoreApplication.translate("Form", u"Deadline", None))
        self.fixed_label.setText(QCoreApplication.translate("Form", u"Fixed Frame", None))
        self.start_label.setText(QCoreApplication.translate("Form", u"Start", None))
        self.start_lineedit.setText("")
        self.end_label.setText(QCoreApplication.translate("Form", u"End", None))
        self.frame_checkbox.setText("")
        self.local_button.setText(QCoreApplication.translate("Form", u"Local Denoise", None))
        self.stop_button.setText(QCoreApplication.translate("Form", u"Local Stop", None))
        self.fram_button.setText(QCoreApplication.translate("Form", u"Farm Denoise", None))
    # retranslateUi

