class NextRound():
    def __init__(self):
        self.round_counter = 0
        self.toggle_screen = True


    def get_num_rounds(self):
        return self.round_counter

    def set_screen(self):
        self.toggle_screen = False

    def next_round(self):
        self.round_counter += 1
