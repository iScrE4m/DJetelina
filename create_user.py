from getpass import getpass
import sys

from app import app
from models import User, db

def main():
    """Main entry point for script."""
    with app.app_context():
        db.metadata.create_all(db.engine)
        if User.query.all():
            print('A user already exists! Create another? (y/n):')
            create = input()
            if create == 'n':
                return

        print('Enter email address: ')
        email = input()
        password = getpass()
        assert password == getpass('Password (again):')

        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        print('User added.')



if __name__ == '__main__':
    sys.exit(main())