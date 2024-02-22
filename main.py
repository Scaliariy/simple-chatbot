import sys
import threading

from PyQt6.QtWidgets import QMainWindow, QTextEdit, QPushButton, QLineEdit, QApplication
from backend import Chatbot


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setMinimumSize(610, 400)

        # add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # add input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_massage)

        # add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_massage)

        self.show()

    def send_massage(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333'><b>Me:</b> {user_input}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(
            f"<p style='color:#333333; background-color:#E9E9E9'><b>Bot:</b> {response[0]} ({response[1]})</p>")


app = QApplication(sys.argv)
app.setStyleSheet('QMainWindow {background-color: darkgray;border: 1px solid black;}')
main_window = ChatbotWindow()
sys.exit(app.exec())
