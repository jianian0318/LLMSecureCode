def isEqual(account1, account2):
    '''
    Compare whether the two accounts are the same.
    '''
    if account1.__dict__ == account2.__dict__:
        return True
    else:
        return False