def checkAdminPassword(password):
    if password == getAdminPassword():
        return True
    else:
        return False

def getAdminPassword():
    return "admin123"