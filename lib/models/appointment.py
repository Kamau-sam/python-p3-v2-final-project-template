

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.db_helper import execute_query, fetch

class Appointment:
    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS appointment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pet_id INTEGER,
            appointment_date TIMESTAMP NOT NULL,
            status TEXT NOT NULL,
            description TEXT,
            FOREIGN KEY (pet_id) REFERENCES pet(id)
        );
        '''
        execute_query(query)

    def drop_table(self):
        query = "DROP TABLE IF EXISTS appointment;"
        execute_query(query)

    def create(self, pet_id, appointment_date, status, description):
        query = '''
        INSERT INTO appointment (pet_id, appointment_date, status, description) 
        VALUES (?, ?, ?, ?);
        '''
        execute_query(query, (pet_id, appointment_date, status, description))

    def all(self):
        query = "SELECT * FROM appointment;"
        return fetch(query)

    def find_by_id(self, appointment_id):
        query = "SELECT * FROM appointment WHERE id = ?;"
        return fetch(query, (appointment_id,))
