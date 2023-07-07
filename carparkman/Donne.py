import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QTimer
import sqlite3


class ParkingLotUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.parking_status = []
        self.initUI()

    def initUI(self):
        # Set window title
        self.setWindowTitle('Parking Lot Occupancy')

        # Create grid layout
        grid = QGridLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(grid)

        # Set central widget
        self.setCentralWidget(self.central_widget)

        # Start timer to update parking status every 1 second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_parking_status)
        self.timer.start(1000)  # 1000 milliseconds = 1 second

    def update_parking_status(self):
        # Connect to the SQLite database
        conn = sqlite3.connect(
            r"C:\Users\hp\Desktop\Projects\CarParkMan\parking_status.db")

        # Execute query to retrieve parking status
        cursor = conn.execute('SELECT status FROM parking_status')
        rows = cursor.fetchall()
        new_parking_status = [row[0] for row in rows]

        # Close the database connection
        conn.close()

        # Check if parking status has changed
        if self.parking_status != new_parking_status:
            self.parking_status = new_parking_status

            # Clear existing labels
            while self.central_widget.layout().count():
                item = self.central_widget.layout().takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

            # Add labels for each parking space
            for i, status in enumerate(self.parking_status):
                label = QLabel()
                if status:
                    label.setStyleSheet("background-color: green;")
                    label.setText("P" + str(i+1) + ": Vacant")
                else:
                    label.setStyleSheet("background-color: red;")
                    label.setText("P" + str(i+1) + ": Occupied")
                self.central_widget.layout().addWidget(label, i // 4, i % 4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    parking_lot_ui = ParkingLotUI()
    parking_lot_ui.show()
    sys.exit(app.exec_())
