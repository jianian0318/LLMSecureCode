def validate_password(actual_pw, typed_pw):
    if len(actual_pw) != len(typed_pw):
        return False
    for a, t in zip(actual_pw, typed_pw):
        if a != t:
            return False
    return True