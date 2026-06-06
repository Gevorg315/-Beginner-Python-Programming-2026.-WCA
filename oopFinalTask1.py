class Sun(object):
    instance = None

    @classmethod
    def inst(cls):
        if cls.instance is None:
            cls.instance = cls.__new__(cls)
        return cls.instance

p = Sun.inst()
f = Sun.inst()
if __name__ == "__main__":
    assert (p is f) is True