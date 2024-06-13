import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.db_helper import execute_query, fetch

class Patient:
    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS patient (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT
        );
        '''
        execute_query(query)

    def drop_table(self):
        query = "DROP TABLE IF EXISTS patient;"
        execute_query(query)

    def create(self, name, age, gender):
        query = '''
        INSERT INTO patient (name, age, gender) 
        VALUES (?, ?, ?);
        '''
        execute_query(query, (name, age, gender))

    def all(self):
        query = "SELECT * FROM patient;"
        return fetch(query)

    def find_by_id(self, patient_id):
        query = "SELECT * FROM patient WHERE id = ?;"
        return fetch(query, (patient_id,))
