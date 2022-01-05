"""Crud File"""

from model import db, User, Reservations, connect_to_db
from datetime import date, time, datetime 


""""User Functions""""

def create_user(fname, lname, user_name, email, password):
    """Create new user"""

    user = User(fname=fname, lname=lname, user_name=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_email(email):
    """Get user by email"""

    user = User.query.filter_by(user_name=username).first()
    
    return user

def get_user_by_username(user_name):
    """Return user by username"""

    user = User.query.filter(user_name=username).first()
    
    return user

def get_all_users():
    """Return all users"""

    users = User.query.all()

    return users

"""Reservation Functions"""

def make_reservation(user, date, time):
    """Create a reservation"""

    reservation = Reservation(user=user, reserve_date=date, reserve_time=time)
    db.session.add(reservation)
    db.session.commit()

    return reservation


def all_reservations_by_email(email):
    """Return all reservations by email"""

    user = get_user_by_email(email)

    return Reservation.query.filter(Reservation.user==user).all()


def get_all_user_reservations(user):
    """ Return all reservations by user"""

    reservation = Reservation.query.filter_by(user=user).all()

    return reservation

if __name__=='__main__':
    from server import app
    connect_to_db(app)