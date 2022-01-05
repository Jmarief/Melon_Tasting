"""Seed Database - Drop db, Create bd"""

from faker import Faker

import os
import crud
import server
import model

from datetime import date, time

os.system('dropdb reservations')
os.system('createdb reservations')

model.connect_to_db(server.app)
model.db.create_all()

"""Create test-fake users"""

users_in_db = []
reservations_in_db = []
fake = Faker()

for i in range(5)
    fname = fake.fname()
    lname = fake.lname()
    user_name = fake.user_name()
    email = fake.email()
    password="9876"
    reserve_date = fake.date()
    reserve_time = fake.time()

    user = crud.create_user(fname, lname, user_name, email, password)
    users_in_db.append(user)

    reservation = crud.create_reservation(reserve_date, reserve_time, user)
    reservations_in_db.append(reservation)
