# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config_input.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(578, 550)
        Dialog.setMinimumSize(QtCore.QSize(400, 550))
        Dialog.setMaximumSize(QtCore.QSize(700, 600))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_nature_of_work = QtWidgets.QLabel(Dialog)
        self.label_nature_of_work.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_nature_of_work.setFont(font)
        self.label_nature_of_work.setObjectName("label_nature_of_work")
        self.horizontalLayout.addWidget(self.label_nature_of_work)
        self.lineEdit_nature_of_work = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(10)
        self.lineEdit_nature_of_work.setFont(font)
        self.lineEdit_nature_of_work.setObjectName("lineEdit_nature_of_work")
        self.horizontalLayout.addWidget(self.lineEdit_nature_of_work)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_state = QtWidgets.QLabel(Dialog)
        self.label_state.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_state.setFont(font)
        self.label_state.setObjectName("label_state")
        self.horizontalLayout_2.addWidget(self.label_state)
        self.lineEdit_state = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_state.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(10)
        self.lineEdit_state.setFont(font)
        self.lineEdit_state.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_state.setCursorPosition(0)
        self.lineEdit_state.setObjectName("lineEdit_state")
        self.horizontalLayout_2.addWidget(self.lineEdit_state)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_p_zak = QtWidgets.QLabel(Dialog)
        self.label_p_zak.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_p_zak.setFont(font)
        self.label_p_zak.setObjectName("label_p_zak")
        self.horizontalLayout_3.addWidget(self.label_p_zak)
        self.lineEdit_p_zak = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(10)
        self.lineEdit_p_zak.setFont(font)
        self.lineEdit_p_zak.setObjectName("lineEdit_p_zak")
        self.horizontalLayout_3.addWidget(self.lineEdit_p_zak)
        spacerItem3 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_z1 = QtWidgets.QLabel(Dialog)
        self.label_z1.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_z1.setFont(font)
        self.label_z1.setObjectName("label_z1")
        self.horizontalLayout_4.addWidget(self.label_z1)
        self.lineEdit_z1 = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(10)
        self.lineEdit_z1.setFont(font)
        self.lineEdit_z1.setObjectName("lineEdit_z1")
        self.horizontalLayout_4.addWidget(self.lineEdit_z1)
        spacerItem5 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem6 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_z2 = QtWidgets.QLabel(Dialog)
        self.label_z2.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_z2.setFont(font)
        self.label_z2.setObjectName("label_z2")
        self.horizontalLayout_5.addWidget(self.label_z2)
        self.lineEdit_z2 = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(10)
        self.lineEdit_z2.setFont(font)
        self.lineEdit_z2.setObjectName("lineEdit_z2")
        self.horizontalLayout_5.addWidget(self.lineEdit_z2)
        spacerItem7 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem8 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_z3 = QtWidgets.QLabel(Dialog)
        self.label_z3.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_z3.setFont(font)
        self.label_z3.setObjectName("label_z3")
        self.horizontalLayout_6.addWidget(self.label_z3)
        self.lineEdit_z3 = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(10)
        self.lineEdit_z3.setFont(font)
        self.lineEdit_z3.setObjectName("lineEdit_z3")
        self.horizontalLayout_6.addWidget(self.lineEdit_z3)
        spacerItem9 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem10 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_x = QtWidgets.QLabel(Dialog)
        self.label_x.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_x.setFont(font)
        self.label_x.setObjectName("label_x")
        self.horizontalLayout_7.addWidget(self.label_x)
        self.lineEdit_x = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(10)
        self.lineEdit_x.setFont(font)
        self.lineEdit_x.setObjectName("lineEdit_x")
        self.horizontalLayout_7.addWidget(self.lineEdit_x)
        spacerItem11 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        spacerItem12 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem12)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_y1 = QtWidgets.QLabel(Dialog)
        self.label_y1.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_y1.setFont(font)
        self.label_y1.setObjectName("label_y1")
        self.horizontalLayout_8.addWidget(self.label_y1)
        self.lineEdit_y1 = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(10)
        self.lineEdit_y1.setFont(font)
        self.lineEdit_y1.setObjectName("lineEdit_y1")
        self.horizontalLayout_8.addWidget(self.lineEdit_y1)
        spacerItem13 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem13)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        spacerItem14 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem14)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_y2 = QtWidgets.QLabel(Dialog)
        self.label_y2.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_y2.setFont(font)
        self.label_y2.setObjectName("label_y2")
        self.horizontalLayout_9.addWidget(self.label_y2)
        self.lineEdit_y2 = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(10)
        self.lineEdit_y2.setFont(font)
        self.lineEdit_y2.setObjectName("lineEdit_y2")
        self.horizontalLayout_9.addWidget(self.lineEdit_y2)
        spacerItem15 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem15)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        spacerItem16 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem16)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_y3_2 = QtWidgets.QLabel(Dialog)
        self.label_y3_2.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_y3_2.setFont(font)
        self.label_y3_2.setObjectName("label_y3_2")
        self.horizontalLayout_10.addWidget(self.label_y3_2)
        self.lineEdit_y3_2 = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(10)
        self.lineEdit_y3_2.setFont(font)
        self.lineEdit_y3_2.setObjectName("lineEdit_y3_2")
        self.horizontalLayout_10.addWidget(self.lineEdit_y3_2)
        spacerItem17 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem17)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem18 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem18)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Настройки пользователя"))
        self.label_nature_of_work.setText(_translate("Dialog", "Характер работы"))
        self.label_state.setText(_translate("Dialog", "Состояние"))
        self.label_p_zak.setText(_translate("Dialog", "P закачки"))
        self.label_z1.setText(_translate("Dialog", "z1"))
        self.label_z2.setText(_translate("Dialog", "z2"))
        self.label_z3.setText(_translate("Dialog", "z3"))
        self.label_x.setText(_translate("Dialog", "x"))
        self.label_y1.setText(_translate("Dialog", "y1"))
        self.label_y2.setText(_translate("Dialog", "y2"))
        self.label_y3_2.setText(_translate("Dialog", "y3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
