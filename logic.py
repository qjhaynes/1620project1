from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_submit.clicked.connect(lambda: self.submit())

    def submit(self):
        if self.label_menu.text() == 'VOTE MENU':
            self.vote()
        elif self.label_menu.text() == 'CANDIDATE MENU':
            self.cast_vote()

    def vote(self):
        try:
            option = self.input_option.text().strip().lower()
            if option != 'v' and option != 'x':
                raise ValueError
        except ValueError:
            self.label_display.setText('Invalid (v/x)')
        else:
            if option == 'x':
                self.display_results()
            else:
                self.label_menu.setText('CANDIDATE MENU')
                self.label_option_1.setText('1: John')
                self.label_option_2.setText('2: Jane')
                self.label_input.setText('Candidate:')
                self.label_display.setText('')
        finally:
            self.input_option.clear()

    def cast_vote(self):
        try:
            candidate = int(self.input_option.text())
            if candidate != 1 and candidate != 2:
                raise ValueError
        except ValueError:
            self.label_display.setText('Invalid (1/2)')
        else:
            with open('votes.txt', 'a') as file:
                file.write(f'{candidate}\n')
            self.label_menu.setText('VOTE MENU')
            self.label_option_1.setText('v: Vote')
            self.label_option_2.setText('x: Exit')
            self.label_input.setText('Option:')
            if candidate == 1:
                self.label_display.setText('Voted John')
            else:
                self.label_display.setText('Voted Jane')
        finally:
            self.input_option.clear()

    def display_results(self):
        john_votes = 0
        jane_votes = 0
        total_votes = 0
        with open('votes.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if int(line) == 1:
                    john_votes += 1
                else:
                    jane_votes += 1
                total_votes += 1
        self.label_display.setText(f'John - {john_votes}, Jane - {jane_votes}, Total - {total_votes}')
        with open('votes.txt', 'w') as file:
            file.write('')
