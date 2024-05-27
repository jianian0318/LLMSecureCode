import base64
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from werkzeug.security import check_password_hash

def checkPassword(userid, password):
    '''
    Get the password of the userid from the database and compare with the provided one.
    '''

    db_string = "mysql://root:password@localhost/mydatabase"
    db = create_engine(db_string)

    # Creating a session to interact with the database
    Session = sessionmaker(bind=db)
    session = Session()

    # Selecting the password hash of the userid from the database
    user = session.query(User).filter_by(id=userid).first()

    # Retrieving the hashed password from the database
    if user is None:
        return False
    else:
        db_password_hash = user.password

    # Closing the database session
    session.close()

    # Comparing the hashed password with the provided one using werkzeug's check_password_hash function
    return check_password_hash(db_password_hash, password)