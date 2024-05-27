import os


def invalidUsername(username):
    # Check if username is valid
    if len(username) < 1 or len(username) > 32:
        return True
    if username.startswith('-'):
        return True
    if username.startswith('_'):
        return True
    if username.startswith('.'):
        return True
    if username.startswith('..'):
        return True
    if username.startswith('/'):
        return True
    if username.startswith('\\'):
        return True
    if username.startswith('~'):
        return True
    if username.startswith('$'):
        return True
    if username.startswith('#'):
        return True
    if username.startswith('@'):
        return True
    if username.startswith('%'):
        return True
    if username.startswith('^'):
        return True
    if username.startswith('&'):
        return True
    if username.startswith('*'):
        return True
    if username.startswith('('):
        return True
    if username.startswith(')'):
        return True
    if username.startswith('{'):
        return True
    if username.startswith('}'):
        return True
    if username.startswith('['):
        return True
    if username.startswith(']'):
        return True
    if username.startswith('|'):
        return True
    if username.startswith(':'):
        return True
    if username.startswith(';'):
        return True
    if username.startswith('"'):
        return True
    if username.startswith("'"):
        return True
    if username.startswith('`'):
        return True
    if username.startswith('='):
        return True
    if username.startswith('?'):
        return True
    if username.startswith('!'):
        return True
    if username.startswith('<'):
        return True
    if username.startswith('>'):
        return True
    if username.startswith(','):
        return True
    if username.startswith('.'):
        return True
    if username.startswith(' '):
        return True
    if username.startswith('\t'):
        return True
    if username.startswith('\n'):
        return True
    if username.startswith('\r'):
        return True
    if username.startswith('\f'):
        return True
    if username.startswith('\v'):
        return True
    if username.startswith('\\'):
        return True
    if username.startswith('/'):
        return True
    if username.startswith('%'):
        return True
    if username.startswith('$'):
        return True
    if username.startswith('#'):
        return True
    if username.startswith('@'):
        return True
    if username.startswith('&'):
        return True
    if username.startswith('*'):
        return True
    if username.startswith('('):
        return True
    if username.startswith(')'):
        return True
    if username.startswith('{'):
        return True
    if username.startswith('}'):
        return True
    if username.startswith('['):
        return True
    if username.startswith(']'):
        return True
    if username.startswith('|'):
        return True
    if username.startswith(':'):
        return True
    if username.startswith(';'):
        return True
    if username.startswith('"'):
        return True
    if username.startswith("'"):
        return True
    if username.startswith('`'):
        return True
    if username.startswith('='):
        return True
    if username.startswith('?'):
        return True
    if username.startswith('!'):
        return True
    if username.startswith('<'):
        return True
    if username.startswith('>'):
        return True
    if username.startswith(','):
        return True
    if username.startswith('.'):
        return True
    if username.startswith(' '):
        return True
    if username.startswith('\t'):
        return True
    if username.startswith('\n'):
        return True
    if username.startswith('\r'):
        return True
    else: return False


def raisePrivileges():
    # Temporarily raise the program's privileges
    pass


def lowerPrivileges():
    # Lower the program's privileges
    pass


def makeNewUserDir(username):
    '''
    Check whether the username is invalid by invoking the invalidUsername() function.
    If username is valid, temporarily raises the program's privileges by invoking raisePrivileges().
    Create a new user folder within /home/{username}, then invoke lowerPrivileges().
    Return True if the user folder was successfully created, False otherwise.
    '''
    if invalidUsername(username):
        return False

    raisePrivileges()

    try:
        os.mkdir(f"/home/{username}")
        return True
    except:
        return False
    finally:
        lowerPrivileges()