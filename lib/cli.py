
import click
from models.appointment import Appointment
from helpers import exit_program, helper_1

appointment = Appointment()

@click.group()
def cli():
    pass

@click.command()
def create_appointment_table():
    appointment.create_table()
    click.echo('Appointment table created.')

@click.command()
def drop_appointment_table():
    appointment.drop_table()
    click.echo('Appointment table dropped.')

@click.command()
@click.argument('pet_id')
@click.argument('appointment_date')
@click.argument('status')
@click.argument('description')
def add_appointment(pet_id, appointment_date, status, description):
    appointment.create(pet_id, appointment_date, status, description)
    click.echo(f'Added appointment for pet {pet_id} on {appointment_date}')

@click.command()
def list_appointments():
    appointments = appointment.all()
    for appt in appointments:
        click.echo(f'Appointment {appt[0]}: Pet {appt[1]}, Date {appt[2]}, Status {appt[3]}, Description {appt[4]}')

@click.command()
@click.argument('appointment_id')
def find_appointment(appointment_id):
    appt = appointment.find_by_id(appointment_id)
    if appt:
        click.echo(f'Appointment {appt[0][0]}: Pet {appt[0][1]}, Date {appt[0][2]}, Status {appt[0][3]}, Description {appt[0][4]}')
    else:
        click.echo('Appointment not found.')

@click.command()
def main_menu():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        elif choice == "2":
            list_appointments()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")
    print("2. List all appointments")

cli.add_command(create_appointment_table)
cli.add_command(drop_appointment_table)
cli.add_command(add_appointment)
cli.add_command(list_appointments)
cli.add_command(find_appointment)
cli.add_command(main_menu)

if __name__ == '__main__':
    cli()
