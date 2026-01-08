from functions import *

def test_add_two_numbers():
# Assemble
    a = 2
    b = 3
    expected = 5
# Act
    actual = add_two_numbers(a,b)
# Assert
    assert expected == actual

def test_minus_two_numbers():
# Assemble
    a = 3
    b = 3
    expected = 0
# Act
    actual = minus_two_numbers(a,b)
# Assert
    assert expected == actual

# def add_mix_two_numbers(a,b):
#     return add_two_numbers(a, b) + mix_two_numbers(a, b)

def test_add_mix_two_numbers():
# Assemble
    a = 2
    b = 3
    expected = 13
# Act
    actual = add_mix_two_numbers(a,b)
# Assert
    assert expected == actual


def test_math_operation():

# Assemble
    a = 6
    b = 15
    result = 10 
    test = "minus"
    expected = 1

# Act
    actual = math_operation(a, b, result, test)

# Assert
    assert actual == expected


test_add_two_numbers()
test_add_mix_two_numbers()
test_math_operation()
