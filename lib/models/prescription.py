
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.db_helper import execute_query, fetch

class MedicalRecord:
    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS medical_record (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            doctor_id INTEGER,
            diagnosis TEXT,
            prescription TEXT,
            FOREIGN KEY (patient_id) REFERENCES patient(id),
            FOREIGN KEY (doctor_id) REFERENCES doctor(id)
        );
        '''
        execute_query(query)

    def drop_table(self):
        query = "DROP TABLE IF EXISTS medical_record;"
        execute_query(query)

    def create(self, patient_id, doctor_id, diagnosis, prescription):
        query = '''
        INSERT INTO medical_record (patient_id, doctor_id, diagnosis, prescription) 
        VALUES (?, ?, ?, ?);
        '''
        execute_query(query, (patient_id, doctor_id, diagnosis, prescription))

    def all(self):
        query = "SELECT * FROM medical_record;"
        return fetch(query)

    def find_by_id(self, record_id):
        query = "SELECT * FROM medical_record WHERE id = ?;"
        return fetch(query, (record_id,))

    def update_diagnosis(self, record_id, new_diagnosis):
        query = "UPDATE medical_record SET diagnosis = ? WHERE id = ?;"
        execute_query(query, (new_diagnosis, record_id))

    def update_prescription(self, record_id, new_prescription):
        query = "UPDATE medical_record SET prescription = ? WHERE id = ?;"
        execute_query(query, (new_prescription, record_id))

    def delete_record(self, record_id):
        query = "DELETE FROM medical_record WHERE id = ?;"
        execute_query(query, (record_id,))
