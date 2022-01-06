"""Models for melon reservations"""

from flask_sqlaclhemy import SQLAlchmy

db = SQLAlchemy()

class User(db.Model):
    """Create a user object for each user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(25))
    lname = db.Column(db.String(25), nullable=True)
    user_name = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

    def check_password(self, input_password):
        return check_password(self.password, input_password)

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email} user_name={self.user_name}>"


class Reservation(db.Modle):
    """Create Reservations for Users"""

    __tablename__ = "reservation"

    res_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    reserve_date = db.Column(db.Date)
    reserve_time = db.Column(db.Time)

    user = db.relationship("User", backref="reservation")

    def __repr__(self):
        return f"<res_id={self.res_id} user={self.user_id} reserve_date={self.reserve_date}>"


def connect_to_db(flask_app, db_uri='postgresql:///reservations', echo=False):    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    connect_to_db(app)