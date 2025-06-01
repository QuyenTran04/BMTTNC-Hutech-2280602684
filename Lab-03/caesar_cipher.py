import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        key_input = self.ui.key.toPlainText()
        if not key_input.strip().isdigit():
            self.show_message("⚠ Vui lòng nhập một số hợp lệ trong ô Key!")
            return

        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.plainText.toPlainText(),
            "key": key_input
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.cipherText.setPlainText(data["encrypted_message"])
                self.show_message("Encrypted Successfully")
            else:
                self.show_message("Encryption failed.")
        except requests.exceptions.RequestException as e:
            self.show_message(f"API Error: {e}")

    def call_api_decrypt(self):
        key_input = self.ui.key.toPlainText()
        if not key_input.strip().isdigit():
            self.show_message("⚠ Vui lòng nhập một số hợp lệ trong ô Key!")
            return

        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.cipherText.toPlainText(),
            "key": key_input
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plainText.setPlainText(data["decrypted_message"])
                self.show_message("Decrypted Successfully")
            else:
                self.show_message("Decryption failed.")
        except requests.exceptions.RequestException as e:
            self.show_message(f"API Error: {e}")

    def show_message(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.setWindowTitle("Notification")
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.setWindowTitle("Caesar Cipher Tool")
    window.show()
    sys.exit(app.exec_())