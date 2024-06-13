
class Appointment:
    def __init__(self, id, patient_id, doctor_id, date, time):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time

    @classmethod
    def get_all_appointments(cls):
        pass

    @classmethod
    def get_appointment_by_id(cls, appointment_id):
        pass

    @classmethod
    def create_appointment(cls, patient, doctor, date, time):
        pass

    def delete_appointment(self):
        pass
