
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.db_helper import execute_query, fetch

class Doctor:
    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS doctor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            specialty TEXT
        );
        '''
        execute_query(query)

    def drop_table(self):
        query = "DROP TABLE IF EXISTS doctor;"
        execute_query(query)

    def create(self, name, specialty):
        query = '''
        INSERT INTO doctor (name, specialty) 
        VALUES (?, ?);
        '''
        execute_query(query, (name, specialty))

    def all(self):
        query = "SELECT * FROM doctor;"
        return fetch(query)

    def find_by_id(self, doctor_id):
        query = "SELECT * FROM doctor WHERE id = ?;"
        return fetch(query, (doctor_id,))
