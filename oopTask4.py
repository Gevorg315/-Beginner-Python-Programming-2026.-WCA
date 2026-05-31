class HistoryDict:
    def __init__(self, dic, dict_len=5):
        self.dict = dic
        self.len = dict_len
        self.changed_keys = []

    def set_value(self, new_key, new_value):
        self.dict[new_key] = new_value
        self.changed_keys.append(new_key)
        if len(self.changed_keys) > self.len:
            self.changed_keys.pop(0)

    def get_history(self):
        return self.changed_keys


one = HistoryDict({"foo": 42})
one.set_value("bar", 43)

if __name__ == "__main__":
    assert one.get_history() == ['bar']
