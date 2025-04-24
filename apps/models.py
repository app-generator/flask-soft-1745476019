# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

class CURRENCY_TYPE(Enum):
    usd = 'usd'
    eur = 'eur'

class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    name          = db.Column(db.String(128),  nullable=False)
    info          = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    currency      = db.Column(db.Enum(CURRENCY_TYPE), default=CURRENCY_TYPE.usd, nullable=False)

    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} / ${self.price}"

    @classmethod
    def find_by_id(cls, _id: int) -> "Product":
        return cls.query.filter_by(id=_id).first() 

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return


#__MODELS__
class Machines(db.Model):

    __tablename__ = 'Machines'

    id = db.Column(db.Integer, primary_key=True)

    #__Machines_FIELDS__
    machine = db.Column(db.Text, nullable=True)

    #__Machines_FIELDS__END

    def __init__(self, **kwargs):
        super(Machines, self).__init__(**kwargs)


class Users(db.Model):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)

    #__Users_FIELDS__
    username = db.Column(db.Text, nullable=True)
    pswrd = db.Column(db.Text, nullable=True)
    name = db.Column(db.Text, nullable=True)
    position = db.Column(db.Text, nullable=True)
    role = db.Column(db.Text, nullable=True)
    hiring_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    email = db.Column(db.Text, nullable=True)
    department = db.Column(db.Text, nullable=True)

    #__Users_FIELDS__END

    def __init__(self, **kwargs):
        super(Users, self).__init__(**kwargs)


class Employees(db.Model):

    __tablename__ = 'Employees'

    id = db.Column(db.Integer, primary_key=True)

    #__Employees_FIELDS__
    employee_id = db.Column(db.Integer, nullable=True)
    name = db.Column(db.Text, nullable=True)
    email = db.Column(db.Text, nullable=True)

    #__Employees_FIELDS__END

    def __init__(self, **kwargs):
        super(Employees, self).__init__(**kwargs)


class Problems(db.Model):

    __tablename__ = 'Problems'

    id = db.Column(db.Integer, primary_key=True)

    #__Problems_FIELDS__
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
    time = db.Column(db.Text, nullable=True)
    person = db.Column(db.Text, nullable=True)
    machine = db.Column(db.Text, nullable=True)
    problem_details = db.Column(db.Text, nullable=True)

    #__Problems_FIELDS__END

    def __init__(self, **kwargs):
        super(Problems, self).__init__(**kwargs)


class Shiftleaders(db.Model):

    __tablename__ = 'Shiftleaders'

    id = db.Column(db.Integer, primary_key=True)

    #__Shiftleaders_FIELDS__
    name = db.Column(db.Text, nullable=True)

    #__Shiftleaders_FIELDS__END

    def __init__(self, **kwargs):
        super(Shiftleaders, self).__init__(**kwargs)


class Penalty(db.Model):

    __tablename__ = 'Penalty'

    id = db.Column(db.Integer, primary_key=True)

    #__Penalty_FIELDS__
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
    time = db.Column(db.Text, nullable=True)
    employee_id = db.Column(db.Integer, nullable=True)
    employee_name = db.Column(db.Text, nullable=True)
    inspector_name = db.Column(db.Text, nullable=True)
    inspector_email = db.Column(db.Text, nullable=True)
    manager = db.Column(db.Text, nullable=True)
    details = db.Column(db.Text, nullable=True)
    decision = db.Column(db.Text, nullable=True)
    decision_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    explanation = db.Column(db.Text, nullable=True)
    penalty_key = db.Column(db.Text, nullable=True)
    penalty_count = db.Column(db.Integer, nullable=True)
    ncr_number = db.Column(db.Integer, nullable=True)

    #__Penalty_FIELDS__END

    def __init__(self, **kwargs):
        super(Penalty, self).__init__(**kwargs)


class Machineopertypes(db.Model):

    __tablename__ = 'Machineopertypes'

    id = db.Column(db.Integer, primary_key=True)

    #__Machineopertypes_FIELDS__
    operation_type = db.Column(db.Text, nullable=True)

    #__Machineopertypes_FIELDS__END

    def __init__(self, **kwargs):
        super(Machineopertypes, self).__init__(**kwargs)



#__MODELS__END
