
class Doctor:
    def __init__(self, id, first_name, last_name, specialization):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.specialization = specialization

    @classmethod
    def get_all_doctors(cls):
        pass

    @classmethod
    def get_doctor_by_name(cls, name):
        pass

    @classmethod
    def get_doctor_by_id(cls, doctor_id):
        pass

    @classmethod
    def create(cls, first_name, last_name, specialization):
        pass

    def delete_doctor(self):
        pass
