
from models.appointment import Appointment

appointment = Appointment()

def main():
    appointments = appointment.all()
    for appt in appointments:
        print(f'Appointment {appt[0]}: Pet {appt[1]}, Date {appt[2]}, Status {appt[3]}, Description {appt[4]}')

if __name__ == "__main__":
    main()