def validate_password(actual_pw, typed_pw):
    '''
    Compare the actual password with the typed_pw by checking whether every character matches.
    '''
    if len(actual_pw) != len(typed_pw):
        return False
    
    result = 0
    for a, b in zip(actual_pw, typed_pw):
        result |= ord(a) ^ ord(b)
    return result == 0