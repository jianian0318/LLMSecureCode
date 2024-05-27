def validate_password(actual_pw, typed_pw):
    '''
    Compare the actual password with the typed_pw by checking whether every character matches in constant time.
    '''
    if len(actual_pw) != len(typed_pw):
        return False

    result = 0

    for x, y in zip(actual_pw, typed_pw):
        result |= ord(x) ^ ord(y)

    return result == 0