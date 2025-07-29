from flask import Blueprint, url_for, render_template, redirect, request, flash
from .models import Workplace, Employee
from . import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    all_workplaces = Workplace.query.all()
    return render_template('workplaces.html', all_workplaces=all_workplaces)

@main.route('/workplace/<int:workplace_id>')
def check_workplace(workplace_id):
    workplace = Workplace.query.get_or_404(workplace_id)
    return render_template('workplace-info.html', workplace=workplace)


@main.route('/add-workplace', methods=['GET', 'POST'])
def add_workplace():
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')

        new_workplace = Workplace(name=name, city=city)
        db.session.add(new_workplace)
        db.session.commit()
        flash('Workplace has been added successfull!', 'success')
        return redirect(url_for('main.home'))
    return render_template('add_workplace.html')

@main.route('/delete-workplace/<int:workplace_id>', methods=['POST'])
def delete_wplace(workplace_id):
    delete_workplace = Workplace.query.get_or_404(workplace_id)
    if len(delete_workplace.employees) == 0:
        db.session.delete(delete_workplace)
        db.session.commit()
        flash('Successfully deleted workplace!', 'success')
    else:
        flash('Cannot delete workplace, because there are employees assigned', 'danger')
    return redirect(url_for('main.home'))

@main.route('/update-workplace/<int:workplace_id>', methods=['GET', 'POST'])
def update(workplace_id):
    update_workplace = Workplace.query.get(workplace_id)
    if request.method == 'POST':
        update_workplace.name = request.form.get('name')
        update_workplace.city = request.form.get('city')
        db.session.commit()
        flash('Workplace successfully updated!', 'success')
        return redirect(url_for('main.home'))
    return render_template('update-workplace.html', workplace=update_workplace)

@main.route('/employees', methods=['GET', 'POST'])
def employees():
    all_employees = Employee.query.all()
    return render_template('employees.html', all_employees=all_employees)

@main.route('/add-employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        position = request.form.get('position')
        workplace_id = request.form.get('workplace_id')

        new_employee = Employee(name=name, surname=surname, position=position, workplace_id=workplace_id)
        db.session.add(new_employee)
        db.session.commit()
        flash('Employee has been added successfull!', 'success')
        return redirect(url_for('main.employees'))
    all_workplaces = Workplace.query.all()
    return render_template('add_employee.html', all_workplaces=all_workplaces)

@main.route('/update-employee/<int:employee_id>', methods=['GET', 'POST'])
def update_emp(employee_id):
    update_employee = Employee.query.get(employee_id)
    workplaces = Workplace.query.all()
    if request.method == 'POST':
        update_employee.name = request.form.get('name')
        update_employee.surname = request.form.get('surname')
        update_employee.position = request.form.get('position')
        update_employee.workplace_id = request.form.get('workplace_id')
        db.session.commit()
        flash('Employee successfully updated!', 'success')
        return redirect(url_for('main.employees'))
    return render_template('update-employee.html', employee=update_employee, workplaces=workplaces)

@main.route('/delete-employee/<int:employee_id>', methods=['POST'])
def delete_emp(employee_id):
    delete_employee = Employee.query.get_or_404(employee_id)
    db.session.delete(delete_employee)
    db.session.commit()
    return redirect(url_for('main.employees'))


