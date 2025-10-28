# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting_form.ui'
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
        Form.resize(994, 218)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_16 = QFrame(Form)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setMinimumSize(QSize(0, 200))
        self.frame_16.setMaximumSize(QSize(16777215, 16777215))
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.groupBox = QGroupBox(self.frame_16)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setMinimumSize(QSize(0, 175))
        self.groupBox.setMaximumSize(QSize(16777215, 175))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 0, 9, 0)
        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.farmLB_4 = QLabel(self.frame_5)
        self.farmLB_4.setObjectName(u"farmLB_4")
        sizePolicy1.setHeightForWidth(self.farmLB_4.sizePolicy().hasHeightForWidth())
        self.farmLB_4.setSizePolicy(sizePolicy1)
        self.farmLB_4.setMinimumSize(QSize(100, 25))
        self.farmLB_4.setMaximumSize(QSize(16777215, 25))
        font = QFont()
        font.setFamily(u"Open Sans")
        font.setPointSize(9)
        self.farmLB_4.setFont(font)
        self.farmLB_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.farmLB_4)

        self.pool_comboBox = QComboBox(self.frame_5)
        self.pool_comboBox.setObjectName(u"pool_comboBox")
        self.pool_comboBox.setMinimumSize(QSize(125, 25))
        self.pool_comboBox.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_10.addWidget(self.pool_comboBox)


        self.horizontalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_21 = QLabel(self.frame_6)
        self.label_21.setObjectName(u"label_21")
        sizePolicy1.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy1)
        self.label_21.setMinimumSize(QSize(100, 25))
        self.label_21.setMaximumSize(QSize(16777215, 25))
        self.label_21.setFont(font)
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.label_21)

        self.secondary_pool_comboBox = QComboBox(self.frame_6)
        self.secondary_pool_comboBox.setObjectName(u"secondary_pool_comboBox")
        sizePolicy1.setHeightForWidth(self.secondary_pool_comboBox.sizePolicy().hasHeightForWidth())
        self.secondary_pool_comboBox.setSizePolicy(sizePolicy1)
        self.secondary_pool_comboBox.setMinimumSize(QSize(125, 25))
        self.secondary_pool_comboBox.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_13.addWidget(self.secondary_pool_comboBox)


        self.horizontalLayout.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_22 = QLabel(self.frame_7)
        self.label_22.setObjectName(u"label_22")
        sizePolicy1.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy1)
        self.label_22.setMinimumSize(QSize(100, 25))
        self.label_22.setMaximumSize(QSize(16777215, 25))
        self.label_22.setFont(font)
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.label_22)

        self.group_comboBox = QComboBox(self.frame_7)
        self.group_comboBox.setObjectName(u"group_comboBox")
        self.group_comboBox.setMinimumSize(QSize(125, 25))
        self.group_comboBox.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_14.addWidget(self.group_comboBox)


        self.horizontalLayout.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_28 = QLabel(self.frame_9)
        self.label_28.setObjectName(u"label_28")
        sizePolicy1.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy1)
        self.label_28.setMinimumSize(QSize(100, 25))
        self.label_28.setMaximumSize(QSize(16777215, 25))
        self.label_28.setFont(font)
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_28)

        self.priority_lineEdit = QLineEdit(self.frame_9)
        self.priority_lineEdit.setObjectName(u"priority_lineEdit")
        self.priority_lineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.priority_lineEdit.sizePolicy().hasHeightForWidth())
        self.priority_lineEdit.setSizePolicy(sizePolicy1)
        self.priority_lineEdit.setMinimumSize(QSize(125, 25))
        self.priority_lineEdit.setMaximumSize(QSize(16777215, 25))
        self.priority_lineEdit.setFont(font)
        self.priority_lineEdit.setLayoutDirection(Qt.LeftToRight)
        self.priority_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.priority_lineEdit)


        self.horizontalLayout_3.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy2)
        self.frame_10.setMinimumSize(QSize(0, 0))
        self.frame_10.setMaximumSize(QSize(16777215, 16777215))
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_25 = QLabel(self.frame_10)
        self.label_25.setObjectName(u"label_25")
        sizePolicy1.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy1)
        self.label_25.setMinimumSize(QSize(100, 25))
        self.label_25.setMaximumSize(QSize(16777215, 25))
        self.label_25.setFont(font)
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_25)

        self.frame_per_task_lineEdit = QLineEdit(self.frame_10)
        self.frame_per_task_lineEdit.setObjectName(u"frame_per_task_lineEdit")
        self.frame_per_task_lineEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_per_task_lineEdit.sizePolicy().hasHeightForWidth())
        self.frame_per_task_lineEdit.setSizePolicy(sizePolicy1)
        self.frame_per_task_lineEdit.setMinimumSize(QSize(125, 25))
        self.frame_per_task_lineEdit.setMaximumSize(QSize(16777215, 25))
        self.frame_per_task_lineEdit.setFont(font)
        self.frame_per_task_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.frame_per_task_lineEdit)


        self.horizontalLayout_3.addWidget(self.frame_10)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy2.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy2)
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setMaximumSize(QSize(16777215, 16777215))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_23 = QLabel(self.frame_8)
        self.label_23.setObjectName(u"label_23")
        sizePolicy1.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy1)
        self.label_23.setMinimumSize(QSize(100, 25))
        self.label_23.setMaximumSize(QSize(16777215, 25))
        self.label_23.setFont(font)
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.label_23)

        self.machine_limit_lineEdit = QLineEdit(self.frame_8)
        self.machine_limit_lineEdit.setObjectName(u"machine_limit_lineEdit")
        sizePolicy1.setHeightForWidth(self.machine_limit_lineEdit.sizePolicy().hasHeightForWidth())
        self.machine_limit_lineEdit.setSizePolicy(sizePolicy1)
        self.machine_limit_lineEdit.setMinimumSize(QSize(125, 25))
        self.machine_limit_lineEdit.setMaximumSize(QSize(16777215, 25))
        self.machine_limit_lineEdit.setFont(font)
        self.machine_limit_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.machine_limit_lineEdit)


        self.horizontalLayout_3.addWidget(self.frame_8)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_14 = QFrame(self.groupBox)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.frame_13 = QFrame(self.frame_14)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.delayed_checkBox = QCheckBox(self.frame_13)
        self.delayed_checkBox.setObjectName(u"delayed_checkBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.delayed_checkBox.sizePolicy().hasHeightForWidth())
        self.delayed_checkBox.setSizePolicy(sizePolicy3)
        self.delayed_checkBox.setMinimumSize(QSize(100, 25))
        self.delayed_checkBox.setMaximumSize(QSize(120, 25))

        self.horizontalLayout_8.addWidget(self.delayed_checkBox)

        self.delayed_dateTimeEdit = QDateTimeEdit(self.frame_13)
        self.delayed_dateTimeEdit.setObjectName(u"delayed_dateTimeEdit")
        self.delayed_dateTimeEdit.setCalendarPopup(True)

        self.horizontalLayout_8.addWidget(self.delayed_dateTimeEdit)


        self.horizontalLayout_9.addWidget(self.frame_13)


        self.verticalLayout.addWidget(self.frame_14)


        self.horizontalLayout_17.addWidget(self.groupBox)

        self.frame_15 = QFrame(self.frame_16)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(225, 0))
        self.frame_15.setMaximumSize(QSize(225, 16777215))
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 27, 9, 27)
        self.label_27 = QLabel(self.frame_15)
        self.label_27.setObjectName(u"label_27")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(15)
        sizePolicy4.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy4)
        self.label_27.setMinimumSize(QSize(110, 15))
        self.label_27.setScaledContents(False)
        self.label_27.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_27.setIndent(-1)

        self.verticalLayout_2.addWidget(self.label_27)

        self.memo_textEdit = QTextEdit(self.frame_15)
        self.memo_textEdit.setObjectName(u"memo_textEdit")

        self.verticalLayout_2.addWidget(self.memo_textEdit)


        self.horizontalLayout_17.addWidget(self.frame_15)


        self.verticalLayout_3.addWidget(self.frame_16)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Job Settings", None))
        self.farmLB_4.setText(QCoreApplication.translate("Form", u"Pool", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Secondary Pool", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Group", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"Prioriry", None))
        self.priority_lineEdit.setText(QCoreApplication.translate("Form", u"100", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"Frame Per Task", None))
        self.frame_per_task_lineEdit.setText(QCoreApplication.translate("Form", u"1", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Machine Limit", None))
        self.machine_limit_lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.delayed_checkBox.setText(QCoreApplication.translate("Form", u"Delayed Job", None))
        self.delayed_dateTimeEdit.setDisplayFormat(QCoreApplication.translate("Form", u"yy. M. d  h:mm", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"memo", None))
    # retranslateUi

