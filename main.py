from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QComboBox, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QFont
from googletrans import Translator
from languages import *

#
class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.settings()
        self.initUI()
        self.button_events()


    def initUI(self):
        self.input_box = QTextEdit()
        self.output_box = QTextEdit()
        self.reverse = QPushButton("Reverse")
        self.reset = QPushButton("Reset")
        self.submit = QPushButton("Translate Now")
        self.input_option = QComboBox()
        self.output_option = QComboBox()
        self.title = QLabel("Translate")

        self.input_option.addItems(values)
        self.output_option.addItems(values)


        self.master = QHBoxLayout()
        col1 = QVBoxLayout()
        col2 = QVBoxLayout()

        col1.addWidget(self.title)
        col1.addWidget(self.input_option)
        col1.addWidget(self.output_option)
        col1.addWidget(self.submit)
        col1.addWidget(self.reset)

        col2.addWidget(self.input_box)
        col2.addWidget(self.reverse)
        col2.addWidget(self.output_box)

        self.master.addLayout(col1, 20)
        self.master.addLayout(col2, 80)
        self.setLayout(self.master)



    def settings(self):
        self.setWindowTitle("Ac's Pocket Translator")
        self.setGeometry(400, 250, 700, 500)

    def button_events(self):
        self.submit.clicked.connect(self.translate_click)
        self.reverse.clicked.connect(self.rev_click)
        self.reset.clicked.connect(self.reset_app)

    def translate_click(self):
        try:
            value_to_key1 = self.output_option.currentText()
            value_to_key2 = self.input_option.currentText()
            key_to_value1 = [k for k, v in LANGUAGES.items() if v == value_to_key1]

            key_to_value2 = [k for k, v in LANGUAGES.items() if v == value_to_key2]
            self.script = self.translate_text(self.input_box.toPlainText(), key_to_value1[0], key_to_value2[0])
            self.output_box.setText(self.script)
        except Exception as e:
            print("Exception:", e)
            self.input_box.setText("You must enter text to translate here...")

    def reset_app(self):
        self.input_box.clear()
        self.output_box.clear()

    def translate_text(self, text, dest_lang, src_lang):
        speaker = Translator()
        translation = speaker.translate(text, dest=dest_lang, src=src_lang)
        return translation.text

    def rev_click(self):
        s1, l1 = self.input_box.toPlainText(), self.input_option.currentText()
        s2, l2 = self.output_box.toPlainText(), self.output_option.currentText()

        self.input_box.setText(s2)
        self.output_box.setText(s1)
        self.input_option.setCurrentText(l2)
        self.output_option.setCurrentText(l1)

if __name__ in "__main__":
    app = QApplication([])
    main = Main()
    main.show()
    app.exec_()

