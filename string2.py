def get_longest_word(s: str) -> str | None:
    if s != "":
        return max(s.split(), key=len)
    return None


if __name__ == "__main__":
    assert get_longest_word("dhfjhdf dhfgfdh dhfgjdgfjudihfci") == "dhfgjdgfjudihfci"
    assert get_longest_word("") is None
