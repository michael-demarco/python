class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        total_cents = self.cents + deposit_cents
        if total_cents > 99:
            carry_over = total_cents // 100
            remainder = total_cents % 100
            self.dollars += deposit_dollars + carry_over
            self.cents += remainder - 1
        else:
            self.dollars += deposit_dollars
            self.cents += deposit_cents
        return self.dollars, self.cents
