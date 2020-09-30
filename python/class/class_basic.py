class Person(object):
    """
    Person class
    Args:
        name (string)
        Age (int)
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def birthday(self):
        self.age += 1