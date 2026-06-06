class PriceControl:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not 0 <= value <= 100:
            raise ValueError("Price must be between 0 and 100.")
        instance.__dict__[self.name] = value


class NameControl:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if self.name in instance.__dict__:
            raise ValueError(f"{self.name.capitalize()} can not be changed.")
        instance.__dict__[self.name] = value


class Book:
    price = PriceControl()
    author = NameControl()
    name = NameControl()

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price


b = Book("William Faulkner", "The Sound and the Fury", 12)

if __name__ == "__main__":
    assert b.price == 12
    assert b.author == "William Faulkner"

    assert b.name == "The Sound and the Fury"