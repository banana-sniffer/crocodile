import entity

class Fruit(entity.Entity):

    def __init__(self):
        super().__init__()
        self.symbol = "F"
        self.x = 0
        self.y = 0
        self.sight = 0
        self.move_status = False
        self.health = 1
        self.stamina = 1000
        self.planted = False
        self.ripeness = 0
        self.dropped = False

    def __repr__(self):
        ret_value = "Name: {}\nPosition: {}\nStatus: {}\nRipeness: {}\nSymbol: {}\n".format(self.name, [self.x, self.y], self.status, self.ripeness, self.symbol)
        return ret_value

    def __str__(self):
        ret_value = "Name: {}\nPosition: {}\nStatus: {}\nRipeness: {}\nSymbol: {}\n".format(self.name, [self.x, self.y], self.status, self.ripeness, self.symbol)
        return ret_value

    def action(self, world):
        if self.dropped:
            pass
        else:
            self.ripeness += 1

    def grow(self):
        self.ripeness += 1

    def drop(self):
        self.dropped = True

    def health_check(self):
        if self.ripeness > 9:
            self.status == "D"
        return self.status
