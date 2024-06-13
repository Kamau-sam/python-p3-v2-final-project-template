import click
from db.models import Patient, Doctor, Appointment, Prescription
from helpers import exit_program

@click.group()
def cli():
    pass

# Helper functions
def list_patients():
    patients = Patient.get_all_patients()
    for patient in patients:
        click.echo(patient)
    return patients

def find_patient_by_name():
    name = click.prompt("Enter patient's name")
    patient = Patient.get_patient_by_name(name)
    click.echo(patient) if patient else click.echo(f"Patient {name} not found")

def find_patient_by_id():
    patient_id = click.prompt("Enter patient's ID", type=int)
    patient = Patient.get_patient_by_id(patient_id)
    click.echo(patient) if patient else click.echo(f"Patient ID {patient_id} not found")

def create_patient():
    first_name = click.prompt("Enter patient's first name")
    last_name = click.prompt("Enter patient's last name")
    dob = click.prompt("Enter patient's date of birth (YYYY-MM-DD)")
    address = click.prompt("Enter patient's address")
    try:
        patient = Patient.create(first_name, last_name, dob, address)
        click.echo(f"Success: {patient} created")
    except Exception as e:
        click.echo(f"Error creating patient: {e}")

def update_patient_address():
    patients = list_patients()
    patient_id = click.prompt("Enter patient's ID to update", type=int)
    patient = Patient.get_patient_by_id(patient_id)
    if patient:
        new_address = click.prompt("Enter new address")
        patient.address = new_address
        patient.update_address()
        click.echo(f"Success: {patient} updated")
    else:
        click.echo(f"Patient ID {patient_id} not found")

def delete_patient():
    patients = list_patients()
    patient_id = click.prompt("Enter patient's ID to delete", type=int)
    patient = Patient.get_patient_by_id(patient_id)
    if patient:
        patient.delete_patient()
        click.echo(f"Success: {patient} deleted")
    else:
        click.echo(f"Patient ID {patient_id} not found")

def list_doctors():
    doctors = Doctor.get_all_doctors()
    for doctor in doctors:
        click.echo(doctor)
    return doctors

def find_doctor_by_name():
    name = click.prompt("Enter doctor's name")
    doctor = Doctor.get_doctor_by_name(name)
    click.echo(doctor) if doctor else click.echo(f"Doctor {name} not found")

def find_doctor_by_id():
    doctor_id = click.prompt("Enter doctor's ID", type=int)
    doctor = Doctor.get_doctor_by_id(doctor_id)
    click.echo(doctor) if doctor else click.echo(f"Doctor ID {doctor_id} not found")

def create_doctor():
    first_name = click.prompt("Enter doctor's first name")
    last_name = click.prompt("Enter doctor's last name")
    specialization = click.prompt("Enter doctor's specialization")
    try:
        doctor = Doctor.create(first_name, last_name, specialization)
        click.echo(f"Success: {doctor} created")
    except Exception as e:
        click.echo(f"Error creating doctor: {e}")

def delete_doctor():
    doctors = list_doctors()
    doctor_id = click.prompt("Enter doctor's ID to delete", type=int)
    doctor = Doctor.get_doctor_by_id(doctor_id)
    if doctor:
        doctor.delete_doctor()
        click.echo(f"Success: {doctor} deleted")
    else:
        click.echo(f"Doctor ID {doctor_id} not found")

def list_appointments():
    appointments = Appointment.get_all_appointments()
    for appointment in appointments:
        click.echo(appointment)
    return appointments

def create_appointment():
    patients = list_patients()
    patient_id = click.prompt("Enter patient's ID for appointment", type=int)
    patient = Patient.get_patient_by_id(patient_id)
    if not patient:
        click.echo(f"Patient ID {patient_id} not found.")
        return

    doctors = list_doctors()
    doctor_id = click.prompt("Enter doctor's ID for appointment", type=int)
    doctor = Doctor.get_doctor_by_id(doctor_id)
    if not doctor:
        click.echo(f"Doctor ID {doctor_id} not found.")
        return

    date = click.prompt("Enter appointment date (YYYY-MM-DD)")
    time = click.prompt("Enter appointment time (HH:MM)")

    try:
        appointment = Appointment.create_appointment(patient, doctor, date, time)
        click.echo(f"Success: Appointment {appointment} created.")
    except Exception as e:
        click.echo(f"Error creating appointment: {e}")

def delete_appointment():
    appointments = list_appointments()
    appointment_id = click.prompt("Enter appointment ID to delete", type=int)
    appointment = Appointment.get_appointment_by_id(appointment_id)
    if appointment:
        appointment.delete_appointment()
        click.echo(f"Success: Appointment {appointment} deleted")
    else:
        click.echo(f"Appointment ID {appointment_id} not found")

def list_prescriptions():
    prescriptions = Prescription.get_all_prescriptions()
    for prescription in prescriptions:
        click.echo(prescription)
    return prescriptions

def create_prescription():
    patients = list_patients()
    patient_id = click.prompt("Enter patient's ID for prescription", type=int)
    patient = Patient.get_patient_by_id(patient_id)
    if not patient:
        click.echo(f"Patient ID {patient_id} not found.")
        return

    doctors = list_doctors()
    doctor_id = click.prompt("Enter doctor's ID for prescription", type=int)
    doctor = Doctor.get_doctor_by_id(doctor_id)
    if not doctor:
        click.echo(f"Doctor ID {doctor_id} not found.")
        return

    medication = click.prompt("Enter prescribed medication")
    instructions = click.prompt("Enter prescription instructions")

    try:
        prescription = Prescription.create_prescription(patient, doctor, medication, instructions)
        click.echo(f"Success: Prescription {prescription} created.")
    except Exception as e:
        click.echo(f"Error creating prescription: {e}")

def delete_prescription():
    prescriptions = list_prescriptions()
    prescription_id = click.prompt("Enter prescription ID to delete", type=int)
    prescription = Prescription.get_prescription_by_id(prescription_id)
    if prescription:
        prescription.delete_prescription()
        click.echo(f"Success: Prescription {prescription} deleted")
    else:
        click.echo(f"Prescription ID {prescription_id} not found")

# Main menu command
@click.command()
def main_menu():
    while True:
        menu()
        choice = click.prompt("=>", type=int)
        if choice == 0:
            exit_program()
        elif choice == 1:
            list_patients()
        elif choice == 2:
            find_patient_by_name()
        elif choice == 3:
            find_patient_by_id()
        elif choice == 4:
            create_patient()
        elif choice == 5:
            update_patient_address()
        elif choice == 6:
            delete_patient()
        elif choice == 7:
            list_doctors()
        elif choice == 8:
            find_doctor_by_id()
        elif choice == 9:
            find_doctor_by_name()
        elif choice == 10:
            create_doctor()
        elif choice == 11:
            delete_doctor()
        elif choice == 12:
            list_appointments()
        elif choice == 13:
            create_appointment()
        elif choice == 14:
            delete_appointment()
        elif choice == 15:
            list_prescriptions()
        elif choice == 16:
            create_prescription()
        elif choice == 17:
            delete_prescription()
        else:
            click.echo("Invalid choice. Please choose a valid option.")

def menu():
    click.echo("What do you want to do?")
    click.echo("0. Quit")
    click.echo("1. List all Patients")
    click.echo("2. Find Patient by Name")
    click.echo("3. Find Patient by ID")
    click.echo("4. Create Patient")
    click.echo("5. Update Patient Address")
    click.echo("6. Delete Patient")
    click.echo("7. List all Doctors")
    click.echo("8. Find Doctor by ID")
    click.echo("9. Find Doctor by Name")
    click.echo("10. Add a new Doctor")
    click.echo("11. Delete Doctor")
    click.echo("12. List all Appointments")
    click.echo("13. Create Appointment")
    click.echo("14. Delete Appointment")
    click.echo("15. List all Prescriptions")
    click.echo("16. Create Prescription")
    click.echo("17. Delete Prescription")

if __name__ == "__main__":
    cli.add_command(main_menu)
    cli()
