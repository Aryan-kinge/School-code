"""
n = [1, 2, 3, 4]
print(list(map(lambda x: x**2, n)))
"""

"""
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number[9])
"""

"""
class Human:
    # Creates a class variable - this is a variable across all humans rather than inside each object of the Human class
    population = 0

    def __init__(self):
        # __init__ runs when the object of the class is made. Since population is a class variable, we must use Human. before it to access it.
        Human.population += 1

person = Human()
print(str(Human.population))
"""

