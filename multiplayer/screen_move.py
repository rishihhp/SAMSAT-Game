import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from attacker import AttackerWindow
from defender import DefenderWindow
from cybercity import Cybercity
from next import NextRound

class MainWindow(QMainWindow):
    def __init__(self, x, y, grid, title, counter, cybercity, main_instance):
        super().__init__()
        self.main_instance = main_instance
        self.setGeometry(x, y, 1458, 1119)
        self.setWindowTitle(title)
        self.active = True
        self.counter = counter
        self.title = title
        self.cybercity = cybercity
        self.grid = grid
        self.budget = {"defender": 50000, "attacker": 50000}
        self.round_counter = 0
        self.time_num = 0
        
        self.protection_actions = {
            "Firewall": {"effect": 0.30, "probability": 0.7},
            "Virus Protection": {"effect": 0.15, "probability": 0.8},
            "Intrusion Detection System": {"effect": 0.25, "probability": 0.9},
            "User Training": {"effect": 0.20, "probability": 1.0},
            "Turn Off Lights": {"effect": 0, "probability": 1.0}
        }  
        self.hacking_actions = {
            "Phishing": {"effect": 0.35, "probability": 0.7},
            "Virus": {"effect": 0.25, "probability": 0.8},
            "Malware": {"effect": 0.20, "probability": 0.9},
            "Skip Turn": {"effect": 0, "probability": 1.0}
        }
        for district in self.cybercity.districts.keys():
            if district not in self.protection_actions:
                self.protection_actions[district] = {"effect": 0, "probability": 1.0}
            if district not in self.hacking_actions:
                self.hacking_actions[district] = {"effect": 0, "probability": 1.0}
        self.attack_window = AttackerWindow(self)
        self.defend_window = DefenderWindow(self)
        self.end = self.counter.get_num_rounds()
        if self.end >= 10:
            output_text = self.centralWidget().findChild(QTextEdit, 'output_text')
            if output_text is None:
                # Create QTextEdit widget if not found
                output_text = QTextEdit()
                output_text.setObjectName('output_text')
                self.centralWidget().layout.addWidget(output_text)

            output_text.append("\n--- End of Game ---")
            return
        if self.title == "attacker":
            self.attack_window.update_image()
            self.setCentralWidget(self.attack_window)

        else:
            self.defend_window.create_widgets()
            self.setCentralWidget(self.defend_window)

    def set_attack(self):
        self.attack_window = AttackerWindow(self)
        self.attack_window.create_widgets()
        self.setCentralWidget(self.attack_window)

    def set_defend(self):
        self.defend_window = DefenderWindow(self)
        self.defend_window.create_widgets()
        self.setCentralWidget(self.defend_window)

    def set_defimage(self):
        self.defend_window = DefenderWindow(self)
        self.defend_window.update_image()
        self.setCentralWidget(self.defend_window)

    def set_atimage(self):
        self.attack_window = AttackerWindow(self)
        self.attack_window.update_image()
        self.setCentralWidget(self.attack_window)
        
    def round_switch(self):
        self.counter.next_round()
        num = self.counter.get_num_rounds()
        print(num)
        if num >= 10:
            output_text = self.centralWidget().findChild(QTextEdit, 'output_text')
            if output_text is None:
                # Create QTextEdit widget if not found
                output_text = QTextEdit()
                output_text.setObjectName('output_text')
                self.centralWidget().layout.addWidget(output_text)

            output_text.append("\n--- End of Game ---")
            return

        self.switch_central_widget(num)
        if hasattr(self, 'defender_window'):
            self.defender_window.defender_budget_label.setText(str(self.budget["defender"]))
        if hasattr(self, 'attacker_window'):
            self.attacker_window.attacker_budget_label.setText(str(self.budget["attacker"]))

        output_text = self.centralWidget().findChild(QTextEdit, 'output_text')
        if output_text is None:
            # Create QTextEdit widget if not found
            output_text = QTextEdit()
            output_text.setObjectName('output_text')
            self.centralWidget().layout.addWidget(output_text)

        if output_text.toPlainText() == "--- Game Started ---":
            output_text.append(f"\n--- Round {self.round_counter} ---")
        else:
            output_text.append("\nAfter turn:")
            output_text.append(self.cybercity.status())
    def switch_central_widget(self, num):

        if num%2 == 0 and self.title == "attacker":
            self.main_instance.render_content(self.title)
        elif  num%2 == 0 and self.title == "defender":
            self.main_instance.render_image(self.title)

        elif num%2 != 0 and self.title =="defender":
            self.main_instance.render_content(self.title)
        elif num%2!=0 and self.title == "attacker":
            self.main_instance.render_image(self.title)

class Main():
    def __init__(self) :
        super().__init__()
        counter = NextRound()
        cybercity = Cybercity()
        num_rows = 10
        num_cols = 10
        self.attacker = MainWindow(50, 50, num_rows, "attacker", counter, cybercity, self)
        self.attacker.show()
        self.defender = MainWindow(700, 50, num_cols, "defender", counter, cybercity, self)
        self.defender.show()

    def render_image(self, title):
        if title == "attacker":
            self.attacker.attack_window.update_image()
            self.attacker.setCentralWidget(self.attacker.attack_window)
            self.defender.set_defend()

        if title == "defender":
            self.defender.set_defimage()
            self.attacker.set_attack()

    def render_content(self, title):
        if title == "attacker":
            self.attacker.attack_window.create_widgets()
            self.attacker.setCentralWidget(self.attacker.attack_window)
            self.defender.set_defimage()
        if title == "defender":     
            print("attacker image") 
            self.attacker.set_atimage()     
            self.defender.set_defend()    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Main()
    sys.exit(app.exec_())
