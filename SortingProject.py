import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Algos import BubbleSort 
import csv
import pandas as pd

# data_list=[]
# df=pd.read_csv("data1.csv")
# data_list=df.values.tolist()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('ScrapSort (Mini Project)')
        self.setGeometry(450,200,1100,700)
        
        central_widget=QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout=QVBoxLayout(central_widget)
        
        self.time_Label=QLabel("Sorting Time: not sorted yet")
        self.time_Label.setStyleSheet("font-size:20px;"
                                      "color:gray;"
                                      "font-weight:bold;"
                                      "padding-left:200;"
                                      "padding-top:20;")
                                      
        main_layout.addWidget(self.time_Label)
        
        
        
        # array=[0,3,7,3,2,1,4,5]
        # start=0
        # end=len(array)
        
        #Button Functions
        # self.BubbleSort.clicked.connect(self.BubbleSort(array,start, end))
        # self.SelectionSort.clicked.connect(self.SelectionSort(array,start, end))
        # self.InsertionSort.clicked.connect(self.InsertionSort(array,start, end))
        # self.MergeSort.clicked.connect(self.MergeSort(array,start, end))
        # self.QuickSort.clicked.connect(self.QuickSort(array,start, end))
        # self.CountingSort.clicked.connect(self.CountingSort(array,start, end))
        # self.RadixSort.clicked.connect(self.RadixSort(array,start, end))
        # self.BucketSort.clicked.connect(self.BucketSort(array,start, end))
        # self.ResetButton.clicked.connect(self.ResetTable(array,start, end))
    
    
    
def load_table(self):
    with open('student.csv', "r",encoding="utf-8") as fileInput:
        roww = 0
        data = list(csv.reader(fileInput))
            
        self.ScrappingTable.setRowCount(len(data))
        for row in data:
            self.ScrappingTable.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row[0])))
            self.ScrappingTable.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row[1])))
            self.ScrappingTable.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row[2])))
            self.ScrappingTable.setItem(roww, 3 , QtWidgets.QTableWidgetItem((row[3])))
            self.ScrappingTable.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row[4])))
            roww =+ 1
        
def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()