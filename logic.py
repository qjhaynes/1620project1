from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    """
    A class that defines what happens when the graphical user interface is interacted with.
    """
    def __init__(self) -> None:
        """
        Method to initialize  the Logic class.
        """
        super().__init__()
        self.setupUi(self)

        self.button_submit.clicked.connect(lambda: self.submit())

    def submit(self) -> None:
        """
        Method for deciding what the submit button does based on the menu the gui has open.
        """
        if self.label_menu.text() == 'VOTE MENU':
            self.vote()
        else:
            self.cast_vote()

    def vote(self) -> None:
        """
        Method to decide whether the menu will change to the voting ballot or exit to show the results of the vote.
        """
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

    def cast_vote(self) -> None:
        """
        Method to decide which candidate to vote for. It then records this vote in a text file.
        """
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

    def display_results(self) -> None:
        """
        Method to read the results from the text file generated, then display them in the gui.
        """
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
