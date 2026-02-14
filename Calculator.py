
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(200, 250)
        Form.setMinimumSize(QtCore.QSize(200, 250))
        Form.setMaximumSize(QtCore.QSize(200, 250))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.input1 = QtWidgets.QLineEdit(Form)
        self.input1.setObjectName("input1")
        self.verticalLayout.addWidget(self.input1)
        self.input2 = QtWidgets.QLineEdit(Form)
        self.input2.setObjectName("input2")
        self.verticalLayout.addWidget(self.input2)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plus = QtWidgets.QPushButton(Form)
        self.plus.setObjectName("plus")
        self.horizontalLayout.addWidget(self.plus)
        self.sub = QtWidgets.QPushButton(Form)
        self.sub.setObjectName("sub")
        self.horizontalLayout.addWidget(self.sub)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        self.output = QtWidgets.QLineEdit(Form)
        self.output.setObjectName("output")
        self.verticalLayout.addWidget(self.output)


        validator = QtGui.QDoubleValidator()
        validator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        self.input1.setValidator(validator)
        self.input2.setValidator(validator)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculator"))
        self.input1.setText(_translate("Form", "0"))
        self.input2.setText(_translate("Form", "0"))
        self.plus.setText(_translate("Form", "+"))
        self.sub.setText(_translate("Form", "-"))
        self.output.setPlaceholderText(_translate("Form", "output"))


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QWidget

    app = QApplication(sys.argv)
    window = QWidget()
    ui = Ui_Form()
    ui.setupUi(window)


    def plus_func():
        try:
            num1 = float(ui.input1.text())
            num2 = float(ui.input2.text())
            ui.output.setText(str(num1 + num2))
        except ValueError:
            ui.output.setText("Error")

    def sub_func():
        try:
            num1 = float(ui.input1.text())
            num2 = float(ui.input2.text())
            ui.output.setText(str(num1 - num2))
        except ValueError:
            ui.output.setText("Error")

    ui.plus.clicked.connect(plus_func)
    ui.sub.clicked.connect(sub_func)

    window.show()
    sys.exit(app.exec_())
