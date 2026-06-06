class Bird:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} bird can walk and fly"

    def fly(self):
        return f"{self.name} bird can fly"

    def walk(self):
        return f"{self.name} bird can walk"


class FlyingBird(Bird):
    def __init__(self, name, ration="grains"):
        self.ration = ration
        super().__init__(name)

    def eat(self):
        return f"It eats mostly {self.ration}"


class NonFlyingBird:
    def __init__(self, name, ration="fish"):
        self.name = name
        self.ration = ration

    def __str__(self):
        return f"{self.name} bird can walk and swim"

    def walk(self):
        return f"{self.name} bird can walk"

    def eat(self):
        return f"It eats mostly {self.ration}"

    def swim(self):
        return f"{self.name} bird can swim"


class SuperBird(NonFlyingBird, FlyingBird):
    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"


b = Bird("Any")
p = NonFlyingBird("Penguin", "fish")
c = FlyingBird("Canary")
s = SuperBird("Gull")

if __name__ == "__main__":
    assert b.walk() == "Any bird can walk"
    assert p.swim() == "Penguin bird can swim"
    assert p.eat() == "It eats mostly fish"
    assert str(c) == "Canary bird can walk and fly"

    assert c.eat() == "It eats mostly grains"
    assert str(s) == "Gull bird can walk, swim and fly"
    assert s.eat() == "It eats mostly fish"