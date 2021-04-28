from database import db
from sqlalchemy.exc import SQLAlchemyError

# Seeds Users table with default values
def seedUsers():
    import dotenv
    from werkzeug.security import generate_password_hash

    from database import Users

    # Load environment variables from .env file
    config = dotenv.dotenv_values(".env")

    username = 'Admin'
    password = config['ADMIN_SECRET']

    # Seeding and escaping if seed fails
    try:
        admin = Users(username='Admin', hash=generate_password_hash(password))
        db.session.add(admin)
        db.session.commit()
    except SQLAlchemyError as e:
        print('SQL error: ', e)
        pass

# Creates DB
def createDB():
    db.create_all()
    seedUsers()

if __name__ ==  "__main__":
    import sys

    if len(sys.argv) > 1:
        execution = sys.argv[1]

        if execution == 'create':
            createDB()
        elif execution == 'seed':
            seedUsers()