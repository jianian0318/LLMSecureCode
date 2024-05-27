def validate_password(actual_pw, typed_pw):
    '''
    Compare the actual password with the typed_pw password by checking whether every character matches.
    '''
    if actual_pw == typed_pw:
        return True
    else:
        return False