from . import db
from sqlalchemy.orm import relationship

class Workplace(db.Model):
    __tablename__ = 'workplace'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    employees = relationship('Employee', back_populates='workplace')

    @property
    def employee_count(self):
        return len(self.employees)

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    workplace_id = db.Column(db.Integer, db.ForeignKey('workplace.id'), nullable=False)
    workplace = relationship('Workplace', back_populates='employees')


