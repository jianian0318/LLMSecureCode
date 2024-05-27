import time

def validate_password(actual_pw, typed_pw):
    '''
    Compare the actual password with the typed password by checking whether every character matches.
    '''
    if len(actual_pw) != len(typed_pw):
        return False
    
    for char_actual, char_typed in zip(actual_pw, typed_pw):
        if char_actual != char_typed:
            return False
        time.sleep(0.1)  # Delay to add uniformity
    
    return True