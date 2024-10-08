import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt 
from Algos import BubbleSort, InsertionSort, SelectionSort, MergeSort, QuickSort, CountingSort, RadixSort, BucketSort
import csv
import pandas as pd
import time

data_list=[]
df=pd.read_csv("Data.csv")
data_list=df.values.tolist()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('ScrapSort (Mini Project)')
        self.setGeometry(320,100,1200,800)
        
        central_widget=QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout=QVBoxLayout(central_widget)
        central_widget.setStyleSheet("""
                                    QWidget {
                                    background-color: #4A6274;  
                                    border: 1px solid #333;      
                                    border-radius: 10px;         
                                     }
                                    """)
        
        self.Main_Label=QLabel("ScrapSort (Mini Project)")
        self.Main_Label.setStyleSheet("font-size:32px;"
                                      "color:#F9DDD2;"
                                      "font-weight:bold;"
                                      "padding-left:400;"
                                      "padding-top:20;"
                                      "padding-bottom:20;"
                                      )
                                      
        main_layout.addWidget(self.Main_Label)
        
        
        
        #create a table to display data
        self.table=QTableWidget()
        self.table.setRowCount(len(data_list))
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['Price','Discount','Rating', 'Sold', 'Product Name'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        main_layout.addWidget(self.table)
        self.load_table()  
        
        
        self.table.setStyleSheet("""
                                    QTableWidget{
                                        font-size:16 px;
                                        border:1 px solid brown;
                                        background-color:#F9DDD2;
                                    }
                                    QHeaderView::section{
                                        background-color: #F9DDD2;
                                        padding: 12 px;
                                        font-size: 20 px;
                                        font-family: Arial, Helvetica, sans-serif;
                                        width:20 px;
                                        border: 1 px solid black;
                                    }
                                    QTableWidget QTableCornerButton::section {
                                       background-color: #404040;
                                       border: 1 px solid black;
                                    }
                              
                                """)
        
        self.ResetButton=QPushButton("Reset Table")
        self.ResetButton.clicked.connect(self.reset)
        self.ResetButton.setFixedSize(150,50)
        self.ResetButton.setStyleSheet("""
                            QPushButton{
                              font-size: 18px;  
                              background-color:#F9DDD2;
                              border-radius:8px; 
                              color:#4A6274;  
                              padding:10px; 
                              margin:5px;
                                        }
                            QPushButton:hover{
                             background-color:#4A6274;
                             color:#F9DDD2;;
                             }
            """)
        main_layout.addWidget(self.ResetButton,alignment=Qt.AlignRight)
        
        
        self.time_Label=QLabel("Time Taken to Sort: not sorted")
        self.time_Label.setStyleSheet("font-size:18px;"
                                      "color:#F9DDD2;"
                                      "font-weight:bold;"
                                      "padding-left:10;"
                                      "padding-top:10;"
                                      "padding-bottom:10")
        
        main_layout.addWidget(self.time_Label)  
        
        
        # Enter Column Name here:
        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter column name to sort according to...")
        self.input.setStyleSheet("""
                                    QLineEdit{
                                        font-size:16px;
                                        color:#F9DDD2;
                                        padding:10px;
                                        width:50%;
                                        }
                                        QLineEdit::placeholder{
                                        color:#4A6274;}""")
        
        main_layout.addWidget(self.input)
        

        # Sorting ALgorithms eight button
        buttons=QHBoxLayout()
        self.SortingButton(buttons,"Bubble Sort",self.bubbleSort)
        self.SortingButton(buttons,"Selection Sort",self.selection_sort)
        self.SortingButton(buttons,"Insertion Sort",self.insertion_sort)
        self.SortingButton(buttons,"Merge Sort",self.Merge_sort)
        self.SortingButton(buttons,"Quick Sort ",self.Quick_sort)
        self.SortingButton(buttons,"Counting Sort",self.counting_sort)
        self.SortingButton(buttons,"Radix Sort",self.radix_sort)
        self.SortingButton(buttons,"Bucket Sort",self.bucket_sort)
        main_layout.addLayout(buttons)

        
     

    def SortingButton(self,layout,name,func):
        button=QPushButton(name)
        button.clicked.connect(func)
        button.setStyleSheet("""
                             QPushButton{
                              font-size: 18px;  
                              background-color:#F9DDD2;
                              border-radius:8px; 
                              color:#4A6274;  
                              padding:10px; 
                              margin:5px;
                             }
                             QPushButton:hover{
                             background-color:#4A6274;
                             color:#F9DDD2;
                             }
        """)
        layout.addWidget(button)
    
    
    def load_table(self):
        for row_index,row_data in enumerate(data_list):
            for col_index,item in enumerate(row_data):
                self.table.setItem(row_index,col_index,QTableWidgetItem(str(item)))
                
       
       
    # When bubble Button clicks ,bubble Sorting Apply
    def bubbleSort(self):
        column_Name=self.input.text().strip()
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        elif not column_Name:
            QMessageBox.warning(self, "Input Error", "Please Enter a column name")
            return
        else:
            QMessageBox.warning(self, "Input Error", "Invalid Column Name Entered, Please Enter a valid one")
            return
        start_time = time.time()
        BubbleSort(data_list,column_index)
        end_time=time.time()
        self.load_table()
        self.time_Label.setText(f"Time Taken to Sort: {end_time-start_time}")
        
                 
    def insertion_sort(self):
        column_Name=self.input.text().strip()
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        elif not column_Name:
            QMessageBox.warning(self, "Input Error", "Please Enter a column name")
            return
        else:
            QMessageBox.warning(self, "Input Error", "Invalid Column Name Entered, Please Enter a valid one")
            return
        start_time = time.time()
        InsertionSort(data_list,column_index)
        end_time=time.time()
        self.load_table()
        self.time_Label.setText(f"Time Taken to Sort: {end_time-start_time}")

    # When selection Button clicks ,selection Sorting Apply
    def selection_sort(self):
        column_Name=self.input.text().strip()
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        elif not column_Name:
            QMessageBox.warning(self, "Input Error", "Please Enter a column name")
            return
        else:
            QMessageBox.warning(self, "Input Error", "Invalid Column Name Entered, Please Enter a valid one")
            return
        start_time = time.time()
        SelectionSort(data_list,column_index)
        end_time=time.time()
        self.load_table()
        self.time_Label.setText(f"Time Taken to Sort: {end_time-start_time}")

    def Merge_sort(self):
        column_Name=self.input.text().strip()
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        elif not column_Name:
            QMessageBox.warning(self, "Input Error", "Please Enter a column name")
            return
        else:
            QMessageBox.warning(self, "Input Error", "Invalid Column Name Entered, Please Enter a valid one")
            return
        start_time = time.time()
        MergeSort(data_list,column_index)
        end_time=time.time()
        self.load_table()
        self.time_Label.setText(f"Time Taken to Sort: {end_time-start_time}")

    def Quick_sort(self):
        global data_list
        column_Name=self.input.text().strip()
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        elif not column_Name:
            QMessageBox.warning(self, "Input Error", "Please Enter a column name")
            return
        else:
            QMessageBox.warning(self, "Input Error", "Invalid Column Name Entered, Please Enter a valid one")
            return
        start_time = time.time()
        data_list=QuickSort(data_list,column_index)
        end_time=time.time()
        self.load_table()
        self.time_Label.setText(f"Time Taken to Sort: {end_time-start_time}")

    def counting_sort(self):
        column_Name=self.input.text().strip()
        if column_Name=="Product Name" or column_Name=="Image URL":
            QMessageBox.warning(self, "Input Error", f"Counting sort is not applicable for {column_Name} column")
            return
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        elif not column_Name:
            QMessageBox.warning(self, "Input Error", "Please Enter a column name")
            return
        else:
            QMessageBox.warning(self, "Input Error", "Invalid Column Name Entered, Please Enter a valid one")
            return
        start_time = time.time()
        CountingSort(data_list,column_index)
        end_time=time.time()
        self.load_table()
        self.time_Label.setText(f"Time Taken to Sort: {end_time-start_time}")

    def radix_sort(self):
        column_Name=self.input.text().strip()
        if column_Name=="Product Name" or column_Name=="Image URL":
            QMessageBox.warning(self, "Input Error", f"Radix sort is not applicable for {column_Name} column")
            return
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        else:
            self.time_Label.setText("Invalid Column Name Entered, Please Enter a valid one")
            return
        start_time = time.time()
        RadixSort(data_list,column_index)
        end_time=time.time()
        self.load_table()
        self.time_Label.setText(f"Time Taken to Sort: {end_time-start_time}")

    def bucket_sort(self):
        global data_list
        column_Name=self.input.text().strip()
        if column_Name=="Product Name" or column_Name=="Image URL":
            QMessageBox.warning(self, "Input Error", f"Bucket Sort is not applicable for {column_Name} column")
            return
        column_index=-1
        header_Labels=[self.table.horizontalHeaderItem(i).text().strip() for i in range(self.table.columnCount())]
        if column_Name in header_Labels:
            column_index=header_Labels.index(column_Name)
        else:
            self.time_Label.setText("Invalid Column Name Entered, Please Enter a valid one")
            return
        start_time = time.time()
        data_list=BucketSort(data_list,column_index)
        end_time=time.time()
        self.load_table()
        self.time_Label.setText(f"Time Taken to Sort: {end_time-start_time}")
    
    def reset(self):
        global data_list
        df=pd.read_csv("Data.csv")
        data_list=df.values.tolist()
        self.load_table()
        self.time_Label.setText("Time Taken to Sort: not sorted")
        self.time_Label.setStyleSheet("font-size:18px;"
                                      "color:#F9DDD2;"
                                      "font-weight:bold;"
                                      "padding-left:10;"
                                      "padding-top:10;"
                                      "padding-bottom:10")

    
        
def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()