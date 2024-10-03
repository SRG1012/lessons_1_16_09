import string
import keyword

def is_valid_variable_name(s):
    if s in keyword.kwlist:
        return False
    if s[0].isdigit():
        return False
    if any(c.isupper() for c in s):
        return False
    valid_chars = string.ascii_lowercase + string.digits + "_"
    if any(c not in valid_chars for c in s):
        return False
    if s.count('_') > 1:
        return False
    return True