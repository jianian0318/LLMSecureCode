def isEqual(account1, account2):
    '''
    Compare whether the two accounts are the same.
    '''
    if account1.username == account2.username and account1.password == account2.password:
        return True
    else:
        return False
