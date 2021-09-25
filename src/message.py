
class Message:
    def __init__():
        super().__init__()

    def errorMessage(self, message):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setText("Error")
        self.msg.setInformativeText(message)
        self.msg.setWindowTitle("Error")
        self.msg.exec_()