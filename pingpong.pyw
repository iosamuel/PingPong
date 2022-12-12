#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
from PyQt5 import QtGui, QtCore, QtWidgets

class PingPong(QtWidgets.QWidget):
	def __init__(self):
		QtWidgets.QWidget.__init__(self)

		self.setGeometry(300, 300, 300, 100)
		self.setWindowTitle("Ping Pong")
		self.setWindowIcon(QtGui.QIcon("PingPong.png"))

		layout = QtWidgets.QGridLayout()
		lbl = QtWidgets.QLabel("<b><i>Introduzca los datos para jugar</i></b>")
		lbl.setAlignment(QtCore.Qt.AlignHCenter)
		lbl1 = QtWidgets.QLabel("Jugador 1:")
		lbl1.setAlignment(QtCore.Qt.AlignHCenter)
		lbl2 = QtWidgets.QLabel("Jugador 2:")
		lbl2.setAlignment(QtCore.Qt.AlignHCenter)
		lbl3 = QtWidgets.QLabel("Puntos a ganar:")
		lbl3.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
		self.txtE1 = QtWidgets.QLineEdit()
		self.txtE2 = QtWidgets.QLineEdit()
		self.spinBox = QtWidgets.QSpinBox()
		self.spinBox.setMinimum(2)
		self.spinBox.setMaximum(100)
		self.spinBox.setValue(11)
		btn = QtWidgets.QPushButton("Aceptar")
		layout.addWidget(lbl, 0, 0, 1, 0)
		layout.addWidget(lbl1, 1, 0)
		layout.addWidget(lbl2, 1, 1)
		layout.addWidget(self.txtE1, 2, 0)
		layout.addWidget(self.txtE2, 2, 1)
		layout.addWidget(lbl3, 3, 0)
		layout.addWidget(self.spinBox, 3, 1)
		layout.addWidget(btn, 4, 1)

		self.setLayout(layout)

		btn.clicked.connect(self.accept)
	
	def accept(self):
		pl1, pl2 = (self.txtE1.text(), self.txtE2.text())
		pnt = self.spinBox.text()
		if len(pl1) <= 0:
			pl1 = "Jugador 1"
		if len(pl2) <= 0:
			pl2 = "Jugador 2"
		
		o = open(".pl", "w")
		o.write(pl1)
		o.write(":")
		o.write(pl2)
		o.write(":")
		o.write(pnt)
		o.close()

		self.hide()
		self.instructions()
	
	def instructions(self):
		with open(".pl") as o:
			pls = o.read()
		pl1 = pls.split(":")[0]
		pl2 = pls.split(":")[1]
		pnt = pls.split(":")[2]
		instr = "Las instrucciones son:<br><b>"+pl1+":</b><br><i>1.) Use las teclas 'W' y 'S' para moverse arriba y abajo.</i><br><br><b>"+pl2+":</b><br><i>1.) Use las teclas 'Flecha arriba' y 'Flecha abajo' para moverse arriba y abajo.</i><br><br>El primero que llegue a los <b>"+pnt+"</b> puntos gana.<br><br>Si desea salir del juego presione la tecla 'ESC'"
		mens = QtWidgets.QMessageBox.information(self, "Instrucciones - PONG",
				instr,
				QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
		
		import pong

app = QtWidgets.QApplication(sys.argv)
pp = PingPong()
pp.show()
sys.exit(app.exec_())