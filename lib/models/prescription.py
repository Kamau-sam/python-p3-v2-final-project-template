class Prescription:
    def __init__(self, id, patient_id, doctor_id, medication, instructions):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.medication = medication
        self.instructions = instructions

    @staticmethod
    def get_all_prescriptions():
        pass

    @staticmethod
    def get_prescription_by_id(prescription_id):
        pass

    @staticmethod
    def create_prescription(patient, doctor, medication, instructions):
        pass

    def delete_prescription(self):
        pass