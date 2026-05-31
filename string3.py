def replacer(s: str) -> str | None:
    if s != "":
        conversion_table = str.maketrans({'"': "'", "'": '"'})
        result = s.translate(conversion_table)
        return result
    return None


if __name__ == "__main__":
    assert replacer("'test' it or test \"this\"") == '"test" it or test \'this\''
    assert replacer("") is None

