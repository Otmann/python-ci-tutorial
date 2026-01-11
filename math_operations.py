def add(a, b):
    """Addiert zwei Zahlen."""
    return a + b

def subtract(a, b):
    """Subtrahiert zwei Zahlen."""
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
	raise ValueError("Cannot divide by zero")
    return a / b
    

# Neuer Kommentar, um Workflow auszulösen
