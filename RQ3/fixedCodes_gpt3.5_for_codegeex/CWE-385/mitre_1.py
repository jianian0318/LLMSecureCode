import time

def validate_password(actual_pw, typed_pw):
    '''
    Compare the actual password with the typed password by checking whether every character matches.
    Utilize time.sleep to introduce a delay to mitigate timing attacks.
    '''
    if len(actual_pw) != len(typed_pw):
        time.sleep(0.5)
        return False
    
    for i in range(len(actual_pw)):
        if actual_pw[i] != typed_pw[i]:
            time.sleep(0.5)
            return False
    
    return True