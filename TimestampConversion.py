import sys
import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton,QComboBox,QMessageBox
from PyQt5.QtCore import Qt, QDateTime

class TimestampConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Timestamp Converter")
        self.layout = QVBoxLayout()



        self.optionlabel = QLabel("option:")
        self.layout.addWidget( self.optionlabel)
 

        self.combo_box = QComboBox()
        self.combo_box.addItem("Timestamp seconds:")
        self.combo_box.addItem("Timestamp milliseconds:")
        self.combo_box.addItem("Remaining time seconds:")
        self.combo_box.addItem("Remaining time milliseconds:")
        self.combo_box.currentIndexChanged.connect(self.on_combobox_changed)
        self.layout.addWidget( self.combo_box)
        self.selectIndex = 0;

        self.timestamp_label = QLabel("Timestamp seconds:")
        self.layout.addWidget(self.timestamp_label)
        
        self.timestamp_input = QLineEdit()
        self.layout.addWidget(self.timestamp_input)
        
        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert_timestamp)
        self.layout.addWidget(self.convert_button)
        
        self.datetime_label = QLabel("Timestamp seconds:")
        self.layout.addWidget(self.datetime_label)
        
        self.datetime_output = QLabel()
        self.layout.addWidget(self.datetime_output)


        self.setLayout(self.layout)
    
    def on_combobox_changed(self):
        self.selectIndex = self.combo_box.currentIndex();
        text = self.combo_box.currentText();
        self.timestamp_label.setText(text);
        self.datetime_label.setText(text);

    
    def convert_remaining_time(self,remaining_time,is_msce):
        if is_msce:
            remaining_time = remaining_time//1000;

        remaining_time = datetime.timedelta(seconds=remaining_time)
        hours = remaining_time.seconds // 3600
        minutes = (remaining_time.seconds % 3600) // 60
        seconds = remaining_time.seconds % 60
        return hours, minutes, seconds

    def convert_timestamp(self):
        try:
            timestamp = int(self.timestamp_input.text())
        except:
            QMessageBox.information(self, "error", "erroneous data !!!");
            return;
        if  self.selectIndex  == 0:
            datetime_obj = QDateTime.fromSecsSinceEpoch(timestamp)
            formatted_datetime = datetime_obj.toString(Qt.ISODate)
            self.datetime_output.setText(formatted_datetime)
        elif  self.selectIndex  == 1:
            datetime_obj = QDateTime.fromMSecsSinceEpoch(timestamp)
            formatted_datetime = datetime_obj.toString(Qt.ISODate)
            self.datetime_output.setText(formatted_datetime)
        elif self.selectIndex == 2:
           hours, minutes, seconds =  self.convert_remaining_time(timestamp,False)
           timestr=str(hours) + ":" +str(minutes) + ":"+str(seconds)
           self.datetime_output.setText(timestr)
        elif self.selectIndex == 3:    
           hours, minutes, seconds =  self.convert_remaining_time(timestamp,True)
           timestr=str(hours) + ":" +str(minutes) + ":"+str(seconds) 
           self.datetime_output.setText(timestr)
            
        
     

if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = TimestampConverter()
    converter.show()
    sys.exit(app.exec_())