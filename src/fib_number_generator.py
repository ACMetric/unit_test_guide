class FibNumberGenerator():
    """Class that returns increasing fibonacci numbers
    """    
    def __init__(self):
        self.previous = 0
        self.current = 1
        
    def get_next_number(self):
        next_number = self.previous + self.current
        self.previous, self.current = self.current, next_number
        return next_number
    