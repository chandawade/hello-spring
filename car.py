class Car:

    def __init__(self, gas):
        self.gas_level = gas
        
    def add_gas(gas):
        self.gas_level += gas
        
    def fill_up(self):
        if self.gas_level < 13:
            return 13 - self.gas_level
        else:
            return 0
