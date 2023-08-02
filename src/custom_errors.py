class NegativeNumberException(Exception):
    """Exception raised when the input variable is negative.
    """    
    
    def __init__(self, num: int):
        self.num = num
        self.message = "Negative numbers are not allowed!"
        super().__init__(self.message)