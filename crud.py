"""Crud File"""

from model import db, User, Reservations, connect_to_db
from datetime import date, time, datetime 


""""User Functions""""

def create_user(fname, lname, user_name, email, password):
    user = User(fname=fname, lname=lname, user_name=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_email(email):
    user = User.query.filter_by(user_name=username).first()
    
    return user

def get_user_by_username(user_name:
    user = User.query.filter(user_name=username).first()
    
    return user

"""Reservation Functions"""

def make_reservation(user, date, time):
    reservation = Reservations(user=user, reserve_date=date, reserve_time=time)
    db.session.add(reservation)
    db.session.commit()

    return reservation


def all_reservations_by_email(email):
    user = get_user_by_email(email)

    return Reservation.query.filter(Reservation.user==user).all()

if __name__=='__main__':
    from server import app
    connect_to_db(app)