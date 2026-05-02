class Calculator:
    """
    A simple calculator class for performing arithmetic operations on two numbers.
    
    Attributes:
        a (int/float): First number
        b (int/float): Second number
    """
    
    def __init__(self, a, b):
        """
        Initialize the Calculator with two numbers.
        
        Args:
            a (int/float): First number
            b (int/float): Second number
        """
        self.a = a
        self.b = b
    
    def add(self):
        """
        Add the two numbers.
        
        Returns:
            int/float: Sum of a and b
        """
        return self.a + self.b
    
    def subtract(self):
        """
        Subtract b from a.
        
        Returns:
            int/float: Difference of a and b
        """
        return self.a - self.b
    
    def multiply(self):
        """
        Multiply the two numbers.
        
        Returns:
            int/float: Product of a and b
        """
        return self.a * self.b
    
    def divide(self):
        """
        Divide a by b.
        
        Returns:
            int/float: Quotient of a divided by b
            str: Error message if b is zero
        """
        # Check for division by zero
        if self.b == 0:
            return "Error: Cannot divide by zero"
        return self.a / self.b


# Main execution block
if __name__ == "__main__":
    # Create a Calculator instance with sample values (10 and 5)
    calc = Calculator(10, 5)
    
    # Test all arithmetic operations
    print("Add:", calc.add())
    print("Subtract:", calc.subtract())
    print("Multiply:", calc.multiply())
    print("Divide:", calc.divide())
