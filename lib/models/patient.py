
class Patient:
    def __init__(self, id, first_name, last_name, dob, address):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.address = address

    @classmethod
    def get_all_patients(cls):
        pass

    @classmethod
    def get_patient_by_name(cls, name):
        pass

    @classmethod
    def get_patient_by_id(cls, patient_id):
        pass

    @classmethod
    def create(cls, first_name, last_name, dob, address):
        pass

    def update_address(self):
        pass

    def delete_patient(self):
        pass
