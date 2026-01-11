import math_operations

def test_add_positive_numbers():
    """Testet die Addition positiver Zahlen."""
    assert math_operations.add(5, 3) == 8

def test_add_negative_numbers():
    """Testet die Addition negativer Zahlen."""
    assert math_operations.add(-5, -3) == -8

def test_subtract():
    """Testet die Subtraktion."""
    assert math_operations.subtract(10, 4) == 6

def test_subtract_negative_result():
    """Testet Subtraktion mit negativem Ergebnis."""
    assert math_operations.subtract(1, 5) == -4

def test_multiply():
    assert math_operations.multiply(3,4) == 12
    assert math_operations.multiply(-2,5) == -10
    assert math_operations.multiply(0,9) == 0



def test_divide():
    """Testet Division."""
    assert math_operations.divide(10, 2) == 5
    with pytest.raises(ValueError):
	math_operations.divide(5,0)

# Ein absichtlich fehlschlagender Test zum Demonstrieren
# def test_failing_example():
#     assert math_operations.add(1, 1) == 3  # Dieser Test würde fehlschlagen
# Ein weiterer Testkommentar
# Kleine Änderung für 2. Push
