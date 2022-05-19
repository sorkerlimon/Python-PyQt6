# from PyQt6.QtWidgets import QApplication,QWidget
# import sys
#
# app = QApplication(sys.argv)
#
# window = QWidget()
# window.setWindowTitle("Sorker Limon")
# window.show()
#
# app.exec()


##### Button created


# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         button = QPushButton("Press Me!")
#         button.setCheckable(True)
#         button.clicked.connect(self.the_button_was_clicked)
#         button.clicked.connect(self.the_button_was_toggled)
#
#         self.setCentralWidget(button)
#
#     def the_button_was_clicked(self):
#         print("Clicked!")
#
#     def the_button_was_toggled(self, checked):
#         print(checked)
#
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()




######## disable the button


# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         self.button = QPushButton("Press Me!")
#         self.button.clicked.connect(self.the_button_was_clicked)
#
#         self.setCentralWidget(self.button)
#
#     def the_button_was_clicked(self):
#         self.button.setText("You already clicked me.")
#         self.button.setEnabled(False)
#         self.setWindowTitle("My Oneshot App")
#
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()

######################## Lima Project
# import numpy as np
# import matplotlib.pyplot as plt
# import json
# import pandas as pd
# from pandas import json_normalize
# import os
#
# from PyQt6.QtWidgets import (QWidget, QPushButton, QLineEdit,
#         QInputDialog, QApplication)
# import sys
#
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#
#     def initUI(self):
#
#         self.btn = QPushButton('Ok', self)
#         self.btn.move(180, 220)
#         self.btn.clicked.connect(self.showDialog)
#
#         self.le = QLineEdit(self)
#         self.le.move(150, 150)
#
#
#
#         self.setGeometry(500, 500, 500, 500)
#         self.setWindowTitle('Log Analysis System Path')
#         self.show()
#
#
#     def showDialog(self):
#
#         text, ok = QInputDialog.getText(self, 'Path Input',
#                                         'Enter your Data Fle Path:')
#
#         if ok:
#             self.le.setText(str(text))
#
#         if text:
#
#             path = open(os.path.expanduser(text))
#
#             # data = pd.read_csv("C:/Users/21100002/Desktop/sammiha.csv")
#             # data = pd.read_csv(text)
#             data = pd.read_csv(path)
#             # print(data)
#
#             column = data.columns
#             # print(column)
#
#             vmcapacity = data["Latency/vmcapacity"].sum()
#             print("Totall vmcapacity : ", vmcapacity)
#
#             processedrequests = data["Latency/processedrequests"].sum()
#             print("Totall processedrequests : ", processedrequests)
#
#             totalrentalcost = data["Latency/totalrentalcost"].sum()
#             print("Totall totalrentalcost : ", totalrentalcost)
#
#             arrivalnewconnections = data["Latency/arrivalnewconnections"].sum()
#             print("Totall arrivalnewconnections : ", arrivalnewconnections)
#
#             fig, axs = plt.subplots(2, 2)
#             fig.suptitle('Log Analysis ')
#
#             axs[0][0].plot(data["Latency/vmcapacity"])
#             axs[0, 0].set_title('Vm Capacity')
#
#             axs[0][1].plot(data["Latency/processedrequests"])
#             axs[0, 1].plot(data["Latency/processedrequests"], 'tab:orange')
#             axs[0, 1].set_title('Processed Requests')
#
#             axs[1][0].plot(data["Latency/totalrentalcost"])
#             axs[1, 0].plot(data["Latency/totalrentalcost"], 'tab:green')
#             axs[1, 0].set_title('Totalrental Cost')
#
#             axs[1][1].plot(data["Latency/arrivalnewconnections"])
#             axs[1, 1].plot(data["Latency/arrivalnewconnections"], 'tab:red')
#             axs[1, 1].set_title('Arrival New Connections')
#
#             plt.show()
#
#             print(path)
#
#
# def main():
#
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec())
#
#     obj = Example()
#     filepath = obj.showDialog()
#     print(filepath)
#
#
#
# if __name__ == '__main__':
#     main()
#



######## Button chnages code
######## Button chnages code
from PyQt6.QtWidgets import QApplication,QMainWindow,QPushButton
import sys
from random import choice

# window_titles = [
#     'My App',
#     'My software',
#     'My abrar',
#     'My tasnim',
#     'My nawshin',
#     'My rafi',
#     'My sorker',
#     'My sadia',
#     'My limon',
#     'Something went wrong',
# ]

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.n_times_clicked = 0
#         self.setWindowTitle("My Application")
#         self.button = QPushButton("Press Me!")
#         self.button.clicked.connect(self.the_button_was_clicked)
#         self.windowTitleChanged.connect(self.the_window_tittle_change)
#         self.setCentralWidget(self.button)
#
#     def the_button_was_clicked(self):
#         print("Clicked")
#         new_window_tittle = choice(window_titles)
#         self.setWindowTitle(new_window_tittle)
#
#
#     def the_window_tittle_change(self,window_tittle):
#         print("Window tittlechanged: %s "% window_tittle)
#
#         if window_tittle == "Something went wrong":
#             self.button.setDisabled(True)
#
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()



######### QLine edit and QVBoxLayout

# from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QLineEdit,QVBoxLayout,QWidget
# import sys
#
# class MainWindow(QMainWindow):
#      def __init__(self):
#          super().__init__()
#
#          self.setWindowTitle("My Applicatio")
#          self.label = QLabel()
#          self.input = QLineEdit()
#          self.input.textChanged.connect(self.label.setText)
#
#
#          layout = QVBoxLayout()
#          layout.addWidget(self.input)
#          layout.addWidget(self.label)
#
#
#          container = QWidget()
#          container.setLayout(layout)
#          self.setCentralWidget(container)
#
#
#
#
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec()













