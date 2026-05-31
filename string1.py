def get_fractions(a_b: str, c_b: str) -> str | bool | None:
    s_c = "/"
    result = None
    if a_b != "" and c_b != "" and len(a_b) >= 3 and len(c_b) >= 3:
        if any(c in s_c for c in a_b) and any(c in s_c for c in c_b):
            a_b = a_b.split('/')
            a_n, a_d = a_b[0], a_b[1]
            c_b = c_b.split('/')
            c_n, c_d = c_b[0], c_b[1]
            if a_n.isdigit() and a_d.isdigit() and c_n.isdigit() and c_d.isdigit() and \
                    a_n != "" and a_d != "" and c_n != "" and c_d != "" and a_d == c_d:
                n_sum = int(c_n) + int(a_n)
                result = f'{n_sum}/{a_d}'
                return result
            return False
        return False
    return result

# def get_fractions(a_b: str, c_b: str) -> str | bool:
#     # Basic validation
#     if not a_b or not c_b:
#         return False
#
#     if '/' not in a_b or '/' not in c_b:
#         return False
#
#     try:
#         a_n, a_d = a_b.split('/')
#         c_n, c_d = c_b.split('/')
#     except ValueError:
#         # Handles cases like "1/2/3"
#         return False
#
#     # Check all parts are digits
#     if not (a_n.isdigit() and a_d.isdigit() and c_n.isdigit() and c_d.isdigit()):
#         return False
#
#     # Denominators must match
#     if a_d != c_d:
#         return False

#    # Perform addition
#    n_sum = int(a_n) + int(c_n)
#    return f"{n_sum}/{a_d}"


print(get_fractions('1/3', '5/3') == '6/3')
if __name__ == "__main__":
    assert get_fractions('1/3', '5/3') == '6/3'
    assert not get_fractions('1/7', '5/3')
    assert not get_fractions('133', '5/3')
    assert not get_fractions('1/g', '5/3')
    assert not get_fractions('1/', '5/3')
    assert not get_fractions('1/', '5/')
