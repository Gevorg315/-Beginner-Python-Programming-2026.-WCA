class Field:
    __value = None
    def __init__(self):
        self.__value = None

    def get_value(self):
        return self.__value

    def set_value(self, __value):
        self.__value = __value
        return self.__value

c = Field()

if __name__ == "__main__":

    assert c.get_value() is None
    assert c.set_value(4) == 4